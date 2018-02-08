import cv2
import numpy as np

# データの読み込み,設定
gamma = 1.5
img = cv2.imread("src/Berry.jpg")
gamma_cvt = np.zeros((256, 1), dtype=np.uint8)

# ガンマ変換の準備
for i in range(256):
    gamma_cvt[1][0] = 255 * (float(i) / 255) ** (1.0 / gamma)

# ガンマ変換を行う
img_gamma = cv2.LUT(img, gamma_cvt)

cv2.imshow("img", img)
cv2.imshow("gamma", img_gamma)
cv2.waitKey(0)
cv2.destroyAllWindows()
