from face_detector import FaceDetector
from user_database import UserDatabase
from attendance_manager import AttendanceManager
from face_recognition_attendance import FaceRecognitionAttendanceSystem
from manual_attendance import ManualAttendanceSystem

# Initialize User Database
db = UserDatabase()
detector = FaceDetector()
manager = AttendanceManager(db)

# Add sample user to the database
db.add_user("Bill Gates", "001", "images/known/bill_gates.jpg")
db.add_user("Elon Musk", "002", "images/known/elon_musk.jpg")


attendance = manager.mark_attendance("images/groups/bill-steve-elon.jpg")
manager.generate_report(attendance)

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
