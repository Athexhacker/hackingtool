# coding=utf-8
import contextlib
import os
import subprocess

from core import HackingTool
from core import HackingToolsCollection

from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich import box

_theme = Theme({"purple": "#7B61FF"})
console = Console(theme=_theme)


class InstaBrute(HackingTool):
    TITLE = "Instagram Attack"
    DESCRIPTION = "Brute force attack against Instagram"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/chinoogawa/instaBrute.git",
        "cd instaBrute;sudo pip2.7 install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/chinoogawa/instaBrute"

    def run(self):
        name = input("Enter Username >> ")
        wordlist = input("Enter wordword list >> ")
        os.chdir("instaBrute")
        subprocess.run(
            ["sudo", "python", "instaBrute.py", "-u", f"{name}", "-d",
             f"{wordlist}"])


class BruteForce(HackingTool):
    TITLE = "AllinOne SocialMedia Attack"
    DESCRIPTION = "Brute_Force_Attack Gmail Hotmail Twitter Facebook Netflix \n" \
                  "[!] python3 Brute_Force.py -g <Account@gmail.com> -l <File_list>"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Matrix07ksa/Brute_Force.git",
        "cd Brute_Force;sudo pip3 install proxylist;pip3 install mechanize"
    ]
    RUN_COMMANDS = ["cd Brute_Force;python3 Brute_Force.py -h"]
    PROJECT_URL = "https://github.com/Matrix07ksa/Brute_Force"


class Faceshell(HackingTool):
    TITLE = "Facebook Attack"
    DESCRIPTION = "Facebook BruteForcer"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Matrix07ksa/Brute_Force.git",
        "cd Brute_Force;sudo pip3 install proxylist;pip3 install mechanize"
    ]
    PROJECT_URL = "https://github.com/Matrix07ksa/Brute_Force"

    def run(self):
        name = input("Enter Username >> ")
        wordlist = input("Enter Wordlist >> ")
        with contextlib.suppress(FileNotFoundError):
            os.chdir("Brute_Force")
        subprocess.run(
            ["python3", "Brute_Force.py", "-f", f"{name}", "-l", f"{wordlist}"])


class AppCheck(HackingTool):
    TITLE = "Application Checker"
    DESCRIPTION = "Tool to check if an app is installed on the target device through a link."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/jakuta-tech/underhanded.git",
        "cd underhanded && sudo chmod +x underhanded.sh"
    ]
    RUN_COMMANDS = ["cd underhanded;sudo bash underhanded.sh"]
    PROJECT_URL = "https://github.com/jakuta-tech/underhanded"


class SocialMediaBruteforceTools(HackingToolsCollection):
    TITLE = "SocialMedia Bruteforce"
    TOOLS = [
        InstaBrute(),
        BruteForce(),
        Faceshell(),
        AppCheck()
    ]

    def pretty_print(self):
        table = Table(title="Social Media Bruteforce Tools", show_lines=True, expand=True)
        table.add_column("Title", style="purple", no_wrap=True)
        table.add_column("Description", style="purple")
        table.add_column("Project URL", style="purple", no_wrap=True)

        for t in self.TOOLS:
            desc = getattr(t, "DESCRIPTION", "") or ""
            url = getattr(t, "PROJECT_URL", "") or ""
            table.add_row(t.TITLE, desc.strip().replace("\n", " "), url)

        panel = Panel(table, title="[purple]Available Tools[/purple]", border_style="purple")
        console.print(panel)

    def show_options(self, parent=None):
        console.print("\n")
        panel = Panel.fit("[bold magenta]Social Media Bruteforce Collection[/bold magenta]\n"
                          "Select a tool to view details or run it.",
                          border_style="purple")
        console.print(panel)

        table = Table(title="[bold cyan]Available Tools[/bold cyan]", show_lines=True, expand=True)
        table.add_column("Index", justify="center", style="bold yellow")
        table.add_column("Tool Name", justify="left", style="bold green")
        table.add_column("Description", justify="left", style="white")

        for i, tool in enumerate(self.TOOLS):
            title = getattr(tool, "TITLE", tool.__class__.__name__)
            desc = getattr(tool, "DESCRIPTION", "—")
            table.add_row(str(i + 1), title, desc or "—")

        table.add_row("[red]99[/red]", "[bold red]Exit[/bold red]", "Return to previous menu")
        console.print(table)

        try:
            choice = Prompt.ask("[bold cyan]Select a tool to view/run[/bold cyan]", default="99")
            choice = int(choice)
            if 1 <= choice <= len(self.TOOLS):
                selected = self.TOOLS[choice - 1]
                if hasattr(selected, "show_options"):
                    selected.show_options(parent=self)
                elif hasattr(selected, "run"):
                    selected.run()
                elif hasattr(selected, "show_info"):
                    selected.show_info()
                else:
                    console.print("[bold yellow]Selected tool has no runnable interface.[/bold yellow]")
            elif choice == 99:
                return 99
        except Exception:
            console.print("[bold red]Invalid choice. Try again.[/bold red]")
        return self.show_options(parent=parent)


if __name__ == "__main__":
    tools = SocialMediaBruteforceTools()
    tools.pretty_print()
    tools.show_options()