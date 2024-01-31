import uuid

from dataclasses import dataclass, asdict

@dataclass
class BasicData:
    code: uuid.UUID
    headers: list
    data: list

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return asdict(self)
