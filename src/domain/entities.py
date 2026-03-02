from dataclasses import dataclass


@dataclass
class JobRecord:
    experience: int
    city: str
    position: str
    skills: str
    salary: float