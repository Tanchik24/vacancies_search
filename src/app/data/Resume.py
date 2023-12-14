from dataclasses import dataclass


@dataclass
class Resume:
    name: str
    surname: str
    city: str
    experience: int
    desired_salary: int
    description: str
