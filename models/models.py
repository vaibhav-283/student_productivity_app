from dataclasses import dataclass
from typing import Optional

@dataclass
class Student:
    id: int
    name: str
    course: str
    semester: str
    weekly_study_goal: int

@dataclass
class StudySession:
    id: int
    subject: str
    topic: str
    date: str
    start_time: Optional[str]
    end_time: Optional[str]
    duration_minutes: int
    notes: Optional[str]

@dataclass
class Task:
    id: int
    title: str
    subject: str
    description: str
    deadline: str
    priority: str
    status: str

@dataclass
class Attendance:
    id: int
    subject: str
    classes_attended: int
    total_classes: int

@dataclass
class Expense:
    id: int
    amount: float
    category: str
    date: str
    description: str

@dataclass
class Goal:
    id: int
    description: str
    target_value: float
    current_value: float
    type: str
    status: str

@dataclass
class Achievement:
    id: int
    title: str
    description: str
    unlocked_date: str
