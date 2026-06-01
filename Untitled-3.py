class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = self.get_avg_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за домашние задания: {avg_grade}\n'
               f'Курсы в процессе изучения: {courses_in_progress_str}\n'
               f'Завершенные курсы: {finished_courses_str}')
        return res

    def get_avg_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if len(all_grades) == 0:
            return 0
        return round(sum(all_grades) / len(all_grades), 1)

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
            return
        return self.get_avg_grade() < other.get_avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Словарь для оценок от студентов

    def __str__(self):
        avg_grade = self.get_avg_grade()
        res = (f'Имя: {self.name}\n'
               f'Фамилия: {self.surname}\n'
               f'Средняя оценка за лекции: {avg_grade}')
        return res

    def get_avg_grade(self):
        all_grades = []
        for grades_list in self.grades.values():
            all_grades.extend(grades_list)
        if len(all_grades) == 0:
            return 0
        return round(sum(all_grades) / len(all_grades), 1)

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        return self.get_avg_grade() < other.get_avg_grade()


class Reviewer(Mentor):
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res



student_1 = Student('Алехина', 'Ольга', 'Ж')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Git']

student_2 = Student('Алексей', 'Алексеев', 'М')
student_2.courses_in_progress += ['Python', 'Java']
student_2.finished_courses += ['C++']

lecturer_1 = Lecturer('Иван', 'Иванов', 'М')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Анна', 'Аннова', 'Ж')
lecturer_2.courses_attached += ['Python', 'Java']

reviewer_1 = Reviewer('Пётр', 'Петров', 'М')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Василий', 'Васильев', 'М')
reviewer_2.courses_attached += ['Python', 'Java']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 8)

reviewer_2.rate_hw(student_2, 'Java', 7)

student_1.rate_lecture(lecturer_1, 'Python', 10)
student_1.rate_lecture(lecturer_1, 'Python', 9)

student_2.rate_lecture(lecturer_2, 'Python', 8)
student_2.rate_lecture(lecturer_2, 'Java', 9)


def avg_student_grade(students_list, course_name):
    total_sum = 0
    count = 0
    for student in students_list:
        if course_name in student.grades:
            total_sum += sum(student.grades[course_name])
            count += len(student.grades[course_name])
    if count == 0:
        return 0
    return round(total_sum / count, 1)

def avg_lecturer_grade(lecturers_list, course_name):
    total_sum = 0
    count = 0
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            total_sum += sum(lecturer.grades[course_name])
            count += len(lecturer.grades[course_name])
    if count == 0:
        return 0
    return round(total_sum / count, 1)


print("Проверка методов __str__:")
print(reviewer_1)
print("-" * 20)
print(lecturer_1)
print("-" * 20)
print(student_1)

print("\nСравнение студентов и лекторов:")
print(f"{student_1.name} лучше {student_2.name}? {student_1 > student_2}")
print(f"{lecturer_1.name} лучше {lecturer_2.name}? {lecturer_1 > lecturer_2}")

print("\nСредние оценки по курсам:")
students_list = [student_1, student_2]
lecturers_list = [lecturer_1, lecturer_2]

print(f"Средняя оценка всех студентов по курсу Python: {avg_student_grade(students_list, 'Python')}")
print(f"Средняя оценка всех лекторов по курсу Python: {avg_lecturer_grade(lecturers_list, 'Python')}")