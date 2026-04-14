from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout
from PySide6.QtCore import QTime

from clock import Clock
from schedule import Schedule
from input_panel import InputPanel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("スケジュール時間管理")

        self.clock = Clock()
        self.schedule = Schedule()
        self.current_time = QTime(9, 0)

        self.input_panel = InputPanel(self.add_schedule)

        layout = QVBoxLayout()
        layout.addWidget(self.clock)
        layout.addWidget(self.input_panel)
        layout.addWidget(self.schedule)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_schedule(self, name, minutes):
        start = self.current_time
        end = self.current_time.addSecs(minutes * 60)

        self.schedule.add_schedule(name, start, end)

        self.current_time = end
        self.clock.advance_minutes(minutes)
