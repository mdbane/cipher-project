import pytest

from cipher import Cipher, Rot13Cipher, Rot47Cipher
from factory import CipherFactory


@pytest.mark.parametrize("rot_type, expected_class", [
    ("rot13", Rot13Cipher),
    ("rot47", Rot47Cipher),
])
def test_create_returns_correct_cipher(
    rot_type: str, expected_class: type[Cipher]
) -> None:
    assert isinstance(CipherFactory.create(rot_type), expected_class)


@pytest.mark.parametrize("rot_type", ["rot 5", "ROT13", ""])
def test_create_unknown_rot_type_raises_value_error(rot_type: str) -> None:
    with pytest.raises(ValueError, match="Unknown cipher type"):
        CipherFactory.create(rot_type)


def test_create_returns_new_object_each_time() -> None:
    first = CipherFactory.create("rot13")
    second = CipherFactory.create("rot13")
    assert first is not second
