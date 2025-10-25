# coding=utf-8
import os
import sys

# Fetching parent directory for importing core.py
current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from core import HackingTool
from core import HackingToolsCollection

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.prompt import Prompt

console = Console()
PURPLE_STYLE = "bold magenta"


class Autopsy(HackingTool):
    TITLE = "Autopsy"
    DESCRIPTION = "Autopsy is a platform that is used by Cyber Investigators.\n" \
                  "[!] Works in any OS\n" \
                  "[!] Recover Deleted Files from any OS & Media \n" \
                  "[!] Extract Image Metadata"
    RUN_COMMANDS = ["sudo autopsy"]

    def __init__(self):
        super(Autopsy, self).__init__(installable=False)


class Wireshark(HackingTool):
    TITLE = "Wireshark"
    DESCRIPTION = "Wireshark is a network capture and analyzer \n" \
                  "tool to see what’s happening in your network.\n " \
                  "And also investigate Network related incident"
    RUN_COMMANDS = ["sudo wireshark"]

    def __init__(self):
        super(Wireshark, self).__init__(installable=False)


class BulkExtractor(HackingTool):
    TITLE = "Bulk extractor"
    DESCRIPTION = "Extract useful information without parsing the file system"
    PROJECT_URL = "https://github.com/simsong/bulk_extractor"

    def __init__(self):
        super(BulkExtractor, self).__init__([
            ('GUI Mode (Download required)', self.gui_mode),
            ('CLI Mode', self.cli_mode)
        ], installable=False, runnable=False)

    def gui_mode(self):
        console.print(Panel(Text(self.TITLE, justify="center"), style=PURPLE_STYLE))
        console.print("[bold magenta]Cloning repository and attempting to run GUI...[/]")
        os.system("sudo git clone https://github.com/simsong/bulk_extractor.git")
        os.system("ls src/ && cd .. && cd java_gui && ./BEViewer")
        console.print(
            "[magenta]If you get an error after clone go to /java_gui/src/ and compile the .jar file && run ./BEViewer[/]")
        console.print(
            "[magenta]Please visit for more details about installation: https://github.com/simsong/bulk_extractor[/]")

    def cli_mode(self):
        console.print(Panel(Text(self.TITLE + " - CLI Mode", justify="center"), style=PURPLE_STYLE))
        os.system("sudo apt install bulk-extractor")
        console.print("[magenta]Showing bulk_extractor help and options:[/]")
        os.system("bulk_extractor -h")
        os.system('echo "bulk_extractor [options] imagefile" | boxes -d headline | lolcat')


class Guymager(HackingTool):
    TITLE = "Disk Clone and ISO Image Acquire"
    DESCRIPTION = "Guymager is a free forensic imager for media acquisition."
    INSTALL_COMMANDS = ["sudo apt install guymager"]
    RUN_COMMANDS = ["sudo guymager"]
    PROJECT_URL = "https://guymager.sourceforge.io/"

    def __init__(self):
        super(Guymager, self).__init__(installable=False)


class Toolsley(HackingTool):
    TITLE = "Toolsley"
    DESCRIPTION = "Toolsley got more than ten useful tools for investigation.\n" \
                  "[+]File signature verifier\n" \
                  "[+]File identifier \n" \
                  "[+]Hash & Validate \n" \
                  "[+]Binary inspector \n " \
                  "[+]Encode text \n" \
                  "[+]Data URI generator \n" \
                  "[+]Password generator"
    PROJECT_URL = "https://www.toolsley.com/"

    def __init__(self):
        super(Toolsley, self).__init__(installable=False, runnable=False)


class ForensicTools(HackingToolsCollection):
    TITLE = "Forensic tools"
    TOOLS = [
        Autopsy(),
        Wireshark(),
        BulkExtractor(),
        Guymager(),
        Toolsley()
    ]

    def _get_attr(self, obj, *names, default=""):
        for n in names:
            if hasattr(obj, n):
                return getattr(obj, n)
        return default

    def pretty_print(self):
        table = Table(title="Forensic Tools", show_lines=True, expand=True)
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
            "[bold magenta]Forensic Tools Collection[/bold magenta]\n"
            "Select a tool to run or view options.",
            border_style=PURPLE_STYLE
        ))

        table = Table(title="[bold cyan]Available Tools[/bold cyan]", show_lines=True)
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
                # delegate to collection-like tools if available
                if hasattr(selected, "show_options"):
                    selected.show_options(parent=self)
                # if tool exposes actions (like BulkExtractor) and has a menu, try to show it
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
    tools = ForensicTools()
    tools.pretty_print()
    tools.show_options()
