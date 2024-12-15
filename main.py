from face_detector import FaceDetector
from user_database import UserDatabase
from attendance_manager import AttendanceManager


database = UserDatabase()
detector = FaceDetector()
manager = AttendanceManager(database)

database.add_user("Bill Gates", "001", "img/known/bill_gates.jpg")
database.add_user("Steve Jobs", "002", "img/known/steve_jobs.jpg")
database.add_user("Elon Musk", "003", "img/known/elon_musk.jpg")
attendance = manager.mark_attendance("img/groups/bill-steve-elon.jpg")
manager.generate_report(attendance)

print(attendance)