from abc import ABC, abstractmethod


class Cipher(ABC):
    @abstractmethod
    def encrypt(self, word: str) -> str: ...
        
    @abstractmethod
    def decrypt(self, word: str) -> str: ...
    
    
class Rot13Cipher(Cipher):
    SHIFT = 13
    ALPHABET_SIZE = 26

    def encrypt(self, text: str) ->  str:
        return ''.join(self._rotate_char(char) for char in text)

    def decrypt(self, text: str) -> str:
        return self.encrypt(text)  

    def _rotate_char(self, char: str) -> str:
        if 'A' <= char <= 'Z':
            base = ord('A')
        elif 'a' <= char <= 'z':
            base = ord('a')
        else:
            return char  

        position = ord(char) - base 
        new_position = (position + self.SHIFT) % self.ALPHABET_SIZE      
        return chr(base + new_position)
