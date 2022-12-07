import  cv2 as cv

img1=cv.imread('PenguinDistorted.bmp')
img2=cv.imread('PenguinOriginal.bmp')

# Method to get the MSE
def mse(img1, img2):

    mse = 0

    for i in range(len(img1)):
        for j in range(len(img1[0])):
            mse += (img1[i][j] - img2[i][j]) ** 2

    return (mse / (len(img1) * len(img1[0])))

print(mse(img1, img2))