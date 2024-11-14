from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QWidget, QLabel
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
        incButton.clicked.connect(self.RaiseHealth)
        

        HealthMonitor.addWidget(decButton)
        HealthMonitor.addWidget(self.healthLabel)
        HealthMonitor.addWidget(incButton)


        widget = QWidget()
        widget.setLayout(HealthMonitor)
        self.setCentralWidget(widget)

        self.setFixedSize(QSize(400,300))
    def LowerHealth(self):
        self.myCharacter.health-=1
        self.UpdateHealthText()

    def RaiseHealth(self):
        self.myCharacter.health += 1
        self.UpdateHealthText()

    def UpdateHealthText(self):
        if(self.myCharacter.health > 0):
            self.healthLabel.setText(str(self.myCharacter.health))
        else:
            self.healthLabel.setText("You have lost!")
    


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
