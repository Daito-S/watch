import math
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen
from PySide6.QtCore import QTimer, Qt

# 時計表示
class Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.angle = 0
        self.setMinimumSize(200, 200)

        timer = QTimer(self)
        # timer.timeout.connect(self.update_angle)
        timer.start(100)

    # 針を1分(6度)回す
    def update_angle(self):
        self.angle = (self.angle + 6) % 360
        self.update()

    # 針を進める
    def advance_minutes(self, minutes):
        self.angle = (self.angle + minutes * 6) % 360
        self.update()

    # 描画(update()時に実行)
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        w, h = self.width(), self.height()
        cx, cy = w // 2, h // 2
        length = min(w, h) // 2 - 10

        rad = math.radians(self.angle)
        x = cx + length * math.sin(rad)
        y = cy - length * math.cos(rad)

        pen = QPen(Qt.black, 4)
        painter.setPen(pen)
        painter.drawLine(cx, cy, x, y)
