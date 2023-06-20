import pyautogui

# Set the coordinates to move the mouse pointer to
x = 100
y = 200

# Move the mouse pointer to the specified coordinates
pyautogui.moveTo(x, y)

while True:
    # Get the current position of the mouse pointer
    x, y = pyautogui.position()
    
    # Print the current position
    print(f"Current mouse position: ({x}, {y})")