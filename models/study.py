from dataclasses import dataclass
from typing import Optional

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
