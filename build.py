#!/usr/bin/env python3
"""
Simple build script for Intelligence Memory Training
Creates standalone executables for Windows, macOS, and Linux
"""
import os
import sys
import subprocess
import platform

def build():
    """Build standalone executable."""
    print("🔨 Building Intelligence Memory Training...")
    print(f"Platform: {platform.system()}")
    
    # PyInstaller command
    cmd = [
        'pyinstaller',
        '--onefile',                    # Single executable
        '--windowed',                   # No console window
        '--name=MemoryTraining',        # Executable name
        '--icon=icon.ico',              # Icon (if exists)
        '--add-data=config.py:.',       # Include config
        '--add-data=database.py:.',     # Include database
        '--add-data=utils.py:.',        # Include utils
        '--hidden-import=sqlite3',      # Ensure sqlite3 included
        '--hidden-import=tkinter',      # Ensure tkinter included
        'app.py'
    ]
    
    # Remove icon if it doesn't exist
    if not os.path.exists('icon.ico'):
        cmd.remove('--icon=icon.ico')
    
    try:
        subprocess.run(cmd, check=True)
        print("\n✅ Build successful!")
        print(f"📦 Executable location: dist/MemoryTraining")
        print(f"   Windows: dist/MemoryTraining.exe")
        print(f"   macOS/Linux: dist/MemoryTraining")
    except subprocess.CalledProcessError:
        print("\n❌ Build failed!")
        print("Make sure PyInstaller is installed: pip install pyinstaller")
        sys.exit(1)
    except FileNotFoundError:
        print("\n❌ PyInstaller not found!")
        print("Install it with: pip install pyinstaller")
        sys.exit(1)

if __name__ == '__main__':
    build()
