import cv2


img = cv2.imread("src/Lena.jpg", 0)

img_canny = cv2.Canny(img, 10, 100)
cv2.imshow("Canny", img_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()


img_canny = cv2.Canny(img, 100, 200)
cv2.imshow("Canny", img_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
