
# Face Recognition Attendance Management System

This is a Python-based **Face Recognition Attendance System** that leverages facial recognition technology to automate attendance tracking. The project also includes a manual attendance logging feature for flexibility. It is designed using object-oriented principles and is structured into reusable modules and classes.

---

## **Features**
- **Facial Recognition Attendance**: Uses images to detect faces and mark attendance automatically.
- **Manual Attendance Logging**: Allows manual addition of attendees.
- **Attendance Reports**: Generates CSV reports with all attendance records, including both automatic and manual entries.
- **User Database Management**: Manages users and their face encodings stored in a JSON file.
- **Modular Design**: The system is divided into separate, reusable modules.

---

## **Project Structure**

### **Files**
1. **`main.py`**: Entry point of the application. Orchestrates the facial recognition and manual attendance systems.
2. **`base_system.py`**: Contains the base class `AttendanceSystem` with shared functionality for all attendance methods.
3. **`attendance_manager.py`**: Handles attendance through facial recognition and generates combined reports.
4. **`manual_attendance.py`**: Manages manual attendance logging.
5. **`user_database.py`**: Manages the user database (stored in `users.json`).
6. **`face_detector.py`**: Handles face detection and encoding using the `face_recognition` library.
7. **`users.json`**: Stores user data, including names, IDs, and face encodings.
8. **`requirements.txt`**: Lists all required Python dependencies.

### **Folders**
1. **`images/`**: Contains image data for facial recognition.
   - **`users/`**: Images of registered users.
   - **`groups/`**: Group photos used for marking attendance.
2. **`reports/`**: Stores generated attendance reports.
   - **`attendance_report.csv`**: The latest attendance report.

---

## **How to Run the Project**

### **Prerequisites**
1. Python 3.8 or later.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### **Steps**
1. **Add Users**:
   - Save user images in the `images/users/` folder.
   - Use the `add_user()` method in `user_database.py` to register users.
   
2. **Run the Application**:
   ```bash
   python main.py
   ```

3. **Mark Attendance**:
   - **Automatic**: Add group images to the `images/groups/` folder and run the attendance system.
   - **Manual**: Use the manual logging feature to add attendees who are not detected automatically.

4. **Generate Reports**:
   - Reports are automatically saved to the `reports/attendance_report.csv` file after attendance is marked.

---

## **Dependencies**
The project relies on the following Python libraries:
- `face_recognition`
- `opencv-python`
- `numpy`
- `pandas`

Refer to `requirements.txt` for the full list of dependencies.

---

## **Usage Example**

### **Add a User**
To register a new user:
```python
from user_database import UserDatabase

db = UserDatabase()
db.add_user("John Doe", "001", "images/users/john_doe.jpg")
```

### **Mark Attendance with Facial Recognition**
```python
from attendance_manager import AttendanceManager
from user_database import UserDatabase

db = UserDatabase()
manager = AttendanceManager(db)
attendance = manager.mark_attendance("images/groups/group_photo.jpg")
manager.generate_report(attendance)
```

### **Manually Log Attendance**
```python
from manual_attendance import ManualAttendanceSystem

manual_system = ManualAttendanceSystem()
manual_system.mark_attendance_manually("002", "Jane Smith")
```

---

## **Future Improvements**
- Add live webcam support for real-time attendance.
- Implement a GUI for user-friendly interaction.
- Extend the user database to include additional metadata.
- Enhance security and encryption for sensitive data like face encodings.

---

## **Credits**
Developed by **Shamisa Shams** with guidance and support. 💡
```
