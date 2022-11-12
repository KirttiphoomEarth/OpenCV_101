# import
import cv2

# เขียนภาพ export 
#=================== Basic 3 =====================================
# import cv2

# img = cv2.imread("image/mark_sad_makmak.jpg") #cv2.imread("photo",Mode) 0 = gary
# imgre = cv2.resize(img, (500, 600))

# cv2.imwrite("mark_no_sad_2.jpg", imgre)       # ("ชื่อภาพ", ภาพอะไร)

# cv2.imshow("output", imgre)
# cv2.waitKey(0)
#================================================================
#=================== Basic 3  Open Camera =====================================
# cap = cv2.VideoCapture(0)                       #จำนวนกล้อง

# while(1):
#     ret , frame = cap.read();                   #รับจากกล้อง Frame ต่อ Fram ret chack อ่านค่าจากกล้องอ่านได้ = 1
#     cv2.imshow("OUTPUT",frame)

#     if cv2.waitKey(1) & 0xFF == ord("e"):       #chack ว่ามีปุ่มกดเข้ามาไหม กดตัวอะไร cast เป็น ascii
#         break
# cap.release()                                   #คืนทรัพยากรให้เครื่อง
# cv2.destroyAllWindows()                         #ปิดทุก windows
#================================================================
#=================== Basic 4  Open Video =====================================
# cap = cv2.VideoCapture("video/video_test.mp4")

# while(cap.isOpened()):                                   #chack ว่า video เปิดได้ไม่มีปัญหา
#         ret, fram = cap.read()                           #ตำแหน่งที่เก็บ video
#         if ret == True:
#             cv2.imshow("OUTPUT", fram)                   #อ่านหมดทุก fram จะ error เพราะไม่มีอะไรให้อ่านต่อ เอา ret มา cheack
#             if cv2.waitKey(1) & 0xFF == ord('s'):
#                      break
#         else :
#             break

# cap.release()
# cv2.destroyAllWindows()
#==============================================================================
#=================== Basic 5 Video edit =====================================
# cap = cv2.VideoCapture("video/video_test.mp4")

# while(cap.isOpened()):
#     ChackVideo, fram = cap.read()

#     if ChackVideo == True:
#         gray = cv2.cvtColor(fram, cv2.COLOR_BGR2GRAY)        #colour chang    
#         cv2.imshow("OUTPUT", gray)
#         if cv2.waitKey(1) & 0xFF == ord("s") :
#             break
#     else :
#         break

# cap.release()
# cv2.destroyAllWindows()
#==============================================================================
#=================== Basic 6 Video Recorder =====================================
# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')                        #ชนิดวิดีโอ OutPut

# result = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480)) #OutPut (ขื่อไฟล์, ประเภท, Fram Rate, size)

# while(cap.isOpened()) :
#     chack, fram = cap.read()
    
#     if chack == True :
#         cv2.imshow("Output", fram)

#         result.write(fram)                                      #เก็บ Fram ลง result
#         if cv2.waitKey(1) & 0xFF == ord('s') :                  #กด S หยุดอัดวิดีโอ
#             break

# result.release()
# cap.release()
# cv2.destroyAllWindows()
#==============================================================================
