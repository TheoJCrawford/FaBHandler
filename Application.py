from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget, QLabel, QVBoxLayout, QWindow
from PyQt5.QtGui import QPalette, QColor
import sys
from Character import Character

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.myCharacter = Character()
        self.setWindowTitle("My App")

        HealthMonitor = QHBoxLayout()
        decButton = QPushButton("-")
        self.healthLabel = QLabel(str(self.myCharacter.health))
        incButton = QPushButton("+")

        decButton.clicked.connect(self.LowerHealth)
        incButton.clicked.connect(self.raise_health)
        
        HealthMonitor.addWidget(decButton)
        HealthMonitor.addWidget(self.healthLabel)
        HealthMonitor.addWidget(incButton)

        primLayout = QVBoxLayout()
        self.Characer = QLabel(self.myCharacter.CharName)
        btnResetBtn = QPushButton("Reset")
        btnCharangeChar = QPushButton("Change Character")


        widget = QWidget()
        widget.setLayout(HealthMonitor)
        self.setCentralWidget(widget)

        self.setFixedSize(QSize(400,300))
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
    

class SelectWindow(QWindow):
    def __init__(self):
        super.__init__(self)
        self.ChangeButton = QPushButton("Blitz")
        
        SelectWindow = QVBoxLayout()
        SelectWindow.addWidget(self.ChangeButton)




app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
