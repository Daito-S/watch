from PySide6.QtWidgets import QTableWidget, QTableWidgetItem
from PySide6.QtCore import QTime

class Schedule_Table(QTableWidget):
    def __init__(self):
        super().__init__(0, 3)
        self.setHorizontalHeaderLabels(["予定名", "開始時刻", "終了時刻"])
        self.minutes_list = []

    # スケジュール追加
    def add_schedule(self, name, start_time, end_time):
        row = self.rowCount()
        self.insertRow(row)

        self.setItem(row, 0, QTableWidgetItem(name))
        self.setItem(row, 1, QTableWidgetItem(start_time.toString("HH:mm")))
        self.setItem(row, 2, QTableWidgetItem(end_time.toString("HH:mm")))
        self.minutes_list.append(
            (end_time.msecsSinceStartOfDay() - start_time.msecsSinceStartOfDay()) // 60000)

    # 開始時刻を更新
    def update_start_times(self, new_start):
        # スケジュール表をリセット
        self.setRowCount(0)
        self.minutes_list.clear()

        current = new_start
        for i in range(self.rowCount()):
            minutes = self.minutes_list[i]
            end = current.addSecs(minutes * 60)
            self.setItem(i, 1, QTableWidgetItem(current.toString("HH:mm")))
            self.setItem(i, 2, QTableWidgetItem(end.toString("HH:mm")))
            current = end
