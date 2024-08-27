import pytest
import project
from pathlib import Path
import csv


def test__init__():
    custom_class = project.Gradebook("CS50", 0)
    with pytest.raises(FileExistsError):
        file_path = Path("gradebook/CS50.csv")
        file_path.touch(exist_ok=False)


def test_addStudent():
    custom_class = project.Gradebook("CS50", 1)
    custom_class.addStudent("Cristiano Ronaldo", 7, 2026, "cristianoronaldo@gmail.com")
    found = False
    file_path = Path("gradebook/CS50.csv")
    with file_path.open("r", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Student ID'] == '7' and row['Student Name'] == "Cristiano Ronaldo" and row["YOG"] == '2026' and row["Email"] == "cristianoronaldo@gmail.com":
                found = True
    assert found == True


def test_deleteStudent():
    custom_class = project.Gradebook("CS50", 1)
    custom_class.deleteStudent(7)
    found = False
    file_path = Path("gradebook/CS50.csv")
    with file_path.open("r", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Student ID'] == '7' and row['Student Name'] == "Cristiano Ronaldo" and row["YOG"] == '2026' and row["Email"] == "cristianoronaldo@gmail.com":
                found = True
    assert found == False


def test_changeInfo():
    custom_class = project.Gradebook("CS50", 1)
    custom_class.addStudent("Cristiano Ronaldo", 7, 2026, "cristianoronaldo@gmail.com")
    custom_class.changeInfo(7, "Email", "cristianoronaldo@outlook.com")
    changedCorrectly = False
    file_path = Path("gradebook/CS50.csv")
    with file_path.open("r", newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Email"] == "cristianoronaldo@outlook.com":
                changedCorrectly = True
    assert changedCorrectly == True
def test_calculateFinal():
    assert int(project.calculateFinal(89, 0.1, None, None, 85)) == 85
    assert int(project.calculateFinal(None, None, 89, 0.1, 85)) == 85
    assert int(project.calculateFinal(85, 0.05, 95, 0.1, 65)) == 69
def test_validateEmail():
    assert project.validateEmail("davidmalan@harvard.edu") == "Valid"
    assert project.validateEmail("johndoe@gmail.com") == "Valid"
    assert project.validateEmail("bobthebuilder@outlook.com") == "Valid"
    assert project.validateEmail("bob@google.co") == "Invalid"
    assert project.validateEmail("bobgoogle.com") == "Invalid"
    assert project.validateEmail("bob][]()@gmail.com") == "Invalid"
def test_generateStudentID():
    assert len(str(project.generateStudentID())) == 5
    assert len(str(project.generateStudentID())) == 5
    assert len(str(project.generateStudentID())) == 5
    assert len(str(project.generateStudentID())) == 5
