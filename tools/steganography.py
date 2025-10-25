# coding=utf-8
import subprocess

from core import HackingTool
from core import HackingToolsCollection
from core import validate_input

from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

_theme = Theme({"purple": "#7B61FF"})
console = Console(theme=_theme)


class SteganoHide(HackingTool):
    TITLE = "SteganoHide"
    INSTALL_COMMANDS = ["sudo apt-get install steghide -y"]

    def run(self):
        choice_run = input(
            "[1] Hide\n"
            "[2] Extract\n"
            "[99]Cancel\n"
            ">> "
        )
        choice_run = validate_input(choice_run, [1, 2, 99])
        if choice_run is None:
            console.print("[bold red]Please choose a valid input[/bold red]")
            return self.run()

        if choice_run == 99:
            return

        if choice_run == 1:
            file_hide = input("Enter Filename to Embed (1.txt) >> ")
            file_to_be_hide = input("Enter Cover Filename (test.jpeg) >> ")
            subprocess.run(["steghide", "embed", "-cf", file_to_be_hide, "-ef", file_hide])

        elif choice_run == 2:
            from_file = input("Enter Filename to Extract Data From >> ")
            subprocess.run(["steghide", "extract", "-sf", from_file])


class StegnoCracker(HackingTool):
    TITLE = "StegnoCracker"
    DESCRIPTION = "SteganoCracker uncovers hidden data inside files using brute-force utility"
    INSTALL_COMMANDS = ["pip3 install stegcracker && pip3 install stegcracker -U --force-reinstall"]

    def run(self):
        filename = input("Enter Filename >> ")
        passfile = input("Enter Wordlist Filename >> ")
        subprocess.run(["stegcracker", filename, passfile])


class StegoCracker(HackingTool):
    TITLE = "StegoCracker"
    DESCRIPTION = "StegoCracker lets you hide and retrieve data in image or audio files"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/W1LDN16H7/StegoCracker.git",
        "sudo chmod -R 755 StegoCracker"
    ]
    RUN_COMMANDS = [
        "cd StegoCracker && python3 -m pip install -r requirements.txt",
        "./install.sh"
    ]
    PROJECT_URL = "https://github.com/W1LDN16H7/StegoCracker"


class Whitespace(HackingTool):
    TITLE = "Whitespace"
    DESCRIPTION = "Use whitespace and unicode characters for steganography"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/beardog108/snow10.git",
        "sudo chmod -R 755 snow10"
    ]
    RUN_COMMANDS = ["cd snow10 && ./install.sh"]
    PROJECT_URL = "https://github.com/beardog108/snow10"


class SteganographyTools(HackingToolsCollection):
    TITLE = "Steganography Tools"
    TOOLS = [SteganoHide(), StegnoCracker(), StegoCracker(), Whitespace()]

    def _get_attr(self, obj, *names, default=""):
        for n in names:
            if hasattr(obj, n):
                return getattr(obj, n)
        return default

    def pretty_print(self):
        table = Table(title="Steganography Tools", show_lines=True, expand=True)
        table.add_column("Title", style="purple", no_wrap=True)
        table.add_column("Description", style="purple")
        table.add_column("Project URL", style="purple", no_wrap=True)

        for t in self.TOOLS:
            title = self._get_attr(t, "TITLE", "Title", "title", default=t.__class__.__name__)
            desc = self._get_attr(t, "DESCRIPTION", "Description", "description", default="").strip().replace("\n", " ")
            url = self._get_attr(t, "PROJECT_URL", "PROJECT_URL", "project_url", "projectUrl", default="")
            table.add_row(str(title), str(desc or "—"), str(url))

        panel = Panel(table, title="[purple]Available Tools[/purple]", border_style="purple")
        console.print(panel)

    def show_options(self, parent=None):
        console.print("\n")
        panel = Panel.fit("[bold magenta]Steganography Tools Collection[/bold magenta]\nSelect a tool to run or view options.", border_style="purple")
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
            choice = int(Prompt.ask("[bold cyan]Select a tool to run[/bold cyan]", default="99"))
            if 1 <= choice <= len(self.TOOLS):
                selected = self.TOOLS[choice - 1]
                if hasattr(selected, "show_options"):
                    selected.show_options(parent=self)
                elif hasattr(selected, "run"):
                    selected.run()
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
    tools = SteganographyTools()
    tools.pretty_print()
    tools.show_options()
