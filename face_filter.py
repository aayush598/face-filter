#Face filter
import cv2

# Initialize face cascade and eye cascade
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_cascade=cv2.CascadeClassifier('haarcascade_eye.xml')

# Capture video frames
cap=cv2.VideoCapture(0)
ex=ey=0
while True:
    ret,img=cap.read()
    # converting image to gray scale and detect face
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.8,5)

    # draw circle on face and near ears
    for (x,y,w,h) in faces:
        cx=int((x)+float(w/2))
        cy=int(float(y)+float(h/2))
        cv2.circle(img,(cx,cy),h,(255,0,0),5)
        cv2.circle(img,(x,y),50,(0,255,0),-1)
        cv2.circle(img,(x+w,y),50,(0,255,0),-1)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)

        # Draw rectangle on eyes
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,225),-1)
    img=cv2.resize(img,(600,600))

    # Showing frame
    cv2.imshow('img',img)
    k=cv2.waitKey(1) & 0xff
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
