Face Attendance System-
This is a simple Python program that uses OpenCV to detect faces in a live video stream and prompts the user to confirm attendance for each person in a list. The program displays a rectangle around each detected face and asks the user to confirm if the detected face belongs to the current person in the list. The user can then press 'y' to add the person to the attendance list or 'n' to move on to the next person.

Requirements-
Python 3.x
OpenCV (cv2) library
Installation
Clone the repository to your local machine:
git clone https://github.com/yourusername/face-attendance-system.git
Install the required libraries using pip:
pip install opencv-python
Download the Haar Cascade classifier file from the OpenCV GitHub repository and save it in the same directory as the main.py file:

https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

Usage-
Open a terminal or command prompt and navigate to the directory containing the attendance.py file.

Run the program using the following command:

python main.py
The program will open a live video stream from your default camera and start detecting faces. The program will prompt you to confirm attendance for each person in the people_names list. Press 'y' to add the person to the attendance list or 'n' to move on to the next person.

Once you have confirmed attendance for all people, press 'q' to quit the program. The final attendance list will be printed to the console.

Contributing-
If you find a bug or have a suggestion for improvement, please feel free to open an issue or submit a pull request.

License-
This project is licensed under the MIT License. See the LICENSE file for details.

Credits-
This program was inspired by the Face Recognition Attendance System example in the face_recognition library by Adam Geitgey.
