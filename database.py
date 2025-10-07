"""
Database management for Intelligence Memory Training
"""
import sqlite3
import json
from datetime import datetime
from typing import Dict, List, Optional, Any
from contextlib import contextmanager


class Database:
    """SQLite database manager for persistent storage."""
    
    def __init__(self, db_file: str = 'memory_stats.db'):
        """Initialize database connection."""
        self.db_file = db_file
        # Keep persistent connection for in-memory databases
        self._persistent_conn = None
        if db_file == ':memory:':
            self._persistent_conn = sqlite3.connect(db_file)
            self._persistent_conn.row_factory = sqlite3.Row
        self.init_database()
    
    @contextmanager
    def get_connection(self):
        """Context manager for database connections."""
        # Use persistent connection for in-memory databases
        if self._persistent_conn:
            try:
                yield self._persistent_conn
                self._persistent_conn.commit()
            except Exception as e:
                self._persistent_conn.rollback()
                raise e
        else:
            conn = sqlite3.connect(self.db_file)
            conn.row_factory = sqlite3.Row
            try:
                yield conn
                conn.commit()
            except Exception as e:
                conn.rollback()
                raise e
            finally:
                conn.close()
    
    def init_database(self) -> None:
        """Create database tables if they don't exist."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Sessions table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    game_type TEXT NOT NULL,
                    score INTEGER NOT NULL,
                    level_reached INTEGER NOT NULL,
                    correct_answers INTEGER DEFAULT 0,
                    total_attempts INTEGER DEFAULT 0,
                    duration_seconds INTEGER DEFAULT 0,
                    practice_mode BOOLEAN DEFAULT 0,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Statistics table (aggregated data)
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS statistics (
                    game_type TEXT PRIMARY KEY,
                    sessions_played INTEGER DEFAULT 0,
                    best_score INTEGER DEFAULT 0,
                    total_score INTEGER DEFAULT 0,
                    best_level INTEGER DEFAULT 0,
                    total_correct INTEGER DEFAULT 0,
                    total_attempts INTEGER DEFAULT 0,
                    last_played DATETIME
                )
            ''')
            
            # Achievements table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS achievements (
                    achievement_id TEXT PRIMARY KEY,
                    unlocked_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                    progress INTEGER DEFAULT 0
                )
            ''')
            
            # User preferences (for multi-user support in future)
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_data (
                    key TEXT PRIMARY KEY,
                    value TEXT,
                    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Daily challenges
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS daily_challenges (
                    date TEXT PRIMARY KEY,
                    game_type TEXT NOT NULL,
                    target_level INTEGER NOT NULL,
                    completed BOOLEAN DEFAULT 0,
                    score INTEGER DEFAULT 0
                )
            ''')
            
            conn.commit()
    
    def record_session(self, game_type: str, score: int, level: int, 
                      correct: int = 0, total: int = 0, duration: int = 0,
                      practice_mode: bool = False) -> int:
        """Record a training session."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            # Insert session
            cursor.execute('''
                INSERT INTO sessions 
                (game_type, score, level_reached, correct_answers, total_attempts, 
                 duration_seconds, practice_mode)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (game_type, score, level, correct, total, duration, practice_mode))
            
            session_id = cursor.lastrowid
            
            # Update statistics
            cursor.execute('''
                INSERT INTO statistics (game_type, sessions_played, best_score, total_score, 
                                       best_level, total_correct, total_attempts, last_played)
                VALUES (?, 1, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
                ON CONFLICT(game_type) DO UPDATE SET
                    sessions_played = sessions_played + 1,
                    best_score = MAX(best_score, ?),
                    total_score = total_score + ?,
                    best_level = MAX(best_level, ?),
                    total_correct = total_correct + ?,
                    total_attempts = total_attempts + ?,
                    last_played = CURRENT_TIMESTAMP
            ''', (game_type, score, score, level, correct, total,
                  score, score, level, correct, total))
            
            return session_id
    
    def get_statistics(self, game_type: Optional[str] = None) -> Dict[str, Any]:
        """Get statistics for a game or all games."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            if game_type:
                cursor.execute('''
                    SELECT * FROM statistics WHERE game_type = ?
                ''', (game_type,))
                row = cursor.fetchone()
                if row:
                    return dict(row)
                return {
                    'sessions_played': 0,
                    'best_score': 0,
                    'total_score': 0,
                    'best_level': 0,
                    'total_correct': 0,
                    'total_attempts': 0
                }
            else:
                cursor.execute('SELECT * FROM statistics')
                rows = cursor.fetchall()
                return {row['game_type']: dict(row) for row in rows}
    
    def get_recent_sessions(self, limit: int = 10, game_type: Optional[str] = None) -> List[Dict]:
        """Get recent training sessions."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            if game_type:
                cursor.execute('''
                    SELECT * FROM sessions 
                    WHERE game_type = ?
                    ORDER BY timestamp DESC 
                    LIMIT ?
                ''', (game_type, limit))
            else:
                cursor.execute('''
                    SELECT * FROM sessions 
                    ORDER BY timestamp DESC 
                    LIMIT ?
                ''', (limit,))
            
            return [dict(row) for row in cursor.fetchall()]
    
    def get_session_history(self, days: int = 30) -> List[Dict]:
        """Get session history for the last N days."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT 
                    DATE(timestamp) as date,
                    COUNT(*) as sessions,
                    SUM(score) as total_score,
                    AVG(score) as avg_score,
                    MAX(level_reached) as max_level
                FROM sessions
                WHERE timestamp >= datetime('now', '-' || ? || ' days')
                GROUP BY DATE(timestamp)
                ORDER BY date DESC
            ''', (days,))
            
            return [dict(row) for row in cursor.fetchall()]
    
    def unlock_achievement(self, achievement_id: str, progress: int = 100) -> bool:
        """Unlock an achievement."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT OR REPLACE INTO achievements (achievement_id, progress, unlocked_at)
                VALUES (?, ?, CURRENT_TIMESTAMP)
            ''', (achievement_id, progress))
            
            return cursor.rowcount > 0
    
    def get_achievements(self) -> Dict[str, Dict]:
        """Get all unlocked achievements."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM achievements')
            rows = cursor.fetchall()
            
            return {row['achievement_id']: {
                'unlocked_at': row['unlocked_at'],
                'progress': row['progress']
            } for row in rows}
    
    def check_achievements(self, session_data: Dict) -> List[str]:
        """Check if any achievements should be unlocked based on session data."""
        from config import config as app_config
        
        newly_unlocked = []
        stats = self.get_statistics()
        unlocked = self.get_achievements()
        
        # Total sessions across all games
        total_sessions = sum(s.get('sessions_played', 0) for s in stats.values())
        
        # Check each achievement
        for achievement_id, achievement in app_config.ACHIEVEMENTS.items():
            if achievement_id in unlocked:
                continue
            
            req = achievement['requirement']
            
            # Check session count
            if 'sessions' in req and total_sessions >= req['sessions']:
                self.unlock_achievement(achievement_id)
                newly_unlocked.append(achievement_id)
            
            # Check max level
            elif 'max_level' in req:
                max_level = max((s.get('best_level', 0) for s in stats.values()), default=0)
                if max_level >= req['max_level']:
                    self.unlock_achievement(achievement_id)
                    newly_unlocked.append(achievement_id)
            
            # Check single score
            elif 'single_score' in req and session_data.get('score', 0) >= req['single_score']:
                self.unlock_achievement(achievement_id)
                newly_unlocked.append(achievement_id)
            
            # Check modules played
            elif 'modules_played' in req and len(stats) >= req['modules_played']:
                self.unlock_achievement(achievement_id)
                newly_unlocked.append(achievement_id)
            
            # Check streak (would need to track this separately)
            elif 'streak' in req and session_data.get('streak', 0) >= req['streak']:
                self.unlock_achievement(achievement_id)
                newly_unlocked.append(achievement_id)
        
        return newly_unlocked
    
    def set_user_data(self, key: str, value: Any) -> None:
        """Store user-specific data."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            value_str = json.dumps(value) if not isinstance(value, str) else value
            
            cursor.execute('''
                INSERT OR REPLACE INTO user_data (key, value, updated_at)
                VALUES (?, ?, CURRENT_TIMESTAMP)
            ''', (key, value_str))
    
    def get_user_data(self, key: str, default: Any = None) -> Any:
        """Retrieve user-specific data."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('SELECT value FROM user_data WHERE key = ?', (key,))
            row = cursor.fetchone()
            
            if row:
                try:
                    return json.loads(row['value'])
                except json.JSONDecodeError:
                    return row['value']
            
            return default
    
    def create_daily_challenge(self, date: str, game_type: str, target_level: int) -> None:
        """Create a daily challenge."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT OR REPLACE INTO daily_challenges (date, game_type, target_level)
                VALUES (?, ?, ?)
            ''', (date, game_type, target_level))
    
    def get_daily_challenge(self, date: str) -> Optional[Dict]:
        """Get daily challenge for a specific date."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT * FROM daily_challenges WHERE date = ?
            ''', (date,))
            
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def complete_daily_challenge(self, date: str, score: int) -> None:
        """Mark daily challenge as completed."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE daily_challenges 
                SET completed = 1, score = ?
                WHERE date = ?
            ''', (score, date))
    
    def export_data(self) -> Dict[str, Any]:
        """Export all data for backup."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            data = {
                'export_date': datetime.now().isoformat(),
                'sessions': [],
                'statistics': {},
                'achievements': {},
                'user_data': {}
            }
            
            # Export sessions
            cursor.execute('SELECT * FROM sessions ORDER BY timestamp')
            data['sessions'] = [dict(row) for row in cursor.fetchall()]
            
            # Export statistics
            cursor.execute('SELECT * FROM statistics')
            data['statistics'] = {row['game_type']: dict(row) for row in cursor.fetchall()}
            
            # Export achievements
            cursor.execute('SELECT * FROM achievements')
            data['achievements'] = {row['achievement_id']: dict(row) for row in cursor.fetchall()}
            
            # Export user data
            cursor.execute('SELECT * FROM user_data')
            for row in cursor.fetchall():
                try:
                    data['user_data'][row['key']] = json.loads(row['value'])
                except json.JSONDecodeError:
                    data['user_data'][row['key']] = row['value']
            
            return data
    
    def import_data(self, data: Dict[str, Any], merge: bool = True) -> None:
        """Import data from backup."""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            
            if not merge:
                # Clear existing data
                cursor.execute('DELETE FROM sessions')
                cursor.execute('DELETE FROM statistics')
                cursor.execute('DELETE FROM achievements')
                cursor.execute('DELETE FROM user_data')
            
            # Import sessions
            for session in data.get('sessions', []):
                cursor.execute('''
                    INSERT INTO sessions 
                    (game_type, score, level_reached, correct_answers, total_attempts, 
                     duration_seconds, practice_mode, timestamp)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (session.get('game_type'), session.get('score'), 
                      session.get('level_reached'), session.get('correct_answers', 0),
                      session.get('total_attempts', 0), session.get('duration_seconds', 0),
                      session.get('practice_mode', 0), session.get('timestamp')))
            
            # Import statistics
            for game_type, stats in data.get('statistics', {}).items():
                cursor.execute('''
                    INSERT OR REPLACE INTO statistics 
                    (game_type, sessions_played, best_score, total_score, best_level,
                     total_correct, total_attempts, last_played)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (game_type, stats.get('sessions_played', 0), stats.get('best_score', 0),
                      stats.get('total_score', 0), stats.get('best_level', 0),
                      stats.get('total_correct', 0), stats.get('total_attempts', 0),
                      stats.get('last_played')))
            
            # Import achievements
            for achievement_id, achievement in data.get('achievements', {}).items():
                cursor.execute('''
                    INSERT OR REPLACE INTO achievements (achievement_id, unlocked_at, progress)
                    VALUES (?, ?, ?)
                ''', (achievement_id, achievement.get('unlocked_at'), 
                      achievement.get('progress', 100)))
            
            # Import user data
            for key, value in data.get('user_data', {}).items():
                value_str = json.dumps(value) if not isinstance(value, str) else value
                cursor.execute('''
                    INSERT OR REPLACE INTO user_data (key, value)
                    VALUES (?, ?)
                ''', (key, value_str))
            
            conn.commit()


# Global database instance
db = Database()
