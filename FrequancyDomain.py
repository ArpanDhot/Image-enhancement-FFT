import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import math

# This method is used to calculate the distance of two given points
def distance(point1, point2):
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)



def ideal_low_pass_filter(shape, cutoff):# Transfer parameters are Fourier transform spectrogram and filter size
    # Getting image properties
    [h, w] = shape

    # The np.zeros() method returns a new array of given shape and type, filled with zeros.
    mask_image = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            # Implementing the low pass filter formula.
            distance = math.sqrt((i - (h / 2)) * (i - (h / 2)) + (j - (w / 2)) * (j - (w / 2)))
            # Checking the distance to be less than or equal to the cutoff, forming a filter size that defines the size.
            # Then set to 1, preserving the low frequency part and 0 is set, to preserve high frequencies.
            if distance <= cutoff:
                mask_image[i][j] = 1
            else:
                mask_image[i][j] = 0

    return mask_image


def ideal_high_pass_filter(shape, cutoff):# Transfer parameters are Fourier transform spectrogram and filter size
    mask_image = 1 - ideal_low_pass_filter(shape, cutoff)
    return mask_image


def ideal_band_pass_filter(shape, cutoff1, cutoff2):# Transfer parameters are Fourier transform spectrogram and filter size
    # Getting image properties
    [h, w] = shape

    # The np.zeros() method returns a new array of given shape and type, filled with zeros.
    mask_image = np.zeros((h, w))
    for i in range(h):
        for j in range(w):
            # Implementing the low pass filter formula.
            distance = math.sqrt((i - (h / 2)) * (i - (h / 2)) + (j - (w / 2)) * (j - (w / 2)))
            # Checking the distance to be less than or equal to the cutoff, forming a filter size that defines the size.
            # Then set to 1, preserving the low frequency part and 0 is set, to preserve high frequencies part.
            if cutoff1 <= distance <= cutoff2:
                mask_image[i][j] = 1
            else:
                mask_image[i][j] = 0

    return mask_image


def ideal_band_stop_filter(shape, cutoff1, cutoff2):# Transfer parameters are Fourier transform spectrogram and filter size
    mask_image = 1 - ideal_band_pass_filter(shape, cutoff1, cutoff2)
    return mask_image


# Reading the image.
img = cv2.imread('PenguinDistorted.bmp')
# cv.cvtColor() method is used to convert an image from one color space to another.
# cv.COLOR_BGR2GRAY extension is used to convert RGB to gray.
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Transforming the image into fourier transform
# fft.fft2() computes the 2-dimensional FFT. This function computes the n-dimensional discrete Fourier Transform over
# any axes in an M-dimensional array by means of the Fast Fourier Transform (FFT).
fourier_transform = np.fft.fft2(img)

# Move frequency domain from upper left to middle
# The fftshift() method shifts the zero-frequency component to the center of the spectrum.
freq_shift_domain = np.fft.fftshift(fourier_transform)
# Plotting
plt.imshow(np.log1p(np.abs(freq_shift_domain)),
           cmap='gray')
plt.axis('off')
plt.show()
#TODO !!! ALL METHODS ARE CALLED BELLOW – MEDIAN, MEAN, BILATERAL FILTERS !!!

# Calling the filter methods made above
mask_image = ideal_low_pass_filter(img.shape, 50)
# mask_image=ideal_high_pass_filter(img.shape, 50)
# mask_image =ideal_band_pass_filter(img.shape, 50, 100)
# mask_image =ideal_band_stop_filter(img.shape, 50, 100)
# Plotting
plt.imshow(np.log1p(np.abs(mask_image)),
           cmap='gray')
plt.axis('off')
plt.show()

# We are applying the mask to the frequency shift domain.
Mshift = freq_shift_domain * mask_image
# Plotting
plt.imshow(np.log1p(np.abs(Mshift)),
           cmap='gray')
plt.axis('off')
plt.show()

# Inverse Fourier Shift
# Move the frequency domain from the middle to the upper left corner
# The inverse of fftshift. Although identical for even-length x, the functions differ by one sample for odd-length x.
inverse_FFT_shift = np.fft.ifftshift(Mshift)
# Plotting
plt.imshow(np.log1p(np.abs(inverse_FFT_shift)),
           cmap='gray')
plt.axis('off')
plt.show()

# Inverse Fourier Transform
# Compute the 2-dimensional inverse discrete Fourier Transform.#
# This function computes the inverse of the 2-dimensional discrete Fourier Transform over any number of axes in an
# M-dimensional array by means of the Fast Fourier Transform (FFT). In other words, ifft2(fft2(a)) == a to within
# numerical accuracy. By default, the inverse transform is computed over the last two axes of the input array.
inverse_FFT_transform = np.abs(np.fft.ifft2(inverse_FFT_shift))
# Plotting
plt.imshow(np.log1p(np.abs(inverse_FFT_transform)),
           cmap='gray')
plt.axis('off')
plt.show()
# Exporting file in .bmp format
cv.imwrite('FD-OUT.bmp', inverse_FFT_transform)
