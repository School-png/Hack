import subprocess
import re

class HackingTerminal:
    def __init__(self):
        self.banner = """
                                _    _           _       _     _____  _____  _    _          
                             | |  | |         | |     | |   |_   _|/ ____|| ____|| |  | |          
                             | |__| | ___   __| | ___ | |     | |  | (___  |  _  || |__| | ___   __ 
                             |  __  |/ _ \ / _` |/ _ \| |    | |   \___ \ | |_| ||  __  |/ _ \ / _| 
                             | |  | | (_) | (_| | (_) | |___ | |  ____) ||  _  || |  | | (_) | (_| 
                             |_|  |_|\___/ \__,_|\___/|_____| \_| |_____/ |_| |_||_|  |_|\___/ \___| 
                                                                                                 
        """
        self.commands = {
            "help": self.show_help,
            "search": self.search_vulnerability,
            "exploit": self.exploit_vulnerability,
            "scan": self.network_scan,
            "bruteforce": self.brute_force_attack,
            "deface": self.deface_website,
        }

    def run(self):
        print(self.banner)
        while True:
            command = input("hacker@terminal:~$ ")
            if command in self.commands:
                self.commands[command]()
            else:
                print("Unknown command. Type 'help' for a list of commands.")

    def show_help(self):
        print("Available commands:")
        for command in self.commands:
            print(f"- {command}")

    def search_vulnerability(self):
        print("Searching for vulnerable targets...")
        # Simulate vulnerability scanning
        subprocess.run(["nmap", "-sV", "-T4", "target_ip"], check=True)

    def exploit_vulnerability(self):
        print("Exploiting vulnerability...")
        # Simulate exploitation
        subprocess.run(["exploit", "vulnerability_name"], check=True)

    def network_scan(self):
        print("Scanning network for targets...")
        # Simulate network scanning
        subprocess.run(["nmap", "-sS", "-T4", "target_network"], check=True)

    def brute_force_attack(self):
        print("Initiating brute force attack...")
        # Simulate brute force attack
        subprocess.run(["hydra", "target_host", "protocol:port", "-L wordlist.txt"], check=True)

    def deface_website(self):
        print("Defacing website...")
        # Simulate website defacement
        website_url = input("Enter the website URL: ")
        new_content = input("Enter the new content for the defaced website: ")
        modified_html = re.sub(r"<h1>.*?</h1>", f"<h1>{new_content}</h1>", open(website_url, "r").read())
        open(website_url, "w").write(modified_html)
        print("Website defaced successfully!")

if __name__ == "__main__":
    terminal = HackingTerminal()
    terminal.run()
