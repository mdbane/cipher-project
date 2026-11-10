from cipher import Cipher, Rot13Cipher, Rot47Cipher


class CipherFactory:
    """Creates cipher objects by their name (rot_type)."""

    _ciphers: dict[str, type[Cipher]] = {
        "rot13": Rot13Cipher,
        "rot47": Rot47Cipher,
    }

    @classmethod
    def create(cls, rot_type: str) -> Cipher:
        """Return a new cipher object based on the provided rot_type.

        Args:
            rot_type: Cipher type, 'rot13' or 'rot47'.

        Returns:
            A new instance of the matching cipher class.

        Raises:
            ValueError: If the rot_type is unknown.
        """
        if rot_type not in cls._ciphers:
            raise ValueError(f"Unknown cipher type: {rot_type}")

        cipher_class = cls._ciphers[rot_type]
        return cipher_class()
