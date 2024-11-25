import face_recognition
import json

class UserDatabase:
    def __init__(self):
        # self.add_user
        pass

    def load_users():
        pass

    def add_user(self, name, user_id, image_path):
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        print(image)

    def save_users():
        pass