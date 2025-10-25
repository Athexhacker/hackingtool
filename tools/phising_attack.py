# coding=utf-8
import os

from core import HackingTool
from core import HackingToolsCollection

from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

_theme = Theme({"purple": "#7B61FF"})
console = Console(theme=_theme)


class autophisher(HackingTool):
    TITLE = "Autophisher RK"
    DESCRIPTION = "Automated Phishing Toolkit"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/CodingRanjith/autophisher.git",
        "cd autophisher"
    ]
    RUN_COMMANDS = ["cd autophisher;sudo bash autophisher.sh"]
    PROJECT_URL = "https://github.com/CodingRanjith/autophisher"


class Pyphisher(HackingTool):
    TITLE = "Pyphisher"
    DESCRIPTION = "Easy to use phishing tool with 77 website templates"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/KasRoudra/PyPhisher",
        "cd PyPhisher/files",
        "pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd PyPhisher;sudo python3 pyphisher.py"]
    PROJECT_URL = "git clone https://github.com/KasRoudra/PyPhisher"


class AdvPhishing(HackingTool):
    TITLE = "AdvPhishing"
    DESCRIPTION = "This is Advance Phishing Tool ! OTP PHISHING"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Ignitetch/AdvPhishing.git",
        "cd AdvPhishing;chmod 777 *;bash Linux-Setup.sh"]
    RUN_COMMANDS = ["cd AdvPhishing && sudo bash AdvPhishing.sh"]
    PROJECT_URL = "https://github.com/Ignitetch/AdvPhishing"


class Setoolkit(HackingTool):
    TITLE = "Setoolkit"
    DESCRIPTION = "The Social-Engineer Toolkit is an open-source penetration\n" \
                  "testing framework designed for social engine"
    INSTALL_COMMANDS = [
        "git clone https://github.com/trustedsec/social-engineer-toolkit/",
        "cd social-engineer-toolkit && sudo python3 setup.py"
    ]
    RUN_COMMANDS = ["sudo setoolkit"]
    PROJECT_URL = "https://github.com/trustedsec/social-engineer-toolkit"


class SocialFish(HackingTool):
    TITLE = "SocialFish"
    DESCRIPTION = "Automated Phishing Tool & Information Collector NOTE: username is 'root' and password is 'pass'"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/UndeadSec/SocialFish.git && sudo apt-get install python3 python3-pip python3-dev -y",
        "cd SocialFish && sudo python3 -m pip install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd SocialFish && sudo python3 SocialFish.py root pass"]
    PROJECT_URL = "https://github.com/UndeadSec/SocialFish"


class HiddenEye(HackingTool):
    TITLE = "HiddenEye"
    DESCRIPTION = "Modern Phishing Tool With Advanced Functionality And " \
                  "Multiple Tunnelling Services \n" \
                  "\t [!]https://github.com/DarkSecDevelopers/HiddenEye"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Morsmalleo/HiddenEye.git ;sudo chmod 777 HiddenEye",
        "cd HiddenEye;sudo pip3 install -r requirements.txt;sudo pip3 install requests;pip3 install pyngrok"
    ]
    RUN_COMMANDS = ["cd HiddenEye;sudo python3 HiddenEye.py"]
    PROJECT_URL = "https://github.com/Morsmalleo/HiddenEye.git"


class Evilginx2(HackingTool):
    TITLE = "Evilginx2"
    DESCRIPTION = "evilginx2 is a man-in-the-middle attack framework used " \
                  "for phishing login credentials along with session cookies,\n" \
                  "which in turn allows to bypass 2-factor authentication protection.\n\n\t " \
                  "[+]Make sure you have installed GO of version at least 1.14.0 \n" \
                  "[+]After installation, add this to your ~/.profile, assuming that you installed GO in /usr/local/go\n\t " \
                  "[+]export GOPATH=$HOME/go \n " \
                  "[+]export PATH=$PATH:/usr/local/go/bin:$GOPATH/bin \n" \
                  "[+]Then load it with source ~/.profiles."
    INSTALL_COMMANDS = [
        "sudo apt-get install git make;go get -u github.com/kgretzky/evilginx2",
        "cd $GOPATH/src/github.com/kgretzky/evilginx2;make",
        "sudo make install;sudo evilginx"
    ]
    RUN_COMMANDS = ["sudo evilginx"]
    PROJECT_URL = "https://github.com/kgretzky/evilginx2"


class ISeeYou(HackingTool):
    TITLE = "I-See_You"
    DESCRIPTION = "[!] ISeeYou is a tool to find Exact Location of Victom By" \
                  " User SocialEngineering or Phishing Engagement..\n" \
                  "[!] Users can expose their local servers to the Internet " \
                  "and decode the location coordinates by looking at the log file"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/Viralmaniar/I-See-You.git",
        "cd I-See-You && sudo chmod u+x ISeeYou.sh"
    ]
    RUN_COMMANDS = ["cd I-See-You && sudo bash ISeeYou.sh"]
    PROJECT_URL = "https://github.com/Viralmaniar/I-See-You"


class SayCheese(HackingTool):
    TITLE = "SayCheese"
    DESCRIPTION = "Take webcam shots from target just sending a malicious link"
    INSTALL_COMMANDS = ["sudo git clone https://github.com/hangetzzu/saycheese"]
    RUN_COMMANDS = ["cd saycheese && sudo bash saycheese.sh"]
    PROJECT_URL = "https://github.com/hangetzzu/saycheese"


class QRJacking(HackingTool):
    TITLE = "QR Code Jacking"
    DESCRIPTION = "QR Code Jacking (Any Website)"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/cryptedwolf/ohmyqr.git && sudo apt -y install scrot"]
    RUN_COMMANDS = ["cd ohmyqr && sudo bash ohmyqr.sh"]
    PROJECT_URL = "https://github.com/cryptedwolf/ohmyqr"


class WifiPhisher(HackingTool):
    TITLE = "WifiPhisher"
    DESCRIPTION = "The Rogue Access Point Framework"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/wifiphisher/wifiphisher.git",
        "cd wifiphisher"]
    RUN_COMMANDS = ["cd wifiphisher && sudo python setup.py"]
    PROJECT_URL = "https://github.com/wifiphisher/wifiphisher"


class BlackEye(HackingTool):
    TITLE = "BlackEye"
    DESCRIPTION = "The ultimate phishing tool with 38 websites available!"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/thelinuxchoice/blackeye",
        "cd blackeye "]
    RUN_COMMANDS = ["cd blackeye && sudo bash blackeye.sh"]
    PROJECT_URL = "https://github.com/An0nUD4Y/blackeye"


class ShellPhish(HackingTool):
    TITLE = "ShellPhish"
    DESCRIPTION = "Phishing Tool for 18 social media"
    INSTALL_COMMANDS = ["git clone https://github.com/An0nUD4Y/shellphish.git"]
    RUN_COMMANDS = ["cd shellphish;sudo bash shellphish.sh"]
    PROJECT_URL = "https://github.com/An0nUD4Y/shellphish"


class Thanos(HackingTool):
    TITLE = "Thanos"
    DESCRIPTION = "Browser to Browser Phishingtoolkit"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/TridevReddy/Thanos.git",
        "cd Thanos && sudo chmod -R 777 Thanos.sh"
    ]
    RUN_COMMANDS = ["cd Thanos;sudo bash Thanos.sh"]
    PROJECT_URL = "https://github.com/TridevReddy/Thanos"


class QRLJacking(HackingTool):
    TITLE = "QRLJacking"
    DESCRIPTION = "QRLJacking"
    INSTALL_COMMANDS = [
        "git clone https://github.com/OWASP/QRLJacking.git",
        "cd QRLJacking",
        "git clone https://github.com/mozilla/geckodriver.git",
        "chmod +x geckodriver",
        "sudo mv -f geckodriver /usr/local/share/geckodriver",
        "sudo ln -s /usr/local/share/geckodriver /usr/local/bin/geckodriver",
        "sudo ln -s /usr/local/share/geckodriver /usr/bin/geckodriver",
        "cd QRLJacker;pip3 install -r requirements.txt"
    ]
    RUN_COMMANDS = ["cd QRLJacking/QRLJacker;python3 QrlJacker.py"]
    PROJECT_URL = "https://github.com/OWASP/QRLJacking"


class Maskphish(HackingTool):
    TITLE = "Miskphish"
    DESCRIPTION = "Hide phishing URL under a normal looking URL (google.com or facebook.com)"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/jaykali/maskphish.git",
        "cd maskphish"]
    RUN_COMMANDS = ["cd maskphish;sudo bash maskphish.sh"]
    PROJECT_URL = "https://github.com/jaykali/maskphish"


class BlackPhish(HackingTool):
    TITLE = "BlackPhish"
    INSTALL_COMMANDS = [
        "sudo git clone https://github.com/iinc0gnit0/BlackPhish.git",
        "cd BlackPhish;sudo bash install.sh"
    ]
    RUN_COMMANDS = ["cd BlackPhish;sudo python3 blackphish.py"]
    PROJECT_URL = "https://github.com/iinc0gnit0/BlackPhish"

    def __init__(self):
        super(BlackPhish, self).__init__([('Update', self.update)])

    def update(self):
        os.system("cd BlackPhish;sudo bash update.sh")


class dnstwist(HackingTool):
    Title = 'dnstwist'
    Install_commands = ['sudo git clone https://github.com/elceef/dnstwist.git','cd dnstwist']
    Run_commands = ['cd dnstwist;sudo python3 dnstwist.py']
    project_url = 'https://github.com/elceef/dnstwist'


class PhishingAttackTools(HackingToolsCollection):
    TITLE = "Phishing attack tools"
    TOOLS = [
        autophisher(),
        Pyphisher(),
        AdvPhishing(),
        Setoolkit(),
        SocialFish(),
        HiddenEye(),
        Evilginx2(),
        ISeeYou(),
        SayCheese(),
        QRJacking(),
        BlackEye(),
        ShellPhish(),
        Thanos(),
        QRLJacking(),
        BlackPhish(),
        Maskphish(),
        dnstwist()
    ]

    def _get_attr_fallback(self, item, *names, default=""):
        for n in names:
            if hasattr(item, n):
                return getattr(item, n)
        return default

    def pretty_print(self):
        table = Table(title="Phishing Attack Tools", show_lines=True, expand=True)
        table.add_column("Title", style="purple", no_wrap=True)
        table.add_column("Description", style="purple")
        table.add_column("Project URL", style="purple", no_wrap=True)

        for t in self.TOOLS:
            # try typical attribute names, then fall back to common variations
            title = (
                self._get_attr_fallback(t, "TITLE", "Title", "title")
                or t.__class__.__name__
            )
            desc = self._get_attr_fallback(t, "DESCRIPTION", "Description", "description", "INSTALL_COMMANDS", default="") or ""
            # prefer PROJECT_URL but also accept project_url or project_url-like fields
            url = self._get_attr_fallback(t, "PROJECT_URL", "PROJECT_URL", "PROJECT", "project_url", "projectUrl", default="") or ""
            table.add_row(str(title), str(desc).strip().replace("\n", " "), str(url))

        panel = Panel(table, title="[purple]Available Tools[/purple]", border_style="purple")
        console.print(panel)

    def show_options(self, parent=None):
        console.print("\n")
        panel = Panel.fit("[bold magenta]Phishing Attack Tools Collection[/bold magenta]\n"
                          "Select a tool to view options or run it.",
                          border_style="purple")
        console.print(panel)

        table = Table(title="[bold cyan]Available Tools[/bold cyan]", show_lines=True, expand=True)
        table.add_column("Index", justify="center", style="bold yellow")
        table.add_column("Tool Name", justify="left", style="bold green")
        table.add_column("Description", justify="left", style="white")

        for i, tool in enumerate(self.TOOLS):
            title = self._get_attr_fallback(tool, "TITLE", "Title", "title", default=tool.__class__.__name__)
            desc = self._get_attr_fallback(tool, "DESCRIPTION", "Description", "description", default="—")
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
    tools = PhishingAttackTools()
    tools.pretty_print()
    tools.show_options()
