# coding=utf-8
import os
import subprocess

from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich import box

from core import HackingTool
from core import HackingToolsCollection

_theme = Theme({"purple": "#7B61FF"})
console = Console(theme=_theme)


class Cupp(HackingTool):
    TITLE = "Cupp"
    DESCRIPTION = "WlCreator is a C program that can create all possibilities of passwords,\n " \
                  "and you can choose Length, Lowercase, Capital, Numbers and Special Chars"
    INSTALL_COMMANDS = ["git clone https://github.com/Mebus/cupp.git"]
    RUN_COMMANDS = ["cd cupp && python3 cupp.py -i"]
    PROJECT_URL = "https://github.com/Mebus/cupp"

    def show_info(self):
        panel = Panel(
            f"[bold purple]{self.TITLE}[/bold purple]\n\n"
            f"[cyan]{self.DESCRIPTION}[/cyan]\n\n"
            f"[green]Repository:[/green] [underline blue]{self.PROJECT_URL}[/underline blue]",
            border_style="purple",
            box=box.ROUNDED,
        )
        console.print(panel)


class WlCreator(HackingTool):
    TITLE = "WordlistCreator"
    DESCRIPTION = "WlCreator is a C program that can create all possibilities" \
                  " of passwords,\n and you can choose Length, Lowercase, " \
                  "Capital, Numbers and Special Chars"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/Z4nzu/wlcreator.git"]
    RUN_COMMANDS = [
        "cd wlcreator && sudo gcc -o wlcreator wlcreator.c && ./wlcreator 5"]
    PROJECT_URL = "https://github.com/Z4nzu/wlcreator"

    def show_info(self):
        panel = Panel(
            f"[bold purple]{self.TITLE}[/bold purple]\n\n"
            f"[cyan]{self.DESCRIPTION}[/cyan]\n\n"
            f"[green]Repository:[/green] [underline blue]{self.PROJECT_URL}[/underline blue]",
            border_style="purple",
            box=box.ROUNDED,
        )
        console.print(panel)


class GoblinWordGenerator(HackingTool):
    TITLE = "Goblin WordGenerator"
    DESCRIPTION = "Goblin WordGenerator"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/UndeadSec/GoblinWordGenerator.git"]
    RUN_COMMANDS = ["cd GoblinWordGenerator && python3 goblin.py"]
    PROJECT_URL = "https://github.com/UndeadSec/GoblinWordGenerator.git"

    def show_info(self):
        panel = Panel(
            f"[bold purple]{self.TITLE}[/bold purple]\n\n"
            f"[cyan]{self.DESCRIPTION}[/cyan]\n\n"
            f"[green]Repository:[/green] [underline blue]{self.PROJECT_URL}[/underline blue]",
            border_style="purple",
            box=box.ROUNDED,
        )
        console.print(panel)


class showme(HackingTool):
    TITLE = "Password list (1.4 Billion Clear Text Password)"
    DESCRIPTION = "This tool allows you to perform OSINT and reconnaissance on " \
                  "an organisation or an individual. It allows one to search " \
                  "1.4 Billion clear text credentials which was dumped as " \
                  "part of BreachCompilation leak. This database makes " \
                  "finding passwords faster and easier than ever before."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Viralmaniar/SMWYG-Show-Me-What-You-Got.git",
        "cd SMWYG-Show-Me-What-You-Got && pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd SMWYG-Show-Me-What-You-Got && python SMWYG.py"]
    PROJECT_URL = "https://github.com/Viralmaniar/SMWYG-Show-Me-What-You-Got"

    def show_info(self):
        panel = Panel(
            f"[bold purple]{self.TITLE}[/bold purple]\n\n"
            f"[cyan]{self.DESCRIPTION}[/cyan]\n\n"
            f"[green]Repository:[/green] [underline blue]{self.PROJECT_URL}[/underline blue]",
            border_style="purple",
            box=box.ROUNDED,
        )
        console.print(panel)


class WordlistGeneratorTools(HackingToolsCollection):
    TITLE = "Wordlist Generator"
    TOOLS = [
        Cupp(),
        WlCreator(),
        GoblinWordGenerator(),
        showme()
    ]

    def show_info(self):
        header = Panel(f"[bold white on purple] {self.TITLE} [/bold white on purple]",
                       border_style="purple", box=box.DOUBLE)
        console.print(header)
        table = Table(box=box.SIMPLE, show_header=True, header_style="bold purple")
        table.add_column("#", justify="center", style="cyan", width=4)
        table.add_column("Tool", style="bold")
        table.add_column("Description", style="dim", overflow="fold")

        for idx, t in enumerate(self.TOOLS, start=1):
            desc = getattr(t, "DESCRIPTION", "") or ""
            table.add_row(str(idx), t.TITLE, desc)

        table.add_row("[red]99[/red]", "[bold red]Exit[/bold red]", "Return to previous menu")
        console.print(table)

    def show_options(self, parent=None):
        console.print("\n")
        panel = Panel.fit("[bold magenta]Wordlist Generator Collection[/bold magenta]\n"
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
                if hasattr(selected, "show_info"):
                    selected.show_info()
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
    tools = WordlistGeneratorTools()
    tools.show_info()
    tools.show_options()