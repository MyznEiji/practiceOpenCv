import cv2
import matplotlib.pyplot as plt


# grayScaleの画像を表示
img = cv2.imread("src/grapes.jpg", 0)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2値化する
threshold = 100
ret, img_th = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
print(ret)
print(img_th.shape)

# 画像を出力
cv2.imshow("img_th", img_th)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 勝手に閾値を決めてくれるOTSUで
ret2, img_o = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
print(ret2)

# ヒストグラムをプロット
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)

# ostuで決めた閾値の画像を表示
cv2.imshow("otsu", img_o)
cv2.waitKey(0)
cv2.destroyAllWindows()


img_ada = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 1)

cv2.imshow("ada", img_ada)
cv2.waitKey(0)
cv2.destroyAllWindows()
