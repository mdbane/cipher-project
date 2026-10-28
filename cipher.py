from abc import ABC, abstractmethod


class Cipher(ABC):
    @abstractmethod
    def encrypt(self, text: str) -> str: ...

    @abstractmethod
    def decrypt(self, text: str) -> str: ...


class Rot13Cipher(Cipher):
    SHIFT = 13
    ALPHABET_SIZE = 26

    def encrypt(self, text: str) -> str:
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


class Rot47Cipher(Cipher):
    FIRST_CHAR = 33
    LAST_CHAR = 126
    CHARS_COUNT = LAST_CHAR - FIRST_CHAR + 1
    SHIFT = 47

    def encrypt(self, text: str) -> str:
        return ''.join(self._rotate_char(char) for char in text)

    def decrypt(self, text: str) -> str:
        return self.encrypt(text)

    def _rotate_char(self, char: str) -> str:
        code = ord(char)
        if not self.FIRST_CHAR <= code <= self.LAST_CHAR:
            return char

        position = code - self.FIRST_CHAR
        new_position = (position + self.SHIFT) % self.CHARS_COUNT
        return chr(self.FIRST_CHAR + new_position)
