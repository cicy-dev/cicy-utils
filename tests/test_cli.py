import subprocess
import sys
import os

def test_cicy_hello_simple():
    """Test that cicy hello --style simple works and contains expected output."""
    # Direct module execution - most reliable on Windows
    cmd = [sys.executable, "-m", "cicy_utils.cli", "hello", "--style", "simple"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
    print(f"Command: {' '.join(cmd)}")
    print(f"Return code: {result.returncode}")
    print(f"Stdout: {repr(result.stdout)}")
    print(f"Stderr: {repr(result.stderr)}")
    
    assert result.returncode == 0, f"Command failed: {result.stderr}"
    assert "Hello, World!" in result.stdout, f"Expected output not found in: {result.stdout}"

def test_cicy_hello_with_name():
    """Test that cicy hello with custom name works."""
    cmd = [sys.executable, "-m", "cicy_utils.cli", "hello", "--name", "Test", "--style", "simple"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
    print(f"Command: {' '.join(cmd)}")
    print(f"Return code: {result.returncode}")
    print(f"Stdout: {repr(result.stdout)}")
    print(f"Stderr: {repr(result.stderr)}")
    
    assert result.returncode == 0, f"Command failed: {result.stderr}"
    assert "Hello, Test!" in result.stdout, f"Expected output not found in: {result.stdout}"

def test_cicy_version():
    """Test that cicy version command works."""
    cmd = [sys.executable, "-m", "cicy_utils.cli", "version"]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    
    print(f"Command: {' '.join(cmd)}")
    print(f"Return code: {result.returncode}")
    print(f"Stdout: {repr(result.stdout)}")
    print(f"Stderr: {repr(result.stderr)}")
    
    assert result.returncode == 0, f"Command failed: {result.stderr}"
    assert "0.1.0" in result.stdout, f"Expected version not found in: {result.stdout}"
