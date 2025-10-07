"""
Unit tests for Intelligence Memory Training
"""
import unittest
import os
import json
from config import Config
from database import Database
from utils import (
    generate_document_code,
    generate_license_plate,
    generate_suspect_profile,
    generate_safe_combination,
    generate_scene_items,
    generate_route,
    calculate_display_time,
    format_time,
    calculate_accuracy,
    get_performance_rating,
    validate_input
)


class TestConfig(unittest.TestCase):
    """Test configuration management."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.test_config_file = 'test_settings.json'
        self.config = Config(self.test_config_file)
    
    def tearDown(self):
        """Clean up test files."""
        if os.path.exists(self.test_config_file):
            os.remove(self.test_config_file)
    
    def test_default_settings(self):
        """Test default settings are loaded."""
        self.assertEqual(self.config.get('theme'), 'dark')
        self.assertEqual(self.config.get('difficulty'), 'medium')
        self.assertTrue(self.config.get('sound_enabled'))
    
    def test_set_and_get(self):
        """Test setting and getting values."""
        self.config.set('theme', 'light')
        self.assertEqual(self.config.get('theme'), 'light')
    
    def test_get_theme(self):
        """Test theme retrieval."""
        theme = self.config.get_theme()
        self.assertIn('bg_primary', theme)
        self.assertIn('text_primary', theme)
    
    def test_get_difficulty(self):
        """Test difficulty preset retrieval."""
        difficulty = self.config.get_difficulty()
        self.assertIn('base_display_time', difficulty)
        self.assertIn('min_display_time', difficulty)
    
    def test_font_multiplier(self):
        """Test font size multiplier."""
        self.config.set('font_size', 'large')
        multiplier = self.config.get_font_multiplier()
        self.assertEqual(multiplier, 1.15)
    
    def test_reset_to_defaults(self):
        """Test resetting to default settings."""
        self.config.set('theme', 'blue')
        self.config.reset_to_defaults()
        self.assertEqual(self.config.get('theme'), 'dark')


class TestDatabase(unittest.TestCase):
    """Test database operations."""
    
    def setUp(self):
        """Set up test database."""
        self.test_db_file = ':memory:'  # Use in-memory database
        self.db = Database(self.test_db_file)
    
    def test_database_initialization(self):
        """Test database tables are created."""
        with self.db.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [row[0] for row in cursor.fetchall()]
            
            self.assertIn('sessions', tables)
            self.assertIn('statistics', tables)
            self.assertIn('achievements', tables)
    
    def test_record_session(self):
        """Test recording a training session."""
        session_id = self.db.record_session(
            game_type='document_recall',
            score=100,
            level=5,
            correct=5,
            total=5
        )
        self.assertIsNotNone(session_id)
        self.assertGreater(session_id, 0)
    
    def test_get_statistics(self):
        """Test retrieving statistics."""
        # Record a session first
        self.db.record_session('document_recall', 100, 5, 5, 5)
        
        stats = self.db.get_statistics('document_recall')
        self.assertEqual(stats['sessions_played'], 1)
        self.assertEqual(stats['best_score'], 100)
    
    def test_unlock_achievement(self):
        """Test unlocking achievements."""
        result = self.db.unlock_achievement('first_steps', 100)
        self.assertTrue(result)
        
        achievements = self.db.get_achievements()
        self.assertIn('first_steps', achievements)
    
    def test_get_recent_sessions(self):
        """Test retrieving recent sessions."""
        # Record multiple sessions
        for i in range(5):
            self.db.record_session('document_recall', i * 10, i, i, i)
        
        sessions = self.db.get_recent_sessions(limit=3)
        self.assertEqual(len(sessions), 3)
    
    def test_export_import_data(self):
        """Test data export and import."""
        # Record some data
        self.db.record_session('document_recall', 100, 5, 5, 5)
        self.db.unlock_achievement('first_steps')
        
        # Export
        exported = self.db.export_data()
        self.assertIn('sessions', exported)
        self.assertIn('achievements', exported)
        
        # Create new database and import
        new_db = Database(':memory:')
        new_db.import_data(exported, merge=False)
        
        # Verify
        stats = new_db.get_statistics('document_recall')
        self.assertEqual(stats['sessions_played'], 1)


class TestUtils(unittest.TestCase):
    """Test utility functions."""
    
    def test_generate_document_code(self):
        """Test document code generation."""
        # Level 1 should generate simple code
        code = generate_document_code(1)
        self.assertIn('-', code)
        self.assertGreater(len(code), 5)
        
        # Higher level should generate longer code
        code_high = generate_document_code(10)
        self.assertGreater(len(code_high), len(code))
    
    def test_generate_license_plate(self):
        """Test license plate generation."""
        plate = generate_license_plate()
        self.assertGreater(len(plate), 5)
        # Should contain letters and numbers
        self.assertTrue(any(c.isalpha() for c in plate))
        self.assertTrue(any(c.isdigit() for c in plate))
    
    def test_generate_suspect_profile(self):
        """Test suspect profile generation."""
        profile = generate_suspect_profile(1)
        
        self.assertIn('name', profile)
        self.assertIn('age', profile)
        self.assertIn('height', profile)
        self.assertIn('features', profile)
        
        self.assertIsInstance(profile['features'], list)
        self.assertGreater(len(profile['features']), 0)
    
    def test_generate_safe_combination(self):
        """Test safe combination generation."""
        combo = generate_safe_combination(1)
        self.assertIn('-', combo)
        self.assertTrue(all(c.isdigit() or c == '-' for c in combo))
    
    def test_generate_scene_items(self):
        """Test scene items generation."""
        items = generate_scene_items(1)
        self.assertIsInstance(items, list)
        self.assertGreater(len(items), 0)
        
        # Higher level should generate more items
        items_high = generate_scene_items(10)
        self.assertGreater(len(items_high), len(items))
    
    def test_generate_route(self):
        """Test route generation."""
        route = generate_route(1)
        self.assertIsInstance(route, list)
        self.assertGreater(len(route), 0)
        
        # All directions should be valid
        valid_directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NE', 'NW', 'SE', 'SW']
        for direction in route:
            self.assertIn(direction, valid_directions)
    
    def test_calculate_display_time(self):
        """Test display time calculation."""
        time1 = calculate_display_time(1, 5000, 300, 2000)
        time2 = calculate_display_time(5, 5000, 300, 2000)
        
        # Higher level should have less time
        self.assertGreater(time1, time2)
        
        # Should not go below minimum
        time_min = calculate_display_time(100, 5000, 300, 2000)
        self.assertEqual(time_min, 2000)
    
    def test_format_time(self):
        """Test time formatting."""
        self.assertEqual(format_time(0), "00:00")
        self.assertEqual(format_time(65), "01:05")
        self.assertEqual(format_time(125), "02:05")
    
    def test_calculate_accuracy(self):
        """Test accuracy calculation."""
        self.assertEqual(calculate_accuracy(5, 5), 100.0)
        self.assertEqual(calculate_accuracy(5, 10), 50.0)
        self.assertEqual(calculate_accuracy(0, 10), 0.0)
        self.assertEqual(calculate_accuracy(0, 0), 0.0)
    
    def test_get_performance_rating(self):
        """Test performance rating."""
        rating1, emoji1 = get_performance_rating(50, 1)
        self.assertEqual(rating1, "Beginner")
        
        rating2, emoji2 = get_performance_rating(100, 15)
        self.assertEqual(rating2, "Legendary")
    
    def test_validate_input(self):
        """Test input validation."""
        self.assertTrue(validate_input("ABC", "ABC"))
        self.assertTrue(validate_input("abc", "ABC"))  # Case insensitive by default
        self.assertFalse(validate_input("ABC", "XYZ"))
        
        # Case sensitive
        self.assertFalse(validate_input("abc", "ABC", case_sensitive=True))
        self.assertTrue(validate_input("ABC", "ABC", case_sensitive=True))


class TestIntegration(unittest.TestCase):
    """Integration tests for the application."""
    
    def setUp(self):
        """Set up integration test environment."""
        self.config = Config(':memory:')
        self.db = Database(':memory:')
    
    def test_full_session_workflow(self):
        """Test a complete training session workflow."""
        # Generate training data
        code = generate_document_code(1)
        self.assertIsNotNone(code)
        
        # Simulate session
        session_id = self.db.record_session(
            game_type='document_recall',
            score=10,
            level=1,
            correct=1,
            total=1
        )
        self.assertGreater(session_id, 0)
        
        # Check statistics
        stats = self.db.get_statistics('document_recall')
        self.assertEqual(stats['sessions_played'], 1)
        self.assertEqual(stats['best_score'], 10)
        
        # Check for achievements
        session_data = {'score': 10, 'level': 1}
        achievements = self.db.check_achievements(session_data)
        self.assertIn('first_steps', achievements)
    
    def test_difficulty_progression(self):
        """Test difficulty increases with level."""
        difficulty = self.config.get_difficulty()
        
        time1 = calculate_display_time(
            1,
            difficulty['base_display_time'],
            difficulty['time_reduction_per_level'],
            difficulty['min_display_time']
        )
        
        time5 = calculate_display_time(
            5,
            difficulty['base_display_time'],
            difficulty['time_reduction_per_level'],
            difficulty['min_display_time']
        )
        
        self.assertGreater(time1, time5)
    
    def test_theme_switching(self):
        """Test switching between themes."""
        themes = ['dark', 'light', 'blue']
        
        for theme_name in themes:
            self.config.set('theme', theme_name)
            theme = self.config.get_theme()
            
            self.assertIn('bg_primary', theme)
            self.assertIn('text_primary', theme)
            self.assertIsInstance(theme['bg_primary'], str)


def run_tests():
    """Run all tests."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestConfig))
    suite.addTests(loader.loadTestsFromTestCase(TestDatabase))
    suite.addTests(loader.loadTestsFromTestCase(TestUtils))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    exit(0 if success else 1)
