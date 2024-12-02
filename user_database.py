import face_recognition
import json

class UserDatabase:
    def __init__(self, db_path = 'users.json'):
        self.db_path = db_path
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.db_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def add_user(self, name, user_id, image_path):
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        self.users[user_id] = {'name': name, 'encoding': encoding.tolist()}
        self.save_users()

    def save_users(self):
        with open(self.db_path, 'w') as file:
            json.dump(self.users, file)