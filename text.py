from dataclasses import dataclass, asdict


@dataclass
class Text:
    """A piece of text with its encryption type and status."""
    text: str
    rot_type: str
    status: str

    def to_dict(self) -> dict[str, str]:
        """Return the object as a dict, ready to be saved to JSON."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> 'Text':
        """Create a Text object from a dict loaded from JSON.

        Raises:
            TypeError: The dict has missing, extra or misnamed keys.
        """
        return cls(**data)
