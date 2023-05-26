from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QVBoxLayout, QMainWindow, QLineEdit
from PySide6.QtGui import QFont, QAction
from PySide6.QtCore import Qt
from qdarktheme import load_stylesheet


def callback():
    print('Cliquei no botão!')


def callback2():
    print('Outra coisa!')


app = QApplication()
app.setStyleSheet(load_stylesheet())


class WindowLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        base = QWidget()
        layout = QVBoxLayout()

        QApplication.setApplicationName("Horoscopo do Dia")

        font = QFont("Inter")
        font.setPixelSize(25)

        self.label = QLabel('Tela de Login')
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag(Qt.AlignCenter))

        button = QPushButton('Login')
        button.setFont(font)
        button.clicked.connect(callback)
        button.clicked.connect(self.change_label)

        # Campos
        self.login_field = QLineEdit()
        self.password_field = QLineEdit()
        self.password_field.setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(self.label)

        layout.addWidget(self.login_field)
        layout.addWidget(self.password_field)
        layout.addWidget(button)

        base.setLayout(layout)

        self.setCentralWidget(base)

    def change_label(self):
        psswrd = self.password_field.text()
        user = self.login_field.text()

        if user == "ABA" and psswrd == "123":
            self.label.setText("APROVADO")
            window = WindowProfile()
            window.show()


class WindowProfile(QMainWindow):
    def __init__(self):
        super().__init__()
        base = QWidget()
        layout = QVBoxLayout()

        QApplication.setApplicationName("Horoscopo do Dia")

        font = QFont("Inter")
        font.setPixelSize(25)

        label = QLabel('Tela de Login')
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag(Qt.AlignCenter))

        layout.addWidget(label)

        base.setLayout(layout)

        self.setCentralWidget(base)


window = WindowLogin()
window.show()

app.exec()
