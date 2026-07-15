# image-processing-internship

A specialized Computer Vision script crafted with Python and OpenCV to segment and isolate aquatic and atmospheric features. By applying precise HSV color-space thresholding, the program filters out non-blue elements to cleanly extract sea and sky regions from complex landscape imagery.

## 🌊 Color Detection Visual Analysis

Below is the verified graphical execution mapping showcasing the original image backdrop alongside the successfully processed and isolated blue color channels:

| Original Reference Artifact | Extracted & Isolated Blue Spectrum |
| :--- | :--- |
| Original Landscape (task3.JPG) | Detected Blue Color (output_sea.JPG) |

## ⚙️ Technical Architecture & Pipeline Logic

The underlying image processing framework executes through a structured mathematical multi-stage filter pattern:

1. Color Plane Transition: Converts the native BGR digital pixel matrix into the decoupled HSV Color Space to isolate color components from light intensity.
2. Single-Threshold Masking: Implements exact lower and upper boundaries to map the blue color spectrum spanning the core region of the HSV circular hue scale:
   * Lower Bound Matrix: [90, 50, 50]
   * Upper Bound Matrix: [130, 255, 255]
3. Bitwise Extraction Matrix: Applies a bitwise logical AND mask overlay onto the original matrix structure, safely dropping all background non-blue artifacts (such as rocks and dark shores).
