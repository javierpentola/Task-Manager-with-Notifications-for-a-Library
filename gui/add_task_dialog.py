from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton

class AddTaskDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Añadir Tarea')

        layout = QVBoxLayout()

        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText('Título')
        layout.addWidget(self.title_input)

        self.description_input = QLineEdit(self)
        self.description_input.setPlaceholderText('Descripción')
        layout.addWidget(self.description_input)

        self.priority_input = QLineEdit(self)
        self.priority_input.setPlaceholderText('Prioridad')
        layout.addWidget(self.priority_input)

        self.deadline_input = QLineEdit(self)
        self.deadline_input.setPlaceholderText('Fecha límite')
        layout.addWidget(self.deadline_input)

        self.add_button = QPushButton('Añadir')
        layout.addWidget(self.add_button)

        self.setLayout(layout)

        self.add_button.clicked.connect(self.accept)
