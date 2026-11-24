from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QColor, QFont, QPainter, QTextOption)
from PySide6.QtWidgets import (QDialog, QLabel, QSizePolicy, QStyle, QStyleOptionTab, QTabBar, QTabWidget, QVBoxLayout, QWidget)


class WrappingTabBar(QTabBar):
    """QTabBar с переносом текста, центрированием и масштабированием вкладок."""

    def __init__(self, parent=None, base_width: int = 525):
        super().__init__(parent)
        self._base_width = max(300, base_width)
        self._scale = 1.0

    def setScale(self, scale: float) -> None:
        self._scale = max(0.85, min(scale, 2.0))
        font = self.font()
        font.setFamilies([u"Futura"])
        font.setPointSizeF(10.0 * self._scale)
        font.setBold(True)
        self.setFont(font)
        self.updateGeometry()
        self.update()

    def tabSizeHint(self, index: int) -> QSize:
        text = self.tabText(index)
        available_width = max(320, self.width())
        tab_count = max(1, self.count())
        # Делим ширину панели вкладок между вкладками с небольшим зазором
        max_tab_width = max(int(95 * self._scale), (available_width - 16) // tab_count - 4)

        fm = self.fontMetrics()
        h_pad = int(14 * self._scale)
        v_pad = int(10 * self._scale)

        text_rect = fm.boundingRect(
            QRect(0, 0, max(50, max_tab_width - h_pad * 2), 200),
            Qt.AlignmentFlag.AlignCenter | Qt.TextFlag.TextWordWrap,
            text,
        )

        width = min(max_tab_width, max(int(80 * self._scale), text_rect.width() + h_pad * 2))
        height = max(int(38 * self._scale), text_rect.height() + v_pad * 2)
        return QSize(width, height)

    def paintEvent(self, event) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        for index in range(self.count()):
            option = QStyleOptionTab()
            self.initStyleOption(option, index)

            tab_rect = self.tabRect(index)
            option.rect = tab_rect
            label_text = option.text
            option.text = ""
            self.style().drawControl(QStyle.ControlElement.CE_TabBarTab, option, painter, self)

            painter.save()
            painter.setFont(self.font())

            if option.state & QStyle.StateFlag.State_Selected:
                text_color = QColor("#FDFDF5")
            elif option.state & QStyle.StateFlag.State_MouseOver:
                text_color = QColor("#162340")
            else:
                text_color = QColor("#24345C")

            painter.setPen(text_color)
            pad_x = int(6 * self._scale)
            pad_y = int(4 * self._scale)
            text_rect = tab_rect.adjusted(pad_x, pad_y, -pad_x, -pad_y)

            text_option = QTextOption(Qt.AlignmentFlag.AlignCenter)
            text_option.setWrapMode(QTextOption.WrapMode.WordWrap)
            painter.drawText(text_rect, label_text, text_option)
            painter.restore()


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        self._base_width = 525
        self._base_height = 495
        Dialog.resize(self._base_width, self._base_height)
        Dialog.setMinimumSize(QSize(440, 380))
        Dialog.setStyleSheet(u"QDialog {\n"
"    background-color: #F5F4F0;\n"
"}")

        self.main_layout = QVBoxLayout(Dialog)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(16, 14, 16, 16)
        self.main_layout.setSpacing(12)

        self.label_title = QLabel(Dialog)
        self.label_title.setObjectName(u"label_title")
        self._base_title_pt = 18.0
        font = QFont()
        font.setFamilies([u"Futura"])
        font.setPointSizeF(self._base_title_pt)
        font.setBold(True)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: #24345C;")
        self.label_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_title.setWordWrap(True)
        self.label_title.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
        )
        self.main_layout.addWidget(self.label_title)

        self.tab_3 = QTabWidget(Dialog)
        self.tab_3.setObjectName(u"tab_3")
        self._tab_bar = WrappingTabBar(self.tab_3, base_width=self._base_width)
        self.tab_3.setTabBar(self._tab_bar)
        self.tab_3.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding
        )
        self.tab_3.setStyleSheet(u"QTabWidget::pane {\n"
"    background-color: #FDFDF5;\n"
"    border: 1px solid #C7D4EE;\n"
"    border-radius: 12px;\n"
"    border-top-left-radius: 0px;\n"
"    top: -1px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #EAF0FC;\n"
"    color: #24345C;\n"
"    border: 1px solid #C7D4EE;\n"
"    border-bottom: none;\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background-color: #9FBAF1;\n"
"    color: #162340;\n"
"    border-color: #86A7EC;\n"
"}\n"
"\n"
"QTabBar::tab:pressed {\n"
"    background-color: #7EA0EA;\n"
"    color: #14203A;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #3D568F;\n"
"    color: #FDFDF5;\n"
"    border-color: #3D568F;\n"
"}")

        for name in ("chart_gender", "chart_age", "chart_bmi_gender", "chart_bmi_age"):
            page = QWidget()
            page.setObjectName(name)
            page.setStyleSheet(u"background-color: #FDFDF5;")
            setattr(self, name, page)
            self.tab_3.addTab(page, "")

        self.main_layout.addWidget(self.tab_3)

        self.retranslateUi(Dialog)
        self.tab_3.setCurrentIndex(3)
        QMetaObject.connectSlotsByName(Dialog)

    def applyScale(self, width: int, height: int) -> None:
        """Масштабирует заголовок и вкладки пропорционально размеру окна."""
        scale = min(width / self._base_width, height / self._base_height)
        scale = max(0.85, min(scale, 2.0))

        title_font = self.label_title.font()
        title_font.setPointSizeF(self._base_title_pt * scale)
        self.label_title.setFont(title_font)

        self._tab_bar.setScale(scale)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_title.setText(QCoreApplication.translate("Dialog", u"Статистика пациентов", None))
        self.tab_3.setTabText(self.tab_3.indexOf(self.chart_gender), QCoreApplication.translate("Dialog", u"Распределение по полу", None))
        self.tab_3.setTabText(self.tab_3.indexOf(self.chart_age), QCoreApplication.translate("Dialog", u"Возраст", None))
        self.tab_3.setTabText(self.tab_3.indexOf(self.chart_bmi_gender), QCoreApplication.translate("Dialog", u"ИМТ по полу", None))
        self.tab_3.setTabText(self.tab_3.indexOf(self.chart_bmi_age), QCoreApplication.translate("Dialog", u"ИМТ и возраст", None))