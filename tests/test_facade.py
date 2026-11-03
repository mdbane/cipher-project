import json
from pathlib import Path

import pytest

from facade import CipherFacade
from text import Text


@pytest.fixture
def facade() -> CipherFacade:
    return CipherFacade()


def test_encrypt(facade: CipherFacade) -> None:
    result = facade.encrypt('Hello', 'rot13')
    assert result == Text('Uryyb', 'rot13', 'encrypted')


def test_decrypt(facade: CipherFacade) -> None:
    result = facade.decrypt('w6==@', 'rot47')
    assert result == Text('Hello', 'rot47', 'decrypted')


def test_results_are_added_to_buffer(facade: CipherFacade) -> None:
    encrypted = facade.encrypt('Hello', 'rot13')
    decrypted = facade.decrypt('w6==@', 'rot47')
    assert facade.get_buffer() == [encrypted, decrypted]


def test_unknown_type_does_not_change_buffer(facade: CipherFacade) -> None:
    with pytest.raises(ValueError):
        facade.encrypt('Hello', 'rot5')
    assert facade.get_buffer() == []


def test_save_buffer_clears_buffer(tmp_path: Path, facade: CipherFacade) -> None:
    facade.encrypt('Hello', 'rot13')
    facade.save_buffer(str(tmp_path / 'data'))
    assert facade.get_buffer() == []


def test_save_and_load(tmp_path: Path, facade: CipherFacade) -> None:
    file_name = str(tmp_path / 'data')
    encrypted = facade.encrypt('Hello', 'rot13')
    decrypted = facade.decrypt('w6==@', 'rot47')
    facade.save_buffer(file_name)

    loaded = facade.load_file(file_name)

    assert loaded == [encrypted, decrypted]
    assert facade.get_buffer() == [encrypted, decrypted]


def test_saving_twice_does_not_duplicate(tmp_path: Path, facade: CipherFacade) -> None:
    file_name = str(tmp_path / 'data')
    first = facade.encrypt('Hello', 'rot13')
    facade.save_buffer(file_name)
    second = facade.encrypt('World', 'rot47')
    facade.save_buffer(file_name)

    assert facade.load_file(file_name) == [first, second]


def test_failed_save_keeps_buffer(tmp_path: Path, facade: CipherFacade) -> None:
    path = tmp_path / 'broken.json'
    path.write_text('not json', encoding='utf-8')
    encrypted = facade.encrypt('Hello', 'rot13')

    with pytest.raises(json.JSONDecodeError):
        facade.save_buffer(str(path))

    assert facade.get_buffer() == [encrypted]


def test_load_missing_file_raises_error(tmp_path: Path, facade: CipherFacade) -> None:
    with pytest.raises(FileNotFoundError):
        facade.load_file(str(tmp_path / 'missing'))


def test_load_invalid_item_does_not_change_buffer(tmp_path: Path, facade: CipherFacade) -> None:
    data = [
        {'text': 'Uryyb', 'rot_type': 'rot13', 'status': 'encrypted'},
        {'tekst': 'Hello'},
    ]
    (tmp_path / 'bad.json').write_text(json.dumps(data), encoding='utf-8')

    with pytest.raises(TypeError):
        facade.load_file(str(tmp_path / 'bad'))

    assert facade.get_buffer() == []
