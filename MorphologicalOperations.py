import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_image_matplotlib(image, title="Image"):
    plt.imshow(image, cmap="gray")
    plt.title(title)
    plt.axis("off")
    plt.show()

def perform_dilation(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    dilated_image = cv2.dilate(image, kernel, iterations=1)
    return dilated_image

def perform_erosion(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    eroded_image = cv2.erode(image, kernel, iterations=1)
    return eroded_image

def perform_opening(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    return opened_image

def perform_closing(image, kernel_size):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return closed_image

if __name__ == "__main__":
    # Read an image (replace 'input_image.jpg' with your image path)
    image_path = "/MorphologicalInput.jpeg"
    original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Define the kernel size for morphological operations
    kernel_size = 3

    # Perform dilation
    dilated_image = perform_dilation(original_image, kernel_size)
    show_image_matplotlib(dilated_image, "Dilated Image")

    # Perform erosion
    eroded_image = perform_erosion(original_image, kernel_size)
    show_image_matplotlib(eroded_image, "Eroded Image")

    # Perform opening
    opened_image = perform_opening(original_image, kernel_size)
    show_image_matplotlib(opened_image, "Opened Image")

    # Perform closing
    closed_image = perform_closing(original_image, kernel_size)
    show_image_matplotlib(closed_image, "Closed Image")


    cv2.imwrite("dilated_image.jpg", dilated_image)
    cv2.imwrite("eroded_image.jpg", eroded_image)

# Morphological Operations: Theory and Explanation
#
# Morphological operations are a set of image processing techniques that process images based on their shapes. They are primarily applied to binary or grayscale images to analyze and modify the structures of objects in an image. These operations rely on a structuring element (kernel) to probe and transform the image.

# ---

# Basic Theory

# 1. Kernel (Structuring Element):
#    - A small matrix, usually square (e.g., 3x3 or 5x5), that slides over the image.
#    - Defines the region of influence for a given operation.
#
# 2. Binary and Grayscale Images:
#    - In binary images, operations focus on foreground (white pixels) and background (black pixels).
#    - In grayscale images, the operations affect pixel intensities relative to their neighbors.

# 3. Key Applications:
#    - Noise removal
#    - Gap filling
#    - Object segmentation
#    - Shape enhancement or simplification

# ---

# Types of Morphological Operations**

# 1. Dilation

#    - Effect: Expands the white regions (foreground) in the image.
#    - How it Works: Adds pixels to the object boundaries based on the kernel shape.
#    - Use Case: Fills small holes or connects broken parts of an object.

# 2. Erosion
#
#    - Effect: Shrinks the white regions (foreground) in the image.
#    - How it Works: Removes pixels from the object boundaries based on the kernel shape.
#    - Use Case: Removes small noise or separates connected objects.

# 3. Opening
#
#    - Effect: Performs erosion followed by dilation.
#    - How it Works: Removes small objects or noise while preserving the larger structures.
#    - Use Case: Cleans noisy images and isolates prominent objects.

# 4. Closing
#
#    - Effect: Performs dilation followed by erosion.
#    - How it Works: Closes small holes or gaps in the foreground objects.
#    - Use Case: Fills gaps, connects components, and smoothens boundaries.
#
# ---

# Explanation of the Code**
#
# 1. Image Input (`cv2.imread`):
#    - Reads the input grayscale image, which is the target for morphological operations.
#
# 2. Kernel Definition (`np.ones`):
#    - A `3x3` square kernel (structuring element) is created for processing the image.

# 3. Morphological Functions:**
#    - Dilation: Expands the foreground regions.
#    - Erosion: Contracts the foreground regions.
#    - Opening: Removes small noise while preserving object structure.
#    - Closing: Fills small gaps in the objects.

# 4. Visualization (`show_image_matplotlib`):
#    - Uses Matplotlib to display the processed images.
#
# 5. Saving Images (`cv2.imwrite`):
#    - Saves the processed images (e.g., `dilated_image.jpg`) for further inspection or use.

# ---

# Real-World Applications
# 1. Noise Removal:
#    - Use **opening** to clean noisy binary images.
#
# 2. Gap Filling:
#    - Use closing to fill small gaps in shapes or contours.
#
# 3. Shape Analysis:
#    - Use erosion and dilation to simplify or modify object shapes.
#
# 4. Object Segmentation:
#    - Morphological operations help isolate objects of interest by smoothing contours or separating connected components.

# ---

