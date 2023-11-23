"https://opencv.org/get-started/"
"https://app.datacamp.com/workspace/w/8bc53cfc-f998-4e87-9924-888f0993c2ce/edit"
import cv2
import matplotlib.pyplot as plt


img = cv2.imread("images\images_test.webp")

gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #create cre-trained Haar Cascade classifier (built-in vy openCV)

face = face_classifier.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(10, 10))
print("Face Detected: ", face)
for (x, y, w, h) in face:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)


img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(20,10))
plt.imshow(img_rgb)
plt.axis('off')
plt.show()
#cv2.imshow("Display window", img)
#k = cv2.waitKey(0) # Wait for a keystroke in the window
print("end")