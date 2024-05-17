from cryptography.fernet import Fernet
import hashlib
import base64


def _get_key() -> bytes:
    key = b"My Secret Key!"  # Byte string
    # Συνάρτηση κατακερματισμού Hash function 
    hlib = hashlib.md5()  # https://docs.python.org/3/library/hashlib.html
    hlib.update(key)
    # Κωδικοποίηση σε μορφή Base64 με ασφαλείς χαρακτήρες για χρήση σε url
    key = base64.urlsafe_b64encode(hlib.hexdigest().encode('utf-8'))
    return key


def encrypt_password(psw:str):
    key = _get_key()
    # symmetric encryption
    # Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key.
    f = Fernet(key)
    secret = f.encrypt(psw.encode('utf-8'))  # generate secret
    return secret.decode('utf-8')  # Returns a string


def decrypt_password(e_psw:str):
    key = _get_key()
    f = Fernet(key)
    return f.decrypt(e_psw).decode("utf-8")  # Returns a string




