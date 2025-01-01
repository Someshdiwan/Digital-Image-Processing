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

