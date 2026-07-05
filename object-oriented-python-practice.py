import re

class Student:
    def __init__(self, name, email, grades):
        self.name = name          # student's name
        self.email = email        # student's email
        self.grades = grades      # list of integers holding all grades

    def add_grade(self, grade):
        # adds a single new grade to the grades list
        self.grades.append(grade)

    def average_grade(self):
        # calculates and returns the average of all grades as a string
        total = 0
        for grade in self.grades:
            total += grade
        return f'Average of all grades: {total / len(self.grades)}'

    def display_info(self):
        # prints the student's name, email, and current grades
        print(f'Name: {self.name}\nEmail: {self.email}\nGrades: {self.grades}')

    def grades_tuple(self):
        # returns the grades list as a tuple
        return tuple(self.grades)


# Part 2: Working with Objects
# create 3 student objects with different names, emails, and initial grades
student1 = Student('John', 'john@gmail.com', [90, 92, 91])
student2 = Student('Karen', 'karen@gmail.com', [80, 82, 81])
student3 = Student('Miranda', 'mir@gmail.com', [100, 99, 98])

# add 2 new grades to each student
student1.add_grade(93)
student1.add_grade(94)
student2.add_grade(83)
student2.add_grade(84)
student3.add_grade(96)
student3.add_grade(97)

# print each student's info and their average grade
student1.display_info()
print(student1.average_grade())
student2.display_info()
print(student2.average_grade())
student3.display_info()
print(student3.average_grade())


# Part 3: Dictionary & Set Integration

# dictionary mapping each student's email to their Student object
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3
}

def get_student_by_email(email):
    # safely retrieves a student object using .get(), returns None if not found
    return student_dict.get(email)

# combine all grades from all students into one set to get unique values
all_grades = set(student1.grades + student2.grades + student3.grades)
print(all_grades)


# Part 4: Tuple Practice

# get student1's grades as a tuple
grades_as_tuple = student1.grades_tuple()
print(grades_as_tuple)

# try to change a value in the tuple to show tuples are immutable
try:
    grades_as_tuple[0] = 100
except TypeError:
    print('Cannot change a tuple, it is immutable')


# Part 5: List Operations

# remove the last grade from each student's grades list
student1.grades.pop()
student2.grades.pop()
student3.grades.pop()

# print the first and last grade for each student
print(student1.grades[0], student1.grades[-1])
print(student2.grades[0], student2.grades[-1])
print(student3.grades[0], student3.grades[-1])

# print how many grades each student has left
print(len(student1.grades))
print(len(student2.grades))
print(len(student3.grades))


# Part 6: Bonus

# regex pattern to check for a valid email format like name@domain.com
email_pattern = r'^[\w.-]+@[\w.-]+\.com$'

# check each student's email against the pattern
print(bool(re.match(email_pattern, student1.email)))
print(bool(re.match(email_pattern, student2.email)))
print(bool(re.match(email_pattern, student3.email)))

# count how many grades across all students are above 90
count_above_90 = 0
for grade in student1.grades + student2.grades + student3.grades:
    if grade > 90:
        count_above_90 += 1

print(count_above_90)