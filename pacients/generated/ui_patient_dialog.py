
from PySide6.QtCore import Qt, QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDialog,
    QDoubleSpinBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QListView
)


class Ui_Dialog(object):

    def setupUi(self, Dialog):

        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")

        Dialog.resize(389, 530)
        Dialog.setStyleSheet("background-color: #F5F4F0;")

        # КНОПКА СОХРАНИТЬ
        self.btn_save = QPushButton(Dialog)
        self.btn_save.setObjectName("btn_save")
        self.btn_save.setGeometry(QRect(59, 470, 137, 46))

        font = QFont()
        font.setFamilies(["Futura"])
        font.setWeight(QFont.DemiBold)

        self.btn_save.setFont(font)

        self.btn_save.setStyleSheet("""
            QPushButton {
                background-color: #EAF3B2;
                color: rgb(40, 55, 88);
                border: 1px solid #D4E384;
                border-radius: 22px;
                min-height: 44px;
                max-height: 44px;
                padding-left: 18px;
                padding-right: 22px;
                font-size: 14px;
                font-weight: 600;
            }

            QPushButton:hover {
                background-color: #DCE994;
                color: #FFFFFF;
                border: 1px solid #C2D468;
            }

            QPushButton:pressed {
                background-color: #CCE072;
                color: #FFFFFF;
                border: 1px solid #B0C952;
            }
        """)

        icon = QIcon()
        icon.addFile(
            "icons/save.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off
        )

        self.btn_save.setIcon(icon)
        self.btn_save.setIconSize(QSize(20, 20))


        # КНОПКА ОТМЕНА
        self.btn_cancel = QPushButton(Dialog)
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_cancel.setGeometry(QRect(210, 470, 117, 46))
        self.btn_cancel.setFont(font)

        self.btn_cancel.setStyleSheet("""
            QPushButton {
                background-color: #F6D8D8;
                color: #5C2323;
                border: 1px solid #E5B6B6;
                border-radius: 22px;
                min-height: 44px;
                max-height: 44px;
                padding-left: 18px;
                padding-right: 22px;
                font-size: 14px;
                font-weight: 600;
            }

            QPushButton:hover {
                background-color: #EBC0C0;
                color: #FFFFFF;
                border: 1px solid #D99E9E;
            }

            QPushButton:pressed {
                background-color: #D99B9B;
                color: #FFFFFF;
                border: 1px solid #C47E7E;
            }
        """)

        icon1 = QIcon()
        icon1.addFile(
            "icons/cancel.png",
            QSize(),
            QIcon.Mode.Normal,
            QIcon.State.Off
        )

        self.btn_cancel.setIcon(icon1)
        self.btn_cancel.setIconSize(QSize(20, 20))


        # ЗАГОЛОВОК
        self.label_title = QLabel(Dialog)
        self.label_title.setObjectName("label_name_6")
        self.label_title.setGeometry(QRect(0, 10, 391, 41))

        font1 = QFont()
        font1.setFamilies(["Futura"])
        font1.setPointSize(18)
        font1.setBold(True)

        self.label_title.setFont(font1)
        self.label_title.setStyleSheet("color: #24345C;")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_title.setWordWrap(True)


        # ОСНОВНОЙ ВИДЖЕТ
        self.widget = QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.widget.setGeometry(QRect(50, 70, 291, 392))

        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        font2 = QFont()
        font2.setFamilies(["Futura"])
        font2.setPointSize(18)

        # ФИО
        self.label_name = QLabel(self.widget)
        self.label_name.setObjectName("label_name")
        self.label_name.setFont(font2)
        self.label_name.setStyleSheet("color: #24345C;")

        self.verticalLayout.addWidget(self.label_name)

        self.edit_name = QLineEdit(self.widget)
        self.edit_name.setObjectName("edit_name")

        self.edit_name.setStyleSheet("""
            QLineEdit {
                background-color: #FDFDF5;
                color: #1E293B;
                border: 1px solid #C7D4EE;
                border-radius: 10px;
                min-height: 36px;
                max-height: 36px;
                padding-left: 12px;
                padding-right: 12px;
                font-size: 13px;
            }

            QLineEdit:hover {
                border: 1px solid #9FBAF1;
            }

            QLineEdit:focus {
                background-color: #FFFFFF;
                border: 2px solid #3D568F;
            }
        """)

        self.verticalLayout.addWidget(self.edit_name)

        # ВОЗРАСТ
        self.label_name_2 = QLabel(self.widget)
        self.label_name_2.setObjectName("label_name_2")
        self.label_name_2.setFont(font2)
        self.label_name_2.setStyleSheet("color: #24345C;")

        self.verticalLayout.addWidget(self.label_name_2)

        self.spin_age = QSpinBox(self.widget)
        self.spin_age.setObjectName("spin_age")
        self.spin_age.setRange(0, 120)

        self.spin_age.setStyleSheet("""
            QSpinBox {
                background-color: #FDFDF5;
                color: #1E293B;
                border: 1px solid #C7D4EE;
                border-radius: 10px;
                min-height: 36px;
                max-height: 36px;
                padding-left: 10px;
                padding-right: 6px;
                font-size: 13px;
            }

            QSpinBox:hover {
                border: 1px solid #9FBAF1;
            }

            QSpinBox:focus {
                background-color: #FFFFFF;
                border: 2px solid #3D568F;
            }

            QSpinBox::up-button:hover,
            QSpinBox::down-button:hover {
                background-color: #EAF3B2;
            }
        """)

        self.verticalLayout.addWidget(self.spin_age)


        # ПОЛ
        self.label_name_3 = QLabel(self.widget)
        self.label_name_3.setObjectName("label_name_3")
        self.label_name_3.setFont(font2)
        self.label_name_3.setStyleSheet("color: #24345C;")

        self.verticalLayout.addWidget(self.label_name_3)

        self.combo_gender = QComboBox(self.widget)
        self.combo_gender.setObjectName("combo_gender")

        self.combo_gender.addItem("")
        self.combo_gender.addItem("")
        self.combo_gender.addItem("")

        # Используем QListView для корректной подсветки пунктов
        self.combo_gender.setView(QListView())

        self.combo_gender.setStyleSheet("""
            QComboBox {
                background-color: #FDFDF5;
                color: #1E293B;
                border: 1px solid #C7D4EE;
                border-radius: 10px;
                min-height: 36px;
                max-height: 36px;
                padding-left: 12px;
                padding-right: 10px;
                font-size: 13px;
            }

            QComboBox:hover {
                border: 1px solid #9FBAF1;
            }

            QComboBox:focus,
            QComboBox:on {
                background-color: #FFFFFF;
                border: 2px solid #3D568F;
            }

            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 30px;
                border: none;
                border-radius: 0px 8px 8px 0px;
            }

            QComboBox::drop-down:hover {
                background-color: #EAF3B2;
            }

            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 6px solid #24345C;
            }

            QComboBox QAbstractItemView {
                background-color: #FDFDF5;
                color: #1E293B;
                border: 1px solid #9FBAF1;
                border-radius: 8px;
                outline: none;
                padding: 4px;
                selection-background-color: #3D568F;
                selection-color: #FFFFFF;
            }

            QComboBox QAbstractItemView::item {
                min-height: 30px;
                padding: 5px 8px;
                border-radius: 5px;
            }

            QComboBox QAbstractItemView::item:hover {
                background-color: #EAF3B2;
                color: #24345C;
            }

            QComboBox QAbstractItemView::item:selected {
                background-color: #3D568F;
                color: #FFFFFF;
            }
        """)

        self.verticalLayout.addWidget(self.combo_gender)

        # РОСТ
        self.label_height= QLabel(self.widget)
        self.label_height.setObjectName("label_name_4")
        self.label_height.setFont(font2)
        self.label_height.setStyleSheet("color: #24345C;")

        self.verticalLayout.addWidget(self.label_height)


        self.spin_height = QSpinBox(self.widget)
        self.spin_height.setObjectName("spin_height")

        self.spin_height.setRange(50, 250)
        self.spin_height.setValue(170)
        self.spin_height.setSingleStep(1)
        self.spin_height.setSuffix(" см")

        self.spin_height.setStyleSheet("""
            QSpinBox {
                background-color: #FDFDF5;
                color: #1E293B;
                border: 1px solid #C7D4EE;
                border-radius: 10px;
                min-height: 36px;
                max-height: 36px;
                padding-left: 10px;
                padding-right: 6px;
                font-size: 13px;
            }

            QSpinBox:hover {
                border: 1px solid #9FBAF1;
            }

            QSpinBox:focus {
                background-color: #FFFFFF;
                border: 2px solid #3D568F;
            }

            QSpinBox::up-button:hover,
            QSpinBox::down-button:hover {
                background-color: #EAF3B2;
            }
        """)

        self.verticalLayout.addWidget(self.spin_height)

        # ВЕС
        self.label_name_5 = QLabel(self.widget)
        self.label_name_5.setObjectName("label_name_5")
        self.label_name_5.setFont(font2)
        self.label_name_5.setStyleSheet("color: #24345C;")

        self.verticalLayout.addWidget(self.label_name_5)

        self.spin_weight = QDoubleSpinBox(self.widget)
        self.spin_weight.setObjectName("spin_weight")

        self.spin_weight.setRange(0, 500)
        self.spin_weight.setValue(60)
        self.spin_weight.setDecimals(1)
        self.spin_weight.setSingleStep(0.1)
        self.spin_weight.setSuffix(" кг")

        self.spin_weight.setStyleSheet("""
            QDoubleSpinBox {
                background-color: #FDFDF5;
                color: #1E293B;
                border: 1px solid #C7D4EE;
                border-radius: 10px;
                min-height: 36px;
                max-height: 36px;
                padding-left: 10px;
                padding-right: 6px;
                font-size: 13px;
            }

            QDoubleSpinBox:hover {
                border: 1px solid #9FBAF1;
            }

            QDoubleSpinBox:focus {
                background-color: #FFFFFF;
                border: 2px solid #3D568F;
            }

            QDoubleSpinBox::up-button:hover,
            QDoubleSpinBox::down-button:hover {
                background-color: #EAF3B2;
            }
        """)

        self.verticalLayout.addWidget(self.spin_weight)
        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)



    def retranslateUi(self, Dialog):

        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", "Dialog", None)
        )

        self.btn_save.setText(
            QCoreApplication.translate("Dialog", "Сохранить", None)
        )

        self.btn_cancel.setText(
            QCoreApplication.translate("Dialog", "Отмена", None)
        )

        self.label_title.setText(
            QCoreApplication.translate(
                "Dialog",
                "Добавление/редактирование пациента",
                None
            )
        )

        self.label_name.setText(
            QCoreApplication.translate("Dialog", "ФИО:", None)
        )

        self.edit_name.setText("")

        self.label_name_2.setText(
            QCoreApplication.translate("Dialog", "Возраст:", None)
        )

        self.label_name_3.setText(
            QCoreApplication.translate("Dialog", "Пол:", None)
        )

        self.combo_gender.setItemText(
            0,
            QCoreApplication.translate("Dialog", "Мужской", None)
        )

        self.combo_gender.setItemText(
            1,
            QCoreApplication.translate("Dialog", "Женский", None)
        )

        self.combo_gender.setItemText(
            2,
            QCoreApplication.translate("Dialog", "Неопределен", None)
        )

        self.label_height.setText(
            QCoreApplication.translate("Dialog", "Рост (см):", None)
        )

        self.label_name_5.setText(
            QCoreApplication.translate("Dialog", "Вес (кг):", None)
        )


# =========================
# ЗАПУСК ОКНА ДЛЯ ПРОВЕРКИ
# =========================
''' 
if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)

    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    Dialog.show()

    sys.exit(app.exec())
'''

