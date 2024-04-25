# Домашнее задание к лекции «Объекты и классы. Инкапсуляция, наследование и полиморфизм»
# ​Привет! Домашняя работа по данной теме является продолжением квиза к предыдущей лекции. Мы продолжим реализовывать логику функционала учебной группы в парадигме ООП. Удачи!
#
# Задание № 1. Наследование
# Исходя из квиза к предыдущему занятию, у нас уже есть класс преподавателей и класс студентов (вы можете взять этот код за основу
# или написать свой).
# Студентов пока оставим без изменения, а вот преподаватели бывают разные, поэтому теперь класс Mentor
# должен стать родительским классом,
# а от него нужно реализовать наследование классов Lecturer (лекторы) и Reviewer (эксперты, проверяющие домашние задания).
# Очевидно, имя, фамилия и список закрепленных курсов логично реализовать на уровне родительского класса.
# А чем же будут специфичны дочерние классы? Об этом в следующих заданиях.
#
# Задание № 2. Атрибуты и взаимодействие классов.
# В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания.
# Теперь это могут делать только Reviewer (реализуйте такой метод)!
# А что могут делать лекторы? Получать оценки за лекции от студентов :)
# Реализуйте метод выставления оценок лекторам у класса Student (оценки по 10-балльной шкале, хранятся в атрибуте-словаре у Lecturer,
# в котором ключи – названия курсов, а значения – списки оценок). Лектор при этом должен быть закреплен за тем курсом, на который записан студент.
#
# Задание № 3. Полиморфизм и магические методы
# Перегрузите магический метод __str__ у всех классов.
# У проверяющих он должен выводить информацию в следующем виде:
#
# print(some_reviewer)
# Имя: Some
# Фамилия: Buddy
# У лекторов:
#
# print(some_lecturer)
# Имя: Some
# Фамилия: Buddy
# Средняя оценка за лекции: 9.9
# А у студентов так:
#
# print(some_student)
# Имя: Ruoy
# Фамилия: Eman
# Средняя оценка за домашние задания: 9.9
# Курсы в процессе изучения: Python, Git
# Завершенные курсы: Введение в программирование
# Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.
# Задание № 4. Полевые испытания
# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:
#
# для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса (в качестве аргументов принимаем список студентов и название курса);
# для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса).

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def mark_for_lector(self, lector, course, mark):
        if isinstance(lector, Lecturer) and course in lector.courses_attached and course in self.courses_in_progress:
            if course in lector.marks_for_lector:
                lector.marks_for_lector[course] += [mark]
            else:
                lector.marks_for_lector[course] = [mark]
        else:
            return 'Ошибка'

    def __str__(self):
        count = 0
        total = 0
        for m in self.grades:
            count += 1
            total += sum(self.grades[m]) / len(self.grades[m])
        if count == 0:
            s_a = 'Пока оценок нет'
        else:
            s_a = round(total / count, 1)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {s_a}\
        \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\
        \nЗавершенные курсы: {" ".join(self.finished_courses)}'

        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    # def rate_hw(self, student, course, grade):
    #     if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
    #         if course in student.grades:
    #             student.grades[course] += [grade]
    #         else:
    #             student.grades[course] = [grade]
    #     else:
    #         return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.marks_for_lector = {}

    def __str__(self):
        count = 0
        total = 0
        for m in self.marks_for_lector:
            count += 1
            total += sum(self.marks_for_lector[m]) / len(self.marks_for_lector[m])
        if count == 0:
            s_a = 'Пока оценок нет'
        else:
            s_a = round(total / count, 1)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {s_a}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

student1 = Student('Margo', 'Robby', 'femaile')
student1.courses_in_progress.append('Python')
student1.courses_in_progress.append('Git')
student1.finished_courses.append('Введение в программирование')

student2 = Student('Johnny', 'Depp', 'maile')
student2.courses_in_progress.append('Python')
student2.courses_in_progress.append('C++')
student2.finished_courses.append('Введение в программирование')

student3 = Student('Silvestr', 'Staglione', 'maile')
student3.courses_in_progress.append('Введение в программирование')


lector1 = Lecturer('Angelina', 'Jolie')
lector1.courses_attached.append('Python')
lector1.courses_attached.append('Git')
lector1.courses_attached.append('Введение в программирование')

lector2 = Lecturer('Brad', 'Pitt')
lector2.courses_attached.append('Python')
lector2.courses_attached.append('C++')


rew1 = Reviewer('Keanu', 'Reeves')
rew1.courses_attached.append('Python')
rew1.courses_attached.append('C++')
rew1.courses_attached.append('Введение в программирование')


student1.mark_for_lector(lector1, 'Python', 7)
student1.mark_for_lector(lector1, 'Git', 9)
student2.mark_for_lector(lector1, 'Python', 10)
student3.mark_for_lector(lector1, 'Введение в программирование', 10)

student2.mark_for_lector(lector2, 'C++', 9)

rew1.rate_hw(student1, 'Python', 9)
rew1.rate_hw(student1, 'Python', 10)
rew1.rate_hw(student1, 'Python', 6)

rew1.rate_hw(student1, 'Git', 9)
rew1.rate_hw(student1, 'Git', 7)
rew1.rate_hw(student1, 'Git', 9)

rew1.rate_hw(student2, 'Python', 9)
rew1.rate_hw(student2, 'Python', 0)
rew1.rate_hw(student2, 'Python', 9)

rew1.rate_hw(student2, 'C++', 9)
rew1.rate_hw(student2, 'C++', 10)
rew1.rate_hw(student2, 'C++', 10)

rew1.rate_hw(student3, 'Введение в программирование', 9)
rew1.rate_hw(student3, 'Введение в программирование', 9)
rew1.rate_hw(student3, 'Введение в программирование', 10)


print(student1)
print()
print(student2)
print()
print(student3)
print()
print()
print(lector1)
print()
print(lector2)
print()
print()
print(rew1)
