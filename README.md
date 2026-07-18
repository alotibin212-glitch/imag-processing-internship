### image-processing-internship

A specialized Computer Vision script crafted with Python and OpenCV to segment and isolate aquatic and atmospheric features. By applying precise HSV color-space thresholding, the program filters out non-blue elements to cleanly extract sea and sky regions from complex landscape imagery.

### 🌊 Color Detection Visual Analysis
Below is the verified graphical execution mapping showcasing the original image backdrop alongside the successfully processed and isolated blue color channels:
1. Original Reference Artifact

   
   <img width="720" height="1280" alt="task3" src="https://github.com/user-attachments/assets/993e42fd-ad86-4737-960e-ca21ebbade9b" />



3. Extracted & Isolated Blue Spectrum
4. 
   <img width="720" height="1280" alt="output_sea" src="https://github.com/user-attachments/assets/45a89c90-5597-4a13-814e-c24fac9c6442" />





## ⚙️ Technical Architecture & Pipeline Logic

The underlying image processing framework executes through a structured mathematical multi-stage filter pattern:

1. Color Plane Transition: Converts the native BGR digital pixel matrix into the decoupled HSV Color Space to isolate color components from light intensity.
2. Single-Threshold Masking: Implements exact lower and upper boundaries to map the blue color spectrum spanning the core region of the HSV circular hue scale:
   * Lower Bound Matrix: [90, 50, 50]
   * Upper Bound Matrix: [130, 255, 255]
3. Bitwise Extraction Matrix: Applies a bitwise logical AND mask overlay onto the original matrix structure, safely dropping all background non-blue artifacts (such as rocks and dark shores).
