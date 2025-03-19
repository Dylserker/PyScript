import os
import random
import time
from datetime import datetime, timedelta
import schedule
import subprocess


def make_dummy_change():
    # Create a timestamp in the dummy file
    with open('dummy_file.txt', 'a') as f:
        f.write(f"Update at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")


def git_push():
    try:
        # Git commands
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', f"Auto commit at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"])
        subprocess.run(['git', 'push', 'origin', 'main'])
        print(f"Push successful at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"Error during push: {str(e)}")


def schedule_pushes():
    schedule.clear()

    num_pushes = random.randint(20, 30)

    start_time = datetime.now().replace(hour=8, minute=0, second=0)
    end_time = datetime.now().replace(hour=20, minute=0, second=0)

    for _ in range(num_pushes):
        random_minutes = random.randint(0, (end_time - start_time).seconds // 60)
        push_time = start_time + timedelta(minutes=random_minutes)
        schedule.every().day.at(push_time.strftime("%H:%M")).do(lambda: (make_dummy_change(), git_push()))


def main():
    schedule_pushes()

    schedule.every().day.at("00:01").do(schedule_pushes)

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()