import cv2

face_cascade=cv2.CascadeClassfier("cat.xml")

img = cv2.imread("")

gray = cv2.cvtColor(img,cv2,COLOR_BGR2GRAY)

faces=face_cascade.detectMultiscale(gray,scaleFactor=1.01.,minneighbor=5)


print(type(faces))
print(faces)
