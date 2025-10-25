# coding=utf-8
from core import HackingTool
from core import HackingToolsCollection

from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich import box

_theme = Theme({"purple": "#7B61FF"})
console = Console(theme=_theme)


class Keydroid(HackingTool):
    TITLE = "Keydroid"
    DESCRIPTION = "Android Keylogger + Reverse Shell\n" \
                  "[!] You have to install Some Manually Refer Below Link:\n " \
                  "[+] https://github.com/F4dl0/keydroid"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/F4dl0/keydroid.git"]
    RUN_COMMANDS = ["cd keydroid && bash keydroid.sh"]
    PROJECT_URL = "https://github.com/F4dl0/keydroid"


class MySMS(HackingTool):
    TITLE = "MySMS"
    DESCRIPTION = "Script that generates an Android App to hack SMS through WAN \n" \
                  "[!] You have to install Some Manually Refer Below Link:\n\t " \
                  "[+] https://github.com/papusingh2sms/mysms"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/papusingh2sms/mysms.git"]
    RUN_COMMANDS = ["cd mysms && bash mysms.sh"]
    PROJECT_URL = "https://github.com/papusingh2sms/mysms"


class LockPhish(HackingTool):
    TITLE = "Lockphish (Grab target LOCK PIN)"
    DESCRIPTION = "Lockphish it's the first tool for phishing attacks on the " \
                  "lock screen, designed to\n Grab Windows credentials,Android" \
                  " PIN and iPhone Passcode using a https link."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/JasonJerry/lockphish.git"]
    RUN_COMMANDS = ["cd lockphish && bash lockphish.sh"]
    PROJECT_URL = "https://github.com/JasonJerry/lockphish"


class Droidcam(HackingTool):
    TITLE = "DroidCam (Capture Image)"
    DESCRIPTION = "Powerful Tool For Grab Front Camera Snap Using A Link"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/kinghacker0/WishFish.git;"
        "sudo apt install php wget openssh-client"
    ]
    RUN_COMMANDS = ["cd WishFish && sudo bash wishfish.sh"]
    PROJECT_URL = "https://github.com/kinghacker0/WishFish"


class EvilApp(HackingTool):
    TITLE = "EvilApp (Hijack Session)"
    DESCRIPTION = "EvilApp is a script to generate Android App that can " \
                  "hijack authenticated sessions in cookies."
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/crypticterminal/EvilApp.git"]
    RUN_COMMANDS = ["cd EvilApp && bash evilapp.sh"]
    PROJECT_URL = "https://github.com/crypticterminal/EvilApp"


class AndroidAttackTools(HackingToolsCollection):
    TITLE = "Android Hacking tools"
    TOOLS = [
        Keydroid(),
        MySMS(),
        LockPhish(),
        Droidcam(),
        EvilApp()
    ]

    def pretty_print(self):
        table = Table(title="Android Attack Tools", show_lines=True, expand=True)
        table.add_column("Title", style="purple", no_wrap=True)
        table.add_column("Description", style="purple")
        table.add_column("Project URL", style="purple", no_wrap=True)

        for t in self.TOOLS:
            desc = getattr(t, "DESCRIPTION", "") or ""
            url = getattr(t, "PROJECT_URL", "") or ""
            table.add_row(t.TITLE, desc.strip().replace("\n", " "), url)

        panel = Panel(table, title="[purple]Available Tools[/purple]", border_style="purple")
        console.print(panel)

    def show_options(self, parent=None):
        console.print("\n")
        panel = Panel.fit("[bold magenta]Android Attack Tools Collection[/bold magenta]\n"
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
                if hasattr(selected, "show_options"):
                    selected.show_options(parent=self)
                elif hasattr(selected, "run"):
                    selected.run()
                elif hasattr(selected, "show_info"):
                    selected.show_info()
                else:
                    console.print("[bold yellow]Selected tool has no runnable interface.[/bold yellow]")
            elif choice == 99:
                return 99
        except Exception:
            console.print("[bold red]Invalid choice. Try again.[/bold red]")
        return self.show_options(parent=parent)


if __name__ == "__main__":
    tools = AndroidAttackTools()
    tools.pretty_print()
    tools.show_options()