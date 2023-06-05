from dataclasses import dataclass


@dataclass(frozen=True)
class Project:
    uuid: str
    name: str
