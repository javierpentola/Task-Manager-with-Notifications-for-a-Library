import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QListWidget, QHBoxLayout, QPushButton, QLineEdit, QLabel, QComboBox, QListWidgetItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Gestor de Tareas para Biblioteca')
        self.setGeometry(100, 100, 800, 600)

        self.main_layout = QVBoxLayout()

        # Search bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText('Buscar tareas...')
        self.search_bar.textChanged.connect(self.filter_tasks)
        self.main_layout.addWidget(self.search_bar)

        # Sorting options
        self.sort_layout = QHBoxLayout()
        self.sort_label = QLabel("Ordenar por:")
        self.sort_combo = QComboBox()
        self.sort_combo.addItems(["Fecha límite", "Prioridad", "Título"])
        self.sort_combo.currentIndexChanged.connect(self.sort_tasks)
        self.sort_layout.addWidget(self.sort_label)
        self.sort_layout.addWidget(self.sort_combo)
        self.main_layout.addLayout(self.sort_layout)

        # Task list
        self.task_list = QListWidget()
        self.main_layout.addWidget(self.task_list)

        # Add task button
        self.add_task_button = QPushButton('Añadir Tarea')
        self.main_layout.addWidget(self.add_task_button)

        container = QWidget()
        container.setLayout(self.main_layout)
        self.setCentralWidget(container)

    def filter_tasks(self):
        filter_text = self.search_bar.text().lower()
        for i in range(self.task_list.count()):
            item = self.task_list.item(i)
            item.setHidden(filter_text not in item.text().lower())

    def sort_tasks(self):
        sort_by = self.sort_combo.currentText()
        tasks = [self.task_list.item(i) for i in range(self.task_list.count())]
        tasks_data = [task.data(100) for task in tasks]

        if sort_by == "Fecha límite":
            tasks_data.sort(key=lambda x: x["deadline"])
        elif sort_by == "Prioridad":
            priority_order = {"Alta": 1, "Media": 2, "Baja": 3}
            tasks_data.sort(key=lambda x: priority_order[x["priority"]])
        elif sort_by == "Título":
            tasks_data.sort(key=lambda x: x["title"])

        self.task_list.clear()
        for task_data in tasks_data:
            self.add_task_to_list(task_data)

    def add_task_to_list(self, task):
        item = QListWidgetItem(f"{task['title']} - {task['priority']} (Hasta: {task['deadline']})")
        item.setData(100, task)
        self.task_list.addItem(item)
