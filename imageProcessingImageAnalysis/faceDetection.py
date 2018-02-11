import cv2

HAAR_FILE = "/Users/miyazonoeiji/.pyenv/versions/anaconda3-5.0.1/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(HAAR_FILE)

img = cv2.imread("src/Solvay_conference_1927.jpg")
img_g = cv2.imread("src/Solvay_conference_1927.jpg", 0)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

face = cascade.detectMultiScale(img_g)


for x, y, w, h in face:
    cv2.rectangle(img, (x, y), (x+w, y+w), (0, 0, 255), 1)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(cv2)
