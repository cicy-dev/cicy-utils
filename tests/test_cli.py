import subprocess
import sys
import os

def test_cicy_hello_simple():
    """Test that cicy hello --style simple works and contains expected output."""
    # Try cicy command first, fallback to python module on Windows
    try:
        result = subprocess.run(["cicy", "hello", "--style", "simple"], 
                              capture_output=True, text=True, timeout=30)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        # Fallback for Windows or if cicy command not found
        result = subprocess.run([sys.executable, "-m", "cicy_utils.cli", "hello", "--style", "simple"], 
                              capture_output=True, text=True, timeout=30)
    
    assert result.returncode == 0, f"Command failed with output: {result.stderr}"
    assert "Hello, World!" in result.stdout

def test_cicy_hello_with_name():
    """Test that cicy hello with custom name works."""
    try:
        result = subprocess.run(["cicy", "hello", "--name", "Test", "--style", "simple"], 
                              capture_output=True, text=True, timeout=30)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        result = subprocess.run([sys.executable, "-m", "cicy_utils.cli", "hello", "--name", "Test", "--style", "simple"], 
                              capture_output=True, text=True, timeout=30)
    
    assert result.returncode == 0, f"Command failed with output: {result.stderr}"
    assert "Hello, Test!" in result.stdout

def test_cicy_version():
    """Test that cicy version command works."""
    try:
        result = subprocess.run(["cicy", "version"], 
                              capture_output=True, text=True, timeout=30)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        result = subprocess.run([sys.executable, "-m", "cicy_utils.cli", "version"], 
                              capture_output=True, text=True, timeout=30)
    
    assert result.returncode == 0, f"Command failed with output: {result.stderr}"
    assert "0.1.0" in result.stdout
