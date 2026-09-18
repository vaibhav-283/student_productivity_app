import os

base_dir = r'C:\Users\User\.gemini\antigravity\scratch\student_productivity_dashboard'

def make_file(path, content=''):
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')

make_file('models/__init__.py')
make_file('models/student.py', 'from dataclasses import dataclass\n\n@dataclass\nclass Student:\n    id: int\n    name: str\n    course: str\n    semester: str\n    weekly_study_goal: int')
make_file('models/task.py', 'from dataclasses import dataclass\n\n@dataclass\nclass Task:\n    id: int\n    title: str\n    subject: str\n    description: str\n    deadline: str\n    priority: str\n    status: str')
make_file('models/study.py', 'from dataclasses import dataclass\nfrom typing import Optional\n\n@dataclass\nclass StudySession:\n    id: int\n    subject: str\n    topic: str\n    date: str\n    start_time: Optional[str]\n    end_time: Optional[str]\n    duration_minutes: int\n    notes: Optional[str]')
make_file('models/attendance.py', 'from dataclasses import dataclass\n\n@dataclass\nclass Attendance:\n    id: int\n    subject: str\n    classes_attended: int\n    total_classes: int')
make_file('models/expense.py', 'from dataclasses import dataclass\n\n@dataclass\nclass Expense:\n    id: int\n    amount: float\n    category: str\n    date: str\n    description: str')
make_file('models/goal.py', 'from dataclasses import dataclass\n\n@dataclass\nclass Goal:\n    id: int\n    description: str\n    target_value: float\n    current_value: float\n    type: str\n    status: str')

make_file('services/__init__.py')
make_file('services/productivity.py')
make_file('services/recommendations.py')
make_file('services/achievements.py')

make_file('ui/__init__.py')
make_file('ui/dashboard.py')
make_file('ui/study_tracker.py')
make_file('ui/task_manager.py')
make_file('ui/attendance.py')
make_file('ui/expenses.py')
make_file('ui/analytics.py')
make_file('ui/settings.py')

make_file('charts/__init__.py')
make_file('charts/charts.py')

print('Files created successfully.')
