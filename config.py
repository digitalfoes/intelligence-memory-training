"""
Configuration settings for Intelligence Memory Training
"""
from typing import Dict, Any
import json
import os


class Config:
    """Application configuration manager."""
    
    # Default theme settings
    THEMES = {
        'dark': {
            'bg_primary': '#0a0e1a',
            'bg_secondary': '#1a1f2e',
            'bg_tertiary': '#2d3748',
            'text_primary': '#00ff41',
            'text_secondary': '#7d8590',
            'text_error': '#ff6b6b',
            'accent': '#ffff00',
            'success': '#00ff41',
            'font_family': 'Helvetica'
        },
        'light': {
            'bg_primary': '#f5f5f5',
            'bg_secondary': '#ffffff',
            'bg_tertiary': '#e0e0e0',
            'text_primary': '#2d3748',
            'text_secondary': '#718096',
            'text_error': '#e53e3e',
            'accent': '#3182ce',
            'success': '#38a169',
            'font_family': 'Helvetica'
        },
        'blue': {
            'bg_primary': '#1a202c',
            'bg_secondary': '#2d3748',
            'bg_tertiary': '#4a5568',
            'text_primary': '#63b3ed',
            'text_secondary': '#a0aec0',
            'text_error': '#fc8181',
            'accent': '#4299e1',
            'success': '#48bb78',
            'font_family': 'Helvetica'
        }
    }
    
    # Difficulty presets
    DIFFICULTY_PRESETS = {
        'easy': {
            'base_display_time': 8000,
            'time_reduction_per_level': 200,
            'min_display_time': 4000,
            'starting_complexity': 0.7,
            'complexity_increase': 0.05
        },
        'medium': {
            'base_display_time': 6000,
            'time_reduction_per_level': 300,
            'min_display_time': 2500,
            'starting_complexity': 1.0,
            'complexity_increase': 0.1
        },
        'hard': {
            'base_display_time': 4000,
            'time_reduction_per_level': 400,
            'min_display_time': 1500,
            'starting_complexity': 1.3,
            'complexity_increase': 0.15
        }
    }
    
    # Default settings
    DEFAULT_SETTINGS = {
        'theme': 'dark',
        'difficulty': 'medium',
        'sound_enabled': True,
        'show_hints': True,
        'font_size': 'medium',  # small, medium, large
        'practice_mode': False,
        'show_timer': True,
        'colorblind_mode': False,
        'window_width': 1000,
        'window_height': 750,
        'stats_file': 'memory_stats.db',
        'backup_enabled': True,
        'tutorial_completed': False
    }
    
    # Font size multipliers
    FONT_SIZES = {
        'small': 0.85,
        'medium': 1.0,
        'large': 1.15
    }
    
    # Game-specific settings
    GAME_CONFIGS = {
        'document_recall': {
            'name': 'Document Codes',
            'description': 'Memorize access codes and document identifiers',
            'icon': '📄',
            'min_length': 6,
            'max_length': 20
        },
        'license_plates': {
            'name': 'License Plates',
            'description': 'Track and recall vehicle identification numbers',
            'icon': '🚗',
            'min_vehicles': 2,
            'max_vehicles': 10
        },
        'face_recognition': {
            'name': 'Face Recognition',
            'description': 'Remember faces and identifying features',
            'icon': '👤',
            'min_features': 2,
            'max_features': 6
        },
        'safe_combinations': {
            'name': 'Number Sequences',
            'description': 'Retain multi-digit codes and combinations',
            'icon': '🔢',
            'min_digits': 4,
            'max_digits': 16
        },
        'surveillance_details': {
            'name': 'Scene Details',
            'description': 'Observe and recall environmental details',
            'icon': '👁️',
            'min_items': 5,
            'max_items': 15
        },
        'map_memorization': {
            'name': 'Route Memory',
            'description': 'Memorize directions and navigation sequences',
            'icon': '🗺️',
            'min_waypoints': 3,
            'max_waypoints': 12
        }
    }
    
    # Achievement definitions
    ACHIEVEMENTS = {
        'first_steps': {
            'name': 'First Steps',
            'description': 'Complete your first training session',
            'icon': '🎯',
            'requirement': {'sessions': 1}
        },
        'dedicated': {
            'name': 'Dedicated Trainee',
            'description': 'Complete 10 training sessions',
            'icon': '💪',
            'requirement': {'sessions': 10}
        },
        'master': {
            'name': 'Memory Master',
            'description': 'Complete 50 training sessions',
            'icon': '🏆',
            'requirement': {'sessions': 50}
        },
        'level_5': {
            'name': 'Rising Star',
            'description': 'Reach level 5 in any module',
            'icon': '⭐',
            'requirement': {'max_level': 5}
        },
        'level_10': {
            'name': 'Expert',
            'description': 'Reach level 10 in any module',
            'icon': '🌟',
            'requirement': {'max_level': 10}
        },
        'level_15': {
            'name': 'Legendary',
            'description': 'Reach level 15 in any module',
            'icon': '💎',
            'requirement': {'max_level': 15}
        },
        'perfect_score': {
            'name': 'Perfect Memory',
            'description': 'Score 200+ points in a single session',
            'icon': '🎖️',
            'requirement': {'single_score': 200}
        },
        'all_modules': {
            'name': 'Well Rounded',
            'description': 'Complete all 6 training modules',
            'icon': '🎓',
            'requirement': {'modules_played': 6}
        },
        'streak_5': {
            'name': 'On Fire',
            'description': 'Get 5 correct answers in a row',
            'icon': '🔥',
            'requirement': {'streak': 5}
        },
        'streak_10': {
            'name': 'Unstoppable',
            'description': 'Get 10 correct answers in a row',
            'icon': '⚡',
            'requirement': {'streak': 10}
        }
    }
    
    def __init__(self, config_file: str = 'settings.json'):
        """Initialize configuration."""
        self.config_file = config_file
        self.settings = self.load_settings()
    
    def load_settings(self) -> Dict[str, Any]:
        """Load settings from file or use defaults."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    loaded = json.load(f)
                    # Merge with defaults to ensure all keys exist
                    settings = self.DEFAULT_SETTINGS.copy()
                    settings.update(loaded)
                    return settings
            except (json.JSONDecodeError, IOError):
                return self.DEFAULT_SETTINGS.copy()
        return self.DEFAULT_SETTINGS.copy()
    
    def save_settings(self) -> None:
        """Save current settings to file."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.settings, f, indent=2)
        except IOError as e:
            print(f"Error saving settings: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a setting value."""
        return self.settings.get(key, default)
    
    def set(self, key: str, value: Any) -> None:
        """Set a setting value and save."""
        self.settings[key] = value
        self.save_settings()
    
    def get_theme(self) -> Dict[str, str]:
        """Get current theme colors."""
        theme_name = self.settings.get('theme', 'dark')
        return self.THEMES.get(theme_name, self.THEMES['dark'])
    
    def get_difficulty(self) -> Dict[str, Any]:
        """Get current difficulty settings."""
        difficulty_name = self.settings.get('difficulty', 'medium')
        return self.DIFFICULTY_PRESETS.get(difficulty_name, self.DIFFICULTY_PRESETS['medium'])
    
    def get_font_multiplier(self) -> float:
        """Get font size multiplier."""
        size = self.settings.get('font_size', 'medium')
        return self.FONT_SIZES.get(size, 1.0)
    
    def reset_to_defaults(self) -> None:
        """Reset all settings to defaults."""
        self.settings = self.DEFAULT_SETTINGS.copy()
        self.save_settings()


# Global config instance
config = Config()
