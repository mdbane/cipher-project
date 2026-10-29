from buffer import Buffer
from factory import CipherFactory
from file_handler import FileHandler
from text import Text


class CipherFacade:
    def __init__(self) -> None:
        self._buffer = Buffer()
        self._file_handler = FileHandler()

    def encrypt(self, text: str, rot_type: str) -> Text:
        cipher = CipherFactory.create(rot_type)
        result = Text(cipher.encrypt(text), rot_type, "encrypted")
        self._buffer.add(result)
        return result

    def decrypt(self, text: str, rot_type: str) -> Text:
        cipher = CipherFactory.create(rot_type)
        result = Text(cipher.decrypt(text), rot_type, "decrypted")
        self._buffer.add(result)
        return result

    def get_buffer(self) -> list[Text]:
        return self._buffer.get_all()
