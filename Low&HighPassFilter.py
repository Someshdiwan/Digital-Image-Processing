import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image_path = 'C:/Users\somes\PycharmProjects\DIP\Low&HighPassInput.jpg'
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Low-pass filtering (Gaussian filtering)
def lowpass_filter(image, kernel_size):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

# High-pass filtering (Laplacian filtering)
def highpass_filter(image):
    kernel = np.array([[0, 1, 0],
                       [1, -4, 1],
                       [0, 1, 0]], dtype=np.float32)
    return cv2.filter2D(image, -1, kernel)

# Apply low-pass and high-pass filters
kernel_size = 5  # Adjust kernel size for the Gaussian filter

lowpass_filtered = lowpass_filter(img, kernel_size)
highpass_filtered = highpass_filter(img)

# Plot the original and filtered images
plt.figure(figsize=(10, 6))
plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(lowpass_filtered, cmap='gray')
plt.title('Low-Pass Filtered Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(highpass_filtered, cmap='gray')
plt.title('High-Pass Filtered Image')
plt.axis('off')

plt.tight_layout()
plt.show()



# image filtering techniques using low-pass and high-pass filters to highlight different aspects of an image.

# What Are Low-Pass and High-Pass Filters?
# Low-Pass Filters (Gaussian Filtering):

# Purpose: Smoothens the image by suppressing high-frequency components (e.g., noise, edges).
# How It Works: Averages pixel values within a defined neighborhood using a Gaussian kernel.
# Use Case: Noise reduction, blurring.
# High-Pass Filters (Laplacian Filtering):

# Purpose: Highlights edges and fine details by emphasizing high-frequency components.
# How It Works: Computes the second derivative using the Laplacian operator to detect rapid intensity changes.
# Use Case: Edge detection, enhancing details.


# Code Explanation:

# Image Loading:

# Reads the image in grayscale using cv2.imread(image_path, cv2.IMREAD_GRAYSCALE).

# Low-Pass Filter:
# Applies a Gaussian blur using cv2.GaussianBlur.
# Kernel size (kernel_size) defines the size of the filter. A larger kernel size results in more blurring.

# High-Pass Filter:
# Implements the Laplacian filter using cv2.filter2D with a predefined kernel.

# The kernel is a simple 3x3 matrix designed for edge detection:

# 0  1  0
# 1 -4  1
# 0  1  0


# Visualization:

# Uses Matplotlib to display the original, low-pass filtered, and high-pass filtered images side by side for comparison.

# Expected Results
# Original Image: Shows the unprocessed input image.
# Low-Pass Filtered Image: Appears blurred, with reduced noise and softened edges.
# High-Pass Filtered Image: Highlights edges and fine details, while suppressing flat regions.


# Modify High-Pass Kernel:

# Experiment with different kernels for edge enhancement or sharpening:
# kernel = np.array([[1, 1, 1],
#                    [1, -8, 1],
#                    [1, 1, 1]], dtype=np.float32)


# Real-World Applications

# Low-Pass Filters:
# Reduce noise in images (e.g., medical imaging, astronomy).
# Smooth transitions in gradient-based image processing.

# High-Pass Filters:
# Detect edges for object recognition.
# Enhance features for detailed analysis (e.g., fingerprint analysis).