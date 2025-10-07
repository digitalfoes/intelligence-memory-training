"""
Setup script for Intelligence Memory Training
"""
from setuptools import setup, find_packages
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="intelligence-memory-training",
    version="2.0.0",
    author="Intelligence Memory Training Project",
    author_email="",
    description="Develop photographic memory and rapid recall skills for intelligence work",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/intelligence-memory-training",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Education",
        "Topic :: Games/Entertainment :: Puzzle Games",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Environment :: X11 Applications",
        "Environment :: Win32 (MS Windows)",
        "Environment :: MacOS X",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "memory-training=app:main",
        ],
    },
    include_package_data=True,
    keywords="memory training intelligence photographic-memory brain-training education",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/intelligence-memory-training/issues",
        "Source": "https://github.com/yourusername/intelligence-memory-training",
        "Documentation": "https://github.com/yourusername/intelligence-memory-training#readme",
    },
)
