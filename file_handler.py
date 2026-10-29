import json


class FileHandler:
    EXTENSION = ".json"

    def read(self, file_name: str) -> list[dict[str, str]]:
        path = self._with_extension(file_name)
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    def write(self, file_name: str, data: list[dict[str, str]]) -> None:
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
