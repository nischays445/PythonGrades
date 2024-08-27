# Python_Grades

#### Description:
Python_Grades is a Python program that uses CSV files to create a gradebook for educators looking for a simple, minimalist approach. This program starts by initializing a new gradebook object with a custom given name. It then creates a CSV file to store the gradebook data using the user-inputted name and the `.csv` extension. After the user enters the name and what they are trying to do (either view and edit a gradebook or create a new one), the user in the terminal is given the option to enter numbers 0-9 with corresponding options.

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

A test file is also provided using pytest, so if you wish to modify this program and add methods, you can do so, and the test file will ensure most of the core methods still work as intended.

#### How to Install:

1. **Ensure you have Python installed:**
   - Check if Python is installed by running:
     ```bash
     python --version
     ```
   - If not installed, download and install it from [python.org](https://www.python.org/).

2. **Clone the repository (if applicable):**
   - Clone this repository to your local machine:
     ```bash
     git clone https://github.com/your-username/your-repository.git
     ```

3. **Navigate to the project directory:**
   - Change to the directory containing the `Python_Grades` file:
     ```bash
     cd path/to/your/repository
     ```

4. **Install dependencies:**
   - If you have a `requirements.txt` file for dependencies, install them using:
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
   - If you want to run the test file to ensure everything is working correctly, use pytest:
     ```bash
     pytest test_python_grades.py
     ```

Make sure to replace `path/to/your/repository` and `your-username/your-repository` with the actual path and repository details. Adjust the file names as needed.
