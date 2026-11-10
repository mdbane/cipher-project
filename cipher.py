from abc import ABC, abstractmethod


class Cipher(ABC):
    """Base class for all ciphers.

    Subclasses must implement the encrypt and decrypt methods.
    """

    @abstractmethod
    def encrypt(self, text: str) -> str:
        """Return the encrypted version of the input text."""

    @abstractmethod
    def decrypt(self, text: str) -> str:
        """Return the decrypted version of the input text."""


class Rot13Cipher(Cipher):
    """ROT13 cipher: shifts Latin letters by 13 positions in the alphabet.

    Other characters stay unchanged.
    """

    SHIFT = 13
    ALPHABET_SIZE = 26

    def encrypt(self, text: str) -> str:
        """Shift each Latin letter by 13 positions, preserving case."""
        return ''.join(self._rotate_char(char) for char in text)

    def decrypt(self, text: str) -> str:
        """Decrypt the text (ROT13 is its own inverse)."""
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
    """ROT47 cipher: shifts printable ASCII characters (33-126) by 47.

    Other characters stay unchanged.
    """

    FIRST_CHAR = 33
    LAST_CHAR = 126
    CHARS_COUNT = LAST_CHAR - FIRST_CHAR + 1
    SHIFT = 47

    def encrypt(self, text: str) -> str:
        """Shift each printable ASCII character by 47 positions."""
        return ''.join(self._rotate_char(char) for char in text)

    def decrypt(self, text: str) -> str:
        """Decrypt the text (ROT47 is its own inverse)."""
        return self.encrypt(text)

    def _rotate_char(self, char: str) -> str:
        code = ord(char)
        if not self.FIRST_CHAR <= code <= self.LAST_CHAR:
            return char

        position = code - self.FIRST_CHAR
        new_position = (position + self.SHIFT) % self.CHARS_COUNT
        return chr(self.FIRST_CHAR + new_position)
