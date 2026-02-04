import subprocess
import sys
import os
import platform

def run_cicy_command(args):
    """Run cicy command with Windows-specific handling."""
    # Always use python module execution for consistency
    cmd = [sys.executable, "-m", "cicy_utils.cli"] + args
    return subprocess.run(cmd, capture_output=True, text=True, timeout=30)

def test_cicy_hello_simple():
    """Test that cicy hello --style simple works and contains expected output."""
    result = run_cicy_command(["hello", "--style", "simple"])
    print(f"Command output: {result.stdout}")
    print(f"Command stderr: {result.stderr}")
    print(f"Return code: {result.returncode}")
    assert result.returncode == 0, f"Command failed with stderr: {result.stderr}, stdout: {result.stdout}"
    assert "Hello, World!" in result.stdout

def test_cicy_hello_with_name():
    """Test that cicy hello with custom name works."""
    result = run_cicy_command(["hello", "--name", "Test", "--style", "simple"])
    print(f"Command output: {result.stdout}")
    print(f"Command stderr: {result.stderr}")
    print(f"Return code: {result.returncode}")
    assert result.returncode == 0, f"Command failed with stderr: {result.stderr}, stdout: {result.stdout}"
    assert "Hello, Test!" in result.stdout

def test_cicy_version():
    """Test that cicy version command works."""
    result = run_cicy_command(["version"])
    print(f"Command output: {result.stdout}")
    print(f"Command stderr: {result.stderr}")
    print(f"Return code: {result.returncode}")
    assert result.returncode == 0, f"Command failed with stderr: {result.stderr}, stdout: {result.stdout}"
    assert "0.1.0" in result.stdout
