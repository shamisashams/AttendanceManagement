from face_detector import FaceDetector
import face_recognition
import pandas as pd
import datetime

class AttendanceManager:
    def __init__(self, user_db):
        self.user_db = user_db

    def mark_attendance(self, image_path):
        face_encodings = FaceDetector().detect_faces(image_path)
        attendance = []

        for encoding in face_encodings:
            for user_id, user in self.user_db.users.items():
                match = face_recognition.compare_faces([user["encoding"]], encoding)
                if match[0]:
                    attendance.append({
                        "id": user_id,
                        "name": user["name"],
                        "timestap": str(datetime.datetime.now())
                    })
        return attendance

    def generate_report(self, attendance, file_name="reports/attendance_report.csv"):
        df = pd.DataFrame(attendance)
        df.to_csv(file_name, index=False)
        print(f'Report saved to {file_name}')
        