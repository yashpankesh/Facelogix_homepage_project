import cv2
import os
from datetime import datetime

def capture_dataset(output_folder, enrollment_number, photo_limit=1):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Unable to access the camera.")
        return
    
    photo_count = 0

    while photo_count < photo_limit:
        ret, frame = cam.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break
        
        cv2.imshow("Dataset-Capture", frame)
        
        now = datetime.now()
        current_datetime = now.strftime("%Y-%m-%d_%H-%M-%S")
        photo_filename = os.path.join(output_folder, f'{enrollment_number}_{current_datetime}.jpg')
        cv2.imwrite(photo_filename, frame)
        print(f"Saved: {photo_filename}")
        
        photo_count += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows() 

if __name__ == "__main__":
    output_folder = "D:/Django-project/facelogix2/dataset"
    enrollment_number = input("Enter enrollment number: ")
    photo_limit = 10
    capture_dataset(output_folder, enrollment_number, photo_limit)



# main
# import cv2  #final
# import os
# from datetime import datetime

# def capture_dataset(output_folder, photo_limit=1):
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
    
#     cam = cv2.VideoCapture(0)
#     if not cam.isOpened():
#         print("Error: Unable to access the camera.")
#         return
    
#     photo_count = 0

#     while photo_count < photo_limit:
#         ret, frame = cam.read()
#         if not ret:
#             print("Error: Failed to capture frame.")
#             break
        
#         cv2.imshow("Dataset-Capture", frame)
        
#         now = datetime.now()
#         current_datetime = now.strftime("%Y-%m-%d_%H-%M-%S")
#         photo_filename = os.path.join(output_folder, f'{current_datetime}.jpg')
#         cv2.imwrite(photo_filename, frame)
#         print(f"Saved: {photo_filename}")
        
#         photo_count += 1

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cam.release()
#     cv2.destroyAllWindows() 

# if __name__ == "__main__":
#     output_folder = "D:/Django-project/facelogix2/dataset"
#     photo_limit = 10
#     capture_dataset(output_folder, photo_limit)

# import cv2
# import os
# from datetime import datetime
# import tkinter as tk
# from tkinter import simpledialog

# def capture_dataset(output_folder, dataset_name, photo_limit=10):
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
    
#     cam = cv2.VideoCapture(0)
#     if not cam.isOpened():
#         print("Error: Unable to access the camera.")
#         return
    
#     photo_count = 0

#     while photo_count < photo_limit:
#         ret, frame = cam.read()
#         if not ret:
#             print("Error: Failed to capture frame.")
#             break
        
#         cv2.imshow("Dataset-Capture", frame)
        
#         now = datetime.now()
#         current_datetime = now.strftime("%Y-%m-%d_%H-%M-%S")
#         photo_filename = os.path.join(output_folder, f'{dataset_name}_{current_datetime}.jpg')
#         cv2.imwrite(photo_filename, frame)
#         print(f"Saved: {photo_filename}")
        
#         photo_count += 1

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cam.release()
#     cv2.destroyAllWindows() 

# def get_dataset_name():
#     root = tk.Tk()
#     root.withdraw()
#     dataset_name = simpledialog.askstring("Input", "Enter dataset name:")
#     return dataset_name

# if __name__ == "__main__":
#     output_folder = "D:/Django-project/facelogix2/dataset"
#     photo_limit = 10
#     dataset_name = get_dataset_name()
#     if dataset_name:
#         capture_dataset(output_folder, dataset_name, photo_limit)

# import cv2
# import os
# import tkinter as tk
# from tkinter import simpledialog
# from datetime import datetime

# def capture_dataset(output_folder):
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Ask user to input name
#     root = tk.Tk()
#     root.withdraw()
#     name = simpledialog.askstring("Input", "Enter your name:")
#     if not name:
#         print("Error: Name not provided.")
#         return

#     # Open the default camera (index 0)
#     cap = cv2.VideoCapture(0)

#     # Check if the camera opened successfully
#     if not cap.isOpened():
#         print("Error: Could not open camera.")
#         return

#     photo_count = 0

#     while True:
#         # Read a frame from the camera
#         ret, frame = cap.read()

#         if not ret:
#             print("Error: Failed to capture frame.")
#             break

#         # Display the frame
#         cv2.imshow("Capture Dataset", frame)

#         # Generate timestamp
#         timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#         # Save the captured image
#         image_path = os.path.join(output_folder, f"{name}_{timestamp}.jpg")
#         cv2.imwrite(image_path, frame)
#         print(f"Image saved as: {image_path}")

#         photo_count += 1

#         # Limit to capturing 10 photos
#         if photo_count >= 10:
#             break

#         # Wait for 'q' key to quit
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     # Release the camera and close OpenCV windows
#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     output_folder = "D:/Django-project/facelogix2/dataset"
#     capture_dataset(output_folder)


