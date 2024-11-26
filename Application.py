from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor, QWindow
import sys
from Character import Character

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myCharacter = Character()
        self.setWindowTitle("My App")

        self.healthWidget = QWidget(self)
        self.HealthMonitor = QHBoxLayout()
        self.decButton = QPushButton("-")
        self.healthLabel = QLabel(str(self.myCharacter.health))
        self.incButton = QPushButton("+")

        self.decButton.clicked.connect(self.LowerHealth)
        self.incButton.clicked.connect(self.raise_health)
        
        self.HealthMonitor.addWidget(self.decButton)
        self.HealthMonitor.addWidget(self.healthLabel)
        self.HealthMonitor.addWidget(self.incButton)

        self.primLayout = QVBoxLayout()
        self.Characer = QLabel(self.myCharacter.CharName)
        self.btnResetBtn = QPushButton("Reset")

        self.select_window = SelectWindow()  # Create the SelectWindow instance
        self.btnCharangeChar = QPushButton("Change Character")
        self.btnCharangeChar.clicked.connect(self.show_select_window)

        self.primLayout.addWidget(self.Characer)
        self.primLayout.addWidget(self.healthWidget)
        self.primLayout.addWidget(self.btnResetBtn)
        self.primLayout.addWidget(self.btnCharangeChar)

        self.healthWidget.setLayout(self.HealthMonitor)


        mainApp = QWidget()
        mainApp.setLayout(self.primLayout)
        self.setCentralWidget(mainApp)

        
    def LowerHealth(self):
        self.myCharacter.health-=1
        self.update_health_text()

    def raise_health(self):
        self.myCharacter.health += 1
        self.update_health_text()

    def update_health_text(self):
        if(self.myCharacter.health > 0):
            self.healthLabel.setText(str(self.myCharacter.health))
        else:
            self.healthLabel.setText("You have lost!")
    
    def show_select_window(self):
        self.select_window.show()

class SelectWindow(QWidget):  # Change to inherit QWidget
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Select Character")
        self.ChangeButton = QPushButton("Blitz")
        self.charSelect = Q
        layout = QVBoxLayout()
        layout.addWidget(self.ChangeButton)
        self.setLayout(layout)




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
