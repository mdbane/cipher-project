# Cipher

Console application for encrypting and decrypting text with ROT13 and ROT47.
Results are kept in an in-memory buffer and can be saved to / loaded from JSON files.

## Features
- ROT13 and ROT47 encryption and decryption
- In-memory buffer of results
- Saving the buffer to a JSON file (appends to an existing file)
- Loading texts from a JSON file into the buffer

## Requirements
- Python 3.10+

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/mdbane/cipher-project.git
   cd cipher-project
   ```
2. Create a virtual environment:
   - Windows: `python -m venv .venv`
   - Linux / macOS: `python3 -m venv .venv`
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - Linux / macOS: `source .venv/bin/activate`
4. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

The application uses only the Python standard library.
`requirements.txt` contains pytest, which is needed to run the tests.

## Usage
```
python main.py
```

## Tests
```
python -m pytest -v
```

## Project structure
- `main.py`: entry point
- `manager.py`: console menu (the only module that talks to the user)
- `facade.py`: single interface to the application logic
- `factory.py`: creates cipher objects by name
- `cipher.py`: `Cipher` base class, ROT13, ROT47
- `buffer.py`: in-memory list of `Text` objects
- `file_handler.py`: reading and writing JSON files
- `text.py`: `Text` dataclass
- `tests/`: unit tests (pytest)

## Design patterns
- **Facade**: `CipherFacade` hides the cipher, buffer and file logic behind
  one simple interface used by the `Manager`.
- **Factory** (simple factory): `CipherFactory` creates the right cipher
  from its name, so no `if/elif` chain is needed.
- **Strategy**: `Rot13Cipher` and `Rot47Cipher` implement the common
  `Cipher` interface, so they can be used interchangeably.

Menu options in `Manager` are dispatched with a dict (option -> method)
instead of an `if/elif` chain.

## File format
```json
[
    {"text": "Uryyb", "rot_type": "rot13", "status": "encrypted"}
]
```
