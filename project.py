from pathlib import Path
import pandas as pd
import sys
import csv
from email_validator import validate_email, EmailNotValidError
import random


class Gradebook:
    def __init__(self, course_name, typeModification):
        if not course_name:
            raise ValueError("Please Enter a coursename")
        try:
            Path.mkdir('gradebook')
        except FileExistsError:
            pass
        self.course_name = course_name
        if typeModification != 0 and typeModification != 1:
            raise ValueError("Incorrect modification type")
        else:
            self.typeModification = typeModification
        self.file_path = file_path = Path(f"gradebook/{course_name}.csv")
        if typeModification == 0:
            try:
                self.file_path.touch(exist_ok=False)
                with self.file_path.open('w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['Student ID', 'Student Name', 'YOG', 'Email',
                                    'Grade', 'Midterm Exam', 'Final Exam', 'Final Grade'])
            except FileExistsError:
                print("Gradebook Already Exists")
        if self.file_path.exists() == False:
            raise ValueError("Gradebook does not exist")

    def __str__(self):
        print("\n")
        with open(self.file_path) as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
        return ""

    def addStudent(self, student_name, ID, YOG, email, grade=None, midterm_exam=None, final_exam=None, final_grade=None):
        # checking if studentID already is in gradebook
        with self.file_path.open('r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == ID:
                    raise ValueError("Student Already exists")
        student = {
            "Student ID": ID,
            "Student Name": student_name,
            "YOG": YOG,
            "Email": email,
            'Grade': grade,
            'Midterm Exam': midterm_exam,
            'Final Exam': final_exam,
            'Final Grade': final_grade
        }
        with self.file_path.open('a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=[
                                    'Student ID', 'Student Name', 'YOG', 'Email', 'Grade', 'Midterm Exam', 'Final Exam', 'Final Grade'])
            writer.writerow(student)

    def deleteStudent(self, ID):
        df = pd.read_csv(self.file_path)
        deleteIndex = df[df['Student ID'] == ID].index
        if deleteIndex.empty:
            print("Student does not exist")
            return
        else:
            df = df.drop(deleteIndex)
            df.to_csv(self.file_path, index=False)
            print("Student successfully Deleted")

    def getStudent(self, ID):
        with self.file_path.open('r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == ID:
                    return row
        return None

    def wipeGradebook(self):
        with self.file_path.open('w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Student ID', 'Student Name', 'YOG', 'Email',
                            'Grade', 'Midterm Exam', 'Final Exam', 'Final Grade'])
        print("Gradebook has been wiped")

    def changeInfo(self, ID, infoToChange, changeValue):
        df = pd.read_csv(self.file_path)
        if ID not in df["Student ID"].values:
            print("Student does not exist")
            return
        if infoToChange not in df.columns:
            print("Value to Change does not exist")
            return
        df.loc[df['Student ID'] == ID, infoToChange] = changeValue
        df.to_csv(self.file_path, index=False)
        print("Student Sucessfully updated")


def calculateFinal(midterm_exam=None, midterm_exam_weight=None, final_exam=None, final_exam_weight=None, currentGrade=None):
    if not final_exam and not midterm_exam:
        print("No Values entered")
        return currentGrade
    elif not final_exam:
        return (((midterm_exam/100 * midterm_exam_weight)) + ((currentGrade/100) * (1-midterm_exam_weight)))*100
    elif not midterm_exam:
        return (((final_exam/100 * final_exam_weight)) + ((currentGrade/100) * (1-final_exam_weight)))*100
    else:
        return (((final_exam/100 * final_exam_weight)) + ((midterm_exam/100 * midterm_exam_weight)) + currentGrade/100 * ((1 - midterm_exam_weight - final_exam_weight)))*100


def validateEmail(email):
    if not email:
        return ("Invalid")
    try:
        emailinfo = validate_email(email, check_deliverability=True)
        return ("Valid")
    except EmailNotValidError as e:
        return ("Invalid")


def generateStudentID():
    return random.randint(10000, 99999)


def main():
    print("Welcome to the Gradebook!")
    courseName = input("Enter the name of the course: ").strip()
    editingSelection = int(
        input("Enter either a 0 to create a new gradebook or 1 to edit an existing gradebook: ").strip())
    try:
        gradebook = Gradebook(courseName, editingSelection)
    except ValueError as e:
        print(str(e))
        sys.exit("Program exiting..")
    try:
        while True:
            userSelection = int(input(
                "Enter 0 to add Student, 1 to delete student, 2 to get student info, 3 to erase the gradebook, 4 to change student info, 5 to output the gradebook contents, 6 to calculate a final grade, 7 to verify an email, 8 to generate an ID, and 9 to exit the program: "))
            if userSelection == 0:
                try:
                    print("You have selected the option to add a student: ")
                    student_name = input("Enter the students name: ").strip()
                    ID = int(input("Enter the students ID Number(only numbers): ").strip())
                    YOG = int(input("Enter the students YOG: ").strip())
                    email = input("Enter the students email: ")
                    try:
                        emailinfo = validate_email(email, check_deliverability=True)
                    except EmailNotValidError as e:
                        print(str(e))
                        print("Email has been excluded, if email inclusion needed, later modification necessary")
                        email = ""
                    grade = input("Enter the students current grade(Can be left blank): ")
                    midterm_exam = input(
                        "Enter the students midterm exam score(Can be left blank): ")
                    final_exam = input("Enter the students final exam score(Can be left blank): ")
                    final_grade = input(
                        "Enter the students final course grade(Can be left blank): ")
                    gradebook.addStudent(student_name, ID, YOG, email, grade,
                                         midterm_exam, final_exam, final_grade)
                    print("Student sucessfully added: ")
                except ValueError as e:
                    print(e)
                    print("Student was not created")
            if userSelection == 1:
                print("You have selected the option to delete a student")
                userInput = int(
                    input("Enter the ID of the Student you want to delete(only numbers): ").strip())
                userInputConfirmation = input(
                    "Are you sure you want to delete this student? it cannot be undone. Enter 'y' for confirmation: ").strip().lower()
                if userInputConfirmation == 'y':
                    gradebook.deleteStudent(userInput)

            if userSelection == 2:
                print("You have selected the option to view student information")
                userInput = input("Enter the ID of the student you want to view(only numbers): ")
                studentInfo = gradebook.getStudent(userInput)
                if studentInfo == None:
                    print("Student was not found")
                else:
                    print(studentInfo)
            if userSelection == 3:
                print("You have selected the option to wipe the gradebook. This cannot be undone, and all gradebook data will be lost! ")
                userConfirmation = input(
                    "Are you fully sure you want to do this? it cannot be undone. Enter 'y' for confirmation: ").strip().lower()
                if userConfirmation == "y":
                    gradebook.wipeGradebook()
            if userSelection == 4:
                print("You have selected the option to change student info")
                userInputId = int(
                    input("Enter the ID of the student you want to modify(only numbers): "))
                userInputToChange = input(
                    "What do you wish to change?('Student ID', 'Student Name', 'YOG', 'Email', 'Grade', 'Midterm Exam', 'Final Exam', 'Final Grade'). Case Sensitive: ").strip()
                userInputValue = input(
                    "What do you want to change it to?(Only numbers for ID, YOG, Grade, Midterm Exam, Final Exam, or Final Grade): ")
                if userInputToChange == 'Student ID' or userInputToChange == 'YOG' or userInputToChange == 'Grade':
                    userInputValue = int(userInputValue)
                if userInputToChange == 'Midterm Exam' or userInputToChange == 'Final Exam' or userInputToChange == 'Final Grade':
                    userInputValue = float(userInputValue)
                gradebook.changeInfo(userInputId, userInputToChange, userInputValue)
            if userSelection == 5:
                print(gradebook)
            if userSelection == 6:
                print("You have selected to calculate a Final Grade")
                current_grade = float(input("Enter current grade: "))
                midterm_grade = (input("Enter midterm grade: (can be left blank) "))
                if midterm_grade != "":
                    midterm_grade = float(midterm_grade)
                    midterm_weight = float(input("Enter midterm weight(decimal): "))
                else:
                    midterm_grade = None
                    midterm_weight = None
                final_grade = (input("Enter the final exam grade: (Can be left blank) "))
                if final_grade != "":
                    final_grade = float(final_grade)
                    final_weight = float(input("Enter final exam weight(decimal): "))
                else:
                    final_grade = None
                    final_weight = None
                print(calculateFinal(midterm_grade, midterm_weight,
                      final_grade, final_weight, current_grade))
            if userSelection == 7:
                print("You have chosen to validate an email: ")
                print(validateEmail(input("Enter an email address to verify: ")))
            if userSelection == 8:
                print("You have chosen to randomly generate a student ID")
                print(generateStudentID())
            if userSelection == 9:
                print("You have chosen to exit the program. Exiting...")
                break
    except ValueError as e:
        print(e)
        sys.exit("Something went wrong. Exiting program, please relaunch")


if __name__ == "__main__":
    main()
