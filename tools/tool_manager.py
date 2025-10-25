# coding=utf-8
import os
import sys
from time import sleep

from core import HackingTool
from core import HackingToolsCollection
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

_theme = Theme({"purple": "#7B61FF"})
console = Console(theme=_theme)


class UpdateTool(HackingTool):
    TITLE = "Update Tool or System"
    DESCRIPTION = "Update Tool or System"

    def __init__(self):
        super(UpdateTool, self).__init__([
            ("Update System", self.update_sys),
            ("Update Hackingtool", self.update_ht)
        ], installable=False, runnable=False)

    def update_sys(self):
        os.system("sudo apt update && sudo apt full-upgrade -y")
        os.system("sudo apt-get install tor openssl curl && sudo apt-get update tor openssl curl")
        os.system("sudo apt-get install python3-pip")

    def update_ht(self):
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/hackingtool/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/hackingtool/;"
                  "mkdir hackingtool;"
                  "cd hackingtool;"
                  "git clone https://github.com/Z4nzu/hackingtool.git;"
                  "cd hackingtool;"
                  "sudo chmod +x install.sh;"
                  "./install.sh")


class UninstallTool(HackingTool):
    TITLE = "Uninstall HackingTool"
    DESCRIPTION = "Uninstall HackingTool"

    def __init__(self):
        super(UninstallTool, self).__init__([
            ('Uninstall', self.uninstall)
        ], installable=False, runnable=False)

    def uninstall(self):
        console.print("hackingtool started to uninstall..\n")
        sleep(1)
        os.system("sudo chmod +x /etc/;"
                  "sudo chmod +x /usr/share/doc;"
                  "sudo rm -rf /usr/share/doc/hackingtool/;"
                  "cd /etc/;"
                  "sudo rm -rf /etc/hackingtool/;")
        console.print("\n[bold green]Hackingtool Successfully Uninstalled... Goodbye.[/bold green]")
        sys.exit()


class ToolManager(HackingToolsCollection):
    TITLE = "Update or Uninstall | Hackingtool"
    TOOLS = [
        UpdateTool(),
        UninstallTool()
    ]

    def pretty_print(self):
        table = Table(title="Tool Manager — Update / Uninstall", show_lines=True, expand=True)
        table.add_column("Title", style="purple", no_wrap=True)
        table.add_column("Description", style="purple")

        for t in self.TOOLS:
            desc = getattr(t, "DESCRIPTION", "") or ""
            table.add_row(t.TITLE, desc.strip().replace("\n", " "))

        panel = Panel(table, title="[purple]Available Manager Tools[/purple]", border_style="purple")
        console.print(panel)

    def show_options(self, parent=None):
        console.print("\n")
        panel = Panel.fit("[bold magenta]Tool Manager[/bold magenta]\nSelect an action to run.", border_style="purple")
        console.print(panel)

        table = Table(title="[bold cyan]Available Options[/bold cyan]", show_lines=True, expand=True)
        table.add_column("Index", justify="center", style="bold yellow")
        table.add_column("Tool Name", justify="left", style="bold green")
        table.add_column("Description", justify="left", style="white")

        for i, tool in enumerate(self.TOOLS):
            title = getattr(tool, "TITLE", tool.__class__.__name__)
            desc = getattr(tool, "DESCRIPTION", "—")
            table.add_row(str(i + 1), title, desc)

        table.add_row("[red]99[/red]", "[bold red]Exit[/bold red]", "Return to previous menu")
        console.print(table)

        try:
            choice = int(Prompt.ask("[bold cyan]Select an option[/bold cyan]", default="99"))
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
    manager = ToolManager()
    manager.pretty_print()
    manager.show_options()
