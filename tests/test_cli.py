import subprocess
import sys
import re

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
    # Use regex to match version pattern instead of hardcoded version
    version_pattern = r"Cicy Utils v\d+\.\d+\.\d+"
    assert re.search(version_pattern, result.stdout), f"Version pattern not found in: {result.stdout}"

def test_cicy_ip():
    """Test that cicy ip command works."""
    cmd = [sys.executable, "-m", "cicy_utils.cli", "ip"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0
    # Allow for various outcomes since network calls can fail
    success_indicators = [
        "IP Address:",
        "Network error:",
        "Failed to get IP",
        "Fetching IP information"
    ]
    assert any(indicator in result.stdout for indicator in success_indicators), \
        f"No expected output found in: {result.stdout}"

def test_cicy_help():
    """Test that cicy --help works."""
    cmd = [sys.executable, "-m", "cicy_utils.cli", "--help"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    assert result.returncode == 0
    assert "Cicy Utils" in result.stdout
    assert "Commands:" in result.stdout
