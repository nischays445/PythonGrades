# Python_Grades

#### Description:
Python_Grades is a Python program that uses CSV files to create a gradebook for educators seeking a simple, minimalist approach. The program initializes a new gradebook object with a custom name, creates a CSV file to store the data, and provides a menu with the following options:

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

A test file using `pytest` is included to ensure that the core methods function as intended.

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
   - Execute the program with:
     ```bash
     python python_grades.py
     ```
   - If your system uses Python 3 as `python3`, use:
     ```bash
     python3 python_grades.py
     ```

2. **Run tests (optional):**
   - To run the test file and verify the functionality, use:
     ```bash
     pytest test_python_grades.py
     ```

