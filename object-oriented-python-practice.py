import re

class Student:
    def __init__(self, name, email, grades):
        self.name = name
        self.email = email
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        total = 0
        for grade in self.grades:
            total += grade
        return f'Average of all grades: {total / len(self.grades)}'

    def display_info(self):
        print(f'Name: {self.name}\nEmail: {self.email}\nGrades: {self.grades}')

    def grades_tuple(self):
        return tuple(self.grades)


# Part 2: Working with Objects
student1 = Student('John', 'john@gmail.com', [90, 92, 91])
student2 = Student('Karen', 'karen@gmail.com', [80, 82, 81])
student3 = Student('Miranda', 'mir@gmail.com', [100, 99, 98])

student1.add_grade(93)
student1.add_grade(94)
student2.add_grade(83)
student2.add_grade(84)
student3.add_grade(96)
student3.add_grade(97)

student1.display_info()
print(student1.average_grade())
student2.display_info()
print(student2.average_grade())
student3.display_info()
print(student3.average_grade())


# Part 3: Dictionary & Set Integration
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

def get_student_by_email(email):
    return student_dict.get(email)

found = get_student_by_email('john@gmail.com')
if found:
    found.display_info()

not_found = get_student_by_email('fake@gmail.com')
print(not_found)

all_grades = set(student1.grades + student2.grades + student3.grades)
print(all_grades)


# Part 4: Tuple Practice
grades_as_tuple = student1.grades_tuple()
print(grades_as_tuple)

try:
    grades_as_tuple[0] = 100
except TypeError:
    print('Cannot change a tuple, it is immutable')


# Part 5: List Operations
student1.grades.pop()
student2.grades.pop()
student3.grades.pop()

print(student1.grades[0], student1.grades[-1])
print(student2.grades[0], student2.grades[-1])
print(student3.grades[0], student3.grades[-1])

print(len(student1.grades))
print(len(student2.grades))
print(len(student3.grades))


# Part 6: Bonus
email_pattern = r'^[\w.-]+@[\w.-]+\.com$'

print(bool(re.match(email_pattern, student1.email)))
print(bool(re.match(email_pattern, student2.email)))
print(bool(re.match(email_pattern, student3.email)))

count_above_90 = 0
for grade in student1.grades + student2.grades + student3.grades:
    if grade > 90:
        count_above_90 += 1

print(count_above_90)