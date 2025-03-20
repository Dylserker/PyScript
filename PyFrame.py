import pyautogui
import time
import keyboard
import sys
from datetime import datetime


class WarframeFoundry:
    def __init__(self):
        self.confidence = 0.8
        self.running = True

    def locate_and_click(self, image_path):
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=self.confidence)
            if location:
                pyautogui.click(location)
                return True
        except Exception as e:
            print(f"Error finding {image_path}: {e}")
        return False

    def claim_items(self):
        try:
            if self.locate_and_click('images/claim_button.png'):
                time.sleep(0.5)
                self.locate_and_click('images/ok_button.png')
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Item claimed")
                time.sleep(1)
                return True
            return False
        except Exception as e:
            print(f"Error during claim process: {e}")
            return False

    def run(self):
        print("Starting Warframe Foundry Auto-Claim")
        print("Press 'Esc' to exit")

        while self.running:
            try:
                if keyboard.is_pressed('esc'):
                    print("\nStopping script...")
                    self.running = False
                    break

                if not self.claim_items():
                    print(f"[{datetime.now().strftime('%H:%M:%S')}] No items to claim")

                time.sleep(5)

            except Exception as e:
                print(f"Error: {e}")
                break


if __name__ == "__main__":
    foundry = WarframeFoundry()
    foundry.run()