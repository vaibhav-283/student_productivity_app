from dataclasses import dataclass

@dataclass
class Attendance:
    id: int
    subject: str
    classes_attended: int
    total_classes: int
