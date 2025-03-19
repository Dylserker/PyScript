import subprocess
import sys


def git_push():
    try:
        subprocess.run(["git", "add", "."], check=True)

        from datetime import datetime
        commit_message = f"Auto commit - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Successfully pushed to GitHub")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    git_push()