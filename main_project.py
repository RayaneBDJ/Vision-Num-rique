"https://opencv.org/get-started/"

import cv2

img = cv2.imread("images\image_test.htm")

cv2.imshow("Display window", img)
k = cv2.waitKey(0) # Wait for a keystroke in the window

