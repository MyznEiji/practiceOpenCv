import cv2
import numpy as np

img = cv2.imread("src/floor.jpg", 0)

ret, img_th = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
cv2.imshow("img", img_th)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel1 = np.ones((3, 3), dtype=np.uint8)
img_d = cv2.dilate(img_th, kernel1)
img_e = cv2.erode(img_th, kernel1)

cv2.imshow("img", img_th)
cv2.imshow("e", img_e)
cv2.imshow("d", img_d)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_c = cv2.morphologyEx(img_th, cv2.MORPH_CROSS, kernel1)
cv2.imshow("c", img_c)
cv2.imshow("d", img_d)
cv2.waitKey(0)
cv2.destroyAllWindows()
