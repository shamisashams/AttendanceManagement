import face_recognition

class FaceDetector:
    def __init__(self):
        pass

    def detect_faces(self, image_path):
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)
        return face_encodings


# person1 = FaceDetector()
# print(person1.detect_faces('./img/known/Bill Gates.jpg'))