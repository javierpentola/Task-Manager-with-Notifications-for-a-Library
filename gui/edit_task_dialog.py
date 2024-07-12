from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton


class EditTaskDialog(QDialog):
    def __init__(self, task):
        super().__init__()
        self.setWindowTitle('Editar Tarea')

        layout = QVBoxLayout()

        self.title_input = QLineEdit(self)
        self.title_input.setText(task['title'])
        layout.addWidget(self.title_input)

        self.description_input = QLineEdit(self)
        self.description_input.setText(task['description'])
        layout.addWidget(self.description_input)

        self.priority_input = QLineEdit(self)
        self.priority_input.setText(task['priority'])
        layout.addWidget(self.priority_input)

        self.deadline_input = QLineEdit(self)
        self.deadline_input.setText(task['deadline'])
        layout.addWidget(self.deadline_input)

        self.edit_button = QPushButton('Guardar Cambios')
        layout.addWidget(self.edit_button)

        self.setLayout(layout)

        self.edit_button.clicked.connect(self.accept)

    def get_updated_task(self):
        return {
            'title': self.title_input.text(),
            'description': self.description_input.text(),
            'priority': self.priority_input.text(),
            'deadline': self.deadline_input.text()
        }
