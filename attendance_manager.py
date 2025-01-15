from base_system import AttendanceSystem
from face_detector import FaceDetector
import face_recognition
import pandas as pd
import os



class AttendanceManager(AttendanceSystem):
    """
    Child class for handling attendance via facial recognition.
    Manages attendance marking and reporting using facial recognition.
    """
    def __init__(self, user_db, manual_system):
        """
        Initialize the face recognition attendance system.

        Args:
            user_db (UserDatabase): Instance of the user database.
        """
        super().__init__()
        self.user_db = user_db
        self.face_detector = FaceDetector()
        self.manual_system = manual_system

    def mark_attendance(self, image_path):
        """
        Marks attendance by detecting faces in an image and comparing them to registered user encodings.

        Args:
            image_path (str): Path to the image containing faces to process.
        """
        face_encodings = self.face_detector.detect_faces(image_path)
        for encoding in face_encodings:
            for user_id, user in self.user_db.users.items():
                match = face_recognition.compare_faces([user["encoding"]], encoding)
                if match[0]:
                    self.log_attendance(user_id, user["name"])  # Log attendance using the parent method

    def generate_report(self, file_name="reports/attendance_report.csv"):
        """
        Generates a CSV report of all attendance records, including both manual and facial recognition logs.

        Args:
            file_name (str): The file path to save the attendance report.
        """
       
        if not os.path.exists("reports"):
            os.makedirs("reports")

        if not file_name:
            file_name = "reports/attendance_report.csv"

        combined_attendance = self.attendance_log + self.manual_system.attendance_log

        # Use the attendance_log from the parent class, which includes all logged attendance
        df = pd.DataFrame(combined_attendance)
        df.to_csv(file_name, index=False)
        print(f"Report saved to {file_name}")

            # df = pd.DataFrame(attendance)






   
# class AttendanceManager(AttendanceSystem):
#     """
#         Child class for handling attendance via facial recognition.

#           Manages attendance marking and reporting using facial recognition.
#     """
#     def __init__(self, user_db):
#         """
#         Initialize the face recognition attendance system.

#         Args:
#             user_db (UserDatabase): Instance of the user database.
#         """
#         super().__init__()  
#         self.user_db = user_db
#         self.face_detector = FaceDetector()

#     def mark_attendance(self, image_path):
#         """
#         Marks attendance by detecting faces in an image and comparing them to registered user encodings.
        
#         Args:
#             image_path (str): Path to the image containing faces to process.

#         Returns:
#             list: A list of dictionaries containing attendance records for recognized users.
#                   Each dictionary contains the user ID, name, and timestamp.
#         """

#         # Detect face encodings from the provided image
#         face_encodings = FaceDetector().detect_faces(image_path)
#         attendance = []

#         for encoding in face_encodings:
#              # Iterate over registered users and compare face encodings
#             for user_id, user in self.user_db.users.items():
#                 match = face_recognition.compare_faces([user["encoding"]], encoding)
#                 if match[0]:
#                     attendance.append({
#                         "id": user_id,
#                         "name": user["name"],
#                         "timestamp": str(datetime.datetime.now())

#                     })
#         return attendance
    
#     def generate_report(self, attendance, file_name="reports/attendance_report.csv"):
#         """
#         Generates a CSV report of the attendance records.

#         Args:
#             attendance (list): A list of dictionaries containing attendance records.
#             file_name (str): The file path to save the attendance report. Default is 'reports/attendance_report.csv'.

#         Returns:
#             None
#         """
#          # Convert attendance data to a Pandas DataFrame
#         df = pd.DataFrame(attendance)

#         # Save the DataFrame to a CSV file
#         df.to_csv(file_name, index=False)
#         print(f'Report saved to {file_name}')