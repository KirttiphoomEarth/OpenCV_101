# แสดงผลภาพ ปรับเปลี่ยนขนาดภาพ
import cv2  # อ่านรูปภาพ โดยใช้ numpy arry

img = cv2.imread("image/mark_sad_makmak.jpg") # ("ชื่อภาพ", โหมดภาพ ขาวดำ เทา สี)
imgresize = cv2.resize(img,(500, 600)) # เปลี่ยนขนาดใหม่
 
# แสดงภาพ 
cv2.imshow("OUTPUT", imgresize)  # ("ชื่อ window", ภาพที่จะแสดง)
cv2.waitKey(delay=0)  # เปิดแล้วปิดเมื่อไร 0 = ปิดเลย
# cv2.destroyAllWindows() # ปิดทั้งหมด
