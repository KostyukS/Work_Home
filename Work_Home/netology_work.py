class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def voto_medio(self):
        lst = []
        for item in self.grades:
            lst += self.grades[item]
        if len(lst) != 0:
            val = round((sum(lst) / len(lst)), 1)
            return val
        else:
            return 0

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        return self.voto_medio() < other.voto_medio()

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.voto_medio()}" \
               f" \nКурсы в процессе изучения: {', '.join(self.courses_in_progress)} " \
               f"\nЗавершенные курсы: {', '.join(self.finished_courses)}"
        return text


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

    def voto_medio(self):
        lst = []
        for item in self.grades:
            lst += self.grades[item]
        if len(lst) != 0:
            val = round((sum(lst) / len(lst)), 1)
            return val
        else:
            return 0

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.voto_medio()} "
        return text


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}"
        return text

        # Студенты


student1 = Student('Piter', 'Soren', 'boy')
student1.courses_in_progress += ['Python', 'CSS', 'Java', 'HTML']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Nicolas', 'Kenis', 'boy')
student2.courses_in_progress += ['Python', 'CSS', 'Java', 'HTML']
student2.finished_courses += ['Введение в программирование']

student3 = Student('Irina', 'Gray', 'gerl')
student3.courses_in_progress += ['Python', 'CSS', 'Java', 'HTML']
student3.finished_courses += ['Введение в программирование']

student4 = Student('Sara', 'Conor', 'gerl')
student4.courses_in_progress += ['Python', 'CSS', 'Java', 'HTML']
student4.finished_courses += ['Введение в программирование']

# Лекторы

lecturer1 = Lecturer('Mikel', 'Stone')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Pol', 'Snake')
lecturer2.courses_attached += ['CSS']

lecturer3 = Lecturer('Ron', 'Folk')
lecturer3.courses_attached += ['Java']

lecturer4 = Lecturer('Jon', 'Martin')
lecturer4.courses_attached += ['HTML']

# Список студентов
lst_stud = [student1, student2, student3, student4]
# Список лекторов
lst_lec = [lecturer1, lecturer2, lecturer3, lecturer4]

# Проверяющие

rewiever1 = Reviewer('Ron', 'Pitersen')
rewiever1.courses_attached += ['Python', 'CSS', 'Java', 'HTML']
rewiever2 = Reviewer('Jack', 'Armstrong')
rewiever2.courses_attached += ['Python', 'CSS', 'Java', 'HTML']

# Оценки проверяющих студентам

rewiever1.rate_hw(student1, 'Python', 2)
rewiever1.rate_hw(student1, 'CSS', 5)
rewiever1.rate_hw(student1, 'Java', 8)
rewiever1.rate_hw(student1, 'HTML', 8)

rewiever2.rate_hw(student2, 'Python', 9)
rewiever2.rate_hw(student2, 'CSS', 6)
rewiever2.rate_hw(student2, 'Java', 7)
rewiever2.rate_hw(student2, 'HTML', 6)

rewiever1.rate_hw(student3, 'Python', 8)
rewiever1.rate_hw(student3, 'CSS', 5)
rewiever1.rate_hw(student3, 'Java', 8)
rewiever1.rate_hw(student3, 'HTML', 8)

rewiever2.rate_hw(student4, 'Python', 5)
rewiever2.rate_hw(student4, 'CSS', 8)
rewiever2.rate_hw(student4, 'Java', 3)
rewiever2.rate_hw(student4, 'HTML', 2)

# Оценки студентов лекторам

student1.rate_hw(lecturer1, 'Python', 7)
student2.rate_hw(lecturer1, 'Python', 9)
student3.rate_hw(lecturer1, 'Python', 9)
student4.rate_hw(lecturer1, 'Python', 5)

student1.rate_hw(lecturer2, 'CSS', 6)
student2.rate_hw(lecturer2, 'CSS', 8)
student3.rate_hw(lecturer2, 'CSS', 5)
student4.rate_hw(lecturer2, 'CSS', 9)

student1.rate_hw(lecturer3, 'Java', 9)
student2.rate_hw(lecturer3, 'Java', 10)
student3.rate_hw(lecturer3, 'Java', 6)
student4.rate_hw(lecturer3, 'Java', 8)

student1.rate_hw(lecturer4, 'Python', 8)
student2.rate_hw(lecturer4, 'Python', 5)
student3.rate_hw(lecturer4, 'Python', 8)
student4.rate_hw(lecturer4, 'Python', 7)


def voto_stud(student, course):
    lst = []
    for item in student:
        if course in item.grades:
            lst += item.grades[course]
    voto = round((sum(lst) / len(lst)), 1)
    print(f'Средняя оценка всех студентов по {course}: {voto}')


def voto_lec(lecturer, course):
    lst = []
    for item in lecturer:
        if course in item.grades:
            lst += item.grades[course]
    voto = round((sum(lst) / len(lst)), 1)
    print(f'Средняя оценка всех лекторов по {course}: {voto}')


print(student1, end='\n' * 2)
print(lecturer1, end='\n' * 2)
print(rewiever1, end='\n' * 2)
print(lecturer3 > student2)
print()
voto_stud(lst_stud, 'CSS')
print()
voto_lec(lst_lec, 'CSS')
