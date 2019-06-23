import cv2
from detect_color import cl
cap = cv2.VideoCapture("VID-20190617-WA0009.mp4")
#cap = cv2.VideoCapture("VID-20190617-WA0010.mp4")
cascade = cv2.CascadeClassifier("cascade.xml")
while True:
    ret, img = cap.read()

    cord = cl.detect(img,[10,10,230])
    print(cord)
    if(cord[0] == 0 and cord[1] == 0 and cord[2] == 0 and cord[3] == 0):
        placa = cascade.detectMultiScale(img, 1.9,5)
        for (x,y,w,h) in placa:
            cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)

    cv2.imshow("shown",img)
    k=cv2.waitKey(30) & 0xff
    if k == 27:
        break
