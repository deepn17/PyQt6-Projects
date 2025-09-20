from PyQt6.QtWidgets import (QMainWindow, QApplication, QWidget,
                             QVBoxLayout, QGroupBox, QLabel,
                             QHBoxLayout, QLineEdit, QPushButton,
                             QListWidget, QMessageBox)
import sys
import json

# Define the main window class for the contact book application
class ContactBook(QMainWindow):

    def __init__(self):
        super().__init__() # Initialize the parent QMainWindow
        self.contacts = {}
        self.initUI() # Set up the user interface
        self.load_contacts()
    
    def initUI(self):
        # Set the window title and size
        self.setWindowTitle("Contact Book") # Sets the title of the main window
        self.setGeometry(100, 100, 500, 600) # Sets the position and size of the window


        # Create the central widget and set it for the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        # Create a vertical layout for the central widget
        main_layout = QVBoxLayout(central_widget)

        # Create a group box for adding a new contact
        add_group = QGroupBox("Add New Contact")
        add_layout = QVBoxLayout()

        # --- Name input section ---
        name_layout = QHBoxLayout()  # Horizontal layout for name
        name_label = QLabel("Name:") # Label for name
        name_layout.addWidget(name_label) # Add label to layout
        self.name_input = QLineEdit() # Text input for name
        name_layout.addWidget(self.name_input) # Add input to layout
        add_layout.addLayout(name_layout) # Add name layout to group box layout

        # --- Phone input section ---
        phone_layout = QHBoxLayout()   # Horizontal layout for phone
        phone_label = QLabel("Phone:") # Label for phone
        phone_layout.addWidget(phone_label) # Add label to layout
        self.phone_input = QLineEdit() # Text input for phone
        phone_layout.addWidget(self.phone_input) # Add input to layout
        add_layout.addLayout(phone_layout) # Add phone layout to group box layout

        # --- Email input section ---
        email_layout = QHBoxLayout()  # Horizontal layout for email
        email_label = QLabel("Email:") # Label for email
        email_layout.addWidget(email_label) # Add label to layout
        self.email_input = QLineEdit() # Text input for email
        email_layout.addWidget(self.email_input) # Add input to layout
        add_layout.addLayout(email_layout) # Add email layout to group box layout

        # --- Add Contact button ---
        self.add_btn = QPushButton("Add Contact") # Button to add contact
         # Code for actioning the Add button
        self.add_btn.clicked.connect(self.add_contact)
        add_layout.addWidget(self.add_btn)     # Add button to group box layout


        add_group.setLayout(add_layout)  # Set the layout for the group box
        # Add the group box to the main layout of the central widget
        main_layout.addWidget(add_group)

        

        # --- Contact List ---
        contact_label = QLabel("Contacts:")
        main_layout.addWidget(contact_label)
        self.contact_list = QListWidget()
        # Add Action item for contact list
        self.contact_list.itemClicked.connect(self.show_contact_details)
        main_layout.addWidget(self.contact_list)


        # Delete button and save button
        button_layout = QHBoxLayout()
        self.delete_btn = QPushButton("Delete Selected")
        button_layout.addWidget(self.delete_btn)

        self.save_btn = QPushButton("Save Contacts")
        self.save_btn.clicked.connect(self.save_contacts)
        button_layout.addWidget(self.save_btn)

        main_layout.addLayout(button_layout)

    

    def add_contact(self):
        # get input values
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()
        email = self.email_input.text().strip()

        # simple validation
        if not name:
            QMessageBox.warning(self, "Warning", "Name cannot be empty")
            return
        self.contacts[name] = {"phone": phone, "email": email}
        self.update_contact_list()
        
        # clear inputs
        self.name_input.clear()
        self.phone_input.clear()
        self.email_input.clear()

        QMessageBox.information(self, "Success", f"Contact {name} added!")
    
    def update_contact_list(self):
        self.contact_list.clear()
        for name in sorted(self.contacts.keys()):
            self.contact_list.addItem(name)
    
    def show_contact_details(self, item):
        """Display phone and email for the selected contact"""
        name = item.text()
        contact = self.contacts[name]
        details = f"Name: {name} \nPhone: {contact['phone']} \nEmail: {contact['email']}"
        QMessageBox.information(self, "Contact Details", details)
    

    def save_contacts(self):
        """Save contacts to contacts.json"""
        try:
            with open("contacts.json", "w") as f:
                json.dump(self.contacts, f)
            QMessageBox.information(self, "Success", "Contacts Saved.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not save contacts: {e}")
    

    def load_contacts(self):
        """Load contacts from contacts.json if it exists"""
        try:
            with open("contacts.json", "r") as f:
                self.contacts = json.load(f)
            self.update_contact_list()
        except FileNotFoundError:
            self.contacts = {}
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not load contacts: {e}")




# Create the application object
app = QApplication(sys.argv)
# Create an instance of the main window
window = ContactBook()
# show the main window
window.show()
# Start the application's event loop
sys.exit(app.exec())

