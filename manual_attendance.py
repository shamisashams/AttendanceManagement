
from base_system import AttendanceSystem

class ManualAttendanceSystem(AttendanceSystem):
    def __init__(self):
        super().__init__()  # Call the parent constructor

    def mark_attendance_manually(self, user_id, name):
        """Manually mark attendance for a user."""
        self.log_attendance(user_id, name)
