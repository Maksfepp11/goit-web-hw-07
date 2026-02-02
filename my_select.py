from sqlalchemy import func, desc
from db import session
from models import Student, Grade, Subject, Group, Teacher

def select_1():
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()

def select_2(subject_name):
    return session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).join(Subject).filter(Subject.name == subject_name)\
        .group_by(Student.id).order_by(desc('avg_grade')).first()

def select_3(subject_name):
    return session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .select_from(Grade).join(Student).join(Group).join(Subject).filter(Subject.name == subject_name)\
        .group_by(Group.id).all()

def select_4():
    return session.query(func.round(func.avg(Grade.grade), 2)).select_from(Grade).scalar()

def select_5(teacher_name):
    return session.query(Subject.name).join(Teacher).filter(Teacher.fullname == teacher_name).all()

def select_6(group_name):
    return session.query(Student.fullname).join(Group).filter(Group.name == group_name).all()

def select_7(group_name, subject_name):
    return session.query(Student.fullname, Grade.grade).join(Group).join(Grade).join(Subject)\
        .filter(Group.name == group_name, Subject.name == subject_name).all()

def select_8(teacher_name):
    return session.query(func.round(func.avg(Grade.grade), 2)).join(Subject).join(Teacher)\
        .filter(Teacher.fullname == teacher_name).scalar()

def select_9(student_name):
    return session.query(Subject.name).join(Grade).join(Student).filter(Student.fullname == student_name)\
        .group_by(Subject.id).all()

def select_10(student_name, teacher_name):
    return session.query(Subject.name).join(Grade).join(Student).join(Teacher, Subject.teacher_id == Teacher.id)\
        .filter(Student.fullname == student_name, Teacher.fullname == teacher_name)\
        .group_by(Subject.id).all()

if __name__ == "__main__":
    # Приклади виклику (імена вибираються з тих, що створив Faker)
    print("Запит 1:", select_1())
    print("Запит 4 (Середній балл):", select_4())