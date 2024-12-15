import face_recognition
import json
import pandas as pd
import datetime


# face detetcor
class FaceDetector:
    def __init__(self):
        pass

    def detect_faces(self, image_path):
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)
        return face_encodings


# user database
class UserDatabase:
    def __init__(self, db_path = 'users.json'):
        self.db_path = db_path
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.db_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def add_user(self, name, user_id, image_path):
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        self.users[user_id] = {'name': name, 'encoding': encoding.tolist()}
        self.save_users()

    def save_users(self):
        with open(self.db_path, 'w') as file:
            json.dump(self.users, file)


# attendance manager

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
        


# ###

database = UserDatabase()
detector = FaceDetector()
manager = AttendanceManager()

database.add_user("Bill Gates", "001", "img/known/bill_gates")
attendance = manager.mark_attendance("img/groups/bill-steve-elon.jpg")
manager.generate_report(attendance)

print(attendance)