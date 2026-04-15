from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QSpinBox, QPushButton, QLabel

# 入力用パネル
class Input_Panel(QWidget):
    def __init__(self, on_add):
        super().__init__()
        layout = QHBoxLayout()
        # ---初期時間---
        # 初期時間設定のボタン
        self.set_initial_minutes_button = QPushButton("初期時間設定")
        self.set_initial_minutes_button.clicked.connect(
            self.set_initial_minutes)
        # 時間指定のスピンボックス(短針)
        self.initial_hour_spin = QSpinBox()
        self.initial_hour_spin.setRange(1, 12)
        self.initial_hour_spin.setSuffix(" 時")
        # 時間指定のスピンボックス(長針)
        self.initial_min_spin = QSpinBox()
        self.initial_min_spin.setRange(0, 59)
        self.initial_min_spin.setSuffix(" 分")
        # レイアウトに追加
        layout.addWidget(self.set_initial_minutes_button)
        layout.addWidget(self.initial_hour_spin)
        layout.addWidget(self.initial_min_spin)


        # ---予定とその時間の追加---
        self.on_add = on_add


        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("予定名")

        self.time_spin = QSpinBox()
        self.time_spin.setRange(1, 600)
        self.time_spin.setSuffix(" 分")

        add_button = QPushButton("追加")
        add_button.clicked.connect(self.add_clicked)

        layout.addWidget(QLabel("予定:"))
        layout.addWidget(self.name_edit)
        layout.addWidget(QLabel("時間:"))
        layout.addWidget(self.time_spin)
        layout.addWidget(add_button)

        self.setLayout(layout)

    # 初期時間設定ボタンがクリックされたときの処理
    def set_initial_minutes(self):
        minutes = self.initial_minutes_spin.value()
        self.on_add("初期時間", minutes)

    # 追加ボタンがクリックされたときの処理
    def add_clicked(self):
        name = self.name_edit.text()
        minutes = self.time_spin.value()

        if name:
            self.on_add(name, minutes)
            self.name_edit.clear()
