class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        cls.student_list.append(student)

    @classmethod
    def find_student(cls, student_id):
        for student in cls.student_list:
            if student.student_id == student_id.strip().upper():
                return student
        raise ValueError(f"Student ID  '{student_id}' not found" )

class Student:
    def __init__(self, studnet_id, name, department, is_enrolled=False):
        self.__student_id = studnet_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

        StudentDatabase.add_student(self)

    @property
    def student_id(self):
        return self.__student_id

    @property
    def name(self):
        return self.__name

    @property
    def department(self):
        return self.__department

    @property
    def is_enrolled(self):
        return self.__is_enrolled


    def enroll_student(self):
        if self.is_enrolled:
            raise ValueError(f"Student {self.__student_id} is already enrolled")
        self.__is_enrolled = True

    def drop_student(self):
        if not self.__is_enrolled:
            raise ValueError(f"Student {self.__student_id} is not enrolled, cannot drop. ")
        self.__is_enrolled = False

    def view_student_info(self):
        return(f"ID: {self.__student_id}, Name: {self.__name}, Department: {self.__department}, Enrolled: {self.__is_enrolled} ")


def manual_student():
    if not StudentDatabase.student_list:
        Student("S101", "Alice Smith", "Computer Science", True)
        Student("S102", "Bob Johnson", "Math", False)
        Student("S103", "Charlie Lee", "Physics", True)

def main():
    manual_student()
    while True:
        print("\n---Student Management Menu ---")
        print("1. View all studnets")
        print("2. Enroll Stuent")
        print("3. Drop Students")
        print("4. Exit")

        choice = input("Enter your choice ")

        if choice == "1":
            if not StudentDatabase.student_list:
                print("No studnet found")
            for student in StudentDatabase.student_list:
                print(student.view_student_info())
        elif choice == "2":
            manual = input("Enter student ID to enroll : ")
            try:
                student = StudentDatabase.find_student(manual)
                student.enroll_student()
                print(f"Student {student.student_id} has enrolled")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "3":
            manual = input ("Enter student ID to drop: ")
            try:
                student = StudentDatabase.find_student(manual)
                student.drop_student()
                print(f"Student {student.student_id} has dropped")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == "4":
            print("Exit the program")
            break
        else:
            print("Invalid Choice, Please enter a number between 1 - 4")

if __name__ == "__main__":
    main()
