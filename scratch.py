import sys
import sqlite3
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QFrame, QVBoxLayout, QHBoxLayout, QPushButton,
    QStackedWidget, QLabel, QTabWidget, QWidget, QMessageBox, QCalendarWidget
)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Room Reservation System")
        self.setMinimumSize(500, 300)
        self.setGeometry(100, 100, 900, 600)
        self.calendar = QCalendarWidget()
        self.init2()
        self.init1()
        self.init3()

    # <--------- USER CONTROL --------->
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
        self.setWindowTitle("Room Reservation System (ADMIN)")
        self.isAdmin = True
        print(self.isAdmin)
        QMessageBox.information(self, "Admin Mode", "Switched to Admin Mode")

    def switch_to_user_mode(self):
        # Placeholder function for switching to user mode
        self.setWindowTitle("Room Reservation System")
        self.isAdmin = False
        print(self.isAdmin)
        QMessageBox.information(self, "User Mode", "Switched to User Mode")

    def exit_application(self):
        # Exit the application
        self.close()

    # <--------- MAIN WINDOW --------->
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
        self.subframe11 = QWidget()
        self.subframe11.setStyleSheet("background-color: pink;")
        self.subframe1_layout.addWidget(self.subframe11)

        # Layout for subframe11
        subframe11_layout = QHBoxLayout(self.subframe11)

        # Create subframe111
        self.subframe111 = QWidget()
        self.subframe111.setStyleSheet("background-color: lightgray;")
        subframe111_layout = QVBoxLayout(self.subframe111)
        subframe111_layout.addWidget(QLabel("Subframe 111"))

        # Create subframe112
        self.subframe112 = QWidget()
        self.subframe112.setStyleSheet("background-color: lightyellow;")
        subframe112_layout = QVBoxLayout(self.subframe112)

        # Create calendar widget for subframe112
        self.calendar_widget = QCalendarWidget()
        subframe112_layout.addWidget(self.calendar_widget, 1)

        # Create subframe1121
        self.subframe1121 = QWidget()
        self.subframe1121.setStyleSheet("background-color: lightcoral;")
        subframe1121_layout = QVBoxLayout(self.subframe1121)
        subframe1121_layout.addWidget(QLabel("Subframe 1121"))
        subframe112_layout.addWidget(self.subframe1121, 2)

        # Add subframe111 and subframe112 to subframe11 layout
        subframe11_layout.addWidget(self.subframe111, 2)  # 2/3 of the space
        subframe11_layout.addWidget(self.subframe112, 1)  # 1/3 of the space

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

    # <--------- MYSQL MAIN --------->
    def init3(self):
        # Connect to SQLite database (creates if not exists)
        connection = sqlite3.connect('roomreserve.db')

        # Create cursor object to execute SQL queries
        cursor = connection.cursor()

        # Create 'sched' table
        cursor.execute('''CREATE TABLE IF NOT EXISTS sched (
                            date VARCHAR(7) PRIMARY KEY
                          )''')

        # Create 'room' table
        cursor.execute('''CREATE TABLE IF NOT EXISTS room (
                            room_ID VARCHAR(5) PRIMARY KEY
                          )''')

        # Create 'timeslot' table with compound primary key
        cursor.execute('''CREATE TABLE IF NOT EXISTS timeslot (
                            date VARCHAR(7),
                            room_ID VARCHAR(5),
                            slot_6_7_30am TINYTEXT,
                            slot_7_30_9am TINYTEXT,
                            slot_9_10_30am TINYTEXT,
                            slot_10_30_12pm TINYTEXT,
                            slot_12_1_30pm TINYTEXT,
                            slot_1_30_3pm TINYTEXT,
                            slot_3_4_30pm TINYTEXT,
                            slot_4_30_6pm TINYTEXT,
                            PRIMARY KEY (date, room_ID),
                            FOREIGN KEY (date) REFERENCES sched(date),
                            FOREIGN KEY (room_ID) REFERENCES room(room_ID)
                          )''')

        # Add room IDs to the room table
        room_ids = [
            'FH101', 'FH102', 'FH103', 'FH104', 'FH105',
            'FH201', 'FH202', 'FH203', 'FH204', 'FH205', 'FH206',
            'FH301', 'FH302', 'FH303', 'FH304', 'FH305', 'FH306'
        ]

        for room_id in room_ids:
            # Check if the room ID already exists in the room table
            cursor.execute("SELECT room_ID FROM room WHERE room_ID = ?", (room_id,))
            existing_room = cursor.fetchone()
            if existing_room:
                print("Room ID", room_id, "already exists.")
            else:
                # Insert the room ID if it doesn't already exist
                cursor.execute("INSERT INTO room (room_ID) VALUES (?)", (room_id,))
                print("Inserted room ID:", room_id)
            print('executed')

        # Select all rows from the room table
        cursor.execute("SELECT * FROM room")

        # Fetch all rows
        room_records = cursor.fetchall()

        # Print the room table
        print("Room Table:")
        print("-----------")
        for record in room_records:
            print(record[0])  # Assuming the room_ID is the first column in the table

        # Commit changes to the database
        connection.commit()

        # Close cursor and connection
        cursor.close()
        connection.close()

        print('SQL init Complete')
        print(self.isAdmin)

    isAdmin = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
