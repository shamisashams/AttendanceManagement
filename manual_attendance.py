
from base_system import AttendanceSystem

class ManualAttendanceSystem(AttendanceSystem):
    """
    Child class for handling manual attendance logging.
    """
    def __init__(self):
        """Initialize the manual attendance system."""
        super().__init__()

    def mark_attendance_manually(self, user_id, name):
        """
        Manually log attendance for a user.

        Args:
            user_id (str): The unique ID of the user.
            name (str): The name of the user.
        """
        self.log_attendance(user_id, name)  # Use parent method to log attendance


