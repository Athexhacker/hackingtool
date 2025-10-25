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

_theme = Theme({"purple": "#7B61FF"})
console = Console(theme=_theme)


class WIFIPumpkin(HackingTool):
    TITLE = "WiFi-Pumpkin"
    DESCRIPTION = (
        "The WiFi-Pumpkin is a rogue AP framework to easily create "
        "these fake networks\n"
        "all while forwarding legitimate traffic to and from the "
        "unsuspecting target."
    )
    INSTALL_COMMANDS = [
        "sudo apt install libssl-dev libffi-dev build-essential",
        "sudo git clone https://github.com/P0cL4bs/wifipumpkin3.git",
        "chmod -R 755 wifipumpkin3",
        "sudo apt install python3-pyqt5",
        "cd wifipumpkin3;sudo python3 setup.py install",
    ]
    RUN_COMMANDS = ["sudo wifipumpkin3"]
    PROJECT_URL = "https://github.com/P0cL4bs/wifipumpkin3"


class pixiewps(HackingTool):
    TITLE = "pixiewps"
    DESCRIPTION = (
        "Pixiewps is a tool written in C used to bruteforce offline "
        "the WPS pin\n "
        "exploiting the low or non-existing entropy of some Access "
        "Points, the so-called pixie dust attack"
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/wiire/pixiewps.git && apt-get -y install build-essential",
        "cd pixiewps*/ && make",
        "cd pixiewps*/ && sudo make install && wget https://pastebin.com/y9Dk1Wjh",
    ]
    PROJECT_URL = "https://github.com/wiire/pixiewps"

    def run(self):
        os.system(
            'echo "'
            '1.> Put your interface into monitor mode using '
            "'airmon-ng start {wireless interface}\n'"
            "'2.> wash -i {monitor-interface like mon0}\'\n'"
            "'3.> reaver -i {monitor interface} -b {BSSID of router} -c {router channel} -vvv -K 1 -f"
            '| boxes -d boy'
        )
        print("You Have To Run Manually By USing >>pixiewps -h ")


class BluePot(HackingTool):
    TITLE = "Bluetooth Honeypot GUI Framework"
    DESCRIPTION = (
        "You need to have at least 1 bluetooth receiver "
        "(if you have many it will work with those, too).\n"
        "You must install/libbluetooth-dev on "
        "Ubuntu/bluez-libs-devel on Fedora/bluez-devel on openSUSE"
    )
    INSTALL_COMMANDS = [
        "sudo wget https://raw.githubusercontent.com/andrewmichaelsmith/bluepot/master/bin/bluepot-0.2.tar.gz"
        "sudo tar xfz bluepot-0.2.tar.gz;sudo rm bluepot-0.2.tar.gz"
    ]
    RUN_COMMANDS = ["cd bluepot && sudo java -jar bluepot.jar"]
    PROJECT_URL = "https://github.com/andrewmichaelsmith/bluepot"


class Fluxion(HackingTool):
    TITLE = "Fluxion"
    DESCRIPTION = "Fluxion is a remake of linset by vk496 with enhanced functionality."
    INSTALL_COMMANDS = [
        "git clone https://github.com/FluxionNetwork/fluxion.git",
        "cd fluxion && sudo chmod +x fluxion.sh",
    ]
    RUN_COMMANDS = ["cd fluxion;sudo bash fluxion.sh -i"]
    PROJECT_URL = "https://github.com/FluxionNetwork/fluxion"


class Wifiphisher(HackingTool):
    TITLE = "Wifiphisher"
    DESCRIPTION = """
        Wifiphisher is a rogue Access Point framework for conducting red team engagements or Wi-Fi security testing. 
        Using Wifiphisher, penetration testers can easily achieve a man-in-the-middle position against wireless clients by performing 
        targeted Wi-Fi association attacks. Wifiphisher can be further used to mount victim-customized web phishing attacks against the
        connected clients in order to capture credentials (e.g. from third party login pages or WPA/WPA2 Pre-Shared Keys) or infect the 
        victim stations with malware..\n
        For More Details Visit >> https://github.com/wifiphisher/wifiphisher
    """
    INSTALL_COMMANDS = [
        "git clone https://github.com/wifiphisher/wifiphisher.git",
        "cd wifiphisher;sudo python3 setup.py install",
    ]
    RUN_COMMANDS = ["cd wifiphisher;sudo wifiphisher"]
    PROJECT_URL = "https://github.com/wifiphisher/wifiphisher"


class Wifite(HackingTool):
    TITLE = "Wifite"
    DESCRIPTION = "Wifite is an automated wireless attack tool"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/derv82/wifite2.git",
        "cd wifite2 && sudo python3 setup.py install",
    ]
    RUN_COMMANDS = ["cd wifite2; sudo wifite"]
    PROJECT_URL = "https://github.com/derv82/wifite2"


class EvilTwin(HackingTool):
    TITLE = "EvilTwin"
    DESCRIPTION = (
        "Fakeap is a script to perform Evil Twin Attack, by getting"
        " credentials using a Fake page and Fake Access Point"
    )
    INSTALL_COMMANDS = ["sudo git clone https://github.com/Z4nzu/fakeap.git"]
    RUN_COMMANDS = ["cd fakeap && sudo bash fakeap.sh"]
    PROJECT_URL = "https://github.com/Z4nzu/fakeap"


class Fastssh(HackingTool):
    TITLE = "Fastssh"
    DESCRIPTION = (
        "Fastssh is an Shell Script to perform multi-threaded scan"
        " \n and brute force attack against SSH protocol using the "
        "most commonly credentials."
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Z4nzu/fastssh.git && cd fastssh && sudo chmod +x fastssh.sh",
        "sudo apt-get install -y sshpass netcat",
    ]
    RUN_COMMANDS = ["cd fastssh && sudo bash fastssh.sh --scan"]
    PROJECT_URL = "https://github.com/Z4nzu/fastssh"


class Howmanypeople(HackingTool):
    TITLE = "Howmanypeople"
    DESCRIPTION = (
        "Count the number of people around you by monitoring wifi "
        "signals.\n"
        "[@] WIFI ADAPTER REQUIRED* \n[*]"
        "It may be illegal to monitor networks for MAC addresses, \n"
        "especially on networks that you do not own. "
        "Please check your country's laws"
    )
    INSTALL_COMMANDS = [
        "sudo apt-get install tshark"
        ";sudo python3 -m pip install howmanypeoplearearound"
    ]
    RUN_COMMANDS = ["howmanypeoplearearound"]


class WirelessAttackTools(HackingToolsCollection):
    TITLE = "Wireless attack tools"
    DESCRIPTION = ""
    TOOLS = [
        WIFIPumpkin(),
        pixiewps(),
        BluePot(),
        Fluxion(),
        Wifiphisher(),
        Wifite(),
        EvilTwin(),
        Fastssh(),
        Howmanypeople(),
    ]

    def pretty_print(self):
        table = Table(title="Wireless Attack Tools", show_lines=True, expand=True)
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
        panel = Panel.fit("[bold magenta]Wireless Attack Tools Collection[/bold magenta]\n"
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
    tools = WirelessAttackTools()
    tools.pretty_print()
    tools.show_options()