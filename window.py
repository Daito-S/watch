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
        self.initial_time = self.current_time

        self.input_panel = Input_Panel(
            self.add_schedule, self.set_initial_time, self.delete_schedule)

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

    # 初期時間設定
    def set_initial_time(self, hour, minute):
        self.current_time = QTime(hour, minute)
        self.initial_time = self.current_time
        self.current_time = self.schedule.update_start_times(self.initial_time)
        self.clock.set_angles(hour, minute)

    # 選択したスケジュールを削除
    def delete_schedule(self):
        if self.schedule.remove_selected_schedule():
            self.current_time = self.schedule.update_start_times(
                self.initial_time)
            self.clock.set_angles(
                self.current_time.hour(), self.current_time.minute())
