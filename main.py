
from face_detector import FaceDetector
from user_database import UserDatabase
from attendance_manager import AttendanceManager

database = UserDatabase()
detector = FaceDetector()
manager = AttendanceManager()

database.add_user("Bill Gates", "001", "img/known/bill_gates")
attendance = manager.mark_attendance("img/groups/bill-steve-elon.jpg")
manager.generate_report(attendance)

print(attendance)