import pytest

from cipher import Cipher, Rot13Cipher, Rot47Cipher


def test_rot13_encrypt() -> None:
    assert Rot13Cipher().encrypt("Hello, World!") == "Uryyb, Jbeyq!"


def test_rot13_keeps_non_latin_characters() -> None:
    assert Rot13Cipher().encrypt("Żółw 1234") == "Żółj 1234"


def test_rot47_encrypt() -> None:
    assert Rot47Cipher().encrypt("Hello, World!") == "w6==@[ (@C=5P"


@pytest.mark.parametrize('cipher', [Rot13Cipher(), Rot47Cipher()])
def test_decrypt_reverses_encrypt(cipher: Cipher) -> None:
    text = "Zażółć gęślą jaźń! 1234"
    assert cipher.decrypt(cipher.encrypt(text)) == text


def test_cipher_is_abstract() -> None:
    with pytest.raises(TypeError):
        Cipher()
