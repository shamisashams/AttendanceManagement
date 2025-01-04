import face_recognition

class FaceDetector:
    """
        Handles face detection and encoding.
    """
    def __init__(self):
        pass

    def detect_faces(self, image_path):
        """
        Detect faces in an image and return their encodings.

        Args:
            image_path (str): Path to the image file.

        Returns:
            list: List of face encodings found in the image.
        """

         # Load the image file
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
         # Find face encodings in the image
        face_encodings = face_recognition.face_encodings(image, face_locations)
        return face_encodings
    
    def get_face_encoding(self, image_path):
        """
        Get the encoding of a single face in an image.

        Args:
            image_path (str): Path to the image file.

        Returns:
            list: Encoding of the detected face.

        Raises:
            ValueError: If no faces or multiple faces are detected.
        """
        encodings = self.detect_faces(image_path)
        if len(encodings) != 1:
            raise ValueError("Image must contain exactly one face.")
        return encodings[0]


