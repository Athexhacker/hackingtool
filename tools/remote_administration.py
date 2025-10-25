# coding=utf-8
from core import HackingTool
from core import HackingToolsCollection

from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

_theme = Theme({"purple": "#7B61FF"})
console = Console(theme=_theme)


class Stitch(HackingTool):
    TITLE = "Stitch"
    DESCRIPTION = "Stitch is a cross platform python framework.\n" \
                  "which allows you to build custom payloads\n" \
                  "For Windows, Mac and Linux."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/nathanlopez/Stitch.git",
        "cd Stitch;sudo pip install -r lnx_requirements.txt"
    ]
    RUN_COMMANDS = ["cd Stitch;python main.py"]
    PROJECT_URL = "https://github.com/nathanlopez/Stitch"


class Pyshell(HackingTool):
    TITLE = "Pyshell"
    DESCRIPTION = "Pyshell is a Rat Tool that can be able to download & upload " \
                  "files,\n Execute OS Command and more.."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/knassar702/Pyshell.git;"
        "sudo pip install pyscreenshot python-nmap requests"
    ]
    RUN_COMMANDS = ["cd Pyshell;./Pyshell"]
    PROJECT_URL = "https://github.com/knassar702/pyshell"


class RemoteAdministrationTools(HackingToolsCollection):
    TITLE = "Remote Administrator Tools (RAT)"
    TOOLS = [
        Stitch(),
        Pyshell()
    ]

    def _get_attr(self, obj, *names, default=""):
        for n in names:
            if hasattr(obj, n):
                return getattr(obj, n)
        return default

    def pretty_print(self):
        table = Table(title="Remote Administration Tools (RAT)", show_lines=True, expand=True)
        table.add_column("Title", style="purple", no_wrap=True)
        table.add_column("Description", style="purple")
        table.add_column("Project URL", style="purple", no_wrap=True)

        for t in self.TOOLS:
            title = self._get_attr(t, "TITLE", "Title", "title", default=t.__class__.__name__)
            desc = self._get_attr(t, "DESCRIPTION", "Description", "description", default="").strip().replace("\n", " ")
            url = self._get_attr(t, "PROJECT_URL", "PROJECT_URL", "PROJECT", "project_url", "projectUrl", default="")
            table.add_row(str(title), str(desc or "—"), str(url))

        panel = Panel(table, title="[purple]Available Tools[/purple]", border_style="purple")
        console.print(panel)

    def show_options(self, parent=None):
        console.print("\n")
        panel = Panel.fit("[bold magenta]Remote Administration Tools (RAT) Collection[/bold magenta]\n"
                          "Select a tool to view options or run it.",
                          border_style="purple")
        console.print(panel)

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
                # Preserve any before_run hooks if present
                elif hasattr(selected, "before_run"):
                    selected.before_run()
                else:
                    console.print("[bold yellow]Selected tool has no runnable interface.[/bold yellow]")
            elif choice == 99:
                return 99
        except Exception:
            console.print("[bold red]Invalid choice. Try again.[/bold red]")
        return self.show_options(parent=parent)


if __name__ == "__main__":
    tools = RemoteAdministrationTools()
    tools.pretty_print()
    tools.show_options()
