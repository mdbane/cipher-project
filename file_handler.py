import json


class FileHandler:
    """Reads and writes lists of dicts to JSON files."""

    EXTENSION = ".json"

    def read(self, file_name: str) -> list[dict[str, str]]:
        """Read a JSON file and return its content as a list of dicts.

        Args:
            file_name: File name, with or without the .json extension.

        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file content is not valid JSON.
            PermissionError: If the file can't be accessed.
        """
        path = self._with_extension(file_name)
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def write(self, file_name: str, data: list[dict[str, str]]) -> None:
        """Append dicts to a JSON file, creating it if it doesn't exist.

        Args:
            file_name: File name, with or without the .json extension.
            data: List of dicts to append to the file.

        Raises:
            PermissionError: If the file can't be accessed.
            json.JSONDecodeError: If the existing file is not valid JSON.
        """
        path = self._with_extension(file_name)
        try:
            existing = self.read(path)
        except FileNotFoundError:
            existing = []

        existing.extend(data)

        with open(path, "w", encoding="utf-8") as file:
            json.dump(existing, file, indent=4, ensure_ascii=False)

    def _with_extension(self, file_name: str) -> str:
        if file_name.endswith(self.EXTENSION):
            return file_name
        return file_name + self.EXTENSION
