import cv2

#　画像を取得し出力する
img = cv2.imread("src/grapes.jpg")
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 高さ、幅、色の種類
print(img.shape)

# 幅、高さの順で指定
size = (300, 200)
img_resize = cv2.resize(img, size)
print(img_resize.shape)

# resizeしたwindowを出力
cv2.imshow("resize", img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 画像を縮小する場合はINTER_AREAを使用する
img_area = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
img_linear = cv2.resize(img, size, interpolation=cv2.INTER_LINEAR)
cv2.imshow("area", img_area)
cv2.imshow("linear", img_linear)
cv2.waitKey(0)
cv2.destroyAllWindows()
