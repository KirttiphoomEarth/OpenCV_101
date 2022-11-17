#import
import cv2
import datetime
#=================== Drawing 1 Draw line  =====================================
# img = cv2.imread("image/mark_sad_makmak.jpg")

# imgsize = cv2.resize(img,(700,700))

# #วาดเส้นตรงไปที่ภาพ
# #line เส้น arrowed ลูกศร (ภาพ, จุดเริ่มต้น(x, y), จุดสุดท้าย(x, y), สี BGR, ความหนา)
# cv2.arrowedLine(imgsize, (100,100), (100,500), (255,0,0), 4)
#   cv2.line(imgsize, (100,100), (100,500), (255,0,0), 4)
# cv2.imshow("OUTPUT", imgsize)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
#==============================================================================
#=================== Drawing 2 Draw Rectangle  ================================
# img = cv2.imread("image/mark_sad_makmak.jpg")

# imgsize = cv2.resize(img, (700,700))

# #Draw Rectangle
# #(ภาพ, มุมบนซ้าย, มุมล่างขวา, สี BGR, ความหนา)
# cv2.rectangle(imgsize, (100, 100), (500, 500), (150,0,100), 5 ) #หนา -1 สีเต็ม

# cv2.imshow("OUTPUT", imgsize)

# cv2.waitKey(0)

# cv2.reslase()
# cv2.destroyAllWindows()
#==============================================================================
#=================== Drawing 3 Draw Circle  ===================================
# img = cv2.imread("image/mark_sad_makmak.jpg")

# imgsesize = cv2.resize(img, (700, 700))

# #Draw Circle
# #(ภาพ, ตำแหน่งจุดศูนย์กลาง (x, y), รัสมี, สี BGR, ความหนา)
# cv2.circle(imgsesize, (300,300), 100, (100,0,200), 5)

# cv2.imshow("OUTPUT", imgsesize)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
#==============================================================================
#=================== Drawing 4 Draw text  =====================================
# img = cv2.imread("image/mark_sad_makmak.jpg")

# imgresize  = cv2.resize(img, (700, 700))

# #test
# #putText (ภาพ, ข้อความ, พิกัดข้อความ, Font (openCV doc), ขนาดข้อความ, สี, ความหนา (openCV doc))
# cv2.putText(imgresize, "Mark No Sad", (100, 200), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (0, 0, 255), cv2.LINE_4)

# cv2.imshow("OUTPUT", imgresize)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
#==============================================================================
#=================== Drawing 5 Time in Video/Camera  ==========================
cap = cv2.VideoCapture("video/video_test.mp4") # 0 = Camera

while(cap.isOpened()) :
    chack, frame = cap.read()

    if chack == True:
        currentDate = str(datetime.datetime.now())
        cv2.putText(frame, currentDate, (10,50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), cv2.LINE_4)                   #เขียนภาพ
        cv2.imshow("OUTPUT", frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    else :
        break
cap.release()
cv2.destroyAllWindows()
#==============================================================================