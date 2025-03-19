import subprocess
import sys
from datetime import datetime


def git_push():
    try:
        status = subprocess.run(["git", "status", "--porcelain"],
                                capture_output=True,
                                text=True,
                                check=True)

        if status.stdout.strip():
            subprocess.run(["git", "add", "."], check=True)
            commit_message = f"Auto commit - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            subprocess.run(["git", "commit", "-m", commit_message], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)
            print("Successfully pushed to GitHub")
        else:
            push_status = subprocess.run(["git", "push", "origin", "main"],
                                         capture_output=True,
                                         text=True)
            if push_status.returncode == 0:
                print("Successfully pushed existing commits to GitHub")
            else:
                print("Nothing to push")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    git_push()