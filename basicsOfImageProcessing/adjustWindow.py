import cv2


# windowをAutoSizeで綺麗な状態で出力できる
img = cv2.imread("src/Lena.jpg")
cv2.namedWindow("window", cv2.WINDOW_AUTOSIZE)
cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Window_normalでwindowを可変することができる
img = cv2.imread("src/Lena.jpg")
cv2.namedWindow("window", cv2.WINDOW_NORMAL)
cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# windowの大きさをリサイズする
img = cv2.imread("src/Lena.jpg")
cv2.namedWindow("window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("window", 640, 480)
cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
