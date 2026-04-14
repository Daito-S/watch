import sys
from PySide6.QtWidgets import QApplication
from main_window import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.resize(500, 700)
window.show()
app.exec()
