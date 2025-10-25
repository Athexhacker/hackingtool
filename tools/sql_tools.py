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


class Sqlmap(HackingTool):
    TITLE = "Sqlmap tool"
    DESCRIPTION = "sqlmap is an open source penetration testing tool that " \
                  "automates the process of detecting and exploiting SQL injection flaws " \
                  "and taking over database servers. [!] python3 sqlmap.py -u [http://example.com] --batch --banner. More usage: https://github.com/sqlmapproject/sqlmap/wiki/Usage"
    INSTALL_COMMANDS = ["sudo git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git sqlmap-dev"]
    RUN_COMMANDS = ["cd sqlmap-dev;python3 sqlmap.py --wizard"]
    PROJECT_URL = "https://github.com/sqlmapproject/sqlmap"


class NoSqlMap(HackingTool):
    TITLE = "NoSqlMap"
    DESCRIPTION = "NoSQLMap is an open source Python tool designed to audit and automate injection attacks. [*] Please install MongoDB."
    INSTALL_COMMANDS = ["git clone https://github.com/codingo/NoSQLMap.git",
                        "sudo chmod -R 755 NoSQLMap;cd NoSQLMap;python setup.py install"]
    RUN_COMMANDS = ["python NoSQLMap"]
    PROJECT_URL = "https://github.com/codingo/NoSQLMap"


class SQLiScanner(HackingTool):
    TITLE = "Damn Small SQLi Scanner"
    DESCRIPTION = "DSSS is a fully functional SQL injection vulnerability scanner also supporting GET and POST parameters. Usage: python3 dsss.py -h | -u [URL]"
    INSTALL_COMMANDS = ["git clone https://github.com/stamparm/DSSS.git"]
    PROJECT_URL = "https://github.com/stamparm/DSSS"

    def __init__(self):
        super(SQLiScanner, self).__init__(runnable=False)


class Explo(HackingTool):
    TITLE = "Explo"
    DESCRIPTION = "Explo is a simple tool to describe web security issues in human and machine readable format. Usage: explo [--verbose|-v] testcase.yaml | explo [--verbose|-v] examples/*.yaml"
    INSTALL_COMMANDS = ["git clone https://github.com/dtag-dev-sec/explo.git",
                        "cd explo;sudo python setup.py install"]
    PROJECT_URL = "https://github.com/dtag-dev-sec/explo"

    def __init__(self):
        super(Explo, self).__init__(runnable=False)


class Blisqy(HackingTool):
    TITLE = "Blisqy - Exploit Time-based blind-SQL injection"
    DESCRIPTION = "Blisqy helps web security researchers find time-based blind SQL injections on HTTP headers and exploit them."
    INSTALL_COMMANDS = ["git clone https://github.com/JohnTroony/Blisqy.git"]
    PROJECT_URL = "https://github.com/JohnTroony/Blisqy"

    def __init__(self):
        super(Blisqy, self).__init__(runnable=False)


class Leviathan(HackingTool):
    TITLE = "Leviathan - Wide Range Mass Audit Toolkit"
    DESCRIPTION = "Leviathan is a mass audit toolkit with service discovery, brute force, SQL injection detection, and custom exploit capabilities. Requires API keys."
    INSTALL_COMMANDS = ["git clone https://github.com/leviathan-framework/leviathan.git",
                        "cd leviathan;sudo pip install -r requirements.txt"]
    RUN_COMMANDS = ["cd leviathan;python leviathan.py"]
    PROJECT_URL = "https://github.com/leviathan-framework/leviathan"


class SQLScan(HackingTool):
    TITLE = "SQLScan"
    DESCRIPTION = "SQLScan is a quick web scanner to find SQL injection points. Not for educational purposes."
    INSTALL_COMMANDS = ["sudo apt install php php-bz2 php-curl php-mbstring curl",
                        "sudo curl https://raw.githubusercontent.com/Cvar1984/sqlscan/dev/build/main.phar --output /usr/local/bin/sqlscan",
                        "chmod +x /usr/local/bin/sqlscan"]
    RUN_COMMANDS = ["sudo sqlscan"]
    PROJECT_URL = "https://github.com/Cvar1984/sqlscan"


class SqlInjectionTools(HackingToolsCollection):
    TITLE = "SQL Injection Tools"
    TOOLS = [Sqlmap(), NoSqlMap(), SQLiScanner(), Explo(), Blisqy(), Leviathan(), SQLScan()]

    def _get_attr(self, obj, *names, default=""):
        for n in names:
            if hasattr(obj, n):
                return getattr(obj, n)
        return default

    def pretty_print(self):
        table = Table(title="SQL Injection Tools", show_lines=True, expand=True)
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
        panel = Panel.fit("[bold magenta]SQL Injection Tools Collection[/bold magenta]\nSelect a tool to view options or run it.", border_style="purple")
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
    tools = SqlInjectionTools()
    tools.pretty_print()
    tools.show_options()
