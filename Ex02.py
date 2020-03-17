import cv2
img = cv2.imread('iphone.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite('test1.jpg',gray)