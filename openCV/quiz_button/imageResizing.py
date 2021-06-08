import cv2
img = cv2.imread('tshirts.jpg')

img1 = img[100:550, :]
img2 = img[550:1000, :]

img1 = cv2.resize(img1, dsize = (400, 400))
img2 = cv2.resize(img2, dsize = (400, 400))

cv2.imwrite('front.jpg', img1)
cv2.imwrite('rear.jpg', img2)