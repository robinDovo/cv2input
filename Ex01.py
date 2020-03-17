import cv2

img = cv2.imread('lena.jpg')
img2 = cv2.imread('iphone.jpg')

key = cv2.waitKey()
if key == ord('A'):
	cv2.imshow('img1',img)
elif key == ord('B'):
	cv2.imshow('img2',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()