from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QLabel, QFrame, QHBoxLayout,
                             QLineEdit, QPushButton, QListWidget)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import sys

class Todoapp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        """Set up the main user interface"""
        self.setWindowTitle("Todo Application")
        self.setGeometry(100, 100, 600, 500)

        # Cental Widget
        cental_widget = QWidget()
        self.setCentralWidget(cental_widget)

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Title
        title = QLabel("My Todo List")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title.setStyleSheet("color: #2c3e50;")

        # Input Selection
        input_frame = QFrame()
        input_frame.setFrameStyle(QFrame.Shape.Box)
        input_frame.setStyleSheet("""
            QFrame {
                border: 1px solid #bdc3c7;
                border-radius: 10px;
                padding: 10px;
                background-color: #f8f9fa;                 
            }

        """)

        input_layout = QHBoxLayout()

        self.todo_input = QLineEdit()
        self.todo_input.setPlaceholderText("Enter a New Todo Item...")
        self.todo_input.setStyleSheet("""
            QLineEdit {
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                padding: 8px;
                font-size: 12px;         
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
            
            }
        """)


        self.add_btn = QPushButton("Add Todo")
        self.add_btn.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.add_btn.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 15px;
                font-weight: bold;                      
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
            QPushButton:pressed {
                background-color: #21618c;
            }
        """)


        input_layout.addWidget(self.todo_input)
        input_layout.addWidget(self.add_btn)
        input_frame.setLayout(input_layout)

        # Todo List
        self.todo_list = QListWidget()
        self.todo_list.setStyleSheet("""
            QListWidget {
                border: 1px solid #bdc3c7;
                border-radius: 5px;
                background-color: white;                
                alternate-background-color: #f8f9fa;                 
            }

        """)






        # Add all widgets to main layout
        main_layout.addWidget(title)
        main_layout.addWidget(input_frame)
        main_layout.addWidget(self.todo_list)


        cental_widget.setLayout(main_layout)


    


app = QApplication(sys.argv)
window = Todoapp()
window.show()
sys.exit(app.exec())