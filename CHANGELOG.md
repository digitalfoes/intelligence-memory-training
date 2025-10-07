# Changelog

All notable changes to Intelligence Memory Training will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-10-07

### Added
- **Modular Architecture**: Separated code into config.py, database.py, and utils.py
- **SQLite Database**: Replaced JSON with proper database for better data persistence
- **Configuration System**: Centralized settings management with themes and difficulty presets
- **Multiple Themes**: Dark, Light, and Blue color schemes
- **Difficulty Levels**: Easy, Medium, and Hard presets
- **Achievements System**: 10 unlockable achievements with progress tracking
- **Practice Mode**: Train without failure penalties
- **Hints System**: Contextual hints for each training module
- **Daily Challenges**: Randomized daily goals
- **Statistics Tracking**: Comprehensive session history and analytics
- **Data Export/Import**: Backup and restore functionality
- **Better Error Handling**: Specific exception handling throughout
- **Type Hints**: Added for better code documentation
- **GitHub Integration**: CI/CD workflows, issue templates, PR templates
- **Comprehensive Documentation**: CONTRIBUTING.md, detailed README
- **Setup Script**: Proper Python package setup with setup.py

### Changed
- **UI Improvements**: Cleaner, more professional interface
- **Simplified Language**: Removed overly dramatic elements
- **Better Performance**: Optimized database queries and UI rendering
- **Enhanced Accessibility**: Better keyboard navigation and screen reader support

### Fixed
- Database connection handling
- Settings persistence
- Statistics calculation accuracy

## [1.0.0] - 2025-10-07

### Added
- Initial release
- 6 training modules:
  - Document Codes
  - License Plates
  - Face Recognition
  - Number Sequences
  - Scene Details
  - Route Memory
- Basic statistics tracking
- Progressive difficulty
- Dark theme UI
- JSON-based data storage

---

## Upcoming Features

### Planned for v2.1.0
- [ ] Progress graphs and charts
- [ ] Sound effects and audio feedback
- [ ] Tutorial mode for new users
- [ ] Customizable difficulty curves
- [ ] Session replay feature
- [ ] Leaderboard (optional online)

### Planned for v2.2.0
- [ ] Mobile companion app
- [ ] Web version
- [ ] Multi-user profiles
- [ ] Advanced analytics dashboard
- [ ] Custom training scenarios
- [ ] Spaced repetition algorithm

### Planned for v3.0.0
- [ ] AI-adaptive difficulty
- [ ] VR/AR support
- [ ] Multiplayer challenges
- [ ] Professional certification mode
- [ ] Integration with learning management systems

---

## Version History

- **2.0.0** - Major refactor with modular architecture and advanced features
- **1.0.0** - Initial release with core functionality
