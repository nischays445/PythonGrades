# Python_Grades

#### Description:
Python_Grades is a Python program that uses CSV files to create a gradebook for educators looking for a simple, minimalist approach. The program initializes a new gradebook object with a custom name, creates a CSV file to store the gradebook data using the user-inputted name and the `.csv` extension. After the user specifies the name and what they want to do (view and edit a gradebook or create a new one), they are given a menu in the terminal with options:

- **0**: Add a student.
- **1**: Delete a student by ID.
- **2**: View student information by ID.
- **3**: Wipe the entire gradebook.
- **4**: Change student information.
- **5**: Display the contents of the gradebook.
- **6**: Calculate a final grade.
- **7**: Validate an email address.
- **8**: Generate a random 5-digit student ID.
- **9**: Exit the program.

A test file using `pytest` is also provided. You can modify the program and add methods, and the test file will ensure that most of the core methods still work as intended.

#### How to Install:

1. **Ensure you have Python installed:**
   - Check if Python is installed by running:
     ```bash
     python --version
     ```
   - If not installed, download and install it from [python.org](https://www.python.org/).

2. **Clone the repository:**
   - Clone this repository to your local machine:
     ```bash
     git clone https://github.com/nischays445/PythonGrades.git
     ```

3. **Navigate to the project directory:**
   - Change to the directory containing the `Python_Grades` file:
     ```bash
     cd PythonGrades
     ```

4. **Install dependencies (if applicable):**
   - If a `requirements.txt` file is provided, install the dependencies using:
     ```bash
     pip install -r requirements.txt
     ```

#### How to Run:

1. **Run the Python file:**
   - Execute the program using the following command:
     ```bash
     python python_grades.py
     ```
   - If your system uses Python 3 as `python3`, use:
     ```bash
     python3 python_grades.py
     ```

2. **Run tests (optional):**
   - To run the test file and ensure everything is working correctly, use:
     ```bash
     pytest test_python_grades.py
     ```

Make sure to adjust the file names and paths as needed. If there are any specific dependencies or setup instructions unique to your project, include those details as well.
