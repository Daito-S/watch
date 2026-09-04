from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView

class Schedule_Table(QTableWidget):
    def __init__(self):
        super().__init__(0, 3)
        self.setHorizontalHeaderLabels(["予定名", "開始時刻", "終了時刻"])
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
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

    # 選択したスケジュールを削除
    def remove_selected_schedule(self):
        rows = sorted({index.row()
                      for index in self.selectedIndexes()}, reverse=True)
        for row in rows:
            self.removeRow(row)
            self.minutes_list.pop(row)
        return bool(rows)

    # 開始時刻を更新
    def update_start_times(self, new_start):
        current = new_start
        for i in range(self.rowCount()):
            minutes = self.minutes_list[i]
            end = current.addSecs(minutes * 60)
            self.setItem(i, 1, QTableWidgetItem(current.toString("HH:mm")))
            self.setItem(i, 2, QTableWidgetItem(end.toString("HH:mm")))
            current = end
        return current
