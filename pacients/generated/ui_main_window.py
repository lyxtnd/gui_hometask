from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QHeaderView, QLabel, QMainWindow, QPushButton, QSizePolicy, QTableWidget, QVBoxLayout, QWidget)
from generated.ui_patient_dialog import Ui_Dialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow: QMainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 550)
        MainWindow.setMinimumSize(760, 440)
        MainWindow.setStyleSheet(u"""
            QMainWindow {
                background-color: #F5F4F0;
            }
            QLabel {
                color: #24345C;
            }
        """)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(28, 18, 28, 22)
        self.main_layout.setSpacing(10)

        # Заголовок
        self.label_title = QLabel(self.centralwidget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self._base_title_font = QFont()
        self._base_title_font.setFamilies([u"Futura"])
        self._base_title_font.setPointSize(34)
        self._base_title_font.setBold(True)
        self.label_title.setFont(self._base_title_font)
        self.main_layout.addWidget(self.label_title)

        # Подзаголовок со счётчиком
        self.label_count = QLabel(self.centralwidget)
        self.label_count.setObjectName(u"label_count")
        self.label_count.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        self._base_count_font = QFont()
        self._base_count_font.setFamilies([u"Futura"])
        self._base_count_font.setPointSize(18)
        self._base_count_font.setBold(False)
        self._base_count_font.setItalic(True)
        self.label_count.setFont(self._base_count_font)
        self.main_layout.addWidget(self.label_count)

        # Контейнер таблицы для корректного скругления всех углов (включая шапку и низ)
        self.table_frame = QFrame(self.centralwidget)
        self.table_frame.setObjectName(u"table_frame")
        self.table_frame.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.table_frame.setStyleSheet(u"""
            QFrame#table_frame {
                background-color: #FDFDF5;
                border: 2px solid #DCE3EC;
                border-radius: 12px;
            }
        """)

        self.table_layout = QVBoxLayout(self.table_frame)
        self.table_layout.setObjectName(u"table_layout")
        self.table_layout.setContentsMargins(2, 2, 2, 2)
        self.table_layout.setSpacing(0)

        self.table_pacients = QTableWidget(self.table_frame)
        self.table_pacients.setObjectName(u"table_pacients")
        self.table_pacients.setColumnCount(6)

        self._headers = [
            "ФИО",
            "Возраст",
            "Пол",
            "Рост, см",
            "Вес, кг",
            "ИМТ",
        ]
        # Пропорциональные веса столбцов и их минимально комфортная ширина (px)
        self._column_weights = [3.4, 1.0, 1.35, 1.25, 1.25, 1.0]
        self._column_min_widths = [220, 85, 115, 110, 110, 85]
        self._last_table_width = -1

        self.table_pacients.setHorizontalHeaderLabels(self._headers)

        self._base_table_font = QFont()
        self._base_table_font.setFamilies([u"Futura"])
        self._base_table_font.setPointSize(14)
        self._base_table_font.setBold(False)
        self.table_pacients.setFont(self._base_table_font)

        self._base_header_font_pt = 12
        self.table_pacients.setStyleSheet(u"""
            QTableWidget {
                background-color: #FDFDF5;
                alternate-background-color: #F1F5FC;
                color: #24345C;
                gridline-color: #D5DDF0;
                border: none;
                border-radius: 10px;
                selection-background-color: #DCE7FC;
                selection-color: #182544;
            }

            QTableWidget::item {
                padding: 6px 10px;
            }

            QHeaderView {
                background-color: #24345C;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }

            QHeaderView::section {
                background-color: #24345C;
                color: #FDFDF5;
                padding: 10px 8px;
                border: none;
                border-right: 1px solid #3F558A;
                font-family: "Futura";
                font-weight: bold;
                font-size: 12pt;
            }

            QHeaderView::section:last {
                border-right: none;
            }
        """)

        # Интерактивный режим позволяет пользователю тянуть разделители вручную,
        # а при изменении размера таблицы пересчитываем ширины пропорционально
        header = self.table_pacients.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        header.setMinimumSectionSize(60)
        header.setStretchLastSection(False)

        self.table_pacients.setAlternatingRowColors(True)
        self.table_pacients.verticalHeader().setVisible(False)
        self.table_pacients.verticalHeader().setDefaultSectionSize(36)

        self.table_layout.addWidget(self.table_pacients)
        self.main_layout.addWidget(self.table_frame, stretch=1)

        # Нижняя панель кнопок по центру
        self.buttons_row = QHBoxLayout()
        self.buttons_row.setObjectName(u"buttons_row")
        self.buttons_row.setContentsMargins(0, 6, 0, 0)
        self.buttons_row.setSpacing(14)

        self.buttons_row.addStretch(1)

        self.btn_add_pacient = QPushButton(self.centralwidget)
        self.btn_add_pacient.setObjectName(u"btn_add_pacient")
        self._base_btn_font = QFont()
        self._base_btn_font.setFamilies([u"Futura"])
        self._base_btn_font.setWeight(QFont.Weight.DemiBold)
        self.btn_add_pacient.setFont(self._base_btn_font)
        self.btn_add_pacient.setStyleSheet(self._add_btn_stylesheet(14, 44))
        icon = QIcon()
        icon.addFile(u"icons/add.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_add_pacient.setIcon(icon)
        self.btn_add_pacient.setIconSize(QSize(26, 26))
        self.buttons_row.addWidget(self.btn_add_pacient)

        self.btn_edit_pacient = QPushButton(self.centralwidget)
        self.btn_edit_pacient.setObjectName(u"btn_edit_pacient")
        self.btn_edit_pacient.setFont(self._base_btn_font)
        self.btn_edit_pacient.setStyleSheet(self._edit_btn_stylesheet(14, 44))
        icon1 = QIcon()
        icon1.addFile(u"icons/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_edit_pacient.setIcon(icon1)
        self.btn_edit_pacient.setIconSize(QSize(26, 26))
        self.buttons_row.addWidget(self.btn_edit_pacient)

        self.btn_statistics = QPushButton(self.centralwidget)
        self.btn_statistics.setObjectName(u"btn_statistics")
        self.btn_statistics.setFont(self._base_btn_font)
        self.btn_statistics.setStyleSheet(self._stats_btn_stylesheet(14, 44))
        icon2 = QIcon()
        icon2.addFile(u"icons/bar-chart.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_statistics.setIcon(icon2)
        self.btn_statistics.setIconSize(QSize(26, 26))
        self.buttons_row.addWidget(self.btn_statistics)

        self.buttons_row.addStretch(1)
        self.main_layout.addLayout(self.buttons_row)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self._install_responsive_scaling(MainWindow)
        self._apply_scale_for_size(MainWindow.size())
        self._update_column_widths(force=True)

        QMetaObject.connectSlotsByName(MainWindow)

    def _add_btn_stylesheet(self, font_px: int, height_px: int) -> str:
        radius = height_px // 2
        return f"""
            QPushButton {{
                background-color: #EAF3B2;
                color: rgb(57, 104, 68);
                border: 1px solid #D4E384;
                border-radius: {radius}px;
                min-height: {height_px}px;
                max-height: {height_px}px;
                padding-left: 18px;
                padding-right: 22px;
                font-family: "Futura";
                font-size: {font_px}px;
                font-weight: 600;
            }}
            QPushButton:hover {{
                background-color: #DCE994;
                color: #1E2B47;
                border: 1px solid #C2D468;
            }}
            QPushButton:pressed {{
                background-color: #CCE072;
                color: #182238;
                border: 1px solid #B0C952;
            }}
        """

    def _edit_btn_stylesheet(self, font_px: int, height_px: int) -> str:
        radius = height_px // 2
        return f"""
            QPushButton {{
                background-color: #9FBAF1;
                color: #1E2F54;
                border: 1px solid #86A7EC;
                border-radius: {radius}px;
                min-height: {height_px}px;
                max-height: {height_px}px;
                padding-left: 18px;
                padding-right: 22px;
                font-family: "Futura";
                font-size: {font_px}px;
                font-weight: 600;
            }}
            QPushButton:hover {{
                background-color: #84A6EE;
                color: #15223E;
                border: 1px solid #6D92E3;
            }}
            QPushButton:pressed {{
                background-color: #6D92E3;
                color: #FDFDF5;
                border: 1px solid #557AD0;
            }}
        """

    def _stats_btn_stylesheet(self, font_px: int, height_px: int) -> str:
        radius = height_px // 2
        return f"""
            QPushButton {{
                background-color: #C0B9DD;
                color: #231F3A;
                border: 1px solid #A69DCE;
                border-radius: {radius}px;
                min-height: {height_px}px;
                max-height: {height_px}px;
                padding-left: 18px;
                padding-right: 22px;
                font-family: "Futura";
                font-size: {font_px}px;
                font-weight: 600;
            }}
            QPushButton:hover {{
                background-color: #A69BCF;
                color: #1B1730;
                border: 1px solid #8D80BE;
            }}
            QPushButton:pressed {{
                background-color: #8E80C2;
                color: #FDFDF5;
                border: 1px solid #7566AE;
            }}
        """

    def _update_column_widths(self, force: bool = False):
        avail_width = self.table_pacients.viewport().width()
        if avail_width <= 0:
            avail_width = max(600, self.table_pacients.width() - 4)

        if not force and avail_width == self._last_table_width:
            return
        self._last_table_width = avail_width

        col_count = self.table_pacients.columnCount()
        weights = self._column_weights[:col_count]
        min_widths = self._column_min_widths[:col_count]

        widths = list(min_widths)
        total_min = sum(widths)

        if avail_width > total_min:
            extra = avail_width - total_min
            total_weight = sum(weights) or 1.0
            fractional = []

            allocated = 0
            for i, w in enumerate(weights):
                exact = extra * (w / total_weight)
                add_px = int(exact)
                widths[i] += add_px
                allocated += add_px
                fractional.append((exact - add_px, i))

            # Распределяем остаток пикселей на столбцы с наибольшей дробной частью
            remainder = extra - allocated
            fractional.sort(reverse=True)
            for idx_rem in range(remainder):
                _, col_idx = fractional[idx_rem % len(fractional)]
                widths[col_idx] += 1

        for col_idx, w_px in enumerate(widths):
            self.table_pacients.setColumnWidth(col_idx, w_px)

    def _install_responsive_scaling(self, MainWindow: QMainWindow):
        original_resize = MainWindow.resizeEvent
        original_table_resize = self.table_pacients.resizeEvent
        ui_self = self

        def scaled_resize_event(event):
            if original_resize is not None:
                original_resize(event)
            ui_self._apply_scale_for_size(event.size())
            ui_self._update_column_widths()

        def table_resize_event(event):
            if original_table_resize is not None:
                original_table_resize(event)
            ui_self._update_column_widths()

        MainWindow.resizeEvent = scaled_resize_event
        self.table_pacients.resizeEvent = table_resize_event

    def _apply_scale_for_size(self, size):
        scale = min(size.width() / 950.0, size.height() / 550.0)
        scale = max(0.85, min(scale, 1.85))

        title_pt = max(22, int(round(34 * scale)))
        count_pt = max(14, int(round(18 * scale)))
        table_pt = max(12, int(round(14 * scale)))
        header_pt = max(11, int(round(12 * scale)))
        btn_px = max(13, int(round(14 * scale)))
        btn_h = max(40, int(round(44 * scale)))
        icon_px = max(22, int(round(26 * scale)))
        row_h = max(32, int(round(36 * scale)))

        f_title = QFont(self._base_title_font)
        f_title.setPointSize(title_pt)
        self.label_title.setFont(f_title)

        f_count = QFont(self._base_count_font)
        f_count.setPointSize(count_pt)
        self.label_count.setFont(f_count)

        f_table = QFont(self._base_table_font)
        f_table.setPointSize(table_pt)
        self.table_pacients.setFont(f_table)
        self.table_pacients.verticalHeader().setDefaultSectionSize(row_h)

        self.table_pacients.setStyleSheet(f"""
            QTableWidget {{
                background-color: #FDFDF5;
                alternate-background-color: #F1F5FC;
                color: #24345C;
                gridline-color: #D5DDF0;
                border: none;
                border-radius: 10px;
                selection-background-color: #DCE7FC;
                selection-color: #182544;
            }}

            QTableWidget::item {{
                padding: 6px 10px;
            }}

            QHeaderView {{
                background-color: #24345C;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }}

            QHeaderView::section {{
                background-color: #24345C;
                color: #FDFDF5;
                padding: {max(8, int(round(10 * scale)))}px 8px;
                border: none;
                border-right: 1px solid #3F558A;
                font-family: "Futura";
                font-weight: bold;
                font-size: {header_pt}pt;
            }}

            QHeaderView::section:last {{
                border-right: none;
            }}
        """)

        self.btn_add_pacient.setStyleSheet(self._add_btn_stylesheet(btn_px, btn_h))
        self.btn_edit_pacient.setStyleSheet(self._edit_btn_stylesheet(btn_px, btn_h))
        self.btn_statistics.setStyleSheet(self._stats_btn_stylesheet(btn_px, btn_h))

        icon_size = QSize(icon_px, icon_px)
        self.btn_add_pacient.setIconSize(icon_size)
        self.btn_edit_pacient.setIconSize(icon_size)
        self.btn_statistics.setIconSize(icon_size)

    def retranslateUi(self, MainWindow: QMainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        for idx, text in enumerate(self._headers):
            item = self.table_pacients.horizontalHeaderItem(idx)
            if item is not None:
                item.setText(QCoreApplication.translate("MainWindow", text, None))

        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Таблица пациентов", None))
        self.label_count.setText(QCoreApplication.translate("MainWindow", u"Всего пациентов: ", None))
        self.btn_add_pacient.setText(QCoreApplication.translate("MainWindow", u"Добавить", None))
        self.btn_edit_pacient.setText(QCoreApplication.translate("MainWindow", u"Изменить", None))
#if QT_CONFIG(shortcut)
        self.btn_edit_pacient.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z, Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.btn_statistics.setText(QCoreApplication.translate("MainWindow", u"Статистика", None))