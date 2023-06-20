import cv2
import numpy as np
import pyautogui

leftB=1524
topB=369
widthB=1918-1524
heightB=671-369

leftt=1679
topt=164
widtht=1759-1679
heightt=264-164

# Load the template image and the four data images
data1 = cv2.imread('template_mario.png')
data2 = cv2.imread('template_luigi.png')
data3 = cv2.imread('template_wario.png')
data4 = cv2.imread('template_yoshi.png')

# Load the bigger image and the template image
#bigger_image = cv2.imread("bigger_image.png")
bigger_image = np.array(pyautogui.screenshot(region=(leftB, topB, widthB, heightB)))
bigger_image = cv2.cvtColor(bigger_image, cv2.COLOR_BGR2RGB)
#template_image = cv2.imread("template_image.png")
template = np.array(pyautogui.screenshot(region=(leftt, topt, widtht, heightt)))
template = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)

cv2.imshow("input", bigger_image)
cv2.waitKey(0)
cv2.imshow("template", template)
cv2.waitKey(0)

"""# Convert the template and data images to grayscale
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
data1_gray = cv2.cvtColor(data1, cv2.COLOR_BGR2GRAY)
data2_gray = cv2.cvtColor(data2, cv2.COLOR_BGR2GRAY)
data3_gray = cv2.cvtColor(data3, cv2.COLOR_BGR2GRAY)
data4_gray = cv2.cvtColor(data4, cv2.COLOR_BGR2GRAY)"""

# Perform template matching using normalized cross-correlation (NCC)
result1 = cv2.matchTemplate(data1, template, cv2.TM_CCORR_NORMED)
result2 = cv2.matchTemplate(data2, template, cv2.TM_CCORR_NORMED)
result3 = cv2.matchTemplate(data3, template, cv2.TM_CCORR_NORMED)
result4 = cv2.matchTemplate(data4, template, cv2.TM_CCORR_NORMED)

# Find the position with the highest matching score in each data image
min_val1, max_val1, min_loc1, max_loc1 = cv2.minMaxLoc(result1)
min_val2, max_val2, min_loc2, max_loc2 = cv2.minMaxLoc(result2)
min_val3, max_val3, min_loc3, max_loc3 = cv2.minMaxLoc(result3)
min_val4, max_val4, min_loc4, max_loc4 = cv2.minMaxLoc(result4)

# Determine which data image has the highest matching score
if max_val1 > max_val2 and max_val1 > max_val3 and max_val1 > max_val4:
    print('Mario is the best match')
    template_image = data1
elif max_val2 > max_val1 and max_val2 > max_val3 and max_val2 > max_val4:
    print('Luigi is the best match')
    template_image = data2
elif max_val3 > max_val1 and max_val3 > max_val2 and max_val3 > max_val4:
    print('Wario is the best match')
    template_image = data3
else:
    print('Yoshi is the best match')
    template_image = data4

cv2.imshow("template gardée", template_image)
cv2.waitKey(0)

# Convert both images to grayscale
bigger_gray = cv2.cvtColor(bigger_image, cv2.COLOR_RGB2GRAY)
template_gray = cv2.cvtColor(template_image, cv2.COLOR_RGB2GRAY)

# Find the template in the bigger image using template matching
result = cv2.matchTemplate(bigger_gray, template_gray, cv2.TM_CCOEFF_NORMED)

# Define a threshold value for the similarity score
threshold = 0.8

# Get the location of the template in the bigger image
locations = np.where(result >= threshold)
locations = list(zip(*locations[::-1]))

# Draw a bounding box around each location where the template was found
for loc in locations:
    top_left = loc
    bottom_right = (top_left[0] + template_image.shape[1], top_left[1] + template_image.shape[0])
    cv2.rectangle(bigger_image, top_left, bottom_right, (0, 0, 255), 1)

# Display the result
cv2.imshow("Result", bigger_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
