class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self):
        return f'Имя: {self.name}nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __str__(self):
        avg_grade = sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values())
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade}'
    
    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __le__(self, other):
        return self.avg_grade() <= other.avg_grade()

    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()

    def __ge__(self, other):
        return self.avg_grade() >= other.avg_grade()

    def avg_grade(self):
        return sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values())

class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Student:
    def __init__(self, name, surname, courses_in_progress, finished_courses):
        self.name = name
        self.surname = surname
        self.courses_in_progress = courses_in_progress
        self.finished_courses = finished_courses
        self.grades = {}

    def __str__(self):
        avg_grade = sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values())
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}'

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade()

    def __le__(self, other):
        return self.avg_grade() <= other.avg_grade()

    def __gt__(self, other):
        return self.avg_grade() > other.avg_grade()

    def __ge__(self, other):
        return self.avg_grade() >= other.avg_grade()

    def avg_grade(self):
        return sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values())


# Создание экземпляров классов
lecturer1 = Lecturer("Иван", "Иванов")
lecturer2 = Lecturer("Петр", "Петров")

reviewer1 = Reviewer("Анна", "Сидорова")
reviewer2 = Reviewer("Мария", "Петрова")

student1 = Student("Алексей", "Смирнов", ["Python", "Git"], ["Введение в программирование"])
student2 = Student("Елена", "Иванова", ["Python", "SQL"], ["ООП в Python"])

# Оценки студентов
student1.grades = {'Python': [5, 4, 5], 'Git': [3, 4, 4]}
student2.grades = {'Python': [4, 5, 5], 'SQL': [4, 4, 5]}

# Оценки лекторов
lecturer1.grades = {'Python': [4, 5, 3]}
lecturer2.grades = {'Python': [5, 5, 5]}




# Вывод информации о созданных экземплярах
print("Информация о лекторах:")
print(lecturer1)
print(" ")
print(lecturer2)
print(" ")

print("Информация о рецензентах:")
print(reviewer1)
print("")
print(reviewer2)
print(" ")

print("Информация о студентах:")
print(student1)
print(" ")
print(student2)
print(" ")

# Функция для подсчета средней оценки за домашние задания по всем студентам 
def avg_hw_grade(students, course):
    total_sum = 0
    total_count = 0
    for student in students:
        if course in student.grades:
            total_sum += sum(student.grades[course])
            total_count += len(student.grades[course])
    return total_sum / total_count if total_count > 0 else 0

# Функция для подсчета средней оценки за лекции всех лекторов 
def avg_lecture_grade(lecturers, course):
    total_sum = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_sum += sum(lecturer.grades[course])
            total_count += len(lecturer.grades[course])
    return total_sum / total_count if total_count > 0 else 0

# Вызовем функции для подсчета средних оценок
avg_hw_grade([student1, student2], "Python")
avg_lecture_grade([lecturer1, lecturer2], "Python")