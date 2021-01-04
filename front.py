import cv2
import time
import datetime
import mysql.connector
face=cv2.CascadeClassifier(r"C:\Users\Home\PycharmProjects\Abhishek\haarcascade_frontalface_default.xml")
eye=cv2.CascadeClassifier(r"C:\Users\Home\PycharmProjects\Abhishek\haarcascade_eye.xml")
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
detect=[0,0,False]
img = cv2.imread("terii2.jpg",1)
cap.set(3,100)
cap.set(4,50)

my=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="abhishek")
h=my.cursor()
while True:
    ret,frame=cap.read()
    if ret==True:

        frame = cv2.flip(frame,1)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=face.detectMultiScale(gray,1.3,5)
        if len(faces):
            if detect[2] == False:
                start = datetime.datetime.now()
                da = str(start.year) + "-" + str(start.month) + "-" + str(start.day)
                start = str(start.hour) + ":" + str(start.minute) + ":" + str(start.second)
                detect[0] = time.time()
                detect[2] = True
            for (a,b,c,d) in faces:
                cv2.rectangle(frame,(a,b),((a+c),(b+d)),(255,255,255),3)
                roi1=frame[a:a+c,b:b+d]
                roi2=gray[a:a+c,b:b+d]
                eyes=eye.detectMultiScale(roi2,1.3,5)
                for (x,y,z,w) in eyes:
                    cv2.rectangle(roi1,(x,y),((x+z),(y+w)),(255,255,255),3)
        else:
            if detect[2] == True:
                end = datetime.datetime.now()
                end = str(end.hour) + ":" + str(end.minute) + ":" + str(end.second)
                detect[1]=time.time()
                detect[2]=False
                d=detect[1] - detect[0]
                d=round(d,2)
                if d>10:a
                    print(d)
                    q = "INSERT INTO camera (Date,Start_Time,End_Time,Duration) VALUES (%s,%s,%s,%s)"
                    v = (da,start,end,d)
                    h.execute(q,v)
                    my.commit()
                    print("database updated")

        img = cv2.resize(img, (640, 480))

        x_offset = 0
        y_offset = 360
        img[y_offset:y_offset+frame.shape[0],x_offset:x_offset+frame.shape[1]] = frame
        cv2.imshow("frame", img)
        # cv2.imshow("camera", frame)

        if cv2.waitKey(1) & 0xFF == ord('a'):
            break
cap.release()
cv2.destroyAllWindows()

