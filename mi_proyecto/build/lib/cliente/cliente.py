# cliente/cliente.py

import time

users_passwords = {}

class Cliente:
    def __init__(self, nombre, apellido, email, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad

    def __str__(self):
        return f"{self.nombre} {self.apellido}, {self.edad} años - Email: {self.email}"

    def verificar_email(self):
        return "@" in self.email and "." in self.email


