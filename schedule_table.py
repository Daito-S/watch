from PySide6.QtWidgets import QTableWidget, QTableWidgetItem

class Schedule_Table(QTableWidget):
    def __init__(self):
        super().__init__(0, 3)
        self.setHorizontalHeaderLabels(["予定名", "開始時刻", "終了時刻"])

    # スケジュール追加
    def add_schedule(self, name, start_time, end_time):
        row = self.rowCount()
        self.insertRow(row)

        self.setItem(row, 0, QTableWidgetItem(name))
        self.setItem(row, 1, QTableWidgetItem(start_time.toString("HH:mm")))
        self.setItem(row, 2, QTableWidgetItem(end_time.toString("HH:mm")))
