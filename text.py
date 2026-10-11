from dataclasses import dataclass, asdict


@dataclass
class Text:
    text: str
    rot_type: str
    status: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> 'Text':
        return cls(**data)