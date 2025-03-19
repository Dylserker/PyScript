import subprocess
import sys
from datetime import datetime


def make_dummy_change():
    with open('dummy_file.txt', 'a') as f:
        f.write(f"Update at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")


def git_push():
    try:
        make_dummy_change()

        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', f"Auto commit at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"],
                       check=True)
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
        print(f"Push successful at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    except subprocess.CalledProcessError as e:
        print(f"Error during push: {e}")
        sys.exit(1)


if __name__ == "__main__":
    git_push()