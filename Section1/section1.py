import cv2

img = cv2.imread("image.jpg")
cv2.imshow("Watch Image", img)

height, width = img.shape[0:2]
# print(height, width)

rotaitionMatrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 0.5)
rotatedImage = cv2.warpAffine(img, rotaitionMatrix, (width, height))
cv2.imshow("Rotated Image", rotatedImage)

img3 = cv2.imwrite("output.png", img, [cv2.IMWRITE_JPEG_QUALITY, 1])
print(img3)
img2 = cv2.imread("output.png")
cv2.imshow("Watch Image", img2)
cv2.waitKey(0)
