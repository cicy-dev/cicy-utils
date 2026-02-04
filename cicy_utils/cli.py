#!/usr/bin/env python3
"""
Cicy Utils CLI - Cross-platform development utilities
"""

import click
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import platform
import sys
import subprocess
import requests
import json
from packaging import version as pkg_version

console = Console()

def get_current_version():
    """Get current version from package"""
    try:
        import importlib.metadata
        return importlib.metadata.version("cicy-utils")
    except Exception:
        return "0.2.0"

def get_latest_version():
    """Get latest version from PyPI"""
    try:
        response = requests.get("https://pypi.org/pypi/cicy-utils/json", timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data["info"]["version"]
    except Exception:
        pass
    return None

@click.group()
@click.version_option(version=get_current_version())
def main():
    """Cicy Utils - Cross-platform development utilities and tools"""
    pass

@main.command()
@click.option('--name', '-n', default='World', help='Name to greet')
@click.option('--style', '-s', 
              type=click.Choice(['simple', 'fancy', 'info']), 
              default='fancy', 
              help='Output style')
def hello(name, style):
    """Say hello with system information"""
    
    if style == 'simple':
        click.echo(f"Hello, {name}!")
        return
    
    # Get system information
    system_info = {
        'Platform': platform.system(),
        'Architecture': platform.machine(),
        'Python Version': f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
        'Node': platform.node(),
    }
    
    if style == 'info':
        console.print(f"[bold green]Hello, {name}![/bold green]")
        console.print("\n[bold blue]System Information:[/bold blue]")
        for key, value in system_info.items():
            console.print(f"  [cyan]{key}:[/cyan] {value}")
        return
    
    # Fancy style (default)
    title = Text(f"Hello, {name}!", style="bold magenta")
    
    info_text = ""
    for key, value in system_info.items():
        info_text += f"[cyan]{key}:[/cyan] [white]{value}[/white]\n"
    
    info_text += f"\n[green]Cicy Utils v{get_current_version()} is ready![/green]"
    
    panel = Panel(
        info_text.strip(),
        title=title,
        border_style="blue",
        padding=(1, 2)
    )
    
    console.print(panel)

@main.command()
def version():
    """Show version information and check for updates"""
    current = get_current_version()
    console.print(f"[bold green]Cicy Utils[/bold green] [cyan]v{current}[/cyan]")
    console.print("Cross-platform development utilities")
    
    # Check for updates
    console.print("\n[yellow]Checking for updates...[/yellow]")
    latest = get_latest_version()
    
    if latest:
        if pkg_version.parse(latest) > pkg_version.parse(current):
            console.print(f"[bold red]Update available![/bold red] Latest version: [green]v{latest}[/green]")
            console.print("Run [bold cyan]cicy update[/bold cyan] to upgrade")
        else:
            console.print("[green]You have the latest version![/green]")
    else:
        console.print("[yellow]Could not check for updates[/yellow]")

@main.command()
def ip():
    """Get public IP information from api.myip.com"""
    try:
        console.print("[yellow]Fetching IP information...[/yellow]")
        response = requests.get("https://api.myip.com", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            # Display detailed information
            console.print("\n[bold green]IP Information:[/bold green]")
            console.print(f"[cyan]IP Address:[/cyan] [white]{data.get('ip', 'N/A')}[/white]")
            console.print(f"[cyan]Country:[/cyan] [white]{data.get('country', 'N/A')}[/white]")
            console.print(f"[cyan]Country Code:[/cyan] [white]{data.get('cc', 'N/A')}[/white]")
            
            # Show just the IP in simple format
            console.print(f"\n[bold]Your IP:[/bold] [green]{data.get('ip', 'N/A')}[/green]")
            
        else:
            console.print(f"[red]Failed to get IP information. Status: {response.status_code}[/red]")
            
    except requests.exceptions.RequestException as e:
        console.print(f"[red]Network error: {e}[/red]")
    except json.JSONDecodeError:
        console.print("[red]Invalid response format[/red]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")

@main.command()
def update():
    """Update cicy-utils to the latest version"""
    current = get_current_version()
    latest = get_latest_version()
    
    if not latest:
        console.print("[red]Could not check for updates[/red]")
        return
    
    if pkg_version.parse(latest) <= pkg_version.parse(current):
        console.print(f"[green]Already up to date! (v{current})[/green]")
        return
    
    console.print(f"[yellow]Updating from v{current} to v{latest}...[/yellow]")
    
    try:
        # Update using pip
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "--upgrade", "cicy-utils"
        ], capture_output=True, text=True, check=True)
        
        console.print(f"[green]Successfully updated to v{latest}![/green]")
        console.print("Run [bold cyan]cicy version[/bold cyan] to verify the update")
        
    except subprocess.CalledProcessError as e:
        console.print(f"[red]Update failed: {e}[/red]")
        console.print("Try running: [bold]pip install --upgrade cicy-utils[/bold]")

if __name__ == '__main__':
    main()
