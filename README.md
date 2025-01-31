### Project Documentation: Task Manager with Notifications for a Library

---

#### **Project Overview**

**Project Name:** Task Manager for Library

**Technologies Used:**
- **Python:** The main programming language used for development.
- **PyQt5:** For creating the graphical user interface (GUI).
- **SQLite:** For storing and managing the tasks data.
- **Plyer:** For sending desktop notifications to remind users of pending tasks.

**Description:** This project is a desktop application designed to help manage tasks in a library. It allows users to create, edit, delete, and categorize tasks. The application also includes features for searching and sorting tasks, and it sends notifications to remind users of their tasks.

---

### **Technologies Usage**

1. **Python:**
   - **Usage:** Python is used as the main programming language to build the backend logic, handle database operations, and manage the GUI.
   - **Files:** All source files (`main.py`, `database.py`, `gui/*.py`, `notifier.py`).

2. **PyQt5:**
   - **Usage:** PyQt5 is used to create the GUI of the application, providing a user-friendly interface for managing tasks.
   - **Files:** `gui/main_window.py`, `gui/add_task_dialog.py`, `gui/edit_task_dialog.py`

3. **SQLite:**
   - **Usage:** SQLite is used as the database to store tasks. It is chosen for its simplicity and ease of use with Python.
   - **Files:** `database.py`

4. **Plyer:**
   - **Usage:** Plyer is used to send desktop notifications, reminding users of their pending tasks.
   - **Files:** `notifier.py`

---

### **Setup and Usage Instructions**

To set up and use the project after downloading the code, follow these steps:

1. **Clone the Repository:**
   - Use `git clone` to clone the repository to your local machine.
   ```bash
   git clone <repository_url>
   ```

2. **Navigate to the Project Directory:**
   - Change your working directory to the project folder.
   ```bash
   cd TaskManager
   ```

3. **Install Dependencies:**
   - Install the required Python packages using `pip`.
   ```bash
   pip install pyqt5 plyer
   ```

4. **Run the Application:**
   - Execute the main Python file to start the application.
   ```bash
   python main.py
   ```

5. **Using the Task Manager Application:**
   - **Add a Task:** Click on the "Añadir Tarea" button, fill out the details in the dialog, and save.
   - **Edit a Task:** Double-click on any task in the list to open the edit dialog, make changes, and save.
   - **Search Tasks:** Use the search bar at the top to filter tasks by keywords.
   - **Sort Tasks:** Use the dropdown menu to sort tasks by priority, title, or deadline.
   - **Receive Notifications:** Notifications will appear on your desktop to remind you of upcoming tasks.

---

### **File Descriptions**

1. **`main.py`:**
   - Initializes the application, sets up the main window, and handles interactions between the GUI and the database.

2. **`database.py`:**
   - Manages the SQLite database, including functions for creating, reading, updating, and deleting tasks.

3. **`gui/main_window.py`:**
   - Defines the main window of the application, including the task list, search bar, sorting options, and add task button.

4. **`gui/add_task_dialog.py`:**
   - Defines the dialog window for adding new tasks, including fields for title, description, priority, and deadline.

5. **`gui/edit_task_dialog.py`:**
   - Defines the dialog window for editing existing tasks with pre-filled fields for the selected task.

6. **`notifier.py`:**
   - Uses Plyer to send desktop notifications to the user about upcoming tasks.
