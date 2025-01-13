from face_detector import FaceDetector
import face_recognition
import pandas as pd
import datetime

class AttendanceManager:
    """
    Manages attendance marking and reporting using facial recognition.
    
    Attributes:
        user_db (UserDatabase): An instance of the UserDatabase class, which holds user information.
    """
    def __init__(self, user_db):
        """
        Initializes the AttendanceManager with a reference to the user database.
        
        Args:
            user_db (UserDatabase): The user database instance containing user details and encodings.
        """
        self.user_db = user_db

    def mark_attendance(self, image_path):
        """
        Marks attendance by detecting faces in an image and comparing them to registered user encodings.
        
        Args:
            image_path (str): Path to the image containing faces to process.

        Returns:
            list: A list of dictionaries containing attendance records for recognized users.
                  Each dictionary contains the user ID, name, and timestamp.
        """

        # Detect face encodings from the provided image
        face_encodings = FaceDetector().detect_faces(image_path)
        attendance = []

        for encoding in face_encodings:
             # Iterate over registered users and compare face encodings
            for user_id, user in self.user_db.users.items():
                match = face_recognition.compare_faces([user["encoding"]], encoding)
                if match[0]:
                    attendance.append({
                        "id": user_id,
                        "name": user["name"],
                        "timestamp": str(datetime.datetime.now())

                    })
        return attendance

    def generate_report(self, attendance, file_name="reports/attendance_report.csv"):
        """
        Generates a CSV report of the attendance records.

        Args:
            attendance (list): A list of dictionaries containing attendance records.
            file_name (str): The file path to save the attendance report. Default is 'reports/attendance_report.csv'.

        Returns:
            None
        """
         # Convert attendance data to a Pandas DataFrame
        df = pd.DataFrame(attendance)

        # Save the DataFrame to a CSV file
        df.to_csv(file_name, index=False)
        print(f'Report saved to {file_name}')