import subprocess
import sys

def test_cicy_hello_simple():
    """Test that cicy hello --style simple works and contains expected output."""
    cmd = [sys.executable, "-m", "cicy_utils.cli", "hello", "--style", "simple"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0
    assert "Hello, World!" in result.stdout

def test_cicy_hello_with_name():
    """Test that cicy hello with custom name works."""
    cmd = [sys.executable, "-m", "cicy_utils.cli", "hello", "--name", "Test", "--style", "simple"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0
    assert "Hello, Test!" in result.stdout

def test_cicy_version():
    """Test that cicy version command works."""
    cmd = [sys.executable, "-m", "cicy_utils.cli", "version"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0
    assert "0.1.0" in result.stdout
