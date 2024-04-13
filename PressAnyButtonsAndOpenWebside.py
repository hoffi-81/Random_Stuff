import webbrowser
import keyboard
import time

# Define the key or key combination that represents a button press (customize this based on your encoder)
BUTTON_KEY = "F12"

while True:
    if keyboard.is_pressed(BUTTON_KEY):
        # Open YouTube when the button is pressed
        webbrowser.open("https://www.youtube.com/")
        #time.sleep(1)  # Adjust the sleep duration as needed
