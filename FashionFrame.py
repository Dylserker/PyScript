import pyautogui
import time
import keyboard
from datetime import datetime


class WarframeFashion:
    def __init__(self):
        self.confidence = 0.8
        self.running = True
        self.colors = {
            'primary': 'images/primary_color.png',
            'secondary': 'images/secondary_color.png',
            'tertiary': 'images/tertiary_color.png',
            'accents': 'images/accents_color.png',
            'emissive1': 'images/emissive1_color.png',
            'emissive2': 'images/emissive2_color.png',
            'energy1': 'images/energy1_color.png',
            'energy2': 'images/energy2_color.png'
        }

    def locate_and_click(self, image_path):
        try:
            location = pyautogui.locateCenterOnScreen(image_path, confidence=self.confidence)
            if location:
                pyautogui.click(location)
                return True
        except Exception as e:
            print(f"Error finding {image_path}: {e}")
        return False

    def apply_color_scheme(self, scheme):
        try:
            for color_slot, color_coords in scheme.items():
                if color_slot in self.colors:
                    if self.locate_and_click(self.colors[color_slot]):
                        time.sleep(0.5)
                        pyautogui.click(color_coords[0], color_coords[1])
                        print(f"Applied {color_slot} color")
                        time.sleep(0.5)
        except Exception as e:
            print(f"Error applying color scheme: {e}")

    def apply_attachments(self, attachments):
        try:
            for attachment, image_path in attachments.items():
                if self.locate_and_click(image_path):
                    print(f"Applied {attachment}")
                    time.sleep(0.5)
        except Exception as e:
            print(f"Error applying attachments: {e}")

    def run(self, color_scheme, attachments):
        print("Starting Warframe Fashion Automation")
        print("Press 'Esc' to exit")

        while self.running:
            try:
                if keyboard.is_pressed('esc'):
                    print("\nStopping script...")
                    self.running = False
                    break

                self.apply_color_scheme(color_scheme)

                self.apply_attachments(attachments)

                print(f"[{datetime.now().strftime('%H:%M:%S')}] Customization complete")
                break

            except Exception as e:
                print(f"Error: {e}")
                break


if __name__ == "__main__":
    my_color_scheme = {
        'primary': (100, 200),
        'secondary': (150, 250),
        'tertiary': (200, 300),
        'accents': (250, 350),
        'emissive1': (300, 400),
        'emissive2': (350, 450),
        'energy1': (400, 500),
        'energy2': (450, 550)
    }

    my_attachments = {
        'syandana': 'images/syandana.png',
        'chest': 'images/chest_attachment.png',
        'shoulders': 'images/shoulders_attachment.png',
        'legs': 'images/legs_attachment.png'
    }

    fashion = WarframeFashion()
    fashion.run(my_color_scheme, my_attachments)