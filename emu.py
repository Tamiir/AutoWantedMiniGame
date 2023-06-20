import cv2
import numpy as np
import pyautogui
import time

# Define the region of interest where the Wanted poster appears
roi_top = 180
roi_left = 20
roi_bottom = 330
roi_right = 220

# Load the template image of the Wanted poster
template = cv2.imread("wanted_template.png", cv2.IMREAD_GRAYSCALE)

# Define the threshold similarity score for matching the template
threshold = 0.95

# Define a function to check if the template is present in a given image
def match_template(image):
    # Crop the image to the region of interest
    roi = image[roi_top:roi_bottom, roi_left:roi_right]
    # Convert the region of interest to grayscale
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    # Apply template matching to the grayscale region of interest
    result = cv2.matchTemplate(gray_roi, template, cv2.TM_CCOEFF_NORMED)
    # Get the maximum similarity score
    max_score = np.max(result)
    # Check if the maximum similarity score is above the threshold
    if max_score >= threshold:
        # Get the location of the maximum similarity score
        _, _, max_loc, _ = cv2.minMaxLoc(result)
        # Compute the location of the Wanted poster in the original image
        wanted_x = max_loc[0] + roi_left
        wanted_y = max_loc[1] + roi_top
        return wanted_x, wanted_y
    else:
        return None

# Define a function to click on the Wanted poster
def click_wanted(x, y):
    # Compute the coordinates of the click relative to the emulator window
    emulator_x = x * 2
    emulator_y = y * 2
    # Move the mouse pointer to the coordinates and click
    pyautogui.moveTo(emulator_x, emulator_y)
    pyautogui.click()

# Start the emulator and load the game
# ...

# Start the game loop
while True:
    # Take a screenshot of the emulator window
    screenshot = pyautogui.screenshot()
    # Convert the screenshot to a NumPy array
    image = np.array(screenshot)
    # Check if the Wanted poster is present in the screenshot
    wanted_location = match_template(image)
    if wanted_location is not None:
        # Click on the Wanted poster
        click_wanted(*wanted_location)
    # Wait for a short amount of time before taking the next screenshot
    time.sleep(0.1)
