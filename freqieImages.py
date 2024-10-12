#Here we will gather the frequency composition of our images

import cv2
import matplotlib.pyplot as plt

# Step 1: Read the image
image = cv2.imread('cat.png')

# Convert BGR to RGB (OpenCV reads the image in BGR format)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Step 2: Split the image into its Red, Green, and Blue channels
r, g, b = cv2.split(image_rgb)

# Step 3: Calculate histograms for each channel
# bins parameter defines the number of bins
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])

# Step 4: Plot the histograms
plt.figure()
plt.title("RGB Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")

plt.plot(hist_r, color='r', label='Red')
plt.plot(hist_g, color='g', label='Green')
plt.plot(hist_b, color='b', label='Blue')
plt.legend()

# Show the plot
plt.xlim([0, 256])  # Pixel values range from 0 to 255
plt.show()