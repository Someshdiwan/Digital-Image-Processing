import cv2
import numpy as np


def image_boundaries_drselva(image_path):
    # Read the input image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Please check the image path.")
        return None

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding for better binary segmentation
    binary_image = cv2.adaptiveThreshold(
        gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
    )

    # Invert the binary image if needed (to ensure contours are extracted correctly)
    binary_image = cv2.bitwise_not(binary_image)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Debugging: Print the number of detected contours
    print(f"Number of contours detected: {len(contours)}")

    # Create an output image to draw the contours
    image_with_regions = np.zeros_like(image)
    cv2.drawContours(image_with_regions, contours, -1, (255, 255, 255), 2)  # Draw contours in white

    return image, image_with_regions  # Return both original and processed images


def combine_images(input_image, output_image):
    # Resize both images to have the same height for side-by-side display
    height = max(input_image.shape[0], output_image.shape[0])
    width = input_image.shape[1] + output_image.shape[1]

    combined_image = np.zeros((height, width, 3), dtype=np.uint8)

    # Place both images side by side
    combined_image[:input_image.shape[0], :input_image.shape[1]] = input_image
    combined_image[:output_image.shape[0], input_image.shape[1]:] = output_image

    return combined_image


if __name__ == "__main__":
    input_image_path = "C:/Users/somes/PycharmProjects/DIP/BoundariesExtractionInput.jpg"
    images = image_boundaries_drselva(input_image_path)

    if images is not None:
        input_image, image_with_regions = images

        # Combine the input image and the output image (with boundaries) side by side
        combined_image = combine_images(input_image, image_with_regions)

        # Display the combined image
        cv2.imshow("Input and Output Side by Side", combined_image)


        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Region and Boundary Extraction in Image Processing

# Region and boundary extraction are fundamental tasks in image analysis and computer vision. They are used to identify and delineate distinct regions or boundaries in an image based on some predefined criteria, such as intensity, color, or texture. The goal is to isolate the objects of interest from the background or other irrelevant elements.
#
# 1. Region Extraction:
#    - Region extraction refers to identifying continuous areas of interest (regions) in an image. These regions can be defined by particular properties such as color, texture, or intensity. Region extraction often involves segmenting the image into homogeneous regions that share similar attributes.
#    - Methods like thresholding, clustering (e.g., K-means), and watershed algorithms are commonly used for region extraction.
#
# 2. Boundary Extraction:
#    - Boundary extraction, on the other hand, is the process of detecting the edges or contours that separate distinct regions in an image. Boundaries mark the transition between different regions, often corresponding to object boundaries or edges within the image.
#    - Boundary extraction is commonly performed using edge detection algorithms such as the Canny edge detector, Sobel operator, or Laplacian of Gaussian.

# ---

# Concepts in Boundary Extraction
#
# 1. Edges vs. Boundaries:
#    - Edge: A local feature that represents the change in intensity or color in an image.
#    - Boundary: A complete outline that forms the shape of an object.
#
# 2. Grayscale Conversion:
#    - Converts the input image into a single intensity channel to simplify analysis.
#    - Helps remove unnecessary color information, retaining only intensity variations.
#
# 3.Thresholding:
#    - Converts a grayscale image to a binary image (black and white).
#    - Types of Thresholding:
#      - Global Thresholding: Applies a single threshold value to the entire image.
#      - Adaptive Thresholding:** Calculates thresholds dynamically based on the local neighborhood, useful for images with varying illumination.
#
# 4. Contours:
#    - Contours are continuous curves or boundaries that enclose the shape of an object.
#    - Extracted from binary images where the object and background are distinctly separated.
#
# 5. Contour Representation:
#    - CHAIN_APPROX_SIMPLE: Reduces memory usage by compressing horizontal, vertical, and diagonal segments.
#    - CHAIN_APPROX_NONE: Retains all contour points, providing a more detailed boundary.
#
# 6. Image Segmentation:
#    - The process of partitioning an image into regions based on intensity or color similarities.
#    - Boundary extraction is a specific form of segmentation that isolates the edges of objects.
#
# ---

# Process of Boundary Extraction
#
# 1. Input Image:
#    - Start with a grayscale or color image.
#
# 2. Preprocessing:
#    - Convert to grayscale.
#    - Smooth or blur the image to reduce noise.
#
# 3. Binary Image Creation:
#    - Apply thresholding to separate the object from the background.
#
# 4. Contour Detection:
#    - Identify the edges or boundaries using algorithms like `cv2.findContours`.
#
# 5. Visualization:
#    - Highlight boundaries on the original image using functions like `cv2.drawContours`.

# ---

# Applications of Boundary Extraction
#
# 1. Object Detection:
#    - Identifying objects in images for recognition or tracking.
#
# 2. Medical Imaging:
#    - Highlighting boundaries of organs, tumors, or other structures.
#
# 3. Shape Analysis:
#    - Extracting object boundaries for measurements or classification.
#
# 4. Autonomous Systems:
#    - Detecting road lanes, signs, or obstacles for navigation.
#
# 5. Image Editing:
#    - Segmenting objects for manipulation or compositing.

# ---

# Advantages of Boundary Extraction
#
# - Simplifies complex images by focusing on essential features.
# - Effective for shape-based analysis.
# - Reduces computational complexity in subsequent processing.
#
# ---
#
# Challenges
#
# 1. Noise:
#    - Small intensity variations may create false boundaries.
#
# 2. Illumination Variations:
#    - Non-uniform lighting can affect thresholding results.
#
# 3. Overlapping Objects:
#    - Difficult to distinguish individual boundaries.
#
# 4. Resolution Issues:
#    - Low-resolution images may lack clear edges.

# ---

# There are several methods for boundary extraction. They can be classified based on the techniques used and the nature of the output.
#
# 1. Edge-Based Boundary Extraction:
#    - This technique identifies changes in intensity or color in an image, which are indicative of object boundaries.
#    - Methods:
#      - Sobel Operator: Detects edges by calculating the gradient (rate of change) in intensity at each pixel in both horizontal and vertical directions.
#      - Canny Edge Detection: A multi-step process that detects edges by filtering the image using Gaussian blurring, finding intensity gradients, non-maximum suppression, and edge tracking by hysteresis.
#      - Laplacian of Gaussian (LoG): Combines Gaussian smoothing with Laplacian edge detection. It’s good for detecting edges of different sizes.
#      - Prewitt Operator: Similar to the Sobel operator but with a different kernel for edge detection.
#
#    - Advantages: These methods are generally robust in detecting sharp transitions (edges) in an image.
#    - Disadvantages: They may not work well on noisy images or for detecting boundaries in regions with gradual transitions.
#
# 2. Region-Based Boundary Extraction:
#    - Region-based techniques focus on detecting homogeneous regions in an image first, then finding their boundaries.
#    - Methods:
#      - Region Growing: Starts with a seed pixel and adds neighboring pixels to the region if they meet a predefined similarity criterion (such as intensity, texture, or color).
#      - Watershed Algorithm: Treats an image as a topographic surface, where the intensity of each pixel corresponds to elevation. The watershed algorithm finds boundaries by simulating water flowing into basins and identifying the lines of highest elevation (watershed lines).
#      - Thresholding: Pixels are grouped based on their intensity values. Binary or multi-level thresholding can be used to extract regions, and the boundaries between regions are marked.
#
#    - Advantages: Region-based methods can be more reliable for detecting complex shapes or regions with soft transitions.
#    - Disadvantages: They are sensitive to initialization (e.g., seed points in region growing) and may struggle with varying lighting conditions or noisy images.
#
# 3. Contour-Based Boundary Extraction:
#    - Contour-based extraction is a specialized approach where the focus is on detecting and tracking contours (curves or boundaries) around objects in the image.
#    - Methods:
#      - FindContours in OpenCV: A function in OpenCV that detects the contours in a binary image. It returns a list of contours and can be used to draw boundaries around regions.
#      - Active Contours (Snakes): A model that evolves to fit the boundary of an object by minimizing an energy function.
#      - Level Sets: A method based on evolving a contour over time to detect boundaries based on geometric properties.
#
#    - Advantages: These methods are particularly effective for extracting smooth and complex boundaries.
#    - Disadvantages: Active contour methods can be computationally expensive and may require careful initialization.
#
# 4. Edge Linking Methods:
#    - After edge detection, the edges are often fragmented, and linking them together is necessary to create continuous boundaries.
#    - Methods:
#      - Hough Transform: A technique used to detect simple geometric shapes like lines, circles, and ellipses. It can be used to link edges and identify boundaries.
#      - Edge Tracing by Hysteresis: After applying edge detection, strong edges are retained while weak edges are linked to strong ones if they are connected.
#
#    - Advantages: Can recover fragmented edges and improve boundary continuity.
#    - Disadvantages: Might lead to over- or under-segmentation if thresholds or parameters are not well-tuned.


# Summary of Common Boundary Extraction Methods:
#
# | **Method**                | **Description**                                                                 | **Use Case**                                           |
# |---------------------------|---------------------------------------------------------------------------------|-------------------------------------------------------|
# | **Sobel Operator**         | Detects edges by computing gradient.                                            | Basic edge detection, primarily for sharp transitions. |
# | **Canny Edge Detection**   | Multi-step method that includes smoothing and edge tracking.                     | High-accuracy edge detection, especially in noisy images. |
# | **Watershed Algorithm**    | Treats the image as a topographic surface and finds watershed lines as boundaries. | Segmenting regions in complex images.                  |
# | **Active Contours**        | Iteratively adjusts the boundary to match the image features.                    | Detecting smooth, complex object boundaries.          |
# | **FindContours (OpenCV)**  | Detects contours in a binary image and marks boundaries.                         | Efficient extraction of object contours.               |
# | **Hough Transform**        | Detects geometric shapes and lines by transforming the image space.             | Detecting simple geometric boundaries (e.g., circles, lines). |


# ---