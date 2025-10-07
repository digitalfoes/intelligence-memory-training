# 🔨 Simple Build Guide

## Super Simple - One Command

```bash
pyinstaller --onefile --windowed --name=MemoryTraining app.py
```

**That's it!** Your executable will be in `dist/MemoryTraining`

---

## Step-by-Step

### 1. Install PyInstaller (one time only)
```bash
pip install pyinstaller
```

### 2. Build
```bash
pyinstaller --onefile --windowed --name=MemoryTraining app.py
```

### 3. Find Your Executable
```
dist/MemoryTraining.exe     (Windows)
dist/MemoryTraining         (macOS/Linux)
```

---

## Alternative: Use Build Script

```bash
python build.py
```

Or on Linux/Mac:
```bash
./build.sh
```

---

## Distribution

### Windows
- Share `dist/MemoryTraining.exe`
- Users just double-click to run
- No Python installation needed

### macOS
- Share `dist/MemoryTraining`
- Users may need to allow in Security settings
- No Python installation needed

### Linux
- Share `dist/MemoryTraining`
- Make executable: `chmod +x MemoryTraining`
- No Python installation needed

---

## Troubleshooting

**"PyInstaller not found"**
```bash
pip install pyinstaller
```

**"Module not found" errors**
```bash
pip install -r requirements.txt
```

**Build too large?**
Use `--onefile` flag (already included)

**Need console for debugging?**
Remove `--windowed` flag from build.py

---

## File Sizes (Approximate)

- Windows: ~15-25 MB
- macOS: ~15-25 MB
- Linux: ~15-25 MB

---

**Build once, run anywhere!** 🚀
