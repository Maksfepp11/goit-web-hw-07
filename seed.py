from faker import Faker
import random
from datetime import datetime
from db import session
from models import Group, Student, Teacher, Subject, Grade

fake = Faker()

def fill_data():
  
    groups = [Group(name=f"Group {name}") for name in ['A', 'B', 'C']]
    session.add_all(groups)
    

    teachers = [Teacher(fullname=fake.name()) for _ in range(5)]
    session.add_all(teachers)
    session.commit()


    subject_names = ['Math', 'Physics', 'History', 'Programming', 'English', 'Art', 'Biology', 'Chemistry']
    subjects = [Subject(name=name, teacher_id=random.choice(teachers).id) for name in subject_names]
    session.add_all(subjects)
    session.commit()

    students = [Student(fullname=fake.name(), group_id=random.choice(groups).id) for _ in range(40)]
    session.add_all(students)
    session.commit()

    for s in students:
        for _ in range(random.randint(10, 20)):
            grade = Grade(
                grade=random.randint(1, 12),
                date_received=fake.date_between(start_date='-1y', end_date='today'),
                student_id=s.id,
                subject_id=random.choice(subjects).id
            )
            session.add(grade)
    session.commit()

if __name__ == "__main__":
    fill_data()
    print("База даних успішно заповнена!")