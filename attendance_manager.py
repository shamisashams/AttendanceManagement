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

       

