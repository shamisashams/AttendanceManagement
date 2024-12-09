from face_detector import FaceDetector
import face_recognition

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
                        "name": user["name"]
                        # "timestamp" dont forget to add 
                    })
        return attendance

    def generate_report(self, attendance, file_name=""):
    
        pass