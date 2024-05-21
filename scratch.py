import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget, QLabel, QTabWidget, QWidget
from PyQt6.QtWidgets import QWidgetAction, QMessageBox


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Split Window Example")
        self.setMinimumSize(500, 300)
        self.setGeometry(100, 100, 900, 600)
        self.init2()
        self.init1()

    def init2(self):
        # Create the menu bar
        menubar = self.menuBar()

        # Create a dropdown menu
        menu = menubar.addMenu('&Menu')
        menu.addAction('Switch to Admin Mode', self.switch_to_admin_mode)
        menu.addAction('Switch to User Mode', self.switch_to_user_mode)
        menu.addSeparator()  # Add a separator line
        menu.addAction('Exit', self.exit_application)

    def switch_to_admin_mode(self):
        # Placeholder function for switching to admin mode
        QMessageBox.information(self, "Admin Mode", "Switched to Admin Mode")

    def switch_to_user_mode(self):
        # Placeholder function for switching to user mode
        QMessageBox.information(self, "User Mode", "Switched to User Mode")

    def exit_application(self):
        # Exit the application
        self.close()

    def init1(self):
        self.central_widget = QFrame(self)
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # Create the first frame
        self.frame1 = QFrame(self.central_widget)
        layout.addWidget(self.frame1, 1)  # 33% of window height
        self.frame1.setStyleSheet("background-color: lightblue;")

        # Create the second frame
        self.frame2 = QFrame(self.central_widget)
        layout.addWidget(self.frame2, 6)  # Takes up rest of the space
        self.frame2.setStyleSheet("background-color: lightgreen;")

        # Create a stacked widget
        self.stacked_widget = QStackedWidget(self.frame2)

        # Create two frames to switch between
        self.subframe1 = QFrame()
        self.subframe2 = QFrame()

        # Add frames to the stacked widget
        self.stacked_widget.addWidget(self.subframe1)
        self.stacked_widget.addWidget(self.subframe2)

        # Add the toggle button to frame1
        self.toggle_button = QPushButton("Switch to Frame 2", self.frame1)
        self.toggle_button.clicked.connect(self.toggle_frames)

        frame1_layout = QVBoxLayout(self.frame1)
        frame1_layout.addWidget(self.toggle_button)
        frame1_layout.addStretch()  # Push button to the top

        # Add content to subframe1
        self.subframe1_layout = QVBoxLayout(self.subframe1)
        # self.subframe1_layout.addWidget(QLabel("Content for Frame 1"))

        # Create subframe1
        subframe1 = QWidget()
        subframe1.setStyleSheet("background-color: lightblue;")

        # Create layout for subframe1

        # Create two buttons aligned horizontally to the top
        button_layout = QHBoxLayout()
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button_layout.addWidget(button1)
        button_layout.addWidget(button2)
        self.subframe1_layout.addLayout(button_layout)

        # Create subframe11
        subframe11 = QWidget()
        subframe11.setStyleSheet("background-color: pink;")
        # subframe11.
        self.subframe1_layout.addWidget(subframe11)




        # Layout for subframe2
        self.subframe2_layout = QVBoxLayout(self.subframe2)

        # Create a horizontal layout for the buttons
        buttons_layout = QHBoxLayout()
        self.button1 = QPushButton("Button 1", self.subframe2)
        self.button2 = QPushButton("Button 2", self.subframe2)
        buttons_layout.addWidget(self.button1)
        buttons_layout.addWidget(self.button2)
        buttons_layout.addStretch()  # Push buttons to the left

        self.subframe2_layout.addLayout(buttons_layout)

        # Create a tab widget
        self.tab_widget = QTabWidget(self.subframe2)
        self.subframe2_layout.addWidget(self.tab_widget)

        # Add tabs to the tab widget
        tab1 = QWidget()
        tab2 = QWidget()
        tab3 = QWidget()
        tab4 = QWidget()
        tab5 = QWidget()
        tab6 = QWidget()
        tab7 = QWidget()
        self.tab_widget.addTab(tab1, "Tab 1")
        self.tab_widget.addTab(tab2, "Tab 2")
        self.tab_widget.addTab(tab3, "Tab 3")
        self.tab_widget.addTab(tab4, "Tab 4")
        self.tab_widget.addTab(tab5, "Tab 5")
        self.tab_widget.addTab(tab6, "Tab 6")
        self.tab_widget.addTab(tab7, "Tab 7")

        # Add content to tabs
        tab1_layout = QVBoxLayout(tab1)
        tab1_layout.addWidget(QLabel("Content for Tab 1"))

        tab2_layout = QVBoxLayout(tab2)
        tab2_layout.addWidget(QLabel("Content for Tab 2"))

        tab3_layout = QVBoxLayout(tab3)
        tab3_layout.addWidget(QLabel("Content for Tab 3"))

        tab4_layout = QVBoxLayout(tab4)
        tab4_layout.addWidget(QLabel("Content for Tab 4"))

        tab5_layout = QVBoxLayout(tab5)
        tab5_layout.addWidget(QLabel("Content for Tab 5"))

        tab6_layout = QVBoxLayout(tab6)
        tab6_layout.addWidget(QLabel("Content for Tab 6"))

        tab7_layout = QVBoxLayout(tab7)
        tab7_layout.addWidget(QLabel("Content for Tab 7"))

        # Add the stacked widget to frame2 layout
        frame2_layout = QVBoxLayout(self.frame2)
        frame2_layout.addWidget(self.stacked_widget)

        # Initially show the first frame
        self.stacked_widget.setCurrentWidget(self.subframe1)

    def toggle_frames(self):
        # Check which frame is currently displayed and switch to the other
        if self.stacked_widget.currentWidget() == self.subframe1:
            self.stacked_widget.setCurrentWidget(self.subframe2)
            self.toggle_button.setText("Switch to Frame 1")
        else:
            self.stacked_widget.setCurrentWidget(self.subframe1)
            self.toggle_button.setText("Switch to Frame 2")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
