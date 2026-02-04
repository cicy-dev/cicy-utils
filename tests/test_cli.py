import subprocess
import sys
import os

def test_cicy_hello_simple():
    """Test that cicy hello --style simple works and contains expected output."""
    # Use the cicy command directly since it's installed
    result = subprocess.run(["cicy", "hello", "--style", "simple"], 
                          capture_output=True, text=True)
    assert result.returncode == 0
    assert "Hello, World!" in result.stdout

def test_cicy_hello_with_name():
    """Test that cicy hello with custom name works."""
    result = subprocess.run(["cicy", "hello", "--name", "Test", "--style", "simple"], 
                          capture_output=True, text=True)
    assert result.returncode == 0
    assert "Hello, Test!" in result.stdout

def test_cicy_version():
    """Test that cicy version command works."""
    result = subprocess.run(["cicy", "version"], 
                          capture_output=True, text=True)
    assert result.returncode == 0
    assert "0.1.0" in result.stdout
