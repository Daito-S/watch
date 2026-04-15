import math
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen, QFont
from PySide6.QtCore import QTimer, Qt, QTime

# 時計表示
class Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.minutes_angle = 0
        self.hour_angle = 0
        self.current_time = QTime(0, 0)
        self.setMinimumSize(200, 200)

        timer = QTimer(self)
        timer.start(100)

    # 短針を1時間分(30度)回す
    def update_hour_angle(self):
        self.hour_angle = (self.hour_angle + 30) % 360
        self.update()

    # 長針を進める(1分で6度)
    def advance_minutes(self, minutes):
        # 変更前の分を取得(短針の更新判定に使用)
        last_minutes = self.minutes_angle // 6 % 60

        self.minutes_angle = (self.minutes_angle + minutes * 6) % 360  # 更新
        self.current_time = self.current_time.addSecs(minutes * 60)

        # 短針更新の判定
        if last_minutes + minutes >= 60:
            count = (last_minutes + minutes) // 60
            for i in range(count):
                self.update_hour_angle()
        self.update()

    # 針の角度を設定
    def set_angles(self, hour, minute):
        self.current_time = QTime(hour, minute)
        self.hour_angle = (hour % 12) * 30 + minute * 0.5
        self.minutes_angle = minute * 6
        self.update()

    # 描画(update()時に実行)
    def paintEvent(self, event):
        # 時計の針を描画
        # 時計の中心から針の先端までの座標を計算して線を描く
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 長針と短針の描画をfor文でまとめる
        for angle, width in [(self.hour_angle, 6), (self.minutes_angle, 4)]:
            # 時計の中心と針の先端の座標を計算(短針なら長さは短く、長針なら長く)
            cx = self.width() / 2
            cy = self.height() / 2
            length = min(cx, cy) * (0.5 if width == 6 else 0.8)

            rad = math.radians(angle)
            x = cx + length * math.sin(rad)
            y = cy - length * math.cos(rad)

            pen = QPen(Qt.black, width)
            painter.setPen(pen)
            painter.drawLine(cx, cy, x, y)

        # デジタル表示
        time_str = self.current_time.toString("HH:mm")
        font = QFont("Arial", 16)
        painter.setFont(font)
        painter.drawText(cx - 30, cy + 50, time_str)
