

import uuid

from app.utils.crypto_utils import decrypt_password, encrypt_password


class User:
    def __init__(self, username:str, password:str, email:str, role:str, active=True):
        self.username = username
        self.password = password
        self.email = email
        self.role = role
        self.active = active
        self.id = str(uuid.uuid4())

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f"{self.id} - {self.username} ({self.email})"

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.password}', '{self.email}', '{self.role}', {self.active})"

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": encrypt_password(self.password),
            "email": self.email,
            "role": self.role,
            "active": self.active,
        }

    def from_dict(self, data):
        self.id = data.get("id") if data.get("id") is not None else self.id
        self.username = data.get("username") if data.get(
            "username") is not None else self.username
        self.password = decrypt_password(data.get("password")) if data.get(
            "password") is not None else self.password
        self.email = data.get("email") if data.get(
            "email") is not None else self.email
        self.role = data.get("role") if data.get(
            "role") is not None else self.role
        self.active = data.get("active") if data.get(
            "active") is not None else self.active
