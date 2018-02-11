import cv2
import numpy as np

img = cv2.imread("src/grapes.jpg")
h, w = img.shape[:2]

# 画像の平行移動するピクセル数
dx, dy = 30, 30

afn_mat = np.float32([[1, 0, dx], [0, 1, dy]])
img_afn = cv2.warpAffine(img, afn_mat, (w, h))

cv2.imshow("trans", img_afn)
cv2.waitKey(0)
cv2.destroyAllWindows()

rot_mat = cv2.getRotationMatrix2D((w/2, h/2), 40, 1)
img_afn2 = cv2.warpAffine(img, rot_mat, (w, h))

cv2.imshow("rotation", img_afn2)
cv2.waitKey(0)
cv2.destroyAllWindows()
