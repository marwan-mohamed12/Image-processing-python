# Image Processing in python using OpenCv

- First You have to install openCv
  ` pip install opencv-python `

## Image representaion

An image is represented by a rectangular array of integers.
An integer represents the brightness or darkness of the image at that point.
N: Number of rows, M: Number of columns, Q: Number of gray levels

## Reading Image

cv2.imread("img.format")
Formats:
-----------------------------|
Format name | Extension
-----------------------------|
TIFF | .tif or .tiff
-----------------------------|
JPEG | .jpg or .jpeg
-----------------------------|
GIF | .gif
-----------------------------|
BMP | .bmp
-----------------------------|
PNG | .png
-----------------------------|

## Image Info

height, widht, channels = img.shape
(height, width) => dimention of image
channels => refer to the different color components that make up an image
img.dtype => get the datatype of img

## Displaying Image

cv2.imshow("image title", img)
cv2.waitKey(0) => to detrmine if the window will close after a certain time

## Rotate Image

img = cv2.imread("image.jpg")
cv2.imshow('Original Image', img)
height, width = img.shape[0:2]
rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)
rotatedImage = cv2.warpAffine(img, rotationMatrix, (width, height))
cv2.imshow('Rotated Image', rotatedImage)
cv2.waitKey(0)

## Writing Image

cv2.imwrite("output.format", img, [cv2.IMWRITE_JPEG_QUALITY, qualityNum])
qualityNum => usedt to control the quality of the image

## Exercise 1

Read image and then output width, height, channels and datatype
img = cv2.imread("image.jpg")
height, width, channels = image.shape
print(height)
print(width)
print(channel)
print(img.dtype)

## Exercise 2

Write a program that reads an image, store with a .png extension with a quality q=25, then show the image.
img = cv2.imread("image.jpg")
cv2.imwrite("image.png", img, [cv2.IMWRITE_JPEG_QUALITY, 25])

## Useful Links

<a href="https://likegeeks.com/python-image-processing/#Install_OpenCV">Tutorial OpenCV</a>
