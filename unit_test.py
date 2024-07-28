import encrypt
import decrypt

class Test:
    def __init__(self, message, shift, choice):
        self.message = message
        self.shift = shift
        self.choice = choice

    def testing(self):
        if self.choice == "encrypt":
            return encrypt.encrypt(self.message, self.shift)
        elif self.choice == "decrypt":
            return decrypt.decrypt(self.message, self.shift)
