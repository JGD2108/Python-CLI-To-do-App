# Clase que maneja y guarda los usuarios en un archivo junto a su contraseña para asi poder iniciar sesion
import os
from hashlib import pbkdf2_hmac
import base64
from cryptography.fernet import Fernet
class Users: 
    def is_strong_password(self, password):
        import re
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[a-z]", password):
            return False
        if not re.search(r"[0-9]", password):
            return False
        return True
    def get_fernet_key(self, password, salt):
        key = pbkdf2_hmac('sha256', password.encode(), salt, 100000, dklen=32)
        return base64.urlsafe_b64encode(key)

    def get_user_file_path(self, username):
        base_dir = 'users_files'
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        return os.path.join(base_dir, f"{username}_tasks.enc")

    def create_encrypted_user_file(self, username, password, initial_data=b''):
        if username not in self.users:
            return False
        _, salt = self.users[username]
        key = self.get_fernet_key(password, salt)
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(initial_data)
        user_file = self.get_user_file_path(username)
        with open(user_file, 'wb') as f:
            f.write(encrypted_data)
        return True

    def read_encrypted_user_file(self, username, password):
        if username not in self.users:
            return None
        _, salt = self.users[username]
        key = self.get_fernet_key(password, salt)
        fernet = Fernet(key)
        user_file = self.get_user_file_path(username)
        if not os.path.exists(user_file):
            return None
        with open(user_file, 'rb') as f:
            encrypted_data = f.read()
        try:
            return fernet.decrypt(encrypted_data)
        except Exception:
            return None

    def write_encrypted_user_file(self, username, password, data):
        if username not in self.users:
            return False
        _, salt = self.users[username]
        key = self.get_fernet_key(password, salt)
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)
        user_file = self.get_user_file_path(username)
        with open(user_file, 'wb') as f:
            f.write(encrypted_data)
        return True
    def __init__(self, filename="users.txt"):
        self.filename = filename
        self.users = self.load_users()
        
    def load_users(self):
        users = {}
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    username, hash_hex, salt_hex = line.strip().split(',')
                    users[username] = (bytes.fromhex(hash_hex), bytes.fromhex(salt_hex))
        except FileNotFoundError:
            pass
        return users
    
    def save_users(self):
        with open(self.filename, 'w') as file:
            for username, (hash, salt) in self.users.items():
                file.write(f"{username},{hash.hex()},{salt.hex()}\n")
    def verify_user(self, username, password):
        if username not in self.users:
            return False
        hash_saved, salt = self.users[username]
        hash_try = pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        return hash_try == hash_saved

    def add_user(self, username, password):
        if username in self.users:
            return False
        salt = os.urandom(16)
        hash = pbkdf2_hmac('sha256', password.encode(), salt, 100000)
        self.users[username] = (hash, salt)
        self.save_users()
        return True
    
    
        


    
    
