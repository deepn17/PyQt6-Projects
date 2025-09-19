from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget,
                             QVBoxLayout, QGroupBox, QLabel,
                             QHBoxLayout, QLineEdit, QPushButton)
import sys

# Define the main window class for the contact book application
class ContactBook(QMainWindow):

    def __init__(self):
        super().__init__() # Initialize the parent QMainWindow
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Contact Book") # Sets the title of the main window
        self.setGeometry(100, 100, 500, 600) # Sets the position and size of the window


        # Central Widget and Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # Add Contact Group
        add_group = QGroupBox("Add New Contact")
        add_layout = QVBoxLayout()

        # Name input
        name_layout = QHBoxLayout()
        name_label = QLabel("Name:")
        name_layout.addWidget(name_label)
        self.name_input = QLineEdit()
        name_layout.addWidget(self.name_input)
        add_layout.addLayout(name_layout)

        # Phone input
        phone_layout = QHBoxLayout()
        phone_label = QLabel("Phone:")
        phone_layout.addWidget(phone_label)
        self.phone_input = QLineEdit()
        phone_layout.addWidget(self.phone_input)
        add_layout.addLayout(phone_layout)

        # email input
        email_layout = QHBoxLayout()
        email_label = QLabel("Email:")
        email_layout.addWidget(email_label)
        self.email_input = QLineEdit()
        email_layout.addWidget(self.email_input)
        add_layout.addLayout(email_layout)

        # Add button
        self.add_btn = QPushButton("Add Contact")
        add_layout.addWidget(self.add_btn)

        add_group.setLayout(add_layout)
        # Code for actioning the Add button
        main_layout.addWidget(add_group)



# Create the application object
app = QApplication(sys.argv)
# Create an instance of the main window
window = ContactBook()
# show the main window
window.show()
# Start the application's event loop
sys.exit(app.exec())

