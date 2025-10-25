# coding=utf-8
import os
import socket
import subprocess
import webbrowser
import sys

from core import HackingTool
from core import HackingToolsCollection
from core import clear_screen

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from rich.table import Table

console = Console()
PURPLE_STYLE = "bold magenta"


class NMAP(HackingTool):
    TITLE = "Network Map (nmap)"
    DESCRIPTION = "Free and open source utility for network discovery and security auditing"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/nmap/nmap.git",
        "sudo chmod -R 755 nmap && cd nmap && sudo ./configure && make && sudo make install"
    ]
    PROJECT_URL = "https://github.com/nmap/nmap"

    def __init__(self):
        super(NMAP, self).__init__(runnable=False)


class Dracnmap(HackingTool):
    TITLE = "Dracnmap"
    DESCRIPTION = "Dracnmap is an open source program which is using to \n" \
                  "exploit the network and gathering information with nmap help."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Screetsec/Dracnmap.git",
        "cd Dracnmap && chmod +x dracnmap-v2.2-dracOs.sh  dracnmap-v2.2.sh"
    ]
    RUN_COMMANDS = ["cd Dracnmap;sudo ./dracnmap-v2.2.sh"]
    PROJECT_URL = "https://github.com/Screetsec/Dracnmap"


class PortScan(HackingTool):
    TITLE = "Port scanning"

    def __init__(self):
        super(PortScan, self).__init__(installable=False)

    def run(self):
        clear_screen()
        console.print(Panel(Text(self.TITLE, justify="center"), style=PURPLE_STYLE))
        target = Prompt.ask("[bold]Select a Target IP[/]", default="", show_default=False)
        subprocess.run(["sudo", "nmap", "-O", "-Pn", target])


class Host2IP(HackingTool):
    TITLE = "Host to IP "

    def __init__(self):
        super(Host2IP, self).__init__(installable=False)

    def run(self):
        clear_screen()
        console.print(Panel(Text(self.TITLE, justify="center"), style=PURPLE_STYLE))
        host = Prompt.ask("Enter host name (e.g. www.google.com):-  ")
        ips = socket.gethostbyname(host)
        console.print(f"[{PURPLE_STYLE}]{host} -> {ips}[/]")


class XeroSploit(HackingTool):
    TITLE = "Xerosploit"
    DESCRIPTION = "Xerosploit is a penetration testing toolkit whose goal is to perform\n" \
                  "man-in-the-middle attacks for testing purposes"
    INSTALL_COMMANDS = [
        "git clone https://github.com/LionSec/xerosploit.git",
        "cd xerosploit && sudo python install.py"
    ]
    RUN_COMMANDS = ["sudo xerosploit"]
    PROJECT_URL = "https://github.com/LionSec/xerosploit"


class RedHawk(HackingTool):
    TITLE = "RED HAWK (All In One Scanning)"
    DESCRIPTION = "All in one tool for Information Gathering and Vulnerability Scanning."
    INSTALL_COMMANDS = [
        "git clone https://github.com/Tuhinshubhra/RED_HAWK.git"]
    RUN_COMMANDS = ["cd RED_HAWK;php rhawk.php"]
    PROJECT_URL = "https://github.com/Tuhinshubhra/RED_HAWK"


class ReconSpider(HackingTool):
    TITLE = "ReconSpider(For All Scanning)"
    DESCRIPTION = "ReconSpider is most Advanced Open Source Intelligence (OSINT)" \
                  " Framework for scanning IP Address, Emails, \n" \
                  "Websites, Organizations and find out information from" \
                  " different sources.\n"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/bhavsec/reconspider.git",
        "sudo apt install python3 python3-pip && cd reconspider && sudo python3 setup.py install"
    ]
    RUN_COMMANDS = ["cd reconspider;python3 reconspider.py"]
    PROJECT_URL = "https://github.com/bhavsec/reconspider"


class IsItDown(HackingTool):
    TITLE = "IsItDown (Check Website Down/Up)"
    DESCRIPTION = "Check Website Is Online or Not"

    def __init__(self):
        super(IsItDown, self).__init__(
            [('Open', self.open)], installable=False, runnable=False)

    def open(self):
        console.print(Panel("Opening isitdownrightnow.com", style=PURPLE_STYLE))
        webbrowser.open_new_tab("https://www.isitdownrightnow.com/")


class Infoga(HackingTool):
    TITLE = "Infoga - Email OSINT"
    DESCRIPTION = "Infoga is a tool gathering email accounts information\n" \
                  "(ip, hostname, country,...) from different public source"
    INSTALL_COMMANDS = [
        "git clone https://github.com/m4ll0k/Infoga.git",
        "cd Infoga;sudo python3 setup.py install"
    ]
    RUN_COMMANDS = ["cd Infoga;python3 infoga.py"]
    PROJECT_URL = "https://github.com/m4ll0k/Infoga"


class ReconDog(HackingTool):
    TITLE = "ReconDog"
    DESCRIPTION = "ReconDog Information Gathering Suite"
    INSTALL_COMMANDS = ["git clone https://github.com/s0md3v/ReconDog.git"]
    RUN_COMMANDS = ["cd ReconDog;sudo python dog"]
    PROJECT_URL = "https://github.com/s0md3v/ReconDog"


class Striker(HackingTool):
    TITLE = "Striker"
    DESCRIPTION = "Recon & Vulnerability Scanning Suite"
    INSTALL_COMMANDS = [
        "git clone https://github.com/s0md3v/Striker.git",
        "cd Striker && pip3 install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/s0md3v/Striker"

    def run(self):
        console.print(Panel(Text(self.TITLE, justify="center"), style=PURPLE_STYLE))
        site = Prompt.ask("Enter Site Name (example.com) >> ")
        os.chdir("Striker")
        subprocess.run(["sudo", "python3", "striker.py", site])


class SecretFinder(HackingTool):
    TITLE = "SecretFinder (like API & etc)"
    DESCRIPTION = "SecretFinder - A python script for find sensitive data \n" \
                  "like apikeys, accesstoken, authorizations, jwt,..etc \n " \
                  "and search anything on javascript files.\n\n " \
                  "Usage: python SecretFinder.py -h"
    INSTALL_COMMANDS = [
        "git clone https://github.com/m4ll0k/SecretFinder.git secretfinder",
        "cd secretfinder; sudo pip3 install -r requirements.txt"
    ]
    PROJECT_URL = "https://github.com/m4ll0k/SecretFinder"

    def __init__(self):
        super(SecretFinder, self).__init__(runnable=False)


class Shodan(HackingTool):
    TITLE = "Find Info Using Shodan"
    DESCRIPTION = "Get ports, vulnerabilities, information, banners,..etc \n " \
                  "for any IP with Shodan (no apikey! no rate limit!)\n" \
                  "[X] Don't use this tool because your ip will be blocked by Shodan!"
    INSTALL_COMMANDS = ["git clone https://github.com/m4ll0k/Shodanfy.py.git"]
    PROJECT_URL = "https://github.com/m4ll0k/Shodanfy.py"

    def __init__(self):
        super(Shodan, self).__init__(runnable=False)


class PortScannerRanger(HackingTool):
    TITLE = "Port Scanner - rang3r"
    DESCRIPTION = "rang3r is a python script which scans in multi thread\n " \
                  "all alive hosts within your range that you specify."
    INSTALL_COMMANDS = [
        "git clone https://github.com/floriankunushevci/rang3r.git;"
        "sudo pip install termcolor"]
    PROJECT_URL = "https://github.com/floriankunushevci/rang3r"

    def run(self):
        console.print(Panel(Text(self.TITLE, justify="center"), style=PURPLE_STYLE))
        ip = Prompt.ask("Enter Ip >> ")
        os.chdir("rang3r")
        subprocess.run(["sudo", "python", "rang3r.py", "--ip", ip])


class Breacher(HackingTool):
    TITLE = "Breacher"
    DESCRIPTION = "An advanced multithreaded admin panel finder written in python."
    INSTALL_COMMANDS = ["git clone https://github.com/s0md3v/Breacher.git"]
    PROJECT_URL = "https://github.com/s0md3v/Breacher"

    def run(self):
        console.print(Panel(Text(self.TITLE, justify="center"), style=PURPLE_STYLE))
        domain = Prompt.ask("Enter domain (example.com) >> ")
        os.chdir("Breacher")
        subprocess.run(["python3", "breacher.py", "-u", domain])


class InformationGatheringTools(HackingToolsCollection):
    TITLE = "Information gathering tools"
    TOOLS = [
        NMAP(),
        Dracnmap(),
        PortScan(),
        Host2IP(),
        XeroSploit(),
        RedHawk(),
        ReconSpider(),
        IsItDown(),
        Infoga(),
        ReconDog(),
        Striker(),
        SecretFinder(),
        Shodan(),
        PortScannerRanger(),
        Breacher()
    ]

    def _get_attr(self, obj, *names, default=""):
        for n in names:
            if hasattr(obj, n):
                return getattr(obj, n)
        return default

    def pretty_print(self):
        table = Table(title="Information Gathering Tools", show_lines=True, expand=True)
        table.add_column("Title", style=PURPLE_STYLE, no_wrap=True)
        table.add_column("Description", style=PURPLE_STYLE)
        table.add_column("Project URL", style=PURPLE_STYLE, no_wrap=True)

        for t in self.TOOLS:
            title = self._get_attr(t, "TITLE", "Title", "title", default=t.__class__.__name__)
            desc = self._get_attr(t, "DESCRIPTION", "Description", "description", default="")
            url = self._get_attr(t, "PROJECT_URL", "PROJECT_URL", "PROJECT", "project_url", "projectUrl", default="")
            table.add_row(str(title), str(desc).replace("\n", " "), str(url))

        console.print(Panel(table, title=f"[magenta]Available Tools[/magenta]", border_style=PURPLE_STYLE))

    def show_options(self, parent=None):
        console.print("\n")
        console.print(Panel.fit(
            "[bold magenta]Information Gathering Collection[/bold magenta]\n"
            "Select a tool to view/run it or return to the previous menu.",
            border_style=PURPLE_STYLE
        ))

        table = Table(title="[bold cyan]Available Tools[/bold cyan]", show_lines=True, expand=True)
        table.add_column("Index", justify="center", style="bold yellow")
        table.add_column("Tool Name", justify="left", style="bold green")
        table.add_column("Description", justify="left", style="white")

        for i, tool in enumerate(self.TOOLS):
            title = self._get_attr(tool, "TITLE", "Title", "title", default=tool.__class__.__name__)
            desc = self._get_attr(tool, "DESCRIPTION", "Description", "description", default="—")
            table.add_row(str(i + 1), title, desc or "—")

        table.add_row("[red]99[/red]", "[bold red]Exit[/bold red]", "Return to previous menu")
        console.print(table)

        try:
            choice = Prompt.ask("[bold cyan]Select a tool to run[/bold cyan]", default="99")
            choice = int(choice)
            if 1 <= choice <= len(self.TOOLS):
                selected = self.TOOLS[choice - 1]
                # delegate to collection-style tools if available
                if hasattr(selected, "show_options"):
                    selected.show_options(parent=self)
                # if tool exposes actions/menu, try to call it
                elif hasattr(selected, "show_actions"):
                    selected.show_actions(parent=self)
                # otherwise try to call run if present
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
    tools = InformationGatheringTools()
    tools.pretty_print()
    tools.show_options()
