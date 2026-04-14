from PySide6.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QSpinBox, QPushButton, QLabel

# 入力用パネル
class Input_Panel(QWidget):
    def __init__(self, on_add):
        super().__init__()
        self.on_add = on_add

        layout = QHBoxLayout()

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

    def add_clicked(self):
        name = self.name_edit.text()
        minutes = self.time_spin.value()

        if name:
            self.on_add(name, minutes)
            self.name_edit.clear()
