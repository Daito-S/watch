from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import QTime

from clock import Clock
from schedule_table import Schedule_Table
from input_panel import Input_Panel

# メインのウィンドウ
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("スケジュール時間管理")

        self.clock = Clock()
        self.schedule = Schedule_Table()
        self.current_time = QTime(9, 0)

        self.input_panel = Input_Panel(self.add_schedule)

        layout = QVBoxLayout()
        layout.addWidget(self.clock)
        layout.addWidget(self.input_panel)
        layout.addWidget(self.schedule)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # スケジュール追加
    def add_schedule(self, name, minutes):
        start = self.current_time
        end = self.current_time.addSecs(minutes * 60)

        self.schedule.add_schedule(name, start, end)

        self.current_time = end
        self.clock.advance_minutes(minutes)
