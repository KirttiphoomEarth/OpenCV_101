#import
import cv2

#=================== Mouser 1 Event แสดงพิกัด =====================================
#(event ทำงานอะไร Mouse ซ้ายขวา,x y , flags รูปแบบ, param)
def clickPosition(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:          # click mouse left
        text = str(x)+","+str(y)
        cv2.putText(img, text, (x,y),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), cv2.LINE_4)
        cv2.imshow("OUTPUT", img)

 
imgINPUT = cv2.imread("image/sea.jpg")
img = cv2.resize(imgINPUT, (1000, 500))

cv2.imshow("OUTPUT", img)
#Mouser Event
cv2.setMouseCallback("OUTPUT",clickPosition)           #Mouse (windown name, call back fun)

cv2.waitKey(0)                  #รอรับ key ปิดหน้าจอ
cv2.destroyAllWindows()
#==============================================================================