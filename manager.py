import json
from collections.abc import Callable

from facade import CipherFacade


class Manager:
    def __init__(self) -> None:
        self._facade = CipherFacade()
        self._running = True
        self._actions: dict[str, Callable[[], None]] = {
            "1": self._encrypt,
            "2": self._decrypt,
            "3": self._show_buffer,
            "4": self._save_to_file,
            "5": self._load_from_file,
            "0": self._exit,
        }

    def run(self) -> None:
        while self._running:
            self._show_menu()
            choice = input("Choose an option: ").strip()
            action = self._actions.get(choice, self._invalid_option)
            action()

    def _show_menu(self) -> None:
        print("\nMenu:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Show buffer")
        print("4. Save buffer to file")
        print("5. Load from file")
        print("0. Exit")

    def _ask_text_and_type(self) -> tuple[str, str]:
        text = input("Text: ")
        rot_type = input("Cipher type (rot13/rot47): ").strip().lower()
        return text, rot_type

    def _encrypt(self) -> None:
        text, rot_type = self._ask_text_and_type()
        try:
            result = self._facade.encrypt(text, rot_type)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            print(f"Encrypted: {result.text}")

    def _decrypt(self) -> None:
        text, rot_type = self._ask_text_and_type()
        try:
            result = self._facade.decrypt(text, rot_type)
        except ValueError as error:
            print(f"Error: {error}")
        else:
            print(f"Decrypted: {result.text}")

    def _show_buffer(self) -> None:
        items = self._facade.get_buffer()
        if not items:
            print("Buffer is empty.")
            return

        for number, item in enumerate(items, start=1):
            print(f"{number}. [{item.rot_type}, {item.status}] {item.text}")

    def _save_to_file(self) -> None:
        if not self._facade.get_buffer():
            print("Buffer is empty. Nothing to save.")
            return

        file_name = input("File name: ").strip()
        if not file_name:
            print("File name cannot be empty.")
            return

        try:
            self._facade.save_buffer(file_name)
        except json.JSONDecodeError:
            print("Error: the file exists but is not a valid JSON file.")
        except PermissionError:
            print("Error: no permission to write to this file.")
        else:
            print(f"Buffer saved to file: {file_name}")

    def _load_from_file(self) -> None:
        file_name = input("File name: ").strip()
        if not file_name:
            print("File name cannot be empty.")
            return

        try:
            items = self._facade.load_file(file_name)
        except FileNotFoundError:
            print(f"Error: file '{file_name}' not found.")
        except PermissionError:
            print(f"Error: no permission to read file '{file_name}'.")
        except json.JSONDecodeError:
            print(f"Error: file '{file_name}' is not a valid JSON file.")
        else:
            print(f"Loaded {len(items)} items from file: {file_name}")

    def _exit(self) -> None:
        self._running = False
        print("Exiting the program. Goodbye!")

    def _invalid_option(self) -> None:
        print("Invalid option. Please try again.")
