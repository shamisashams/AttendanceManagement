
class AttendanceSystem:
    def __init__(self):
        self.attendance_log = []

    def log_attendance(self, user_id, name):
        """Log attendance with user details."""
        from datetime import datetime
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.attendance_log.append({"id": user_id, "name": name, "timestamp": timestamp})
        print(f"Attendance logged: {name} ({user_id}) at {timestamp}")

    def view_attendance_log(self):
        """Display all logged attendance."""
        for record in self.attendance_log:
            print(f"{record['id']} - {record['name']} at {record['timestamp']}")