import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QListWidget, QLineEdit

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List")
        self.layout = QVBoxLayout()

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter a task")
        self.add_button = QPushButton("Add Task")
        self.task_list = QListWidget()

        self.layout.addWidget(self.task_input)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.task_list)

        self.setLayout(self.layout)
        self.add_button.clicked.connect(self.add_task)

    def add_task(self):
        task = self.task_input.text()
        if task:
            self.task_list.addItem(task)
            self.task_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    sys.exit(app.exec_())
