# Key Concepts
# 1. Image Smoothing:
#    - Smoothing reduces noise or details in an image by averaging pixel intensities in a local neighborhood defined by the kernel size.
#    - Implemented using Gaussian Blur, which applies a Gaussian function to weight pixels, providing a smooth and natural blurring effect.

# 2. Image Sharpening:
#    - Enhances edges and fine details in an image by combining the original image and a blurred version.
#    - Achieved using the formula: text{sharpened} = (1 + amount) x image - amount x blurred.
#    - Where:
#      - amount determines the intensity of sharpening.
#      - A Gaussian blur is used to smooth the image before subtracting it.

# Code Explanation
# 1. Sharpening Function (sharpen_image_selva):
# - Input Parameters:
#      - `image`: Input image.
#      - `kernel_size`: Size of the Gaussian kernel used for blurring (default: 5 x 5)).
#      - `amount`: Sharpening intensity (default: (1.0)).

#    - Steps:
#      1. Blur the image using `cv2.GaussianBlur`.
#      2. Combine the original image and the blurred image using `cv2.addWeighted`.

# 2. Smoothing Function (smooth_image_selva):
#    - Input Parameters:
#      - `image`: Input image.
#      - `kernel_size`: Size of the Gaussian kernel (default: (5 x 5)).

#      - Steps:
#      1. Apply Gaussian blur directly using `cv2.GaussianBlur`.

# 3. Main Execution:
#    - Reads the input image using `cv2.imread`.
#    - Verifies if the image was successfully loaded.
#    - Applies:
#      - Sharpening: Creates a sharpened version of the image.
#      - Smoothing: Creates a smoothed (blurred) version of the image.
#      - Displays the original, sharpened, and smoothed images using `cv2_imshow` (specific to Google Colab).

# 4. Error Handling:
#    - Ensures the input image path is correct and readable.

# ---

# Adjusting Parameters
# 1.Sharpening:
#    - Increase `amount` for more pronounced sharpening.
#    - Decrease `amount` for subtle sharpening.

# 2. Smoothing:
#    - Increase the kernel size (e.g., (11 x 11)) for stronger blurring.
#    - Decrease the kernel size (e.g., (3 x 3)) for mild smoothing.

# ---

import cv2
import numpy as np
import matplotlib.pyplot as plt

def sharpen_image_selva(image, kernel_size=(5, 5), amount=1.0):
    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(image, kernel_size, 0)
    # Sharpen the image
    sharpened = cv2.addWeighted(image, 1 + amount, blurred, -amount, 0)
    return sharpened

def smooth_image_selva(image, kernel_size=(5, 5)):
    # Apply Gaussian Blur (Smoothing)
    return cv2.GaussianBlur(image, kernel_size, 0)

if __name__ == "__main__":
    # Replace with the path to your image
    input_image_path = "C:/Users/somes/PycharmProjects/DIP/Smoothing&SharpeningImageInput.png"

    # Read the input image
    image = cv2.imread(input_image_path)

    if image is None:
        print("Error: Unable to read the input image.")
    else:
        # Perform image sharpening with an amount of 1.5 and kernel size of (5, 5)
        sharpened_image = sharpen_image_selva(image, kernel_size=(5, 5), amount=1.5)

        # Perform image smoothing (blurring) with kernel size (7, 7)
        smoothed_image = smooth_image_selva(image, kernel_size=(7, 7))

        # Convert images to RGB for displaying with matplotlib (since OpenCV loads images in BGR)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        sharpened_image_rgb = cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB)
        smoothed_image_rgb = cv2.cvtColor(smoothed_image, cv2.COLOR_BGR2RGB)

        # Plot all images in one figure using matplotlib
        plt.figure(figsize=(15, 5))  # Set the figure size

        # Display Original Image
        plt.subplot(1, 3, 1)  # 1 row, 3 columns, 1st image
        plt.imshow(image_rgb)
        plt.title("Original Image")
        plt.axis("off")

        # Display Sharpened Image
        plt.subplot(1, 3, 2)  # 1 row, 3 columns, 2nd image
        plt.imshow(sharpened_image_rgb)
        plt.title("Sharpened Image")
        plt.axis("off")

        # Display Smoothed Image
        plt.subplot(1, 3, 3)  # 1 row, 3 columns, 3rd image
        plt.imshow(smoothed_image_rgb)
        plt.title("Smoothed Image")
        plt.axis("off")

        # Show all images in a single figure
        plt.tight_layout()
        plt.show()


# Spatial Domain Filters:
# In digital image processing, **spatial domain filters** are techniques applied directly on the pixels of an image to achieve specific transformations or enhancements.
# These filters operate in the spatial domain, meaning they process the image by manipulating the pixel values at specific locations (spatial coordinates) based on their neighbors.

# Key Concepts

# 1. Spatial Domain:
#    - Refers to the pixel space where the image intensity values are represented as a function of spatial coordinates (e.g., (f(x, y)), where (x) and (y) are the pixel positions).
# 2. Filtering in the Spatial Domain:
#    - Involves applying a kernel (a small matrix, often called a mask or filter) to each pixel and its neighbors to compute a new value for the pixel.


# Types of Spatial Domain Filters
# 1. Linear Filters:
# - Operate using convolution, applying a kernel uniformly across the image.
#    - Examples:
#      - Low-Pass Filters (Smoothing):
#        - Reduce noise or blur the image.
#        - Common filter: Gaussian blur.
#        - High-Pass Filters (Sharpening):
#        - Enhance edges or fine details.
#        - Common filter: Laplacian.

# 2.Non-Linear Filters:
#    - Use non-linear operations on the pixel values.
#    - Examples:
#      - Median Filter:
#        - Replaces each pixel with the median of its neighbors.
#        - Effective for removing salt-and-pepper noise.
#        - Bilateral Filter:
#        - Smooths the image while preserving edges.

# ---

# Advantages of Spatial Domain Filters
# 1. Intuitive Understanding:
#    - Operate directly on pixels, making the effects easy to visualize and interpret.

# 2. Versatility:
#    - Can be used for various tasks like smoothing, sharpening, edge detection, and noise removal.

# 3. Efficiency:
#    - Relatively simple to implement, especially for small kernels.

# Limitations
# 1. Artifacts:
#    - May introduce artifacts (e.g., ringing effects near edges with high-pass filters).

# 2. Global Features:
#    - Ineffective at capturing large-scale or global features in an image (e.g., periodic patterns).

# 3. Performance:
#    - Large kernel sizes can be computationally expensive.


# Applications
# 1. Image Enhancement:

#    - Smoothing to reduce noise or sharpening to enhance details.

# 2. Feature Extraction:

#    - Detecting edges, lines, and corners.
# 3. Noise Removal:
#    - Reducing unwanted noise while preserving essential details.