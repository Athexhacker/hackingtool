# coding=utf-8
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


class FacialFind(HackingTool):
    TITLE = "Find SocialMedia By Facial Recognation System"
    DESCRIPTION = "A Social Media Mapping Tool that correlates profiles\n " \
                  "via facial recognition across different sites."
    INSTALL_COMMANDS = [
        "sudo apt install -y software-properties-common",
        "sudo add-apt-repository ppa:mozillateam/firefox-next && sudo apt update && sudo apt upgrade",
        "sudo git clone https://github.com/Greenwolf/social_mapper.git",
        "sudo apt install -y build-essential cmake libgtk-3-dev libboost-all-dev",
        "cd social_mapper/setup",
        "sudo python3 -m pip install --no-cache-dir -r requirements.txt",
        'echo "[!]Now You have To do some Manually\n'
        '[!] Install the Geckodriver for your operating system\n'
        '[!] Copy & Paste Link And Download File As System Configuration\n'
        '[#] https://github.com/mozilla/geckodriver/releases\n'
        '[!!] On Linux you can place it in /usr/bin "| boxes | lolcat'
    ]
    PROJECT_URL = "https://github.com/Greenwolf/social_mapper"

    def run(self):
        os.system("cd social_mapper/setup")
        os.system("sudo python social_mapper.py -h")
        print("""\033[95m 
                You have to set Username and password of your AC Or Any Fack Account
                [#] Type in Terminal nano social_mapper.py
        """)
        os.system(
            'echo "python social_mapper.py -f [<imageFoldername>] -i [<imgFolderPath>] -m fast [<AcName>] -fb -tw"| boxes | lolcat')


class FindUser(HackingTool):
    TITLE = "Find SocialMedia By UserName"
    DESCRIPTION = "Find usernames across over 75 social networks"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/xHak9x/finduser.git",
        "cd finduser && sudo chmod +x finduser.sh"
    ]
    RUN_COMMANDS = ["cd finduser && sudo bash finduser.sh"]
    PROJECT_URL = "https://github.com/xHak9x/finduser"


class Sherlock(HackingTool):
    TITLE = "Sherlock"
    DESCRIPTION = "Hunt down social media accounts by username across social networks \n " \
                  "For More Usage \n" \
                  "\t >>python3 sherlock --help"
    INSTALL_COMMANDS = [
        "git clone https://github.com/sherlock-project/sherlock.git",
        "cd sherlock;sudo python3 -m pip install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/sherlock-project/sherlock"

    def run(self):
        name = input("Enter Username >> ")
        os.chdir('sherlock')
        subprocess.run(["sudo", "python3", "sherlock", f"{name}"])


class SocialScan(HackingTool):
    TITLE = "SocialScan | Username or Email"
    DESCRIPTION = "Check email address and username availability on online " \
                  "platforms with 100% accuracy"
    INSTALL_COMMANDS = ["sudo pip install socialscan"]
    PROJECT_URL = "https://github.com/iojw/socialscan"

    def run(self):
        name = input(
            "Enter Username or Emailid (if both then please space between email & username) >> ")
        subprocess.run(["sudo", "socialscan", f"{name}"])


class SocialMediaFinderTools(HackingToolsCollection):
    TITLE = "SocialMedia Finder"
    TOOLS = [
        FacialFind(),
        FindUser(),
        Sherlock(),
        SocialScan()
    ]

    def pretty_print(self):
        table = Table(title="Social Media Finder Tools", show_lines=True, expand=True)
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
        panel = Panel.fit("[bold magenta]Social Media Finder Collection[/bold magenta]\n"
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
    tools = SocialMediaFinderTools()
    tools.pretty_print()
    tools.show_options()