# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 20:38:29 2022

@author: LocalAdmin
"""

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecture(self, lecturer, course, grade):
        
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __lt__(self, student):
        
        if isinstance(student, Student):
            if self.medle_rate() < student.medle_rate():
                return True
            else:
                return False
        else:
            return 'Ошибка'
    
    def __rt__(self, student):
        
        if isinstance(student, Student):
            if self.medle_rate() > student.medle_rate():
                return True
            else:
                return False
        else:
            return 'Ошибка'
            
    def __eq__(self, student):
        
        if isinstance(student, Student):
            if self.medle_rate() == student.medle_rate():
                return True
            else:
                return False
        else:
            return 'Ошибка'
        
    def medle_rate(self):
        
        self.medle_gr = 0
        if self.grades != {}:
            for i in self.grades.values():
                self.medle_gr += sum(i)/len(list(i))
            self.medle_gr /= len(self.grades) 
            
        return self.medle_gr
            
    def __str__(self):
        
        self.medle_rate()
        return f'''Имя: {self.name}\nФамилия: {self.surname}
Средняя оценка за домашние задания: {self.medle_gr}
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}
Завершенные курсы: {", ".join(self.finished_courses)}''' 
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self):
        
        return f'Имя: {self.name}\n' f'Фамилия: {self.surname}'
        
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        
    def medle_rate(self):
        
        self.medle_gr = 0
        if self.grades != {}:
            for i in self.grades.values():
                self.medle_gr += sum(i)/len(list(i))
            self.medle_gr /= len(self.grades) 
            
        return self.medle_gr
    
    def __lt__(self, lecturer):
        
        if isinstance(lecturer, Lecturer):
            if self.medle_rate() < lecturer.medle_rate():
                return True
            else:
                return False
        else:
            return 'Ошибка'
    
    def __rt__(self, lecturer):
        
        if isinstance(lecturer, Lecturer):
            if self.medle_rate() > lecturer.medle_rate():
                return True
            else:
                return False
        else:
            return 'Ошибка'
            
    def __eq__(self, lecturer):
        
        if isinstance(lecturer, Lecturer):
            if self.medle_rate() == lecturer.medle_rate():
                return True
            else:
                return False
        else:
            return 'Ошибка'
            
    def __str__(self):
        
        self.medle_rate()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.medle_gr}' 
        
        
class Rewiewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
def medle_rate_stud(students, course):
    
    sum_rate = 0
    for i in students:
        for cour, grade in i.grades.items():
            if course == cour:
                sum_rate += sum(grade)/len(grade)
    
    return sum_rate/len(students)

def medle_rate_lect(lecturers, course):
    
    sum_rate = 0
    for i in lecturers:
        for cour, grade in i.grades.items():
            if course == cour:
                sum_rate += sum(grade)/len(grade)
    
    return sum_rate/len(lecturers)
                     
 
student1 = Student('Николай', 'Сидоров', 'male')
student2 = Student('Анастасия', 'Александрова', 'female')

students_list = [student1, student2]


lecturer1 = Lecturer('Петр', 'Васильев')
lecturer2 = Lecturer('Сергей', 'Иванов')

lecturers_list = [lecturer1, lecturer2]

rewiewer1 = Rewiewer('Юрий', 'Петров')
rewiewer2 = Rewiewer('Дмитрий', 'Гордеев')


student1.courses_in_progress += ['Python', 'Git']
student2.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Git', 'C++']
student2.finished_courses += ['Git', 'C++', 'Java']

lecturer1.courses_attached += ['Python', 'Git', 'CSS', 'Java']
lecturer2.courses_attached += ['Python', 'Git', 'CSS', 'Java']
rewiewer1.courses_attached += ['Python', 'Git', 'CSS', 'Java']
rewiewer2.courses_attached += ['Python', 'Git', 'CSS', 'Java']

rewiewer1.rate_hw(student1, 'Python', 9.5)
rewiewer1.rate_hw(student1, 'Git', 10)
rewiewer1.rate_hw(student2, 'Python', 9.1)
rewiewer1.rate_hw(student2, 'Git', 9.5)
rewiewer2.rate_hw(student1, 'Python', 9.7)
rewiewer2.rate_hw(student1, 'Git', 10)
rewiewer2.rate_hw(student2, 'Python', 9.6)
rewiewer2.rate_hw(student2, 'Git', 10)

student1.rate_lecture(lecturer1, 'Python', 9.9)
student1.rate_lecture(lecturer2, 'Python', 9)
student1.rate_lecture(lecturer1, 'Git', 8)
student1.rate_lecture(lecturer2, 'Git', 8.5)
student2.rate_lecture(lecturer1, 'Python', 10)
student2.rate_lecture(lecturer2, 'Python', 8.5)
student2.rate_lecture(lecturer1, 'Git', 8.8)
student2.rate_lecture(lecturer2, 'Git', 9)

print(student1, student2, lecturer1, lecturer2, rewiewer1, rewiewer2, sep=2*'\n' )
print()
print(lecturer1 < lecturer2)
print(student1 > student2)
print()
subject = 'Python'
print(f'Средняя оценка за ДЗ по {subject} у студентов: {medle_rate_stud(students_list, subject)}')
print(f'Средняя оценка за лекции по {subject} у преподавателей: {medle_rate_lect(lecturers_list, subject)}')
