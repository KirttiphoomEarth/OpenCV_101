import cv2
import numpy
#==============================================================================
#=================== Detect 1 Color Oject =====================================
#use mask , layer mask  ระบุช่วงของสีเข้มถึงออน เข้ม->ค่าน้อย อ่อน->ค่ามาก
# while True :
#     imgINPUT = cv2.imread("image/color_ball.jpg")
#     img = cv2.resize(imgINPUT, (500, 500))

#     #ช่วงสี ball red
#     lower = numpy.array([30, 24, 133])        #สีเข้ม
#     upper = numpy.array([122, 142, 254])      #สีอ่อน
    
#     mask = cv2.inRange(img,lower, upper)      #สีในช่วง (รูป,เข้ม, อ่อน)
#     result = cv2.bitwise_and(img, img, mask=mask)   #กลับ 0 1 (รูป, รูป, mask)

#     cv2.imshow("OUTPUT", img)
#     cv2.imshow("Mask", mask)
#     cv2.imshow("result", result)

#     if cv2.waitKey(0) & 0xFF == ord('e'):
#         break

# cv2.destroyAllWindows()
#==============================================================================
#========================= Detect 2  Face Detection from Photo  ===========================
#Error found 3/5 member T-T
img = cv2.imread("image/g_idle.jpg")
img = cv2.resize(img, (800,500))

#read Classification
face = cv2.CascadeClassifier("data/haarcascade_frontalface_default.xml") 

#Colour to Gary
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#แยกใบหน้า
scaleFactor = 1.20                   #defult = 1.1 ย่อขนาดภาพเป็นสัดส่วน 0.20 = 20%
minNeighber = 3                     #defult = 3 เจอหน้าที่ไหนจะสร้างสี่เหลี่ยมบริเวณที่เจอที่ข้าง ๆ ด้วย 0 ถี่สุด เจอกี่รอบถึงเป็นหน้า
face_detect = face.detectMultiScale(gray, scaleFactor, minNeighber) #ตามค่าที่ระบุ

#แสดงตำแหน่งใบหน้า
for(x, y, w, h) in face_detect:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 0), 3)

cv2.imshow("OUTPUT", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
