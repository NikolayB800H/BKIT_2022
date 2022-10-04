from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


# Проверяем работу pyqt6:
import sys
from PyQt6.QtWidgets import QApplication, QPushButton
app = QApplication(sys.argv)
window = QPushButton("Hello, world!")
window.show()
app.exec()
#

def main():
    r = Rectangle("синего", 3, 2)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()
