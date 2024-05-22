import cv2
import os
from datetime import datetime
import face_recognition
import csv

def load_known_faces(dataset_folder):
    known_face_encodings = []
    known_face_names = []

    for root, dirs, files in os.walk(dataset_folder):
        for file in files:
            if file.endswith("jpg") or file.endswith("png"):
                image_path = os.path.join(root, file)
                name = os.path.basename(root)
                image = face_recognition.load_image_file(image_path)
                encoding = face_recognition.face_encodings(image)[0]
                known_face_encodings.append(encoding)
                known_face_names.append(name)

    return known_face_encodings, known_face_names

def mark_attendance(name, attendance_file):
    with open(attendance_file, 'a', newline='') as file:
        writer = csv.writer(file)
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([date_time, name])

def take_attendance(dataset_folder, attendance_file):
    # Load known faces from the dataset folder
    known_face_encodings, known_face_names = load_known_faces(dataset_folder)
    
    # Initialize webcam
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Unable to access the camera.")
        return
    
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break
        
        # Find faces in the frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        
        for face_encoding in face_encodings:
            # Compare with known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            # Mark attendance
            mark_attendance(name, attendance_file)

            print(f"Attendance marked for: {name}")

        cv2.imshow("Attendance System", frame)
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows() 

if __name__ == "__main__":
    dataset_folder = "D:/Django-project/facelogix2/dataset"
    attendance_file = "attendance.csv"
    
    take_attendance(dataset_folder, attendance_file)
