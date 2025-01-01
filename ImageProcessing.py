import numpy as np
import cv2
import matplotlib.pyplot as plt

def contrast_stretching(image, low_percentile=1, high_percentile=99):
    low_bound = np.percentile(image, low_percentile)
    high_bound = np.percentile(image, high_percentile)
    stretched_image = np.clip((image - low_bound) * 255.0 / (high_bound - low_bound), 0, 255).astype(np.uint8)
    return stretched_image

def adjust_brightness(image, brightness_factor):
    adjusted_image = np.clip(image * brightness_factor, 0, 255).astype(np.uint8)
    return adjusted_image

def invert_image(image):
    inverted_image = 255 - image
    return inverted_image

# Load the image
image_path = "/ImageProcessingInput.jpg"
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Apply contrast stretching (adjust low_percentile and high_percentile as needed)
stretched_image = contrast_stretching(image, low_percentile=5, high_percentile=95)

# Adjust brightness (use a factor less than 1 to make the image darker and greater than 1 to make it brighter)
brightness_factor = 1.5
brightened_image = adjust_brightness(image, brightness_factor)

# Invert the image
inverted_image = invert_image(image)

# Display the original and processed images
plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original Image")

plt.subplot(2, 2, 2)
plt.imshow(stretched_image, cmap='gray')
plt.title("Contrast Stretched Image")

plt.subplot(2, 2, 3)
plt.imshow(brightened_image, cmap='gray')
plt.title("Brightened Image")

plt.subplot(2, 2, 4)
plt.imshow(inverted_image, cmap='gray')
plt.title("Inverted Image")

plt.tight_layout()
plt.show()

#image using three techniques: contrast stretching, brightness adjustment, and image inversion.

# 1. Contrast Stretching

# Purpose: Enhances the contrast of the image by remapping pixel intensities.
# How it works:
# Computes the lower and upper percentiles (low_percentile and high_percentile) of the pixel intensity distribution in the image.
# Rescales pixel intensities so that the range between these percentiles maps to [0, 255].
# Clips any pixel values outside this range.

# stretched_image = contrast_stretching(image, low_percentile=5, high_percentile=95)

# 2. Brightness Adjustment
# Purpose: Makes the image brighter or darker by scaling the pixel values.
# How it works:
# Multiplies each pixel value in the image by a brightness_factor.
# Uses np.clip to ensure pixel values stay within the valid range [0, 255].
# A factor > 1 increases brightness, while a factor < 1 decreases brightness.Brightness Adjustment
# Purpose: Makes the image brighter or darker by scaling the pixel values.

# How it works:
# Multiplies each pixel value in the image by a brightness_factor.
# Uses np.clip to ensure pixel values stay within the valid range [0, 255].
# A factor > 1 increases brightness, while a factor < 1 decreases brightness.

# brightness_factor = 1.5
# brightened_image = adjust_brightness(image, brightness_factor)

# 3. Image Inversion
# Purpose: Produces a photographic negative of the image.
# How it works:
# Subtracts each pixel value from 255, effectively flipping the pixel intensity values.

# Usage in code:
# inverted_image = invert_image(image)



