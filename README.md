# 🧠 Intelligence Memory Training

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)](https://github.com/yourusername/intelligence-memory-training)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

A focused training program for developing photographic memory and rapid recall skills useful in intelligence work, security, and professional fields requiring exceptional memory.

![Screenshot](docs/screenshot.png)

## ⭐ Features

- **6 Training Modules** - Diverse exercises for comprehensive memory development
- **Progressive Difficulty** - Automatic scaling based on performance
- **Multiple Themes** - Dark, Light, and Blue color schemes
- **Achievement System** - 10 unlockable achievements
- **Practice Mode** - Train without pressure
- **Statistics Tracking** - Detailed performance analytics
- **Daily Challenges** - New goals every day
- **Offline First** - No internet required
- **Cross-Platform** - Works on Windows, macOS, and Linux

## 📋 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Training Modules](#-training-modules)
- [Installation](#-installation)
- [Usage](#-usage)
- [Configuration](#-configuration)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/intelligence-memory-training.git
cd intelligence-memory-training

# Run the application
python app.py
```

That's it! No installation required. Python 3.7+ with tkinter (included by default).

## Overview

This application provides six training exercises designed to improve:
- Code and document memorization
- Vehicle identification and tracking
- Facial recognition and profiling
- Number sequence retention
- Environmental observation
- Route and navigation memory

## 💻 Installation

### Option 1: Run Directly (Recommended)
```bash
python app.py
```

### Option 2: Install as Package
```bash
pip install -e .
memory-training
```

### Option 3: Build Executable
```bash
pip install pyinstaller
pyinstaller --onefile --windowed app.py
```

**Requirements:** Python 3.7+ with tkinter (included by default)

## Training Modules

### 1. Document Codes
Memorize and reproduce alphanumeric codes and access identifiers.

**Use cases:** Passwords, document references, access codes  
**Progression:** 6 characters → 15+ characters  
**Skills:** Pattern recognition, chunking, visual encoding

### 2. License Plates
Track and recall multiple vehicle identification numbers.

**Use cases:** Surveillance, vehicle tracking, parking enforcement  
**Progression:** 3 vehicles → 8+ vehicles  
**Skills:** Multi-target tracking, sequential memory

### 3. Face Recognition
Remember faces with identifying features and physical descriptions.

**Use cases:** Security, witness identification, networking  
**Progression:** Basic profiles → Complex multi-feature profiles  
**Skills:** Facial feature retention, detail observation

### 4. Number Sequences
Retain multi-digit codes and combinations.

**Use cases:** Safe combinations, PIN codes, phone numbers  
**Progression:** 4 digits → 12+ digits  
**Skills:** Numerical memory, rhythm techniques

### 5. Scene Details
Observe environments and identify changes or missing elements.

**Use cases:** Security inspection, evidence collection, awareness  
**Progression:** 5 items → 12+ items  
**Skills:** Environmental scanning, change detection

### 6. Route Memory
Memorize directional sequences and navigation routes.

**Use cases:** Navigation without GPS, escape planning, territory knowledge  
**Progression:** 3 waypoints → 10+ waypoints  
**Skills:** Spatial memory, sequential directions

## How It Works

1. **Select a module** from the main menu
2. **Study the information** presented (codes, faces, items, etc.)
3. **Recall from memory** when prompted
4. **Progress through levels** - each success increases difficulty
5. **Track your improvement** via the statistics page

## Scoring

- **Points:** Level × 10 per successful round
- **Progression:** Automatic difficulty increase
- **Failure:** One mistake ends the session
- **Statistics:** Tracked automatically in `omts_stats.json`

## Training Tips

**General Techniques:**
- **Chunking** - Break information into smaller segments
- **Visualization** - Create mental images
- **Association** - Link to familiar concepts
- **Repetition** - Mental rehearsal during display time
- **Patterns** - Look for sequences and structures

**Module-Specific:**
- **Document Codes:** Group by segments (AB-12 not AB12)
- **License Plates:** Create stories linking plates together
- **Faces:** Focus on distinguishing features first
- **Numbers:** Use rhythm or pair grouping
- **Scenes:** Systematic left-to-right scanning
- **Routes:** Visualize yourself moving through the path

## Recommended Practice

**Beginners (Weeks 1-2):**
- 15 minutes daily
- Focus on Document Codes and Number Sequences
- Goal: Reach Level 3

**Intermediate (Weeks 3-6):**
- 20 minutes daily
- Practice all modules
- Goal: Reach Level 7 in all modules

**Advanced (2+ months):**
- 25-30 minutes daily
- Focus on weak areas
- Goal: Level 10+ across all modules

## Real-World Applications

**Professional:**
- Security and law enforcement
- Intelligence and investigation work
- Executive protection
- Corporate security

**Academic:**
- Exam preparation
- Research data retention
- Language learning
- Technical memorization

**Personal:**
- Remember names and faces
- Navigate without GPS
- Recall phone numbers
- Shopping without lists

## Performance Tracking

The application automatically tracks:
- Sessions played per module
- Best score achieved
- Average performance

View your statistics anytime from the main menu.

## ⚙️ Configuration

The application supports extensive customization through `settings.json`:

### Themes
- **Dark** (default) - Easy on the eyes for extended sessions
- **Light** - For bright environments
- **Blue** - Alternative dark theme

### Difficulty Levels
- **Easy** - Longer display times, slower progression
- **Medium** (default) - Balanced challenge
- **Hard** - Quick display times, rapid progression

### Other Settings
- Sound effects (on/off)
- Hints display (on/off)
- Font size (small/medium/large)
- Practice mode (on/off)
- Timer display (on/off)
- Colorblind mode (on/off)

Access settings through the main menu or edit `settings.json` directly.

## 📊 Statistics & Analytics

Track your progress with comprehensive statistics:
- **Session History** - View all past training sessions
- **Performance Metrics** - Best scores, averages, accuracy
- **Progress Graphs** - Visual representation of improvement
- **Achievement Tracking** - Unlock 10 unique achievements
- **Daily Challenges** - Complete special goals
- **Export Data** - Backup your progress to JSON/CSV

## 🏆 Achievements

Unlock achievements as you progress:
- 🎯 **First Steps** - Complete your first session
- 💪 **Dedicated Trainee** - Complete 10 sessions
- 🏆 **Memory Master** - Complete 50 sessions
- ⭐ **Rising Star** - Reach level 5
- 🌟 **Expert** - Reach level 10
- 💎 **Legendary** - Reach level 15
- 🎖️ **Perfect Memory** - Score 200+ points
- 🎓 **Well Rounded** - Complete all 6 modules
- 🔥 **On Fire** - 5 correct answers in a row
- ⚡ **Unstoppable** - 10 correct answers in a row

## 📁 Project Structure

```
intelligence-memory-training/
├── app.py              # Main application entry point
├── config.py           # Configuration and settings management
├── database.py         # SQLite database operations
├── utils.py            # Utility functions and generators
├── requirements.txt    # Python dependencies
├── setup.py            # Package installation script
├── settings.json       # User preferences (auto-generated)
├── memory_stats.db     # Statistics database (auto-generated)
├── README.md           # This file
├── CONTRIBUTING.md     # Contribution guidelines
├── CHANGELOG.md        # Version history
├── LICENSE             # MIT License
└── .github/            # GitHub templates and workflows
    ├── workflows/
    │   └── python-app.yml
    ├── ISSUE_TEMPLATE/
    └── pull_request_template.md
```

## 🔧 Technical Details

- **Platform:** Cross-platform (Windows, macOS, Linux)
- **Language:** Python 3.7+
- **GUI Framework:** tkinter (built-in)
- **Database:** SQLite3 (built-in)
- **Dependencies:** Optional (matplotlib, pillow for advanced features)
- **Storage:** Local SQLite database
- **Network:** Fully offline, no telemetry

## Tips for Success

1. **Consistency** - Daily practice beats occasional long sessions
2. **Focus** - Eliminate distractions during training
3. **Rest** - Ensure adequate sleep for memory consolidation
4. **Patience** - Improvement takes time and regular practice
5. **Application** - Use these skills in daily life

## Troubleshooting

**Can't progress past a level?**
- Slow down during observation
- Use more memory techniques
- Practice the specific module offline

**Inconsistent performance?**
- Train at the same time daily
- Ensure proper rest and hydration
- Reduce external stressors

**Specific module difficulty?**
- Review technique tips above
- Start at lower levels to build confidence
- Practice related real-world exercises

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Ways to Contribute
- 🐛 Report bugs
- 💡 Suggest features
- 📝 Improve documentation
- 🔧 Submit pull requests
- ⭐ Star the repository

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by cognitive science research on memory training
- Built with Python and tkinter
- Community contributions and feedback

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/yourusername/intelligence-memory-training/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/intelligence-memory-training/discussions)
- **Documentation:** [Wiki](https://github.com/yourusername/intelligence-memory-training/wiki)

## 🗺️ Roadmap

See [CHANGELOG.md](CHANGELOG.md) for upcoming features and version history.

### Coming Soon
- Progress graphs and visualizations
- Sound effects and audio feedback
- Tutorial mode for beginners
- Custom training scenarios
- Mobile companion app

---

**Start developing your memory skills today! 🧠✨**

Made with ❤️ for intelligence professionals, students, and memory enthusiasts.
