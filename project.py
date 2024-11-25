# Import necessary PyQt5 modules
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
import sys

# Define the main window class
class DemoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("PyQt5 Demo App")
        self.setGeometry(100, 100, 400, 200)  # x, y, width, height

        # Create a layout
        layout = QVBoxLayout()

        # Add a label
        self.label = QLabel("Welcome to PyQt5!")
        layout.addWidget(self.label)

        # Add a button
        self.button = QPushButton("Click Me!")
        self.button.clicked.connect(self.on_button_click)  # Connect the button click to a function
        layout.addWidget(self.button)

        # Set the central widget and layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # Define the button click event
    def on_button_click(self):
        self.label.setText("You clicked the button!")  # Update the label text


# Main function to run the application
def main():
    app = QApplication(sys.argv)  # Create the application
    window = DemoApp()           # Create an instance of the main window
    window.show()                # Show the main window
    sys.exit(app.exec_())        # Run the application event loop


# Run the application if this script is executed
if __name__ == "__main__":
    main()
