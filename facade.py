from buffer import Buffer
from factory import CipherFactory
from file_handler import FileHandler
from text import Text


class CipherFacade:
    """Single entry point to file operations, buffer and encryption."""
    def __init__(self) -> None:
        self._buffer = Buffer()
        self._file_handler = FileHandler()

    def encrypt(self, text: str, rot_type: str) -> Text:
        """Encrypt the text, add result to buffer and return the Text object.

        Raises:
            ValueError: If the rot_type is unknown.
        """
        cipher = CipherFactory.create(rot_type)
        result = Text(cipher.encrypt(text), rot_type, "encrypted")
        self._buffer.add(result)
        return result

    def decrypt(self, text: str, rot_type: str) -> Text:
        """Decrypt the text, add result to buffer and return the Text object.

        Raises:
            ValueError: If the rot_type is unknown.
        """
        cipher = CipherFactory.create(rot_type)
        result = Text(cipher.decrypt(text), rot_type, "decrypted")
        self._buffer.add(result)
        return result

    def get_buffer(self) -> list[Text]:
        """Return a copy of all Text objects in the buffer."""
        return self._buffer.get_all()

    def save_buffer(self, file_name: str) -> None:
        """Append the buffer to a JSON file and clear the buffer.

        The buffer is cleared only after a successful write.

        Raises:
            json.JSONDecodeError: If the existing file is not valid JSON.
            PermissionError: If the file can't be accessed.
        """
        data = [item.to_dict() for item in self._buffer.get_all()]
        self._file_handler.write(file_name, data)
        self._buffer.clear()

    def load_file(self, file_name: str) -> list[Text]:
        """Load items from a JSON file into the buffer and return them.

        If any item is invalid, nothing is added to the buffer.

        Args:
            file_name: Name of the file to load.

        Returns:
            A list of Text objects loaded from the file.

        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file content is not valid JSON.
            TypeError: If an item in the file has missing, extra or
                misnamed keys.
            PermissionError: If the file can't be accessed.
        """
        data = self._file_handler.read(file_name)
        items = [Text.from_dict(item) for item in data]
        self._buffer.extend(items)
        return items
