from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QSpinBox, QPushButton, QLabel

# 入力用パネル
class Input_Panel(QWidget):
    def __init__(self, on_add, on_set_initial):
        super().__init__()
        layout_set_initial = QHBoxLayout()  # 水平レイアウト(初期時間)
        layout_add_schedule = QHBoxLayout()  # 水平レイアウト(予定追加)
        layout = QVBoxLayout()  # 全体のレイアウト(垂直)

        # ---初期時間---
        # 時間指定のスピンボックス(短針)
        self.initial_hour_spin = QSpinBox()
        self.initial_hour_spin.setRange(0, 12)
        self.initial_hour_spin.setSuffix(" 時")
        # 時間指定のスピンボックス(長針)
        self.initial_min_spin = QSpinBox()
        self.initial_min_spin.setRange(0, 59)
        self.initial_min_spin.setSuffix(" 分")
        # 初期時間設定のボタン
        self.set_initial_minutes_button = QPushButton("リセット")
        self.set_initial_minutes_button.clicked.connect(
            self.set_initial_time)
        # レイアウトに追加
        # 初期時間設定のラベル
        layout_set_initial.addWidget(QLabel("初期時間:"))
        layout_set_initial.addWidget(self.initial_hour_spin)
        layout_set_initial.addWidget(self.initial_min_spin)
        layout_set_initial.addWidget(self.set_initial_minutes_button)

        # ---予定とその時間の追加---
        self.on_add = on_add
        self.on_set_initial = on_set_initial
        # 予定名のテキスト
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("予定名")
        # 時間指定のスピンボックス
        self.time_spin = QSpinBox()
        self.time_spin.setRange(1, 600)
        self.time_spin.setSuffix(" 分")
        # 追加ボタン
        add_button = QPushButton("追加")
        add_button.clicked.connect(self.add_clicked)

        # レイアウトに追加
        layout_add_schedule.addWidget(QLabel("　予定　:"))
        layout_add_schedule.addWidget(self.name_edit)
        layout_add_schedule.addWidget(QLabel("時間:"))
        layout_add_schedule.addWidget(self.time_spin)
        layout_add_schedule.addWidget(add_button)

        # 全体のレイアウトに各部分を追加
        layout.addLayout(layout_set_initial)
        layout.addLayout(layout_add_schedule)

        self.setLayout(layout)

    # 初期時間設定ボタンがクリックされたときの処理
    def set_initial_time(self):
        hour = self.initial_hour_spin.value()
        minute = self.initial_min_spin.value()
        self.on_set_initial(hour, minute)

    # 追加ボタンがクリックされたときの処理
    def add_clicked(self):
        name = self.name_edit.text()
        minutes = self.time_spin.value()

        if name:
            self.on_add(name, minutes)
            self.name_edit.clear()
