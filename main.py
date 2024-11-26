import face_recognition
from face_detector import FaceDetector
from user_database import UserDatabase


image = face_recognition.load_image_file('./img/groups/team2.jpg')
face_locations = face_recognition.face_locations(image)

print(f'number of faces in the frame: {len(face_locations)}')

