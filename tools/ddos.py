# coding=utf-8
import os
import subprocess

from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text
from rich.table import Table

from core import HackingTool
from core import HackingToolsCollection

console = Console()
P_COLOR = "magenta"  # primary purple/magenta theme for styling


class ddos(HackingTool):
    TITLE = "ddos"
    DESCRIPTION = (
        "Best DDoS Attack Script With 36 Plus Methods."
        "DDoS attacks\n\b "
        "for SECURITY TESTING PURPOSES ONLY! "
    )

    INSTALL_COMMANDS = [
        "git clone https://github.com/the-deepnet/ddos.git",
        "cd ddos;sudo pip3 install -r requirements.txt",
    ]
    PROJECT_URL = "https://github.com/the-deepnet/ddos.git"

    def run(self):
        console.print(Panel(Text(self.TITLE, justify="center"), style=f"bold {P_COLOR}"))
        method = Prompt.ask("Enter Method >>")
        url = Prompt.ask("Enter URL >>")
        threads = Prompt.ask("Enter Threads >>")
        proxylist = Prompt.ask("Enter ProxyList >>")
        multiple = Prompt.ask("Enter Multiple >>")
        timer = Prompt.ask("Enter Timer >>")
        os.system("cd ddos;")
        subprocess.run(
            [
                "sudo",
                "python3 ddos",
                method,
                url,
                "socks_type5.4.1",
                threads,
                proxylist,
                multiple,
                timer,
            ]
        )


class SlowLoris(HackingTool):
    TITLE = "SlowLoris"
    DESCRIPTION = (
        "Slowloris is basically an HTTP Denial of Service attack."
        "It send lots of HTTP Request"
    )
    INSTALL_COMMANDS = ["sudo pip3 install slowloris"]

    def run(self):
        console.print(Panel(Text(self.TITLE, justify="center"), style=f"bold {P_COLOR}"))
        target_site = Prompt.ask("Enter Target Site:-")
        subprocess.run(["slowloris", target_site])


class Asyncrone(HackingTool):
    TITLE = "Asyncrone | Multifunction SYN Flood DDoS Weapon"
    DESCRIPTION = (
        "aSYNcrone is a C language based, mulltifunction SYN Flood "
        "DDoS Weapon.\nDisable the destination system by sending a "
        "SYN packet intensively to the destination."
    )
    INSTALL_COMMANDS = [
        "git clone https://github.com/fatih4842/aSYNcrone.git",
        "cd aSYNcrone;sudo gcc aSYNcrone.c -o aSYNcrone -lpthread",
    ]
    PROJECT_URL = "https://github.com/fatihsnsy/aSYNcrone"

    def run(self):
        console.print(Panel(Text(self.TITLE, justify="center"), style=f"bold {P_COLOR}"))
        source_port = Prompt.ask("Enter Source Port >>")
        target_ip = Prompt.ask("Enter Target IP >>")
        target_port = Prompt.ask("Enter Target port >>")
        os.system("cd aSYNcrone;")
        subprocess.run(
            ["sudo", "./aSYNcrone", source_port, target_ip, target_port, 1000]
        )


class UFONet(HackingTool):
    TITLE = "UFOnet"
    DESCRIPTION = (
        "UFONet - is a free software, P2P and cryptographic "
        "-disruptive \n toolkit- that allows to perform DoS and "
        "DDoS attacks\n\b "
        "More Usage Visit"
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/epsylon/ufonet.git",
        "cd ufonet;sudo python3 setup.py install;sudo pip3 install GeoIP;sudo pip3 install python-geoip;sudo pip3 install pygeoip;sudo pip3 install requests;sudo pip3 install pycrypto;sudo pip3 install pycurl;sudo pip3 install whois;sudo pip3 install scapy-python3",
    ]
    RUN_COMMANDS = ["sudo python3 ufonet --gui"]
    PROJECT_URL = "https://github.com/epsylon/ufonet"


class GoldenEye(HackingTool):
    TITLE = "GoldenEye"
    DESCRIPTION = (
        "GoldenEye is a python3 app for SECURITY TESTING PURPOSES ONLY!\n"
        "GoldenEye is a HTTP DoS Test Tool."
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/jseidl/GoldenEye.git;"
        "chmod -R 755 GoldenEye"
    ]
    PROJECT_URL = "https://github.com/jseidl/GoldenEye"

    def run(self):
        console.print(Panel(Text(self.TITLE, justify="center"), style=f"bold {P_COLOR}"))
        os.system("cd GoldenEye ;sudo ./goldeneye.py")
        console.print("Go to Directory\n[*] USAGE: ./goldeneye.py <url> [OPTIONS]")


class Saphyra(HackingTool):
    TITLE = "SaphyraDDoS"
    DESCRIPTION = "A complex python code to DDoS any website with a very easy usage.!\n"
    INSTALL_COMMANDS = [
        "sudo su",
        "git clone https://github.com/anonymous24x7/Saphyra-DDoS.git",
        "cd Saphyra-DDoS",
        "chmod +x saphyra.py",
        "python saphyra.py",
    ]
    PROJECT_URL = "https://github.com/anonymous24x7/Saphyra-DDoS"

    def run(self):
        console.print(Panel(Text(self.TITLE, justify="center"), style=f"bold {P_COLOR}"))
        url = Prompt.ask("Enter url>>>")
        try:
            os.system("python saphyra.py " + url)
        except Exception:
            console.print("Enter a valid url.", style="bold red")


class DDOSTools(HackingToolsCollection):
    TITLE = "DDOS Attack Tools"
    TOOLS = [SlowLoris(), Asyncrone(), UFONet(), GoldenEye(), Saphyra()]

    def _get_attr(self, obj, *names, default=""):
        for n in names:
            if hasattr(obj, n):
                return getattr(obj, n)
        return default

    def pretty_print(self):
        table = Table(title="DDOS Attack Tools", show_lines=True, expand=True)
        table.add_column("Title", style="magenta", no_wrap=True)
        table.add_column("Description", style="magenta")
        table.add_column("Project URL", style="magenta", no_wrap=True)

        for t in self.TOOLS:
            title = self._get_attr(t, "TITLE", "Title", "title", default=t.__class__.__name__)
            desc = self._get_attr(t, "DESCRIPTION", "Description", "description", default="")
            url = self._get_attr(t, "PROJECT_URL", "PROJECT_URL", "PROJECT", "project_url", "projectUrl", default="")
            table.add_row(str(title), str(desc).strip().replace("\n", " "), str(url))

        panel = Panel(table, title=f"[{P_COLOR}]Available Tools[/ {P_COLOR}]", border_style=P_COLOR)
        console.print(panel)

    def show_options(self, parent=None):
        console.print("\n")
        console.print(Panel.fit(
            "[bold magenta]DDOS Attack Tools Collection[/bold magenta]\n"
            "Select a tool to view options or run it.",
            border_style=P_COLOR
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
                # If tool exposes show_options (collection-style), delegate to it
                if hasattr(selected, "show_options"):
                    selected.show_options(parent=self)
                # Otherwise, if runnable, call its run method
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
    tools = DDOSTools()
    tools.pretty_print()
    tools.show_options()
