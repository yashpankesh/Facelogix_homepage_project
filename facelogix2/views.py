from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.db import connection
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from .models import UserInfo 
from django.contrib import messages
from django.http import JsonResponse
from .capture import capture_dataset
import cv2
import os
from django.http import JsonResponse
from datetime import datetime
import json
from django.contrib import messages
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required


def HomePage(request):
    return render(request,"index.html")

def profile(request):
    return render(request,"profile.html")

def AboutUs(request):
    return render(request,"aboutus.html")

def contact(request):
    return render(request,"contact.html")

def capture(request):
    return render(request,"capture.html")

def Register(request):
    return render(request,'register.html')

def Attendance(request):
    return render(request, 'attendance.html')




def Registration(request):
    if request.method == "POST":
        enrollment = request.POST.get('enrollment')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        
        if not enrollment or not email or not pass1 or not pass2:
            messages.error(request, "Please fill in all the required fields.")
            return redirect('register')  # Redirect back to the registration page

        # Check if the username already exists
        if User.objects.filter(username=enrollment).exists():
            messages.error(request, "Username already exists! Please choose a different one.")
            return redirect('register')  # Redirect back to the registration page

        # Check if the email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered! Please use a different email.")
            return redirect('register')  # Redirect back to the registration page

        # Create a new user
        try:
            myuser = User.objects.create_user(username=enrollment, email=email, password=pass1)
            myuser.first_name = 'DefaultFirstName'  # Set your default first name
            myuser.last_name = 'DefaultLastName'  # Set your default last name
            myuser.is_active = True
            myuser.save()
            messages.success(request, "Your account has been created successfully! Please check your email for confirmation.")
            return redirect('login')  # Redirect to login page
        except Exception as e:
            # Handle any exceptions that may occur during user creation
            messages.error(request, f"Error: {str(e)}")
            return redirect('register')  # Redirect back to the registration page

    # Handle GET request or other cases
    return redirect('register')  # Redirect back to the registration page


# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('pass')
        
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             auth_login(request, user)
#             # Check if the username matches the enrollment number from run_capture
#             enrollment_number = request.POST.get('enrollment_number')
#             if username == enrollment_number:
#                 return redirect('profile')  # Redirect to profile page upon successful login
#             else:
#                 return JsonResponse({'status': 'error', 'message': 'Please try again!'}, status=400)
#         else:
#             return render(request, 'login.html', {'error_message': 'Invalid credentials'})

#     return render(request, 'login.html')

@login_required
def run_capture(request):
    try:
        # Get the enrollment number from the authenticated user
        enrollment_number = request.user.username

        # Get the enrollment number from the request
        requested_enrollment_number = request.POST.get('enrollment_number')

        # Ensure the requested enrollment number is not empty
        if not requested_enrollment_number:
            return JsonResponse({'status': 'error', 'message': 'Enrollment number is required.'}, status=400)

        # Check if the requested enrollment number matches the logged-in user's username
        if requested_enrollment_number != enrollment_number:
            return JsonResponse({'status': 'error', 'message': 'Invalid enrollment number.'}, status=400)

        # Define the output folder where images will be saved
        output_folder = os.path.join("D:/Django-project/facelogix2/dataset", enrollment_number)

        # Create the output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Capture dataset
        photo_limit = 10
        now = datetime.now()
        current_date = now.strftime("%Y-%m-%d")
        name = current_date
        capture_dataset(output_folder, photo_limit)

        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})



# @login_required #final2 
# def run_capture(request):
#     try:
#         # Get the enrollment number from the authenticated user
#         enrollment_number = request.user.username

#         # Define the output folder where images will be saved
#         output_folder = os.path.join("D:/Django-project/facelogix2/dataset", enrollment_number)

#         # Ensure the enrollment number is not empty
#         if not enrollment_number:
#             return JsonResponse({'status': 'error', 'message': 'Enrollment number is required.'}, status=400)

#         # Create the output folder if it doesn't exist
#         os.makedirs(output_folder, exist_ok=True)

#         # Capture dataset
#         photo_limit = 10
#         now = datetime.now()
#         current_date = now.strftime("%Y-%m-%d")
#         name = current_date
#         capture_dataset(output_folder, photo_limit)

#         return JsonResponse({'status': 'success'})
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': str(e)})


def login(request): #rec final 2
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('profile')  # Redirect to profile page upon successful login
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'login.html')


# def index(request):
#     if not request.user.is_authenticated:
#         return render(request, 'login.html', {'error_message': 'Please Log in'})  # Return message "Please Log in"
#     else:
#         return render(request, 'index.html')



# def login(request): #final
#      print(f"Handling {request.method} request")
#      if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('pass')
        
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             auth_login(request, user)
#             return redirect('profile')
#   # Assuming 'profile' is the name of your URL pattern for the profile page
#         else:
#             return render(request, 'login.html', {'error_message': 'Invalid credentials'})

#      return render(request, 'login.html')


# def run_capture(request):  #final
#     try:
#         output_folder = "D:/Django-project/facelogix2/dataset"
#         photo_limit = 10
#         now = datetime.now()
#         current_date = now.strftime("%Y-%m-%d")
#         name = current_date
#         capture_dataset(output_folder, photo_limit)
#         return JsonResponse({'status': 'success'})
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': str(e)})

# def run_capture(request): #final
#     try:
#         # Get the enrollment number from the request
#         enrollment_number = request.POST.get('enrollment_number')

#         # Ensure the enrollment number is not empty
#         if not enrollment_number:
#             return JsonResponse({'status': 'error', 'message': 'Enrollment number is required.'}, status=400)

#         # Define the output folder where images will be saved
#         output_folder = os.path.join("D:/Django-project/facelogix2/dataset", enrollment_number)

#         # Create the output folder if it doesn't exist
#         os.makedirs(output_folder, exist_ok=True)

#         # Capture dataset
#         photo_limit = 10
#         now = datetime.now()
#         current_date = now.strftime("%Y-%m-%d")
#         name = current_date
#         capture_dataset(output_folder, photo_limit)

#         return JsonResponse({'status': 'success'})
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': str(e)})


# from django.http import JsonResponse
# import subprocess

# def run_capture(request):
#     if request.method == 'POST':
#         enrollment_number = request.POST.get('enrollment_number')
#         if enrollment_number:
#             # Execute the Python file using subprocess
#             try:
#                 subprocess.run(['python', 'path_to_capture.py', enrollment_number], check=True)
#                 return JsonResponse({'message': 'Image captured and saved successfully!'})
#             except subprocess.CalledProcessError as e:
#                 return JsonResponse({'error': f'Error capturing image: {e}'}, status=500)
#         else:
#             return JsonResponse({'error': 'Enrollment number not provided.'}, status=400)
#     else:
#         return JsonResponse({'error': 'Invalid request method.'}, status=405)


# from django.shortcuts import render
# from django.http import JsonResponse
# import cv2
# import os
# import face_recognition
# import csv
# from datetime import datetime

# def load_known_faces(dataset_folder):
#     known_face_encodings = []
#     known_face_names = []

#     for root, dirs, files in os.walk(dataset_folder):
#         for dir_name in dirs:
#             dir_path = os.path.join(root, dir_name)
#             for file_name in os.listdir(dir_path):
#                 if file_name.endswith(".jpg") or file_name.endswith(".png"):
#                     image_path = os.path.join(dir_path, file_name)
#                     name = dir_name
#                     image = face_recognition.load_image_file(image_path)
#                     face_encodings = face_recognition.face_encodings(image)
#                     if len(face_encodings) > 0:
#                         encoding = face_encodings[0]
#                         known_face_encodings.append(encoding)
#                         known_face_names.append(name)

#     return known_face_encodings, known_face_names


# def detect_faces_and_print_name(known_face_encodings, known_face_names):
#     # Open webcam
#     cap = cv2.VideoCapture(0)

#     while True:
#         # Capture frame-by-frame
#         ret, frame = cap.read()

#         # Convert the image from BGR color (OpenCV) to RGB color (face_recognition)
#         rgb_frame = frame[:, :, ::-1]

#         # Find all face locations and encodings in the current frame
#         face_locations = face_recognition.face_locations(rgb_frame)
#         face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

#         # Iterate through each face found in the frame
#         for face_encoding in face_encodings:
#             # Compare the detected face with the known faces
#             matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#             name = "Unknown"

#             # If a match is found, print the corresponding folder name
#             if True in matches:
#                 match_index = matches.index(True)
#                 name = known_face_names[match_index]
#                 print("Face detected with name:", name)

#                 # Write the folder name to a CSV file
#                 with open('attendance.csv', 'a', newline='') as file:
#                     writer = csv.writer(file)
#                     now = datetime.now()
#                     writer.writerow([now.strftime("%Y-%m-%d %H:%M:%S"), name])

#         # Display the resulting frame
#         cv2.imshow('Video', frame)

#         # Check for 'q' key press to exit
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release video capture object and close windows
#     cap.release()
#     cv2.destroyAllWindows()

# def run_face_detection(request):
#     try:
#         dataset_folder = "D:/Django-project/facelogix2/dataset"
        
#         # Load known faces from the dataset folder
#         known_face_encodings, known_face_names = load_known_faces(dataset_folder)
        
#         # Detect faces from webcam and print folder names to CSV file
#         detect_faces_and_print_name(known_face_encodings, known_face_names)

#         return JsonResponse({'status': 'success'})
#     except Exception as e:
#         return JsonResponse({'status': 'error', 'message': str(e)})

# # facerecognition/views.py
# from django.shortcuts import render
# from django.http import JsonResponse
# import cv2
# import face_recognition
# import os
# import csv
# from datetime import datetime

# def load_known_faces(dataset_folder):
#     # Your implementation of load_known_faces function
#     known_face_encodings = []
#     known_enrollment_numbers = []

#     for folder_name in os.listdir(dataset_folder):
#         folder_path = os.path.join(dataset_folder, folder_name)
#         if os.path.isdir(folder_path):
#             for file_name in os.listdir(folder_path):
#                 file_path = os.path.join(folder_path, file_name)
#                 if file_name.endswith(".jpg") or file_name.endswith(".png"):
#                     image = face_recognition.load_image_file(file_path)
#                     encoding = face_recognition.face_encodings(image)[0]
#                     known_face_encodings.append(encoding)
#                     known_enrollment_numbers.append(folder_name)

#     return known_face_encodings, known_enrollment_numbers

# def mark_attendance(enrollment_number, csv_file):
#     # Your implementation of mark_attendance function
#     with open(csv_file, 'a', newline='') as file:
#         writer = csv.writer(file)
#         now = datetime.now()
#         date_time = now.strftime("%Y-%m-%d %H:%M:%S")
#         writer.writerow([date_time, enrollment_number])

# def capture_and_recognize_faces(request):
#     dataset_folder = "D:/Django-project/facelogix2/dataset"
#     csv_file = "attendance.csv"

#     known_face_encodings, known_enrollment_numbers = load_known_faces(dataset_folder)

#     cam = cv2.VideoCapture(0)
#     if not cam.isOpened():
#         return JsonResponse({'status': 'error', 'message': 'Unable to access the camera.'}, status=500)

#     while True:
#         ret, frame = cam.read()
#         if not ret:
#             return JsonResponse({'status': 'error', 'message': 'Failed to capture frame.'}, status=500)

#         # Convert the image from BGR color (OpenCV format) to RGB color (face_recognition format)
#         rgb_frame = frame[:, :, ::-1]

#         # Find all the faces and face encodings in the current frame
#         face_locations = face_recognition.face_locations(rgb_frame)
#         face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

#         for face_encoding in face_encodings:
#             # Compare the face with known faces
#             matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#             if True in matches:
#                 first_match_index = matches.index(True)
#                 enrollment_number = known_enrollment_numbers[first_match_index]
#                 mark_attendance(enrollment_number, csv_file)
#                 print(f"Attendance marked for: {enrollment_number}")

#         # Display the resulting image
#         cv2.imshow('Webcam', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cam.release()
#     cv2.destroyAllWindows()

#     return JsonResponse({'status': 'success'})

# facerecognition/views.py
from django.shortcuts import render
from django.http import JsonResponse
import cv2
import face_recognition
import numpy as np
import os
import csv
from datetime import datetime

def capture_and_recognize_faces(request):
    # Load known face encodings
    dataset_folder = "D:/Django-project/facelogix2/dataset"
    known_face_encodings, known_face_names = load_known_faces(dataset_folder)

    # Initialize video capture
    video_capture = cv2.VideoCapture(0)

    attendance_data = []

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Convert frame to RGB for face recognition
        rgb_frame = frame[:, :, ::-1]

        # Find all face locations and encodings
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            # Compare face encoding with known face encodings
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # If match found, assign the name
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

                # Append attendance data
                attendance_data.append({'name': name, 'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

            # Draw rectangle around the face and label with name
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release video capture and close all OpenCV windows
    video_capture.release()
    cv2.destroyAllWindows()

    # Write attendance data to CSV file
    csv_file_path = "attendance.csv"
    write_attendance_to_csv(attendance_data, csv_file_path)

    return JsonResponse({'status': 'success'})

def load_known_faces(dataset_folder):
    known_face_encodings = []
    known_face_names = []

    for root, dirs, files in os.walk(dataset_folder):
        for file in files:
            if file.endswith(".jpg") or file.endswith(".png"):
                image_path = os.path.join(root, file)
                name = os.path.basename(os.path.dirname(image_path))
                image = face_recognition.load_image_file(image_path)
                face_encodings = face_recognition.face_encodings(image)
                if face_encodings:
                    encoding = face_encodings[0]
                    known_face_encodings.append(encoding)
                    known_face_names.append(name)

    return known_face_encodings, known_face_names


def write_attendance_to_csv(attendance_data, csv_file_path):
    with open(csv_file_path, 'w', newline='') as csvfile:
        fieldnames = ['name', 'timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in attendance_data:
            writer.writerow(entry)
