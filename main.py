import cv2
import numpy as np

# 1. Read the newly updated image file
image_path = 'task3.JPG'
img = cv2.imread(image_path)

if img is None:
    print("Error: Could not read task3.JPG!")
else:
    # 2. Convert BGR to HSV color space
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # 3. Define HSV range for detecting blue color (Sky and Sea)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    # 4. Create mask for blue color
    blue_mask = cv2.inRange(img_hsv, lower_blue, upper_blue)
    
    # 5. Extract blue color components
    detected_blue = cv2.bitwise_and(img, img, mask=blue_mask)
    
    # 6. Save the processed image
    cv2.imwrite('output_sea.JPG', detected_blue)
    print("Success! The processed image has been saved as 'output_sea.JPG'")