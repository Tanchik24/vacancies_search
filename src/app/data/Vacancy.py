from dataclasses import dataclass


@dataclass
class Vacancy:
    name: str
    city: str
    salary: int
    description: str
