
class AttendanceSystem:
    """
        Base class for attendance systems. Handles common functionality such as logging and viewing attendance.
    """
      
    def __init__(self):
        # Initialize an empty attendance log
        self.attendance_log = []

    def log_attendance(self, user_id, name):
        """
        Log attendance with user details and a timestamp.

        Args:
            user_id (str): The unique ID of the user.
            name (str): The name of the user.
        """
        from datetime import datetime
        # Generate a timestamp for the attendance entry
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
         # Append the attendance record to the log
        self.attendance_log.append({"id": user_id, "name": name, "timestamp": timestamp})
        print(f"Attendance logged: {name} ({user_id}) at {timestamp}")

    def view_attendance_log(self):
        """Display all logged attendance."""
        for record in self.attendance_log:
            print(f"{record['id']} - {record['name']} at {record['timestamp']}")