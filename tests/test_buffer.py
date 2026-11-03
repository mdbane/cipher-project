import pytest

from buffer import Buffer
from text import Text

ENCRYPTED = Text("Urryb", "rot13", "encrypted")
DECRYPTED = Text("Hello", "rot13", "decrypted")
LOADED = Text('w6==@', 'rot47', 'encrypted')


@pytest.fixture
def buffer() -> Buffer:
    return Buffer()


def test_new_buffer_is_empty(buffer: Buffer) -> None:
    assert buffer.is_empty()
    assert buffer.get_all() == []


def test_add(buffer: Buffer) -> None:
    buffer.add(ENCRYPTED)
    assert not buffer.is_empty()
    assert buffer.get_all() == [ENCRYPTED]


def test_extend_keeps_order(buffer: Buffer) -> None:
    buffer.add(ENCRYPTED)
    buffer.extend([DECRYPTED, LOADED])
    assert buffer.get_all() == [ENCRYPTED, DECRYPTED, LOADED]


def test_extend_with_empty_list(buffer: Buffer) -> None:
    buffer.add(ENCRYPTED)
    buffer.extend([])
    assert buffer.get_all() == [ENCRYPTED]


def test_get_all_returns_copy(buffer: Buffer) -> None:
    buffer.add(ENCRYPTED)
    items = buffer.get_all()
    items.append(DECRYPTED)
    assert buffer.get_all() == [ENCRYPTED]


def test_clear(buffer: Buffer) -> None:
    buffer.extend([ENCRYPTED, DECRYPTED])
    buffer.clear()
    assert buffer.is_empty()


def test_buffers_do_not_share_items() -> None:
    first = Buffer()
    second = Buffer()
    first.add(ENCRYPTED)
    assert second.is_empty()
