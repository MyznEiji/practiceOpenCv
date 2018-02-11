import cv2


img = cv2.imread("src/Lena.jpg", 0)
cv2.imshow("src", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


img_sobelx = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
img_sobely = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)


cv2.imshow("x", img_sobelx)
cv2.imshow("y", img_sobely)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_lap = cv2.Laplacian(img, cv2.CV_32F)

cv2.imshow("y", img_lap)
cv2.waitKey(0)
cv2.destroyAllWindows()

    img_blur = cv2.GaussianBlur(img, (21, 21), 2)
    img_lep2 = cv2.Laplacian(img_blur, cv2.CV_32F)

cv2.imshow("y", img_lap2)
cv2.waitKey(0)
cv2.destroyAllWindows()
