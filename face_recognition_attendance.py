
from base_system import AttendanceSystem
from face_detector import FaceDetector
from user_database import UserDatabase
import face_recognition

class FaceRecognitionAttendanceSystem(AttendanceSystem):
    def __init__(self, user_db):
        super().__init__()  # Call the parent constructor
        self.user_db = user_db
        self.face_detector = FaceDetector()

    def mark_attendance_from_image(self, image_path):
        face_encodings = self.face_detector.detect_faces(image_path)

        for encoding in face_encodings:
            for user_id, user in self.user_db.users.items():
                match = face_recognition.compare_faces([user["encoding"]], encoding)
                if match[0]:
                    self.log_attendance(user_id, user["name"])
                    break
