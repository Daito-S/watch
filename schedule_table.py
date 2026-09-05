from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView, QCheckBox

class Schedule_Table(QTableWidget):
    def __init__(self):
        super().__init__(0, 4)
        self.setHorizontalHeaderLabels(["選択", "予定名", "開始時刻", "終了時刻"])
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.minutes_list = []

    # スケジュール追加
    def add_schedule(self, name, start_time, end_time):
        row = self.rowCount()
        self.insertRow(row)
        check_box = QCheckBox()

        self.setCellWidget(row, 0, check_box)
        self.setItem(row, 1, QTableWidgetItem(name))
        self.setItem(row, 2, QTableWidgetItem(start_time.toString("HH:mm")))
        self.setItem(row, 3, QTableWidgetItem(end_time.toString("HH:mm")))

        self.minutes_list.append(
            (end_time.msecsSinceStartOfDay() - start_time.msecsSinceStartOfDay()) // 60000)

    # 選択したスケジュールを削除
    def remove_selected_schedule(self):
        selected_rows = []

        for row in range(self.rowCount()):
            check_box = self.cellWidget(row, 0)

            if check_box is not None and check_box.isChecked():
                selected_rows.append(row)

        # 後から削除
        for row in reversed(selected_rows):
            check_box = self.cellWidget(row, 0)
            if check_box is not None:
                check_box.deleteLater()
            self.removeRow(row)
            self.minutes_list.pop(row)

        return bool(selected_rows)

    # 開始時刻を更新
    def update_start_times(self, new_start):
        current = new_start
        for row in range(self.rowCount()):
            minutes = self.minutes_list[row]
            end = current.addSecs(minutes * 60)
            self.setItem(row, 2, QTableWidgetItem(current.toString("HH:mm")))
            self.setItem(row, 3, QTableWidgetItem(end.toString("HH:mm")))
            current = end
        return current
