# Attendance Management System

## Overview
The Attendance Management System is a Python-based application designed to log and manage attendance using both facial recognition and manual entry methods. It demonstrates key programming concepts such as object-oriented programming (OOP), inheritance, and modular design.

## Features
- **Facial Recognition Attendance**: Automatically marks attendance for users by recognizing their faces from an image.
- **Manual Attendance Logging**: Allows manual logging of attendance for users.
- **Attendance Logs**: View attendance records with timestamps.
- **User Database Management**: Add, store, and retrieve user details using a JSON file.

## Project Structure
```
attendance_management_system/
├── main.py                      # Main script to run the application
├── base_system.py               # Base class for attendance systems
├── face_recognition_attendance.py # Facial recognition-based attendance system
├── manual_attendance.py         # Manual attendance system
├── user_database.py             # Manages user data storage and retrieval
├── face_detector.py             # Handles face detection and encoding
├── data/
│   └── users.json               # JSON database for user details
├── images/                      # Directory for storing user images
└── tests/                       # Unit tests for the system
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/attendance-management-system.git
   cd attendance-management-system
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure you have `dlib` and `face_recognition` installed. For installation instructions, refer to the [face_recognition documentation](https://github.com/ageitgey/face_recognition).

## Usage
### Adding a User
1. Add a new user to the database by providing their name, unique ID, and an image file:
   ```python
   from user_database import UserDatabase

   db = UserDatabase()
   db.add_user("John Doe", "001", "images/john_doe.jpg")
   ```

### Running the Facial Recognition System
1. Initialize the system and mark attendance from an image:
   ```python
   from face_recognition_attendance import FaceRecognitionAttendanceSystem

   face_recognition_system = FaceRecognitionAttendanceSystem(db)
   face_recognition_system.mark_attendance_from_image("images/group_photo.jpg")
   ```

### Running the Manual Attendance System
1. Log attendance manually:
   ```python
   from manual_attendance import ManualAttendanceSystem

   manual_system = ManualAttendanceSystem()
   manual_system.mark_attendance_manually("002", "Jane Smith")
   ```

### Viewing Attendance Logs
1. View the logged attendance records:
   ```python
   face_recognition_system.view_attendance_log()
   manual_system.view_attendance_log()
   ```

## Tests
1. Run the test suite to ensure all components are functioning correctly:
   ```bash
   python -m unittest discover tests/
   ```

## Future Enhancements
- Add a web or mobile interface for easier interaction.
- Enable real-time facial recognition using a webcam.
- Integrate with external APIs for notifications or reporting.

## Contributions
Contributions are welcome! Please feel free to submit a pull request or open an issue for any feature requests or bugs.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments
- [face_recognition](https://github.com/ageitgey/face_recognition) library for facial recognition.
- Python community for its incredible libraries and resources.
