"""Fernet encryption/decryption utility class"""

from cryptography.fernet import Fernet, InvalidToken


class FernetHelper(object):
    """JWT encode decode helper. Envery parameter must be encoded"""

    def __init__(self):
        # key = Fernet.generate_key() --> generates key/ for prod use your own key
        key = "ZiBE12H-xg0KWUTiqL6b57JnIEsAWJ170LfnYm0CgFw="
        self.fernet = Fernet(key=key.encode("utf-8"))

    def encrypt(self, plain_text):
        """Encryptes the data"""
        encrypted = self.fernet.encrypt(plain_text.encode("utf-8"))
        return encrypted.decode("utf-8")

    def decrypt(self, cipher_text):
        decrypted = None
        try:
            decrypted = self.fernet.decrypt(cipher_text.encode("utf-8"))
        except InvalidToken:
            return None
        return decrypted.decode("utf-8")
