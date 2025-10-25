# coding=utf-8
import os

from core import HackingTool
from core import HackingToolsCollection

from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

_theme = Theme({"purple": "#7B61FF"})
console = Console(theme=_theme)


class TheFatRat(HackingTool):
    TITLE = "The FatRat"
    DESCRIPTION = "TheFatRat Provides An Easy way to create Backdoors and Payloads " \
                  "which can bypass most anti-virus"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Screetsec/TheFatRat.git",
        "cd TheFatRat && sudo chmod +x setup.sh"
    ]
    RUN_COMMANDS = ["cd TheFatRat && sudo bash setup.sh"]
    PROJECT_URL = "https://github.com/Screetsec/TheFatRat"

    def __init__(self):
        super(TheFatRat, self).__init__([
            ('Update', self.update),
            ('Troubleshoot', self.troubleshoot)
        ])

    def update(self):
        os.system("cd TheFatRat && bash update && chmod +x setup.sh && bash setup.sh")

    def troubleshoot(self):
        os.system("cd TheFatRat && sudo chmod +x chk_tools && ./chk_tools")


class Brutal(HackingTool):
    TITLE = "Brutal"
    DESCRIPTION = "Brutal is a toolkit to quickly create various payloads, powershell attacks, " \
                  "virus attacks and launch listener for a Human Interface Device"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Screetsec/Brutal.git",
        "cd Brutal && sudo chmod +x Brutal.sh"
    ]
    RUN_COMMANDS = ["cd Brutal && sudo bash Brutal.sh"]
    PROJECT_URL = "https://github.com/Screetsec/Brutal"

    def show_info(self):
        super(Brutal, self).show_info()
        console.print("""
[!] Requirement
    >> Arduino Software (I used v1.6.7)
    >> TeensyDuino
    >> Linux udev rules
    >> Copy and paste the PaensyLib folder inside your Arduino libraries

[!] Visit for Installation for Arduino: 
    >> https://github.com/Screetsec/Brutal/wiki/Install-Requirements 
""")


class Stitch(HackingTool):
    TITLE = "Stitch"
    DESCRIPTION = "Stitch is Cross Platform Python Remote Administrator Tool\n" \
                  "[!] Refer Below Link For Wins & Mac OS"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/nathanlopez/Stitch.git",
        "cd Stitch && sudo pip install -r lnx_requirements.txt"
    ]
    RUN_COMMANDS = ["cd Stitch && sudo python main.py"]
    PROJECT_URL = "https://nathanlopez.github.io/Stitch"


class MSFVenom(HackingTool):
    TITLE = "MSFvenom Payload Creator"
    DESCRIPTION = "MSFvenom Payload Creator (MSFPC) is a wrapper to generate multiple types of payloads, " \
                  "based on user choice. Simplifies payload creation."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/g0tmi1k/msfpc.git",
        "cd msfpc;sudo chmod +x msfpc.sh"
    ]
    RUN_COMMANDS = ["cd msfpc;sudo bash msfpc.sh -h -v"]
    PROJECT_URL = "https://github.com/g0tmi1k/msfpc"


class Venom(HackingTool):
    TITLE = "Venom Shellcode Generator"
    DESCRIPTION = "Venom 1.0.11 (malicious_server) exploits apache2 webserver to deliver LAN payloads via fake webpages."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/r00t-3xp10it/venom.git",
        "sudo chmod -R 775 venom*/ && cd venom*/ && cd aux && sudo bash setup.sh",
        "sudo ./venom.sh -u"
    ]
    RUN_COMMANDS = ["cd venom && sudo ./venom.sh"]
    PROJECT_URL = "https://github.com/r00t-3xp10it/venom"


class Spycam(HackingTool):
    TITLE = "Spycam"
    DESCRIPTION = "Generates a Win32 payload that captures webcam images every 1 minute and sends them to the attacker."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/indexnotfound404/spycam.git",
        "cd spycam && bash install.sh && chmod +x spycam"
    ]
    RUN_COMMANDS = ["cd spycam && ./spycam"]
    PROJECT_URL = "https://github.com/indexnotfound404/spycam"


class MobDroid(HackingTool):
    TITLE = "Mob-Droid"
    DESCRIPTION = "Generates metasploit payloads easily without typing long commands."
    INSTALL_COMMANDS = [
        "git clone https://github.com/kinghacker0/mob-droid.git"
    ]
    RUN_COMMANDS = ["cd mob-droid;sudo python mob-droid.py"]
    PROJECT_URL = "https://github.com/kinghacker0/Mob-Droid"


class Enigma(HackingTool):
    TITLE = "Enigma"
    DESCRIPTION = "Enigma is a Multiplatform payload dropper."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/UndeadSec/Enigma.git"
    ]
    RUN_COMMANDS = ["cd Enigma;sudo python enigma.py"]
    PROJECT_URL = "https://github.com/UndeadSec/Enigma"


class PayloadCreatorTools(HackingToolsCollection):
    TITLE = "Payload creation tools"
    TOOLS = [
        TheFatRat(),
        Brutal(),
        Stitch(),
        MSFVenom(),
        Venom(),
        Spycam(),
        MobDroid(),
        Enigma()
    ]

    def pretty_print(self):
        table = Table(title="Payload Creation Tools", show_lines=True, expand=True)
        table.add_column("Title", style="purple", no_wrap=True)
        table.add_column("Description", style="purple")
        table.add_column("Project URL", style="purple", no_wrap=True)

        for t in self.TOOLS:
            desc = getattr(t, "DESCRIPTION", "") or ""
            url = getattr(t, "PROJECT_URL", "") or ""
            table.add_row(t.TITLE, desc.strip().replace("\n", " "), url)

        console.print(Panel(table, title="[purple]Available Tools[/purple]", border_style="purple"))

    def show_options(self):
        console.print("\n")
        console.print(Panel.fit(
            "[bold purple]Payload Creator Collection[/bold purple]\n"
            "Select a tool to run it or exit.",
            border_style="purple"
        ))

        table = Table(title="[bold cyan]Available Tools[/bold cyan]", show_lines=True, expand=True)
        table.add_column("Index", justify="center", style="bold yellow")
        table.add_column("Tool Name", justify="left", style="bold green")
        table.add_column("Description", justify="left", style="white")

        for i, tool in enumerate(self.TOOLS):
            desc = getattr(tool, "DESCRIPTION", "") or "—"
            table.add_row(str(i + 1), tool.TITLE, desc.replace("\n", " "))

        table.add_row("[red]99[/red]", "[bold red]Exit[/bold red]", "Return to previous menu")
        console.print(table)

        try:
            choice = Prompt.ask("[bold cyan]Select a tool to run[/bold cyan]", default="99")
            choice = int(choice)
            if 1 <= choice <= len(self.TOOLS):
                selected = self.TOOLS[choice - 1]
                if hasattr(selected, "run"):
                    selected.run()
                elif hasattr(selected, "show_actions"):
                    selected.show_actions()
                else:
                    console.print("[bold yellow]Selected tool has no runnable interface.[/bold yellow]")
            elif choice == 99:
                return 99
        except Exception:
            console.print("[bold red]Invalid choice. Try again.[/bold red]")

        return self.show_options()


if __name__ == "__main__":
    tools = PayloadCreatorTools()
    tools.pretty_print()
    tools.show_options()
