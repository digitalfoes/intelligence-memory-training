# Contributing to Intelligence Memory Training

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Your environment (OS, Python version)
- Screenshots if applicable

### Suggesting Features

Feature requests are welcome! Please:
- Check if the feature has already been requested
- Clearly describe the feature and its benefits
- Explain how it would work
- Consider implementation complexity

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the existing code style
   - Add comments for complex logic
   - Update documentation as needed

4. **Test your changes**
   - Ensure the app runs without errors
   - Test all affected features
   - Add unit tests if applicable

5. **Commit your changes**
   ```bash
   git commit -m "Add: brief description of changes"
   ```
   
   Use conventional commits:
   - `Add:` for new features
   - `Fix:` for bug fixes
   - `Update:` for improvements
   - `Refactor:` for code restructuring
   - `Docs:` for documentation

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Describe what you changed and why
   - Reference any related issues
   - Request review from maintainers

## Code Style Guidelines

### Python Style
- Follow PEP 8
- Use type hints where appropriate
- Maximum line length: 100 characters
- Use descriptive variable names

### Documentation
- Add docstrings to all functions and classes
- Update README.md for user-facing changes
- Comment complex algorithms

### Git Commits
- Write clear, concise commit messages
- One logical change per commit
- Reference issue numbers when applicable

## Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/intelligence-memory-training.git
   cd intelligence-memory-training
   ```

2. **Create virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

## Project Structure

```
intelligence-memory-training/
├── app.py              # Main application entry point
├── config.py           # Configuration and settings
├── database.py         # Database management
├── utils.py            # Utility functions
├── requirements.txt    # Python dependencies
├── README.md           # User documentation
└── CONTRIBUTING.md     # This file
```

## Adding New Features

### New Training Module
To add a new training module:

1. Add configuration to `config.py` in `GAME_CONFIGS`
2. Create generator function in `utils.py`
3. Implement game logic in main app
4. Add database support if needed
5. Update documentation

### New Theme
To add a new color theme:

1. Add theme definition to `config.py` in `THEMES`
2. Ensure all UI elements use theme colors
3. Test with all modules
4. Update settings UI

## Testing

Currently, the project uses manual testing. Contributions to add automated tests are welcome!

### Manual Testing Checklist
- [ ] All 6 training modules work
- [ ] Settings save and load correctly
- [ ] Statistics track properly
- [ ] Achievements unlock correctly
- [ ] UI is responsive
- [ ] No console errors
- [ ] Works on Windows/Mac/Linux

## Questions?

Feel free to:
- Open an issue for questions
- Start a discussion
- Contact the maintainers

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow
- Focus on what's best for the project

Thank you for contributing! 🎯
