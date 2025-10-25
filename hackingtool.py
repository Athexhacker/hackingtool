#!/usr/bin/env python3
# Version 1.1.0 (rich UI - green theme)
import os
import sys
import webbrowser
from platform import system
from time import sleep

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.align import Align
from rich.text import Text
from rich import box
from rich.columns import Columns
from rich.rule import Rule
from rich.padding import Padding

from core import HackingToolsCollection
from tools.anonsurf import AnonSurfTools
from tools.ddos import DDOSTools
from tools.exploit_frameworks import ExploitFrameworkTools
from tools.forensic_tools import ForensicTools
from tools.information_gathering_tools import InformationGatheringTools
from tools.other_tools import OtherTools
from tools.payload_creator import PayloadCreatorTools
from tools.phising_attack import PhishingAttackTools
from tools.post_exploitation import PostExploitationTools
from tools.remote_administration import RemoteAdministrationTools
from tools.reverse_engineering import ReverseEngineeringTools
from tools.sql_tools import SqlInjectionTools
from tools.steganography import SteganographyTools
from tools.tool_manager import ToolManager
from tools.webattack import WebAttackTools
from tools.wireless_attack_tools import WirelessAttackTools
from tools.wordlist_generator import WordlistGeneratorTools
from tools.xss_attack import XSSAttackTools

console = Console()

ASCII_LOGO = r"""
███████╗              ███████╗ ██████╗  ██████╗██╗███████╗████████╗██╗   ██╗
██╔════╝              ██╔════╝██╔═══██╗██╔════╝██║██╔════╝╚══██╔══╝╚██╗ ██╔╝
█████╗      █████╗    ███████╗██║   ██║██║     ██║█████╗     ██║    ╚████╔╝ 
██╔══╝      ╚════╝    ╚════██║██║   ██║██║     ██║██╔══╝     ██║     ╚██╔╝  
██║                   ███████║╚██████╔╝╚██████╗██║███████╗   ██║      ██║   
╚═╝                   ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚══════╝   ╚═╝      ╚═╝ 
                                                                     
"""

tool_definitions = [
    ("Anonymously Hiding Tools", "🛡️"),
    ("Information gathering tools", "🔍"),
    ("Wordlist Generator", "📚"),
    ("Wireless attack tools", "📶"),
    ("SQL Injection Tools", "🧩"),
    ("Phishing attack tools", "🎣"),
    ("Web Attack tools", "🌐"),
    ("Post exploitation tools", "🔧"),
    ("Forensic tools", "🕵️"),
    ("Payload creation tools", "📦"),
    ("Exploit framework", "🧰"),
    ("Reverse engineering tools", "🔁"),
    ("DDOS Attack Tools", "⚡"),
    ("Remote Administrator Tools (RAT)", "🖥️"),
    ("XSS Attack Tools", "💥"),
    ("Steganograhy tools", "🖼️"),
    ("Other tools", "✨"),
    ("Update or Uninstall | F-SOCIETY", "♻️"),
]

all_tools = [
    AnonSurfTools(),
    InformationGatheringTools(),
    WordlistGeneratorTools(),
    WirelessAttackTools(),
    SqlInjectionTools(),
    PhishingAttackTools(),
    WebAttackTools(),
    PostExploitationTools(),
    ForensicTools(),
    PayloadCreatorTools(),
    ExploitFrameworkTools(),
    ReverseEngineeringTools(),
    DDOSTools(),
    RemoteAdministrationTools(),
    XSSAttackTools(),
    SteganographyTools(),
    OtherTools(),
    ToolManager()
]


class AllTools(HackingToolsCollection):
    TITLE = "All tools"
    TOOLS = all_tools

    def show_info(self):
        header = Text()
        header.append(ASCII_LOGO, style="bold green")
        header.append("\n\n",)
        footer = Text.assemble(
            (" F-SOCIETY TOOLKIT ", "bold bright_black"),
            (" | ",),
            ("Version 1.1.0", "bold green"),
        )
        warning = Text(" Please Don't Use For illegal Activity ", style="bold green")
        panel = Panel(
            Align.center(header + Text("\n") + footer + Text("\n") + warning),
            box=box.DOUBLE,
            padding=(1, 2),
            border_style="green"
        )
        console.print(panel)


def build_menu():
    table = Table.grid(expand=True)
    table.add_column("idx", width=6, justify="right")
    table.add_column("name", justify="left")

    for idx, (title, icon) in enumerate(tool_definitions):
        if idx == 17:
            label = "[bold green]99[/bold green]"
            name = f"[bold green]{icon} {title}[/bold green]"
        else:
            label = f"[bold green]{idx}[/bold green]"
            name = f"[white]{icon}[/white]  [green]{title}[/green]"
        table.add_row(label, name)

    top_panel = Panel(
        Align.center(Text("F-SOCIETY — Main Menu", style="bold white on green"), vertical="middle"),
        style="green",
        padding=(0, 1),
        box=box.ROUNDED
    )
    menu_panel = Panel.fit(
        table,
        title="[bold green]Select a tool[/bold green]",
        border_style="bright_green",
        box=box.SQUARE
    )
    footer = Align.center(Text("Choose number and press Enter — 99 to exit", style="italic bright_black"))
    console.print(top_panel)
    console.print(menu_panel)
    console.print(Rule(style="bright_black"))
    console.print(footer)
    console.print("")


def choose_path():
    fpath = os.path.expanduser("~/fsociety_path.txt")
    if not os.path.exists(fpath):
        os.system("clear" if system() == "Linux" else "cls")
        build_menu()
        console.print(Panel("Setup path for tool installations", border_style="green"))
        choice = Prompt.ask("[green]Set Path[/green]", choices=["1", "2"], default="2")
        if choice == "1":
            inpath = Prompt.ask("[green]Enter Path (with Directory Name)[/green]")
            with open(fpath, "w") as f:
                f.write(inpath)
            console.print(f"[green]Successfully Set Path to:[/green] {inpath}")
        else:
            autopath = "/home/fsociety/"
            with open(fpath, "w") as f:
                f.write(autopath)
            console.print(f"[green]Your Default Path Is:[/green] {autopath}")
            sleep(1)
    return fpath


def interact_menu():
    while True:
        try:
            build_menu()
            choice = IntPrompt.ask("[green]Choose a tool to proceed[/green]", default=0)
            if choice == 99:
                console.print(Panel("[bold white on green]Goodbye — Come Back Safely[/bold white on green]"))
                break
            if 0 <= choice < len(all_tools):
                tool = all_tools[choice]
                name = tool_definitions[choice][0]
                console.print(Panel(f"[bold green]{tool_definitions[choice][1]}  Selected:[/bold green] [white]{name}"))
                try:
                    fn = getattr(tool, "show_options", None)
                    if callable(fn):
                        fn()
                    else:
                        console.print(f"[green]Tool '{name}' has no interactive menu (show_options).[/green]")
                except Exception as e:
                    console.print(Panel(f"[green]Error while opening {name}[/green]\n{e}", border_style="green"))
                if not Confirm.ask("[green]Return to main menu?[/green]", default=True):
                    console.print(Panel("[bold white on green]Exiting...[/bold white on green]"))
                    break
            else:
                console.print("[green]Invalid selection. Pick a number from the menu.[/green]")
        except KeyboardInterrupt:
            console.print("\n[bold green]Interrupted by user — exiting[/bold green]")
            break

def main():
    try:
        if system() == "Linux":
            fpath = choose_path()
            with open(fpath) as f:
                archive = f.readline().strip()
                os.makedirs(archive, exist_ok=True)
                os.chdir(archive)
                AllTools().show_info()
                interact_menu()
        elif system() == "Windows":
            console.print(Panel("[bold green]Please run this tool on a Debian/Linux system for best results[/bold green]"))
            if Confirm.ask("Open guidance link in your browser?", default=True):
                webbrowser.open_new_tab("https://tinyurl.com/y522modc")
            sleep(2)
        else:
            console.print("[green]Please Check Your System or Open New Issue ...[/green]")
    except KeyboardInterrupt:
        console.print("\n[bold green]Exiting ..!!![/bold green]")
        sleep(1)


if __name__ == "__main__":
    main()