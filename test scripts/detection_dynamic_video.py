"https://opencv.org/get-started/"
"https://app.datacamp.com/workspace/w/8bc53cfc-f998-4e87-9924-888f0993c2ce/edit"
import cv2
import matplotlib.pyplot as plt

def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces
#type of alog: "haarcascade_frontalface_default.xml"

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") #create cre-trained Haar Cascade classifier (built-in vy openCV)
video_capture = cv2.VideoCapture(0) #0 mean acces to our camera // our video videos/test_case.mov

# Check if camera opened successfully
if (video_capture.isOpened()== False): 
  print("Error opening video stream or file")
 
# Read until video is completed
while(video_capture.isOpened()):
  result, frame = video_capture.read() # Capture frame-by-frame
  if result == True:
    faces = detect_bounding_box(frame) # apply the function we created to the video frame to detect faces in each frames
    cv2.imshow('Project',frame) # Display the resulting frame
 
    if cv2.waitKey(25) & 0xFF == ord('q'): # Press Q on keyboard to  exit
      break
 
  # Break the loop if result not true 
  else: 
    break
 
# When everything done, release the video capture object
video_capture.release()
 
# Closes all the frames
cv2.destroyAllWindows()


print("end")
quit()

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(20,10))
plt.imshow(img_rgb)
plt.axis('off')
plt.show()

print("end")