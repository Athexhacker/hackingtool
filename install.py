#!/usr/bin/env python3
# install_hackingtool.py  (rich-based installer UI)
import os
import sys
import shutil
import subprocess
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt, Confirm, IntPrompt
from rich.table import Table
from rich.align import Align
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text
from rich import box
from random import choice

console = Console()

REPO_URL = "https://github.com/Athexhacker/hackingtool.git"
INSTALL_DIR = Path("/usr/share/hackingtool")
BIN_PATH = Path("/usr/bin/hackingtool")
VENV_DIR_NAME = "venv"
REQUIREMENTS = "requirements.txt"


def check_root():
    if os.geteuid() != 0:
        console.print(Panel("[green]This installer must be run as root. Use: sudo python3 install_hackingtool.py[/green]"))
        sys.exit(1)


def run_cmd(cmd, check=True, capture=False, env=None):
    return subprocess.run(cmd, shell=True, check=check, capture_output=capture, text=True, env=env)


def colorful_logo():
    logos = ["green", "bright_green", "green", "green", "green", "green"]
    style = choice(logos)
    logo_lines = r"""
███████╗              ███████╗ ██████╗  ██████╗██╗███████╗████████╗██╗   ██╗
██╔════╝              ██╔════╝██╔═══██╗██╔════╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝
█████╗      █████╗    ███████╗██║   ██║██║     ██║█████╗     ██║    ╚████╔╝ 
██╔══╝      ╚════╝    ╚════██║██║   ██║██║     ██║██╔══╝     ██║     ╚██╔╝  
██║                   ███████║╚██████╔╝╚██████╗██║███████╗   ██║      ██║   
╚═╝                   ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚══════╝   ╚═╝      ╚═╝ 
                                                                     
"""
    panel = Panel(Text(logo_lines, style=style), box=box.DOUBLE, border_style=style)
    console.print(panel)
    console.print(f"[bold {style}]https://github.com/Athexhacker/hackingtool[/bold {style}]\n")


def choose_distro():
    console.print(Panel("[bold green]Select installation target[/bold green]\n\n[1] Kali / Parrot (apt)\n[2] Arch (pacman)\n[0] Exit", border_style="bright_green"))
    choice = IntPrompt.ask("Choice", choices=["0", "1", "2"], default=1)
    return choice


def check_internet():
    console.print("[green]* Checking internet connectivity...[/green]")
    try:
        run_cmd("curl -sSf --max-time 10 https://www.google.com > /dev/null", check=True)
        console.print("[green][✔] Internet connection OK[/green]")
        return True
    except Exception:
        try:
            run_cmd("curl -sSf --max-time 10 https://github.com > /dev/null", check=True)
            console.print("[green][✔] Internet connection OK[/green]")
            return True
        except Exception:
            console.print("[green][✘] Internet connection not available[/green]")
            return False


def system_update_and_install(choice):
    if choice == 1:
        console.print("[green]* Running apt update/upgrade...[/green]")
        try:
            run_cmd("apt update -y && apt upgrade -y")
        except subprocess.CalledProcessError as e:
            console.print(f"[green][!][/green] apt update/upgrade failed (non-fatal). Continuing installation. Error: {e}")
        console.print("[green]* Installing required packages (apt)...[/green]")
        try:
            run_cmd("apt-get install -y git python3-pip python3-venv figlet boxes php curl xdotool wget")
        except subprocess.CalledProcessError as e:
            console.print(f"[green][!][/green] apt-get install failed (non-fatal). You may need to install some packages manually. Error: {e}")
    elif choice == 2:
        console.print("[green]* Running pacman update...[/green]")
        try:
            run_cmd("pacman -Syu --noconfirm")
        except subprocess.CalledProcessError as e:
            console.print(f"[green][!][/green] pacman update failed (non-fatal). Continuing installation. Error: {e}")
        console.print("[green]* Installing required packages (pacman)...[/green]")
        try:
            run_cmd("pacman -S --noconfirm git python-pip")
        except subprocess.CalledProcessError as e:
            console.print(f"[green][!][/green] pacman install failed (non-fatal). You may need to install some packages manually. Error: {e}")
    else:
        console.print("[green]Invalid package manager choice[/green]")


def prepare_install_dir():
    if INSTALL_DIR.exists():
        console.print(f"[green]The directory {INSTALL_DIR} already exists.[/green]")
        if Confirm.ask("Replace it? This will remove the existing directory", default=False):
            run_cmd(f"rm -rf {str(INSTALL_DIR)}")
        else:
            console.print("[green]Installation aborted by user.[/green]")
            sys.exit(1)
    INSTALL_DIR.mkdir(parents=True, exist_ok=True)


def git_clone():
    console.print("[green]* Cloning hackingtool repository...[/green]")
    try:
        run_cmd(f"git clone {REPO_URL} {str(INSTALL_DIR)}")
        console.print("[green][✔] Repository cloned[/green]")
        return True
    except Exception as e:
        console.print(f"[green][✘] Failed to clone repository: {e}[/green]")
        return False


def create_venv_and_install(choice):
    venv_path = INSTALL_DIR / VENV_DIR_NAME
    console.print("[green]* Creating virtual environment...[/green]")
    run_cmd(f"python3 -m venv {str(venv_path)}")
    activate = venv_path / "bin" / "activate"
    pip = str(venv_path / "bin" / "pip")
    if (INSTALL_DIR / REQUIREMENTS).exists():
        console.print("[green]* Installing Python requirements...[/green]")
        run_cmd(f"{pip} install -r {str(INSTALL_DIR / REQUIREMENTS)}")
    else:
        console.print("[green]requirements.txt not found, skipping pip install.[/green]")
    if choice == 1:
        run_cmd("apt install figlet -y")
    elif choice == 2:
        # try pacman and fallback to AUR instructions
        try:
            run_cmd("pacman -S --noconfirm figlet")
        except Exception:
            console.print("[green]figlet not available in pacman automatically. Consider installing from AUR.[/green]")


def create_launcher():
    console.print("[green]* Creating launcher script...[/green]")
    launcher = INSTALL_DIR / "hackingtool.sh"
    with open(launcher, "w") as f:
        f.write("#!/bin/bash\n")
        f.write(f"source {str(INSTALL_DIR / VENV_DIR_NAME)}/bin/activate\n")
        f.write(f"python3 {str(INSTALL_DIR / 'hackingtool.py')} \"$@\"\n")
    os.chmod(launcher, 0o755)
    # move to /usr/bin/hackingtool
    if BIN_PATH.exists():
        BIN_PATH.unlink()
    shutil.move(str(launcher), str(BIN_PATH))
    console.print(f"[green][✔] Launcher installed at {str(BIN_PATH)}[/green]")


def final_messages():
    panel = Panel(
        "[bold green]Installation complete[/bold green]\n\nType [bold green]hackingtool[/bold green] in terminal to start.",
        border_style="green",
    )
    console.print(panel)

def main():
    check_root()
    console.clear()
    colorful_logo()
    choice = choose_distro()
    if choice == 0:
        console.print("[green]Exiting...[/green]")
        sys.exit(0)
    if not check_internet():
        sys.exit(1)

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
        progress.add_task(description="Preparing system...", total=None)
        system_update_and_install(choice)

    prepare_install_dir()
    ok = git_clone()
    if not ok:
        sys.exit(1)

    with Progress(SpinnerColumn(), TextColumn("[progress.description]{task.description}")) as progress:
        progress.add_task(description="Setting up virtualenv & requirements...", total=None)
        create_venv_and_install(choice)

    create_launcher()
    final_messages()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[green]Installation interrupted by user[/green]")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        console.print(f"[green]Command failed: {e}[/green]")
        sys.exit(1)
