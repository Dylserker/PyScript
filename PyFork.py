import subprocess
import platform
import sys


class TerminalLauncher:
    def __init__(self):
        self.os_type = platform.system().lower()

    def open_terminal(self):
        try:
            if self.os_type == "windows":
                subprocess.Popen("cmd.exe")
            else:
                print("Unsupported operating system")
                sys.exit(1)
            print("Terminal launched successfully")
        except Exception as e:
            print(f"Error launching terminal: {e}")


if __name__ == "__main__":
    launcher = TerminalLauncher()
    launcher.run()