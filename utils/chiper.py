from cryptography.fernet import Fernet



class Encrypter:
    def __init__(self):
        pass


    def generate_key(self) -> bytes:
        user_key = Fernet.generate_key()
        return user_key.decode()


    def encrypt(self, text, key):
        Fernet.generate_key()
        cipher = Fernet(key)
        return cipher.encrypt(text.encode()).decode()
      

    def decrypt(self, encrypted_text, key):
        cipeher = Fernet(key)
        decrypted_text = cipeher.decrypt(encrypted_text.encode())
        return decrypted_text.decode()
    

    def encrypt_user_key(self, text, user_key):
        chiper = Fernet(key=user_key)
        return chiper.encrypt(text.encode()).decode()
    
    def decrypt_user_key(self, encrypted_text, user_key):
        chiper = Fernet(key=user_key)
        decrypted_text = chiper.decrypt(encrypted_text.encode())
        return decrypted_text.decode()
    