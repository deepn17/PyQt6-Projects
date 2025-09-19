from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget)
import sys

# Define the main window class for the contact book application
class ContactBook(QMainWindow):

    def __init__(self):
        super().__init__() # Initialize the parent QMainWindow
        self.initUI()
    
    def initUI(self):
        pass

# Create the application object
app = QApplication(sys.argv)
# Create an instance of the main window
window = ContactBook()
# show the main window
window.show()
# Start the application's event loop
sys.exit(app.exec())

