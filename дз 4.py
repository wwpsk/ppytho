import random

class NumberEncryptor:
    def __init__(self):
        self.hidden_number = None

    def encrypt(self, number):
        self.hidden_number = number + random.randint(1, 10)

    def decrypt(self):
        if self.hidden_number is not None:
            return self.hidden_number - random.randint(1, 10)
        else:
            return None

encryptor = NumberEncryptor()

number = 42
encryptor.encrypt(number)

print("Зашифроване число:", encryptor.hidden_number)

decrypted_number = encryptor.decrypt()

print("Розшифроване число:", decrypted_number)