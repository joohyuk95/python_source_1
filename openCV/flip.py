import cv2

img = cv2.imread('.//quiz_button//front.jpg')

img1 = cv2.flip(img, 1)     #  1 : 좌우반전
img2 = cv2.flip(img, 0)     #  0 : 상하반전
img3 = cv2.flip(img1, 0)

cv2.imshow('source', img)
cv2.imshow('left and right',img1)
cv2.imshow('up and down',img2)
cv2.imshow('LR and UD',img3)

cv2.waitKey()
cv2.destroyAllWindows()