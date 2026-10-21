class Student:
    def __init__(self, name, grades=None):
        self.grades = grades if grades is not None else []
        self.name = name

    def add_grade(self, grade=None):
        if grade is None:
            grade = int(input("Введите оценку для добавления (от 1 до 5): "))
            if 0 < grade <= 5:
                self.grades.append(grade)
                print(f"Студенту под именем {self.name} добавлена оценка: {grade}")
            else:
                print("Вы ввели значение вне оценочных рамок (от 1 до 5)")
                return

    def average(self):
        if not self.grades:
            print("У студента еще нет оценок для вычисления среднего балла")
            return 0.0
        else:
            middle_grade = sum(self.grades) / len(self.grades)
            print(f"Средний балл студента: {middle_grade:.2f}")
            return middle_grade

    def display_info(self):
        print(f"Имя студента: {self.name}")
        if not self.grades:
            print("У студента еще нет оценок для вычисления среднего балла")
        Student.average(self)

class Group:
    def __init__(self, title):
        self.title = title
        self.list_students = []

    def add_student(self, student=None):
        if student is None:
            student_name = input("Введите имя студента: ")
            student = Student(student_name, [])
        self.list_students.append(student)
        print(f"Студент {student.name} добавлен в группу {self.title}")


    def best_student(self):
        if not self.list_students:
            print("В группе нет студентов")
            return None

        best_student = None
        best_average = -1

        for student in self.list_students:
            if student.grades:
                average = sum(student.grades) / len(student.grades)
                if average > best_average:
                    best_average = average
                    best_student = student

        if best_student:
            print(f"Лучший студент: {best_student.name} со средним баллом {best_average:.2f}")
            return best_student
        else:
            print("Ни у одного студента нет оценок")
            return None


    def quantity(self):
        print(f"Количество студентов в группе {self.title}: {len(self.list_students)}")