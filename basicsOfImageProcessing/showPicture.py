import cv2
import os
import src

img = cv2.imread("src/Berry.jpg")
print(img.shape)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

os.mkdir("./basicsOfImageProcessing/output")
cv2.imwrite("./basicsOfImageProcessing/output/test.jpg", img)
