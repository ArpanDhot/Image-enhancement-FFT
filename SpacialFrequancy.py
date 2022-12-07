import cv2
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve2d, medfilt2d

def mean_filter(image: np.ndarray, radius: int, mask_std: float) -> np.ndarray:
    # Getting the kernel size. Kernel size is used by the filters, because the filters do not work directly on the
    # images. However, they so work on the image size.
    kernel_size = 2 * radius + 1
    # We are creating grid in form of row and colors. It is doing by using the "indices()" method and taking the
    # kernel size and subtracting by the radius.
    y, x = np.indices((kernel_size, kernel_size)) - radius  # y - change in rows, x - change in columns
    # Creating the gaussian filter.
    gaussian_filter = np.exp(-(x ** 2 + y ** 2) / (2 * (mask_std ** 2)))
    # Total grids into glassian sum
    gaussian_filter /= np.sum(gaussian_filter)
    # Calling the convolve2d() the Compute the gradient of an image by 2D convolution with a complex Scharr operator.
    # Use symmetric boundary condition to avoid creating edges at the image boundaries.
    gaussian_image = convolve2d(image, gaussian_filter, mode='same')
    return gaussian_image

def median_filter(image: np.ndarray, radius: int) -> np.ndarray:
    # Getting the kernel size. Kernel size is used by the filters, because the filters do not work directly on the
    # images. However, they so work on the image size.
    kernel_size = 2 * radius + 1
    # Applying Median Filter on image
    median_image = medfilt2d(image, kernel_size)
    return median_image

def bilateral_filter(image: np.ndarray, radius: int, std_spatial: float, std_intensity: float) -> np.ndarray:
    bilateral_image = image.copy()
    # Getting the kernel size. Kernel size is used by the filters, because the filters do not work directly on the
    # images. However, they so work on the image size.
    kernel_size = 2 * radius + 1
    # Extracting image rows
    rows = image.shape[0]
    # Extracting image columns
    columns = image.shape[1]
    y, x = np.indices((kernel_size, kernel_size)) - radius  # y - change in rows, x - change in columns
    # Creating the gaussian distance filter applying it formula.
    gaussian_distances_mask: np.ndarray = np.exp(-(x ** 2 + y ** 2) / (2 * (std_spatial ** 2)))
    # Total grids into glassian sum
    gaussian_distances_mask /= np.sum(gaussian_distances_mask)

    for i in range(radius, rows - radius):
        for j in range(radius, columns - radius):
            # Getting image properties
            window = image[(i - radius):(i + radius + 1), (j - radius):(j + radius + 1)]
            # Creating the gaussian intensity filter applying it formula.
            gaussian_intensity_mask = np.power(np.e, -((window - image[i, j]) ** 2) / (2 * (std_intensity ** 2)))
            # Total grids into glassian sum
            gaussian_intensity_mask /= np.sum(gaussian_intensity_mask)
            # Applying the gaussian filters to the image
            bilateral_image[i, j] = np.divide(np.sum(gaussian_intensity_mask * gaussian_distances_mask * window),
                                              np.sum(gaussian_intensity_mask * gaussian_distances_mask))

    return bilateral_image






# Reading the image.
img_or = cv2.imread('PenguinDistorted.bmp')
# cv.cvtColor() method is used to convert an image from one color space to another.
# cv.COLOR_BGR2GRAY extension is used to convert RGB to gray.
img_gray = cv2.cvtColor(img_or, cv2.COLOR_BGR2GRAY)
# Filter radius size
radius = 10
# std deviation of the image implies a gross measure of the imprecision/variation about the target value of light
# intensity, at each such data point.
#Only used in the mean filter
std = 2
#TODO ALL METHODS ARE CALLED BELLOW

# Calling the mean filter method defined above.
#filter_image =  median_filter(img_gray, radius)
#filter_image = mean_filter(img_gray, radius, std)
filter_image = bilateral_filter(img_gray, radius, 2, 5)


# Exporting the file into the .bmp format.
cv2.imwrite("bilateral.bmp", filter_image)
# Displaying image original.
cv2.imshow("original image ", img_or)
# Displaying image final
filter_image_read = cv2.imread("bilateral.bmp")
cv2.imshow("filter image", filter_image_read)
# Allow the user to display a window until a key is pressed by the user.
cv2.waitKey(0)

