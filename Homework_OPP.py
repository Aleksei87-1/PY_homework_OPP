class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}

    def rate_hw(self, reviewer, course, grade):
        pass

    def rate_lecture(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and 
            course in lecturer.courses_attached and 
            course in self.courses_in_progress and 
            1 <= grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg_hw = round(sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values()), 1) if self.grades else 0
        courses_in_progress_str = ", ".join(self.courses_in_progress) if self.courses_in_progress else "Нет текущих курсов"
        finished_courses_str = ", ".join(self.finished_courses) if self.finished_courses else "Нет завершенных курсов"
        
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {avg_hw}\n'
                f'Курсы в процессе изучения: {courses_in_progress_str}\n'
                f'Завершенные курсы: {finished_courses_str}')

    def __lt__(self, other):
        if not isinstance(other, Student):
            return False
        avg_self = sum(sum(self.grades.values())) / sum(len(g) for g in self.grades.values()) if self.grades else 0
        avg_other = sum(sum(other.grades.values())) / sum(len(g) for g in other.grades.values()) if other.grades else 0
        return avg_self < avg_other


class Lecturer(Student):
    def __init__(self, name, surname):
        super().__init__(name, surname, "Не указано")
        self.courses_attached = []

    def __str__(self):
        avg_lecture = round(sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values()), 1) if self.grades else 0
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_lecture}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return False
        avg_self = sum(sum(self.grades.values())) / sum(len(g) for g in self.grades.values()) if self.grades else 0
        avg_other = sum(sum(other.grades.values())) / sum(len(g) for g in other.grades.values()) if other.grades else 0
        return avg_self < avg_other


class Reviewer(Student):
    def __init__(self, name, surname):
        super().__init__(name, surname, "Не указано")
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and 
            course in self.courses_attached and 
            course in student.courses_in_progress and 
            1 <= grade <= 10):
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

def get_average_hw_grade(students_list, course_name):
    """Подсчет средней оценки за домашние задания по всем студентам в рамках курса."""
    all_grades = []
    for student in students_list:
        if course_name in student.grades:
            all_grades.extend(student.grades[course_name])
    return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0


def get_average_lecture_grade(lecturers_list, course_name):
    """Подсчет средней оценки за лекции всех лекторов в рамках курса."""
    all_grades = []
    for lecturer in lecturers_list:
        if course_name in lecturer.grades:
            all_grades.extend(lecturer.grades[course_name])
    return round(sum(all_grades) / len(all_grades), 1) if all_grades else 0


student1 = Student("Алехина", "Ольга", "Ж")
student2 = Student("Иван", "Петров", "М")

lecturer1 = Lecturer("Иван", "Иванов")
lecturer2 = Lecturer("Василиса", "Васильева")

reviewer1 = Reviewer("Пётр", "Петров")
reviewer2 = Reviewer("Елена", "Еленова")

student1.courses_in_progress = ['Python', 'Java']
student2.courses_in_progress = ['Python', 'C++']

lecturer1.courses_attached = ['Python', 'Java']
lecturer2.courses_attached = ['Python', 'C++']

reviewer1.courses_attached = ['Python', 'Java']
reviewer2.courses_attached = ['Python', 'C++']

reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 10)

student1.rate_lecture(lecturer1, 'Python', 8)
student1.rate_lecture(lecturer1, 'Python', 9)
student2.rate_lecture(lecturer2, 'Python', 7)
student2.rate_lecture(lecturer2, 'Python', 8)

print("=== ИНФОРМАЦИЯ О УЧАСТНИКАХ ===")
print(student1)
print("\n---")
print(student2)
print("\n---")
print(lecturer1)
print("\n---")
print(lecturer2)
print("\n---")
print(reviewer1)
print("\n---")
print(reviewer2)

students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]
course = 'Python'

avg_hw = get_average_hw_grade(students_list, course)
avg_lecture = get_average_lecture_grade(lecturers_list, course)

print(f"\n=== РЕЗУЛЬТАТЫ ПО КУРСУ '{course}' ===")
print(f"Средняя оценка за домашние задания (по всем студентам): {avg_hw}")
print(f"Средняя оценка за лекции (по всем лекторам): {avg_lecture}")
