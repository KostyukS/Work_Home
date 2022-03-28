class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.voto = voto_medio(self)

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
        text = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:" \
               f" \nКурсы в процессе изучения: \nЗавершенные курсы:"
        return text


def voto_medio(obj):
    lst = []
    for item in obj.grades:
        for val in item.values():
            lst.append(int(val))
    voto = sum(lst) / len(lst)
    return voto


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
        self.grades = {}
        self.courses_attached = []

    def __str__(self):
        text = f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: "
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


sudent1 = Student('Piter', 'Soren', 'boy')
student2 = Student('Nicolas', 'Kenis', 'boy')
student3 = Student('Irina', 'Gray', 'gerl')
student4 = Student('Sara', 'Conor', 'gerl')
