"""
Utility functions for Intelligence Memory Training
"""
import random
import string
from typing import List, Tuple, Dict, Any
from datetime import datetime, timedelta


def generate_document_code(level: int, difficulty_multiplier: float = 1.0) -> str:
    """Generate a document code based on level and difficulty."""
    base_length = int(6 + (level * difficulty_multiplier))
    
    if level <= 2:
        # Simple: ABC-123
        letters = ''.join(random.choices(string.ascii_uppercase, k=3))
        numbers = ''.join(random.choices(string.digits, k=3))
        return f"{letters}-{numbers}"
    
    elif level <= 5:
        # Medium: AB12-CD34
        segments = []
        num_segments = 2
        for _ in range(num_segments):
            seg = ''.join(random.choices(string.ascii_uppercase, k=2))
            seg += ''.join(random.choices(string.digits, k=2))
            segments.append(seg)
        return '-'.join(segments)
    
    else:
        # Advanced: A1B2-C3D4-E5F6
        num_segments = min(3, 1 + level // 3)
        segments = []
        for _ in range(num_segments):
            seg = ''
            for _ in range(2):
                seg += random.choice(string.ascii_uppercase)
                seg += random.choice(string.digits)
            segments.append(seg)
        return '-'.join(segments)


def generate_license_plate(format_type: str = 'random') -> str:
    """Generate a realistic license plate."""
    formats = [
        lambda: ''.join(random.choices(string.ascii_uppercase, k=3)) + '-' + 
                ''.join(random.choices(string.digits, k=4)),
        lambda: ''.join(random.choices(string.digits, k=2)) + '-' + 
                ''.join(random.choices(string.ascii_uppercase, k=3)) + '-' + 
                ''.join(random.choices(string.digits, k=2)),
        lambda: ''.join(random.choices(string.ascii_uppercase, k=2)) + 
                ''.join(random.choices(string.digits, k=3)) + 
                ''.join(random.choices(string.ascii_uppercase, k=1))
    ]
    
    if format_type == 'random':
        return random.choice(formats)()
    else:
        return formats[0]()


def generate_suspect_profile(level: int) -> Dict[str, Any]:
    """Generate a suspect profile with increasing complexity."""
    first_names = ['ALEX', 'BLAKE', 'CASEY', 'DREW', 'ELLIS', 'FINLEY', 
                   'GRAY', 'HARPER', 'JORDAN', 'KELLY', 'MORGAN', 'PARKER']
    last_names = ['ANDERSON', 'BROOKS', 'CARTER', 'DAVIS', 'EVANS', 'FOSTER',
                  'GRANT', 'HAYES', 'IRWIN', 'JONES', 'KING', 'LOPEZ']
    
    features = [
        'SCAR ON LEFT CHEEK', 'TATTOO ON NECK', 'GLASSES', 'BEARD',
        'BALD', 'LONG HAIR', 'EARRING', 'MUSTACHE', 'NOSE RING',
        'FACIAL SCAR', 'GOLD TOOTH', 'EYE PATCH', 'BIRTHMARK',
        'CREW CUT', 'PONYTAIL', 'GOATEE'
    ]
    
    num_features = min(2 + level // 2, 6)
    
    return {
        'name': f"{random.choice(first_names)} {random.choice(last_names)}",
        'age': random.randint(25, 65),
        'height': f"{random.randint(5,6)}'{random.randint(0,11)}\"",
        'weight': f"{random.randint(140, 240)} lbs",
        'features': random.sample(features, num_features)
    }


def generate_safe_combination(level: int, difficulty_multiplier: float = 1.0) -> str:
    """Generate a safe combination."""
    combo_length = int(min(4 + (level * difficulty_multiplier), 16))
    segments = []
    
    for _ in range(combo_length // 2):
        segments.append(''.join(random.choices(string.digits, k=2)))
    
    return '-'.join(segments)


def generate_scene_items(level: int) -> List[str]:
    """Generate items for scene observation."""
    items = [
        '📱', '💼', '🔑', '📄', '💻', '🎒', '☕', '📚', '🕶️', '⌚',
        '🔦', '📷', '🎧', '📝', '✏️', '📎', '🔒', '💳', '🎫', '📰',
        '🗂️', '📊', '📈', '🖊️', '📌', '🔍', '📞', '💡', '🔋', '🗝️'
    ]
    
    num_items = min(5 + level, 15)
    return random.sample(items, num_items)


def generate_route(level: int) -> List[str]:
    """Generate a navigation route."""
    directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NE', 'NW', 'SE', 'SW']
    num_waypoints = min(3 + level, 12)
    
    return [random.choice(directions) for _ in range(num_waypoints)]


def calculate_display_time(level: int, base_time: int, reduction: int, min_time: int) -> int:
    """Calculate display time based on level and difficulty settings."""
    time_ms = max(min_time, base_time - (level * reduction))
    return time_ms


def format_time(seconds: int) -> str:
    """Format seconds into MM:SS."""
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes:02d}:{secs:02d}"


def calculate_accuracy(correct: int, total: int) -> float:
    """Calculate accuracy percentage."""
    if total == 0:
        return 0.0
    return (correct / total) * 100


def get_performance_rating(score: int, level: int) -> Tuple[str, str]:
    """Get performance rating based on score and level."""
    if level >= 15:
        return ("Legendary", "💎")
    elif level >= 10:
        return ("Expert", "🌟")
    elif level >= 7:
        return ("Advanced", "⭐")
    elif level >= 5:
        return ("Proficient", "✨")
    elif level >= 3:
        return ("Competent", "📈")
    else:
        return ("Beginner", "🎯")


def generate_hint(game_type: str, level: int, data: Any) -> str:
    """Generate a helpful hint based on game type."""
    hints = {
        'document_recall': [
            "Try breaking the code into smaller chunks",
            "Look for patterns in the letters and numbers",
            "Visualize the code as you read it",
            "Repeat the code silently 2-3 times"
        ],
        'license_plates': [
            "Create a story linking the plates together",
            "Group plates by their format type",
            "Focus on one plate at a time",
            "Use mnemonics for difficult combinations"
        ],
        'face_recognition': [
            "Pay attention to distinguishing features first",
            "Create a mental image of the person",
            "Link the name to someone you know",
            "Notice unique characteristics"
        ],
        'safe_combinations': [
            "Group numbers in pairs",
            "Create a rhythm for the sequence",
            "Visualize typing the combination",
            "Look for number patterns"
        ],
        'surveillance_details': [
            "Scan systematically from left to right",
            "Count the total number of items",
            "Group similar items together",
            "Create a mental snapshot"
        ],
        'map_memorization': [
            "Visualize yourself walking the route",
            "Use landmarks at each turn",
            "Remember: Never Eat Soggy Waffles (N-E-S-W)",
            "Trace the path with your finger"
        ]
    }
    
    game_hints = hints.get(game_type, ["Focus and take your time"])
    return random.choice(game_hints)


def get_encouragement(level: int, streak: int = 0) -> str:
    """Get encouraging message based on performance."""
    if streak >= 10:
        messages = [
            "Unstoppable! 🔥",
            "Incredible streak!",
            "You're on fire!",
            "Phenomenal performance!"
        ]
    elif streak >= 5:
        messages = [
            "Great streak going!",
            "Keep it up!",
            "Excellent work!",
            "You're doing amazing!"
        ]
    elif level >= 10:
        messages = [
            "Expert level achieved!",
            "Outstanding progress!",
            "Impressive skills!",
            "You're a natural!"
        ]
    elif level >= 5:
        messages = [
            "Nice progress!",
            "You're improving!",
            "Keep going!",
            "Well done!"
        ]
    else:
        messages = [
            "Good start!",
            "You can do this!",
            "Stay focused!",
            "Keep practicing!"
        ]
    
    return random.choice(messages)


def create_daily_challenge() -> Dict[str, Any]:
    """Create a random daily challenge."""
    from config import config
    
    game_types = list(config.GAME_CONFIGS.keys())
    game_type = random.choice(game_types)
    target_level = random.randint(5, 10)
    
    return {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'game_type': game_type,
        'target_level': target_level,
        'description': f"Reach level {target_level} in {config.GAME_CONFIGS[game_type]['name']}"
    }


def export_stats_to_csv(sessions: List[Dict], filename: str = 'stats_export.csv') -> None:
    """Export session data to CSV file."""
    import csv
    
    if not sessions:
        return
    
    keys = sessions[0].keys()
    
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(sessions)


def calculate_streak(sessions: List[Dict]) -> int:
    """Calculate current winning streak from session history."""
    if not sessions:
        return 0
    
    streak = 0
    for session in sorted(sessions, key=lambda x: x.get('timestamp', ''), reverse=True):
        if session.get('score', 0) > 0:
            streak += 1
        else:
            break
    
    return streak


def get_next_milestone(current_level: int) -> Tuple[int, str]:
    """Get the next achievement milestone."""
    milestones = [
        (5, "Rising Star ⭐"),
        (10, "Expert 🌟"),
        (15, "Legendary 💎"),
        (20, "Master 👑")
    ]
    
    for level, name in milestones:
        if current_level < level:
            return (level, name)
    
    return (current_level + 5, "Keep Going! 🚀")


def validate_input(user_input: str, expected: str, case_sensitive: bool = False) -> bool:
    """Validate user input against expected answer."""
    if not case_sensitive:
        return user_input.strip().upper() == expected.strip().upper()
    return user_input.strip() == expected.strip()


def sanitize_filename(filename: str) -> str:
    """Sanitize filename for safe file operations."""
    import re
    # Remove invalid characters
    filename = re.sub(r'[<>:"/\\|?*]', '', filename)
    # Limit length
    return filename[:255]
