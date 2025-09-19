from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget,
                             QVBoxLayout, QGroupBox)
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

        add_group.setLayout(add_layout)
        main_layout.addWidget(add_group)



# Create the application object
app = QApplication(sys.argv)
# Create an instance of the main window
window = ContactBook()
# show the main window
window.show()
# Start the application's event loop
sys.exit(app.exec())

