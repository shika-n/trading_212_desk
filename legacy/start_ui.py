import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtQml import QQmlApplicationEngine

def main():
    app = QApplication(sys.argv)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('ui/main_window.qml')
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()