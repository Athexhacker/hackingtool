# coding=utf-8
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


class AndroGuard(HackingTool):
    TITLE = "Androguard"
    DESCRIPTION = "Androguard is a Reverse engineering, Malware and goodware " \
                  "analysis of Android applications and more"
    INSTALL_COMMANDS = ["sudo pip3 install -U androguard"]
    PROJECT_URL = "https://github.com/androguard/androguard "

    def __init__(self):
        super(AndroGuard, self).__init__(runnable=False)


class Apk2Gold(HackingTool):
    TITLE = "Apk2Gold"
    DESCRIPTION = "Apk2Gold is a CLI tool for decompiling Android apps to Java"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/lxdvs/apk2gold.git",
        "cd apk2gold;sudo bash make.sh"
    ]
    PROJECT_URL = "https://github.com/lxdvs/apk2gold "

    def run(self):
        uinput = input("Enter (.apk) File >> ")
        subprocess.run(["sudo", "apk2gold", uinput])


class Jadx(HackingTool):
    TITLE = "JadX"
    DESCRIPTION = "Jadx is Dex to Java decompiler.\n" \
                  "[*] decompile Dalvik bytecode to java classes from APK, dex," \
                  " aar and zip files\n" \
                  "[*] decode AndroidManifest.xml and other resources from " \
                  "resources.arsc"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/skylot/jadx.git",
        "cd jadx;./gradlew dist"
    ]
    PROJECT_URL = "https://github.com/skylot/jadx"

    def __init__(self):
        super(Jadx, self).__init__(runnable=False)


class ReverseEngineeringTools(HackingToolsCollection):
    TITLE = "Reverse engineering tools"
    TOOLS = [
        AndroGuard(),
        Apk2Gold(),
        Jadx()
    ]

    def _get_attr(self, obj, *names, default=""):
        for n in names:
            if hasattr(obj, n):
                return getattr(obj, n)
        return default

    def pretty_print(self):
        table = Table(title="Reverse Engineering Tools", show_lines=True, expand=True)
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
        panel = Panel.fit("[bold magenta]Reverse Engineering Tools Collection[/bold magenta]\n"
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
    tools = ReverseEngineeringTools()
    tools.pretty_print()
    tools.show_options()
