import json
from pathlib import Path

import pytest

from file_handler import FileHandler

FIRST = {"text": "Uryyb", "rot_type": "rot13", "status": "encrypted"}
SECOND = {"text": "Hello", "rot_type": "rot47", "status": "decrypted"}


@pytest.fixture
def handler() -> FileHandler:
    return FileHandler()


def test_write_and_read(tmp_path: Path, handler: FileHandler) -> None:
    file_name = str(tmp_path / "data")
    handler.write(file_name, [FIRST])
    assert handler.read(file_name) == [FIRST]


def test_write_appends_to_existing_file(tmp_path: Path, handler: FileHandler) -> None:
    file_name = str(tmp_path / "data")
    handler.write(file_name, [FIRST])
    handler.write(file_name, [SECOND])
    assert handler.read(file_name) == [FIRST, SECOND]


def test_extension_is_added(tmp_path: Path, handler: FileHandler) -> None:
    handler.write(str(tmp_path / "data"), [FIRST])
    assert (tmp_path / "data.json").exists()


def test_extension_is_not_doubled(tmp_path: Path, handler: FileHandler) -> None:
    handler.write(str(tmp_path / "data.json"), [FIRST])
    assert (tmp_path / "data.json").exists()
    assert not (tmp_path / "data.json.json").exists()


def test_write_does_not_modify_passed_data(tmp_path: Path, handler: FileHandler) -> None:
    data = [FIRST]
    handler.write(str(tmp_path / "data"), data)
    handler.write(str(tmp_path / "data"), data)
    assert data == [FIRST]


def test_polish_characters_are_saved_as_is(tmp_path: Path, handler: FileHandler) -> None:
    item = {"text": "Zażółć gęślą jaźń", "rot_type": "rot13",
            "status": "decrypted"}
    handler.write(str(tmp_path / "data"), [item])
    content = (tmp_path / "data.json").read_text(encoding="utf-8")
    assert "Zażółć gęślą jaźń" in content
    assert handler.read(str(tmp_path / "data")) == [item]


def test_read_missing_file_raises_error(tmp_path: Path, handler: FileHandler) -> None:
    with pytest.raises(FileNotFoundError):
        handler.read(str(tmp_path / "missing"))


def test_read_invalid_json_raises_error(tmp_path: Path, handler: FileHandler) -> None:
    (tmp_path / "broken.json").write_text("not a json", encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        handler.read(str(tmp_path / "broken"))


def test_write_to_invalid_json_keeps_file_unchanged(tmp_path: Path, handler: FileHandler) -> None:
    path = tmp_path / "broken.json"
    path.write_text("not json", encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        handler.write(str(path), [FIRST])
    assert path.read_text(encoding="utf-8") == "not json"
