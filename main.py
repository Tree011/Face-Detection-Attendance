import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
people_names = ['Saashaa', 'Suraj','Avi','LORD Siddhesh']

# define the text display parameters
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.5
font_color = (0, 255, 0)
line_type = 2

# initialize variables
attendance_list = []
face_detected = False
current_person_idx = 0

# capture frames from the camera
while True:
    ret, frame = cap.read()
    if not ret:
        print("Unable to capture video")
        break

    # convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # check if a face is detected
    if len(faces) > 0:
        face_detected = True
        name = ""
        for (x, y, w, h) in faces:
            # draw a rectangle around the face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # prompt the user to confirm attendance for each person
            if current_person_idx < len(people_names):
                name = people_names[current_person_idx]
                text = f'is this {name}?'
                name_position = (x, y - 10)
                cv2.putText(frame, text, name_position, font, font_scale, font_color, line_type)

    # display the frame
    cv2.imshow('Attendance', frame)

    # wait for user input
    key = cv2.waitKey(1) & 0xFF

    # if the 'q' key is pressed, quit the program
    if key == ord('q'):
        break

    # if the 'y' key is pressed, add the current person to the attendance list
    elif key == ord('y') and face_detected:
        attendance_list.append(name)
        face_detected = False
        current_person_idx += 1

    # if the 'n' key is pressed, move on to the next person
    elif key == ord('n') and face_detected:
        face_detected = False
        current_person_idx += 1

    # print the final attendance list
print("Attendance List:")
for name in attendance_list:
    print(name)

# release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()