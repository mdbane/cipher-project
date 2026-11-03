import pytest

from text import Text


def test_to_dict() -> None:
    text = Text("Urryb", "rot13", "encrypted")
    assert text.to_dict() == {
        "text": "Urryb",
        "rot_type": "rot13",
        "status": "encrypted",
    }


def test_from_dict() -> None:
    data = {"text": "Urryb", "rot_type": "rot13", "status": "encrypted"}
    assert Text.from_dict(data) == Text("Urryb", "rot13", "encrypted")


def test_dict_round_trip() -> None:
    text = Text("Zażółć", "rot47", "decrypted")
    assert Text.from_dict(text.to_dict()) == text


@pytest.mark.parametrize('data', [
    {'text': 'a', 'rot_type': 'rot13'},
    {'text': 'a', 'rot_type': 'rot13', 'status': 'encrypted', 'extra': 'x'},
    {'tekst': 'a', 'rot_type': 'rot13', 'status': 'encrypted'},
], ids=['missing_key', 'extra_key', 'wrong_key'])
def test_from_dict_invalid_keys(data: dict[str, str]) -> None:
    with pytest.raises(TypeError):
        Text.from_dict(data)
