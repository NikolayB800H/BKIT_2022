from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

"""
Для приложения pyqt6
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel

"""
Моя кнопка
"""
class Button(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton("Выход", self)
        self.btn.setGeometry(100, 20, 100, 30)
        self.btn.clicked.connect(self.onClicked)
        self.setWindowTitle("Кнопка")
        self.setGeometry(10, 10, 300, 70)
        self.show()

    def onClicked(self):
        print("Пока!")
        QApplication.quit()

def main():
    r = Rectangle("синего", 3, 3)
    c = Circle("зеленого", 3)
    s = Square("красного", 3)
    print(r)
    print(c)
    print(s)
    """
    Приложение pyqt6
    """
    app = QApplication(sys.argv)
    button = Button()
    app.exec()

if __name__ == "__main__":
    main()
