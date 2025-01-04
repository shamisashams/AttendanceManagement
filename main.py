from face_detector import FaceDetector
from user_database import UserDatabase
from attendance_manager import AttendanceManager
from face_recognition_attendance import FaceRecognitionAttendanceSystem
from manual_attendance import ManualAttendanceSystem

db = UserDatabase()
detector = FaceDetector()
manager = AttendanceManager(db)

db.add_user("Bill Gates", "001", "images/known/bill_gates.jpg")
db.add_user("Steve Jobs", "002", "images/known/steve_jobs.jpg")
db.add_user("Elon Musk", "003", "images/known/elon_musk.jpg")

# Facial Recognition Attendance System
face_recognition_system = FaceRecognitionAttendanceSystem(db)
face_recognition_system.mark_attendance_from_image("images/group_photo.jpg")

# Manual Attendance System
manual_system = ManualAttendanceSystem()
manual_system.mark_attendance_manually("002", "Jane Smith")


# View Attendance Logs
print("\nFacial Recognition System Logs:")
face_recognition_system.view_attendance_log()

print("\nManual Attendance System Logs:")
manual_system.view_attendance_log()