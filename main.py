import cv2
import imutils

# Open the camera from url address of ip camera from phone
fire_cascade = cv2.CascadeClassifier('fire_detection_cascade_model.xml')

vid = cv2.VideoCapture("https://192.168.201.70:8080/video")

# Set the font for the displayed text
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
font_color = (255, 0, 0)
thickness = 2

number = 0
# Loop through each frame in the video stream
while True:
    # Read a frame from the ip camera (phone)
    ret, frame = vid.read()
    frame = imutils.resize(frame, width=600, height=800)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect fires in the current frame
    fire = fire_cascade.detectMultiScale(frame)

    # Draw bounding boxes around the detected fires
    for (x, y, w, h) in fire:
        number = number + 1
        cv2.rectangle(frame, (x - 20, y - 20), (x + w + 20, y + h + 20), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        cv2.putText(frame, f"Number of fire {number}", (10, 30), font, font_scale, font_color, thickness,
                    cv2.LINE_AA)
        number = 0
    # Display the frame in a window
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break