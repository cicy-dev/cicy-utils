import subprocess
import sys
import os
import platform

def run_cicy_command(args):
    """Run cicy command with Windows-specific handling."""
    if platform.system() == "Windows":
        # On Windows, always use python module execution
        cmd = [sys.executable, "-m", "cicy_utils.cli"] + args
    else:
        # On Unix systems, try cicy command first, fallback to module
        try:
            result = subprocess.run(["cicy"] + args, 
                                  capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                return result
        except (FileNotFoundError, subprocess.TimeoutExpired):
            pass
        cmd = [sys.executable, "-m", "cicy_utils.cli"] + args
    
    return subprocess.run(cmd, capture_output=True, text=True, timeout=30)

def test_cicy_hello_simple():
    """Test that cicy hello --style simple works and contains expected output."""
    result = run_cicy_command(["hello", "--style", "simple"])
    assert result.returncode == 0, f"Command failed with stderr: {result.stderr}, stdout: {result.stdout}"
    assert "Hello, World!" in result.stdout

def test_cicy_hello_with_name():
    """Test that cicy hello with custom name works."""
    result = run_cicy_command(["hello", "--name", "Test", "--style", "simple"])
    assert result.returncode == 0, f"Command failed with stderr: {result.stderr}, stdout: {result.stdout}"
    assert "Hello, Test!" in result.stdout

def test_cicy_version():
    """Test that cicy version command works."""
    result = run_cicy_command(["version"])
    assert result.returncode == 0, f"Command failed with stderr: {result.stderr}, stdout: {result.stdout}"
    assert "0.1.0" in result.stdout
