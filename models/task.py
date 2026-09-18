from dataclasses import dataclass

@dataclass
class Task:
    id: int
    title: str
    subject: str
    description: str
    deadline: str
    priority: str
    status: str
