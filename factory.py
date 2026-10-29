from cipher import Cipher, Rot13Cipher, Rot47Cipher


class CipherFactory:
    _ciphers: dict[str, type[Cipher]] = {
        "rot13": Rot13Cipher,
        "rot47": Rot47Cipher
    }


    @classmethod
    def create_cipher(cls, rot_type: str) -> Cipher:
        if rot_type not in cls._ciphers:
            raise ValueError(f"Unknown cipher type: {rot_type}")

        cipher_class = cls._ciphers[rot_type]
        return cipher_class()
