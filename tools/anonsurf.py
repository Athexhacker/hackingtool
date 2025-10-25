# coding=utf-8
import os

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.table import Table

from core import HackingTool
from core import HackingToolsCollection

console = Console()
P_COLOR = "magenta"


class AnonymouslySurf(HackingTool):
    TITLE = "Anonymously Surf"
    DESCRIPTION = (
        "It automatically overwrites the RAM when\n"
        "the system is shutting down and also change Ip."
    )
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Und3rf10w/kali-anonsurf.git",
        "cd kali-anonsurf && sudo ./installer.sh && cd .. && sudo rm -r kali-anonsurf",
    ]
    RUN_COMMANDS = ["sudo anonsurf start"]
    PROJECT_URL = "https://github.com/Und3rf10w/kali-anonsurf"

    def __init__(self):
        super(AnonymouslySurf, self).__init__([("Stop", self.stop)])

    def stop(self):
        console.print(Panel(Text(self.TITLE, justify="center"), style=f"bold {P_COLOR}"))
        console.print("Stopping Anonsurf...", style=f"bold {P_COLOR}")
        os.system("sudo anonsurf stop")


class Multitor(HackingTool):
    TITLE = "Multitor"
    DESCRIPTION = "How to stay in multi places at the same time"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/trimstray/multitor.git",
        "cd multitor;sudo bash setup.sh install",
    ]
    RUN_COMMANDS = [
        "multitor --init 2 --user debian-tor --socks-port 9000 --control-port 9900 --proxy privoxy --haproxy"
    ]
    PROJECT_URL = "https://github.com/trimstray/multitor"

    def __init__(self):
        # keep original behavior (non-runnable) while still initializing
        super(Multitor, self).__init__(runnable=False)


class AnonSurfTools(HackingToolsCollection):
    TITLE = "Anonymously Hiding Tools"
    DESCRIPTION = ""
    TOOLS = [
        AnonymouslySurf(),
        Multitor(),
    ]

    def _get_attr(self, obj, *names, default=""):
        for n in names:
            if hasattr(obj, n):
                return getattr(obj, n)
        return default

    def pretty_print(self):
        table = Table(title="Anonymously Hiding Tools", show_lines=True, expand=True)
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
            "[bold magenta]Anonymously Hiding Tools Collection[/bold magenta]\n"
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
                # delegate if collection-style interface exists
                if hasattr(selected, "show_options"):
                    selected.show_options(parent=self)
                # otherwise, if the tool has actions or a run method, prefer those
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
    tools = AnonSurfTools()
    tools.pretty_print()
    tools.show_options()
