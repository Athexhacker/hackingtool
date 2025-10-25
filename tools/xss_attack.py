# coding=utf-8
import os
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

from core import HackingTool
from core import HackingToolsCollection

console = Console()


class Dalfox(HackingTool):
    TITLE = "DalFox (Finder of XSS)"
    DESCRIPTION = "XSS Scanning and Parameter Analysis tool."
    INSTALL_COMMANDS = [
        "sudo apt-get install golang",
        "sudo git clone https://github.com/hahwul/dalfox",
        "cd dalfox;go install"
    ]
    RUN_COMMANDS = [
        "~/go/bin/dalfox",
        'echo "You Need To Run manually by using [!]~/go/bin/dalfox [options]"'
    ]
    PROJECT_URL = "https://github.com/hahwul/dalfox"


class XSSPayloadGenerator(HackingTool):
    TITLE = "XSS Payload Generator"
    DESCRIPTION = "XSS PAYLOAD GENERATOR - XSS SCANNER - XSS DORK FINDER"
    INSTALL_COMMANDS = [
        "git clone https://github.com/capture0x/XSS-LOADER.git",
        "cd XSS-LOADER;sudo pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd XSS-LOADER;sudo python3 payloader.py"]
    PROJECT_URL = "https://github.com/capture0x/XSS-LOADER.git"


class XSSFinder(HackingTool):
    TITLE = "Extended XSS Searcher and Finder"
    DESCRIPTION = "Extended XSS Searcher and Finder"
    INSTALL_COMMANDS = [
        "git clone https://github.com/Damian89/extended-xss-search.git"]
    PROJECT_URL = "https://github.com/Damian89/extended-xss-search"

    def after_install(self):
        console.print(Panel.fit(
            "[bold cyan]Follow These Steps After Installation:[/bold cyan]\n"
            "[red]*[/red] Go to [yellow]extended-xss-search[/yellow] directory\n"
            "[green]*[/green] Rename [bold]example.app-settings.conf[/bold] → [bold]app-settings.conf[/bold]",
            title="[ Install Notes ]",
            border_style="magenta"
        ))
        input("Press ENTER to continue")

    def run(self):
        console.print(Panel.fit(
            "[bold cyan]You need to add links to scan[/bold cyan]\n"
            "[red]*[/red] Go to [yellow]extended-xss-search/config/urls-to-test.txt[/yellow]\n"
            "[green]*[/green] Run: [bold]python3 extended-xss-search.py[/bold]",
            title="[ Run Instructions ]",
            border_style="blue"
        ))


class XSSFreak(HackingTool):
    TITLE = "XSS-Freak"
    DESCRIPTION = "An XSS scanner fully written in Python 3 from scratch."
    INSTALL_COMMANDS = [
        "git clone https://github.com/PR0PH3CY33/XSS-Freak.git",
        "cd XSS-Freak;sudo pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd XSS-Freak;sudo python3 XSS-Freak.py"]
    PROJECT_URL = "https://github.com/PR0PH3CY33/XSS-Freak"


class XSpear(HackingTool):
    TITLE = "XSpear"
    DESCRIPTION = "XSpear is an XSS Scanner built on Ruby Gems."
    INSTALL_COMMANDS = ["gem install XSpear"]
    RUN_COMMANDS = ["XSpear -h"]
    PROJECT_URL = "https://github.com/hahwul/XSpear"


class XSSCon(HackingTool):
    TITLE = "XSSCon"
    INSTALL_COMMANDS = [
        "git clone https://github.com/menkrep1337/XSSCon.git",
        "sudo chmod 755 -R XSSCon"
    ]
    PROJECT_URL = "https://github.com/menkrep1337/XSSCon"

    def run(self):
        console.print(Panel.fit(
            "Enter target website to scan with XSSCon:",
            title="[bold yellow]XSSCon[/bold yellow]",
            border_style="bright_yellow"
        ))
        website = Prompt.ask("[bold cyan]Enter Website[/bold cyan]")
        os.system("cd XSSCon;")
        subprocess.run(["python3", "xsscon.py", "-u", website])


class XanXSS(HackingTool):
    TITLE = "XanXSS"
    DESCRIPTION = "Reflected XSS searching tool that creates payloads from templates."
    INSTALL_COMMANDS = ["git clone https://github.com/Ekultek/XanXSS.git"]
    PROJECT_URL = "https://github.com/Ekultek/XanXSS"

    def run(self):
        os.system("cd XanXSS; python xanxss.py -h")
        console.print(
            "[cyan]You have to run it manually using:[/cyan]\n[bold yellow]python xanxss.py [options][/bold yellow]"
        )


class XSSStrike(HackingTool):
    TITLE = "Advanced XSS Detection Suite"
    DESCRIPTION = "XSStrike is a Python-based tool designed to detect and exploit XSS vulnerabilities."
    INSTALL_COMMANDS = [
        "sudo rm -rf XSStrike",
        "git clone https://github.com/UltimateHackers/XSStrike.git "
        "&& cd XSStrike && pip install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/UltimateHackers/XSStrike"

    def __init__(self):
        super(XSSStrike, self).__init__(runnable=False)


class RVuln(HackingTool):
    TITLE = "RVuln"
    DESCRIPTION = "Multi-threaded and Automated Web Vulnerability Scanner written in Rust."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/iinc0gnit0/RVuln.git;"
        "curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh;"
        "source $HOME/.cargo/env;"
        "sudo apt install librust-openssl-dev;"
        "cd RVuln;sudo su;cargo build --release;mv target/release/RVuln"
    ]
    RUN_COMMANDS = ["RVuln"]
    PROJECT_URL = "https://github.com/iinc0gnit0/RVuln"


class XSSAttackTools(HackingToolsCollection):
    TITLE = "XSS Attack Tools"
    TOOLS = [
        Dalfox(),
        XSSPayloadGenerator(),
        XSSFinder(),
        XSSFreak(),
        XSpear(),
        XSSCon(),
        XanXSS(),
        XSSStrike(),
        RVuln()
    ]

    def show_info(self):
        console.print(Panel.fit(
            "[bold magenta]XSS Attack Tools Collection[/bold magenta]\n"
            "A curated set of tools for XSS vulnerability analysis and exploitation.",
            border_style="bright_magenta"
        ))

    def show_options(self, parent=None):
        console.print("\n")
        self.show_info()

        table = Table(title="[bold cyan]Available Tools[/bold cyan]", show_lines=True)
        table.add_column("Index", justify="center", style="bold yellow")
        table.add_column("Tool Name", justify="left", style="bold green")
        table.add_column("Description", justify="left", style="white")

        for i, tool in enumerate(self.TOOLS):
            table.add_row(str(i + 1), tool.TITLE, tool.DESCRIPTION or "—")

        table.add_row("[red]99[/red]", "[bold red]Exit[/bold red]", "Return to Main Menu")

        console.print(table)

        try:
            choice = Prompt.ask("[bold cyan]Select a tool to run[/bold cyan]")
            choice = int(choice)
            if 1 <= choice <= len(self.TOOLS):
                self.TOOLS[choice - 1].show_options(parent=self)
            elif choice == 99:
                return 99
        except Exception:
            console.print("[bold red]Invalid choice. Try again.[/bold red]")
        return self.show_options(parent=parent)
