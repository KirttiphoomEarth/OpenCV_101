# เขียนภาพ export 
import cv2

img = cv2.imread("image/mark_sad_makmak.jpg")
imgre = cv2.resize(img, (500, 600))

cv2.imwrite("mark_no_sad.jpg", imgre) # ("ชื่อภาพ", ภาพอะไร)

cv2.imshow("output", imgre)
cv2.waitKey(0)