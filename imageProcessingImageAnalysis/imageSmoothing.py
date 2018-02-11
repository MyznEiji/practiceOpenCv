import cv2

img = cv2.imread("src/buildings.jpg")
img_blur = cv2.blur(img, (3, 3))

cv2.imshow("img", img_blur)
cv2.imshow("src", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_ga = cv2.GaussianBlur(img, (9, 9), 2)

cv2.imshow("img", img_ga)
cv2.imshow("src", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_me = cv2.medianBlur(img, 5)

cv2.imshow("img", img_me)
cv2.imshow("src", img)
cv2.waitKey(0)
cv2.destroyAllWi    ndows()

img_bi = cv2.bilateralFilter(img, 20, 30, 30)
cv2.imshow("img", img_bi)
cv2.imshow("src", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
