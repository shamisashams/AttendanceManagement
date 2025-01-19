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
db.add_user("Walter White", "001", "images/users/walter_white.png")

# Manual Attendance System
manual_system.mark_attendance_manually("007", "Vince Gilligan")

# Mark attandance in a group 
attendance = manager.mark_attendance("images/groups/g-4.png")

# Generate report of the attendees
manager.generate_report(attendance)



