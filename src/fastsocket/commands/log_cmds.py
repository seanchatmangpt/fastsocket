# src/fastsocket/commands/log_cmds.py
import time

import typer
from pathlib import Path
from rich import print
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.progress import track
import asyncio
import os
import sys

app = typer.Typer(help="Commands related to log management.")

LOG_FILE_PATH = Path("logs/debug.log")
console = Console()


@app.command()
def view_logs(lines: int = typer.Option(100, help="Number of lines to display from the end of the log file.")):
    """
    View the last N lines of the log file.
    """
    if not LOG_FILE_PATH.exists():
        console.print(f"[red]Log file '{LOG_FILE_PATH}' does not exist.[/red]")
        raise typer.Exit(code=1)

    try:
        with LOG_FILE_PATH.open("r") as f:
            lines_to_show = f.readlines()[-lines:]
            syntax = Syntax("".join(lines_to_show), "python", theme="monokai", line_numbers=True)
            console.print(Panel(syntax, title="Last {lines} Log Entries".format(lines=lines)))
    except Exception as e:
        console.print(f"[red]Error reading log file: {e}[/red]")
        raise typer.Exit(code=1)


@app.command()
def clear_logs():
    """
    Clear the log file.
    """
    if not LOG_FILE_PATH.exists():
        console.print(f"[yellow]Log file '{LOG_FILE_PATH}' does not exist. Nothing to clear.[/yellow]")
        raise typer.Exit()

    try:
        LOG_FILE_PATH.unlink()
        LOG_FILE_PATH.touch()
        console.print(f"[green]Log file '{LOG_FILE_PATH}' has been cleared.[/green]")
    except Exception as e:
        console.print(f"[red]Error clearing log file: {e}[/red]")
        raise typer.Exit(code=1)


@app.command()
def tail_logs():
    """
    Tail the log file in real-time.
    """
    if not LOG_FILE_PATH.exists():
        console.print(f"[red]Log file '{LOG_FILE_PATH}' does not exist.[/red]")
        raise typer.Exit(code=1)

    console.print(f"[bold green]Tailing log file: {LOG_FILE_PATH}[/bold green]")
    try:
        with LOG_FILE_PATH.open("r") as f:
            # Go to the end of the file
            f.seek(0, os.SEEK_END)
            while True:
                line = f.readline()
                if not line:
                    # Sleep briefly to wait for new lines
                    time.sleep(0.1)
                    continue
                console.print(line.strip())
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Stopped tailing logs.[/bold yellow]")
    except Exception as e:
        console.print(f"[red]Error tailing log file: {e}[/red]")
        raise typer.Exit(code=1)
