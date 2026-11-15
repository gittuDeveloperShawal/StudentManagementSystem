# StudentManagementSystem
Python OOP Student Management System
# StudentManagementSystem

A menu-driven **Python OOP** console application to view, enroll and drop students.

## Features
- `StudentDatabase` class that stores all students in a class-level list (`student_list`)
- `Student` class with **private attributes** (`student_id`, `name`, `department`, `is_enrolled`) for data privacy
- `enroll_student()`, `drop_student()` and `view_student_info()` methods
- Menu system: View All Students, Enroll Student, Drop Student, Exit
- Error handling for:
  - Invalid student ID
  - Enrolling a student who is already enrolled
  - Dropping a student who is not enrolled

## How to Run
1. Make sure Python 3 is installed
2. Run:

       python student_management.py

## Sample Students
| ID   | Name        | Department       | Enrolled |
|------|-------------|------------------|----------|
| S101 | Alice Smith | Computer Science | True     |
| S102 | Bob Johnson | Math             | False    |
| S103 | Charlie Lee | Physics          | True     |

## Sample Output

    --- Student Management Menu ---
    1. View All Students
    2. Enroll Student
    3. Drop Student
    4. Exit
    Enter your choice (1-4): 3
    Enter Student ID to drop: S103
    Student S103 has been dropped.

## Author
gittuDeveloperShawal
