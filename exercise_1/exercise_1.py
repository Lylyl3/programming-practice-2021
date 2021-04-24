from abc import ABC, abstractmethod

teacher_list = ['Lee', 'Liu', 'Wang']
student_list = ['Win', 'Best', 'Champ', 'Kevin', 'Yiluo', 'Too']
lts_dic = {'Math':        ['Lee', ['Win', 'Yiluo', 'Too']],
           'Physics':     ['Liu', ['Best', 'Kevin', 'Yiluo', 'Too']],
           'Programming': ['Wang', ['Champ', 'Kevin', 'Too']],
           'Biology':     ['Lee', ['Win', 'Best', 'Champ', 'Too']]}

# Give student id, teacher id, and lecture id
student_id = 90000
teacher_id = 5000
lecture_id = 100


class Person(ABC):  # Task 1: natural error?
    name = ""

    @abstractmethod
    def get_attributes(self):
        pass


class Student(Person):  # Task 2.1

    def __init__(self, name):
        self.name = name
        self.student_id = student_id  # Task 6: give every students an ID
        self.lecture_enrolled = []

    def get_attributes(self):
        pass


class Teacher(Person):  # Task 2.2
    def __init__(self, name):
        self.name = name
        self.teacher_id = teacher_id  # Task 6: give every teachers an ID
        self.lecture_taught = ""

    def get_attributes(self):
        pass


class Lecture(Person):  # Task 3
    def __init__(self, lecture_name):
        self.name = lecture_name
        self.lecture_id = "L" + str(lecture_id)  # Task 6: give every lectures an ID
        self.students = []
        self.lecturer = ""

    def assign_teacher(self, lecturer_name):
        if self.lecturer == "":  # Task 4.1: check the lecturer
            self.lecturer = lecturer_name
            teacher_id_dic[self.lecturer].lecture_taught += self.name + " "
        else:  # Task 4.1: return error if the lecture has two or more lecturer
            print(lecturer_name + " can not teach this lecture because " + self.lecturer + " is the lecturer")

    def get_teacher(self):
        return self.lecturer

    def assign_students(self, students_list):
        self.students = students_list
        for n in students_list:  # Task 4.1: check the students
            student_id_dic[n].lecture_enrolled.append(self.name)
            if len(student_id_dic[n].lecture_enrolled) > 3:
                print(n + " can not take " + self.name + " because " + n + " has already chosen more than 3 lectures.")
    # Task 4.1: return error if students has more than 3 lectures

    def get_student(self):
        return self.students

    def get_attributes(self):
        pass

def exercise_1(inputs): # DO NOT CHANGE THIS LINE
    """
    This functions receives the input in the parameter 'inputs'. 
    Change the code, so that the output is sqaure of the given input.
    """
    student_id_dic = {}  # empty dictionary for students
    for num in range(0, len(student_list)):
        stu_name = student_list[num]
        student_id += 1
        student_id_dic[stu_name] = Student(stu_name)

    teacher_id_dic = {}  # empty dictionary for teachers
    for num in range(0, len(teacher_list)):
        tea_name = teacher_list[num]
        teacher_id += 1
        teacher_id_dic[tea_name] = Teacher(tea_name)

    lecturer_dic = {}  # empty dictionary for lectures
    for le_name in lts_dic:
        lecture_id += 1
        lecturer_dic[le_name] = Lecture(le_name)
        lecturer_dic[le_name].assign_teacher(lts_dic[le_name][0])
        lecturer_dic[le_name].assign_students(lts_dic[le_name][1])

################## Print out to check ######################
# for stu_name in student_list:
#     print("Student name:", student_id_dic[stu_name].name,
#           "Student ID:", student_id_dic[stu_name].student_id,
#           "Lecture enrolled:", student_id_dic[stu_name].lecture_enrolled,)
# print("")
# for tea_name in teacher_list:
#     print("Teacher name:", teacher_id_dic[tea_name].name,
#           "Teacher ID:", teacher_id_dic[tea_name].teacher_id,
#           "Lecture taught:", teacher_id_dic[tea_name].lecture_taught)
# print("")
# for le_name in lecturer_dic:
#     print("Lecture name:", lecturer_dic[le_name].name,
#           "Lecture ID:", lecturer_dic[le_name].lecture_id,
#           "Lecturer:", lecturer_dic[le_name].lecturer,
#           "Students:", lecturer_dic[le_name].students)

    output = {
        1: [Person],
        2: [Teacher, Student, student_id_dic, teacher_id_dic],
        3: [Lecture, lecturer_dic],
        4: [Lecture, lecturer_dic],
        6: [Teacher, Student, student_id_dic, teacher_id_dic],
    }  # Sorry I tried my best but I don't really understand how to write task 5

    return output       # DO NOT CHANGE THIS LINE
