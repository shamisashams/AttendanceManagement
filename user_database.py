import face_recognition
import json

class UserDatabase:
    """
        Manages the storage and retrieval of user data.
    """
    def __init__(self, db_path = 'users.json'):
        """
        Initialize the user database.

        Args:
            db_path (str): Path to the JSON file storing user data.
        """
        self.db_path = db_path
        self.users = self.load_users()

    def load_users(self):
        """
            Load users from the JSON database file.
        """
        try:
            with open(self.db_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
              # Create an empty JSON file if none exists
            self.users = {}
            self.save_users()


    def add_user(self, name, user_id, image_path):
        """
        Add a new user to the database.

        Args:
            name (str): Name of the user.
            user_id (str): Unique ID for the user.
            image_path (str): Path to the user's image.
        """
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        self.users[user_id] = {'name': name, 'encoding': encoding.tolist()}
        self.save_users()


    def save_users(self):
        """
            Save the current user data to the JSON database file.
        """
        with open(self.db_path, 'w') as file:
            json.dump(self.users, file)

    def get_user(self, user_id):
        """
            Retrieve user details by ID.

            Args:
                user_id (str): The unique ID of the user.

            Returns:
                dict: user details or none if not found.
        """
        return self.users.get(user_id)