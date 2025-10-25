# coding=utf-8
import subprocess
from core import HackingTool
from core import HackingToolsCollection

from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

_theme = Theme({"purple": "#7B61FF"})
console = Console(theme=_theme)


class Web2Attack(HackingTool):
    TITLE = "Web2Attack"
    DESCRIPTION = "Web hacking framework with tools, exploits by python"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/santatic/web2attack.git"
    ]
    RUN_COMMANDS = ["cd web2attack && sudo python3 w2aconsole"]
    PROJECT_URL = "https://github.com/santatic/web2attack"


class Skipfish(HackingTool):
    TITLE = "Skipfish"
    DESCRIPTION = (
        "Skipfish – Fully automated, active web application "
        "security reconnaissance tool \n "
        "Usage: skipfish -o [FolderName] targetip/site"
    )
    RUN_COMMANDS = [
        "sudo skipfish -h",
        'echo "skipfish -o [FolderName] targetip/site"|boxes -d headline | lolcat'
    ]

    def __init__(self):
        super(Skipfish, self).__init__(installable=False)


class SubDomainFinder(HackingTool):
    TITLE = "SubDomain Finder"
    DESCRIPTION = (
        "Sublist3r is a python tool designed to enumerate "
        "subdomains of websites using OSINT \n "
        "Usage:\n\t[1] python3 sublist3r.py -d example.com \n"
        "[2] python3 sublist3r.py -d example.com -p 80,443"
    )
    INSTALL_COMMANDS = [
        "sudo pip3 install requests argparse dnspython",
        "sudo git clone https://github.com/aboul3la/Sublist3r.git",
        "cd Sublist3r && sudo pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd Sublist3r && python3 sublist3r.py -h"]
    PROJECT_URL = "https://github.com/aboul3la/Sublist3r"


class CheckURL(HackingTool):
    TITLE = "CheckURL"
    DESCRIPTION = (
        "Detect evil urls that uses IDN Homograph Attack.\n\t"
        "[!] python3 checkURL.py --url google.com"
    )
    INSTALL_COMMANDS = ["sudo git clone https://github.com/UndeadSec/checkURL.git"]
    RUN_COMMANDS = ["cd checkURL && python3 checkURL.py --help"]
    PROJECT_URL = "https://github.com/UndeadSec/checkURL"


class Blazy(HackingTool):
    TITLE = "Blazy(Also Find ClickJacking)"
    DESCRIPTION = "Blazy is a modern login page bruteforcer"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/UltimateHackers/Blazy.git",
        "cd Blazy && sudo pip2.7 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd Blazy && sudo python2.7 blazy.py"]
    PROJECT_URL = "https://github.com/UltimateHackers/Blazy"


class SubDomainTakeOver(HackingTool):
    TITLE = "Sub-Domain TakeOver"
    DESCRIPTION = (
        "Sub-domain takeover vulnerability occur when a sub-domain "
        "\n (subdomain.example.com) is pointing to a service "
        "(e.g: GitHub, AWS/S3,..)\nthat has been removed or deleted.\n"
        "Usage:python3 takeover.py -d www.domain.com -v"
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/edoardottt/takeover.git",
        "cd takeover;sudo python3 setup.py install"
    ]
    PROJECT_URL = "https://github.com/edoardottt/takeover"

    def __init__(self):
        super(SubDomainTakeOver, self).__init__(runnable=False)


class Dirb(HackingTool):
    TITLE = "Dirb"
    DESCRIPTION = (
        "DIRB is a Web Content Scanner. It looks for existing "
        "(and/or hidden) Web Objects.\n"
        "It basically works by launching a dictionary based "
        "attack against \n a web server and analyzing the response."
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://gitlab.com/kalilinux/packages/dirb.git",
        "cd dirb;sudo bash configure;make"
    ]
    PROJECT_URL = "https://gitlab.com/kalilinux/packages/dirb"

    def run(self):
        uinput = input("Enter Url >> ")
        subprocess.run(["sudo", "dirb", uinput])


class WebAttackTools(HackingToolsCollection):
    TITLE = "Web Attack tools"
    DESCRIPTION = ""
    TOOLS = [
        Web2Attack(),
        Skipfish(),
        SubDomainFinder(),
        CheckURL(),
        Blazy(),
        SubDomainTakeOver(),
        Dirb()
    ]

    def pretty_print(self):
        table = Table(title="Web Attack Tools", show_lines=True, expand=True)
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
        panel = Panel.fit("[bold magenta]Web Attack Tools Collection[/bold magenta]\n"
                          "Select a tool to view options or run it.",
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
            choice = Prompt.ask("[bold cyan]Select a tool to run[/bold cyan]", default="99")
            choice = int(choice)
            if 1 <= choice <= len(self.TOOLS):
                selected = self.TOOLS[choice - 1]
                if hasattr(selected, "show_options"):
                    selected.show_options(parent=self)
                elif hasattr(selected, "run"):
                    selected.run()
                else:
                    console.print("[bold yellow]Selected tool has no runnable interface.[/bold yellow]")
            elif choice == 99:
                return 99
        except Exception:
            console.print("[bold red]Invalid choice. Try again.[/bold red]")
        return self.show_options(parent=parent)


if __name__ == "__main__":
    tools = WebAttackTools()
    tools.pretty_print()
    tools.show_options()