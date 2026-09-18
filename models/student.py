from dataclasses import dataclass

@dataclass
class Student:
    id: int
    name: str
    course: str
    semester: str
    weekly_study_goal: int
