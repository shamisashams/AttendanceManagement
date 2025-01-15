from face_detector import FaceDetector
from user_database import UserDatabase
from attendance_manager import AttendanceManager
from manual_attendance import ManualAttendanceSystem

# Initialize User Database
db = UserDatabase()
detector = FaceDetector()
manual_system = ManualAttendanceSystem()
manager = AttendanceManager(db, manual_system)

# Add user to the database
db.add_user("Margot Robbie", "002", "images/users/margot_robbie.png")
db.add_user("Dua Lipa", "003", "images/users/dualipa.png")

# Manual Attendance System
manual_system.mark_attendance_manually("004", "Philomena Cunk")

attendance = manager.mark_attendance("images/groups/dua_margot_billie.png")
# Generate report of the attendees
manager.generate_report(attendance)


from base_system import AttendanceSystem