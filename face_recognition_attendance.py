
from base_system import AttendanceSystem
from face_detector import FaceDetector
from user_database import UserDatabase
import face_recognition

class FaceRecognitionAttendanceSystem(AttendanceSystem):
    """
        Child class for handling attendance via facial recognition.
    """
    def __init__(self, user_db):
        """
        Initialize the face recognition attendance system.

        Args:
            user_db (UserDatabase): Instance of the user database.
        """
        super().__init__()  # Call the parent constructor
        self.user_db = user_db
        self.face_detector = FaceDetector()

    def mark_attendance_from_image(self, image_path):
        """
        Detect faces in an image and log attendance for recognized users.

        Args:
            image_path (str): Path to the image containing faces.
        """

         # Get face encodings from the image
        face_encodings = self.face_detector.detect_faces(image_path)

        for encoding in face_encodings:
            for user_id, user in self.user_db.users.items():
                # Compare the detected face encoding with stored encodings
                match = face_recognition.compare_faces([user["encoding"]], encoding)
                if match[0]:
                    # Log attendance for the recognized user
                    self.log_attendance(user_id, user["name"])
                    break
