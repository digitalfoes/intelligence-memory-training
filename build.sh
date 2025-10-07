#!/bin/bash
# Simple build script for Intelligence Memory Training

echo "🔨 Building Memory Training executable..."

# Check if pyinstaller is available
if ! command -v pyinstaller &> /dev/null; then
    echo "Installing PyInstaller..."
    pip3 install --user pyinstaller
fi

# Build the executable
pyinstaller --onefile --windowed --name=MemoryTraining \
    --add-data="config.py:." \
    --add-data="database.py:." \
    --add-data="utils.py:." \
    app.py

echo ""
echo "✅ Build complete!"
echo "📦 Executable: dist/MemoryTraining"
