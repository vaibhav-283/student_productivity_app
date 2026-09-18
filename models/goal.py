from dataclasses import dataclass

@dataclass
class Goal:
    id: int
    description: str
    target_value: float
    current_value: float
    type: str
    status: str
