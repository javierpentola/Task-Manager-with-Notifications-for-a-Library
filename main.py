import sys
from PyQt5.QtWidgets import QApplication
from gui.main_window import MainWindow
from gui.add_task_dialog import AddTaskDialog
from gui.edit_task_dialog import EditTaskDialog
from database import add_task, get_all_tasks, update_task
from notifier import send_notification

def show_add_task_dialog():
    dialog = AddTaskDialog()
    if dialog.exec_():
        title = dialog.title_input.text()
        description = dialog.description_input.text()
        priority = dialog.priority_input.text()
        deadline = dialog.deadline_input.text()
        add_task(title, description, priority, deadline)
        send_notification('Nueva Tarea Añadida', f'{title} - {deadline}')
        load_tasks()

def show_edit_task_dialog(item):
    task = item.data(100)
    dialog = EditTaskDialog(task)
    if dialog.exec_():
        updated_task = dialog.get_updated_task()
        update_task(task['id'], updated_task['title'], updated_task['description'], updated_task['priority'], updated_task['deadline'])
        send_notification('Tarea Actualizada', f'{updated_task["title"]} - {updated_task["deadline"]}')
        load_tasks()

def load_tasks():
    tasks = get_all_tasks()
    main_window.task_list.clear()
    for task in tasks:
        main_window.add_task_to_list({
            'id': task[0],
            'title': task[1],
            'description': task[2],
            'priority': task[3],
            'deadline': task[4]
        })

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()

    main_window.add_task_button.clicked.connect(show_add_task_dialog)
    main_window.task_list.itemDoubleClicked.connect(show_edit_task_dialog)
    load_tasks()
    main_window.show()
    sys.exit(app.exec_())
