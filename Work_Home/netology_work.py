# def voto_medio(obj):
#     lst = []
#     for item in obj:
#         lst += obj[item]
#     if len(lst) != 0:
#         voto = round((sum(lst) / len(lst)), 1)
#         return voto
#     else:
#         return 'Нет оценок'


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
            return 'Нет оценок'

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
        return self.voto < other.voto

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.voto}" \
               f" \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}"
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
            return 'Нет оценок'

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.voto} "
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


student1 = Student('Piter', 'Soren', 'boy')
student1.courses_in_progress += ['Python', 'CSS', 'Java', 'HTML']

student2 = Student('Nicolas', 'Kenis', 'boy')
student2.courses_in_progress += ['Python', 'CSS', 'Java', 'HTML']

student3 = Student('Irina', 'Gray', 'gerl')
student3.courses_in_progress += ['Python', 'CSS', 'Java', 'HTML']

student4 = Student('Sara', 'Conor', 'gerl')
student4.courses_in_progress += ['Python', 'CSS', 'Java', 'HTML']

# lecturer1 = Lecturer('Mikel', 'Stone')
# lecturer1.courses_attached += ['Python']
#
# lecturer2 = Lecturer('Pol', 'Snake')
# lecturer2.courses_attached += ['CSS']
#
# lecturer3 = Lecturer('Ron', 'Folk')
# lecturer3.courses_attached += ['Java']
#
# lecturer4 = Lecturer('Jon', 'Martin')
# lecturer4.courses_attached += ['HTML']

rewiever = Reviewer('Ron', 'Pitersen')
rewiever.courses_attached += ['Python', 'CSS', 'Java', 'HTML']
rewiever.rate_hw(student1, 'Python', 8)

# lecturer1.rate_hw(student1, 'Python', 8)
print(student1.grades)
print(student1)
print(student1.voto)
# print(rewiever)
# print(student1, end='\n' * 2)
# print(lecturer1)
# voto_medio(student1)
