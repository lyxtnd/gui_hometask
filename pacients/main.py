from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem, QVBoxLayout
from data.manager import Patient, load_patients, save_patients
from generated.ui_main_window import Ui_MainWindow
from generated.ui_patient_dialog import Ui_Dialog
from generated.ui_statistics_dialog import Ui_Dialog as Ui_StatisticsDialog

from PySide6.QtCore import Signal
from data.fake_data import generate_patients

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure



class StatisticsDialog(QDialog):
    def __init__(self, patients, parent=None):
        super().__init__(parent)

        self.ui = Ui_StatisticsDialog()
        self.ui.setupUi(self)

        self.patients = patients

        # Единая цветовая палитра под интерфейс (крем, глубокий синий, голубой, лайм, лаванда)
        self.bg_color = "#FDFDF5"
        self.text_color = "#24345C"
        self.grid_color = "#DCE5F7"
        self.spine_color = "#C7D4EE"
        self.palette = ["#9FBAF1", "#EAF3B2", "#C0B9DD", "#3D568F"]

        # Создаём области для графиков с фоном в тон вкладкам
        self.figure_gender = Figure(facecolor=self.bg_color)
        self.canvas_gender = FigureCanvasQTAgg(self.figure_gender)

        self.figure_age = Figure(facecolor=self.bg_color)
        self.canvas_age = FigureCanvasQTAgg(self.figure_age)

        self.figure_bmi_gender = Figure(facecolor=self.bg_color)
        self.canvas_bmi_gender = FigureCanvasQTAgg(self.figure_bmi_gender)

        self.figure_bmi_age = Figure(facecolor=self.bg_color)
        self.canvas_bmi_age = FigureCanvasQTAgg(self.figure_bmi_age)

        # Размещаем графики во вкладках
        self._embed_canvas(self.ui.chart_gender, self.canvas_gender)
        self._embed_canvas(self.ui.chart_age, self.canvas_age)
        self._embed_canvas(self.ui.chart_bmi_gender, self.canvas_bmi_gender)
        self._embed_canvas(self.ui.chart_bmi_age, self.canvas_bmi_age)

        # Первичное масштабирование UI и отрисовка графиков
        if hasattr(self.ui, "applyScale"):
            self.ui.applyScale(self.width(), self.height())

        self.refresh_plots()

    def _embed_canvas(self, container_widget, canvas):
        """Кладёт холст matplotlib внутрь вкладки с небольшими полями."""
        layout = QVBoxLayout(container_widget)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.addWidget(canvas)

    def _style_axes(self, ax, title: str, xlabel: str = "", ylabel: str = "", grid: bool = True):
        """Применяет единый аккуратный стиль к осям графика."""
        ax.set_facecolor(self.bg_color)
        ax.set_title(title, color=self.text_color, fontsize=12, fontweight="bold", pad=12)

        if xlabel:
            ax.set_xlabel(xlabel, color=self.text_color, fontsize=10, labelpad=6)
        if ylabel:
            ax.set_ylabel(ylabel, color=self.text_color, fontsize=10, labelpad=6)

        ax.tick_params(colors=self.text_color, labelsize=9)

        for spine_name in ("top", "right"):
            ax.spines[spine_name].set_visible(False)
        for spine_name in ("bottom", "left"):
            ax.spines[spine_name].set_color(self.spine_color)
            ax.spines[spine_name].set_linewidth(1.0)

        if grid:
            ax.grid(True, linestyle="--", linewidth=0.7, color=self.grid_color, alpha=0.9)
            ax.set_axisbelow(True)

    def refresh_plots(self):
        """Перерисовывает все 4 графика."""
        self.plot_gender()
        self.plot_age()
        self.plot_bmi_gender()
        self.plot_bmi_age()

    # 1. Распределение по полу
    def plot_gender(self):
        self.figure_gender.clear()
        ax = self.figure_gender.add_subplot(111)

        counts = {}
        for patient in self.patients:
            if patient.gender:
                counts[patient.gender] = counts.get(patient.gender, 0) + 1

        if counts:
            colors = [self.palette[i % len(self.palette)] for i in range(len(counts))]
            wedges, texts, autotexts = ax.pie(
                list(counts.values()),
                labels=list(counts.keys()),
                autopct="%1.1f%%",
                startangle=90,
                colors=colors,
                wedgeprops={"edgecolor": self.bg_color, "linewidth": 2},
                textprops={"color": self.text_color, "fontsize": 10},
            )
            for autotext in autotexts:
                autotext.set_color("#1E293B")
                autotext.set_fontweight("bold")
        else:
            ax.text(
                0.5, 0.5, "Нет данных о поле пациентов",
                ha="center", va="center", color="#64748B", fontsize=11
            )
            ax.set_xticks([])
            ax.set_yticks([])

        self._style_axes(ax, "Распределение пациентов по полу", grid=False)
        self.figure_gender.tight_layout()
        self.canvas_gender.draw()

    # 2. Распределение по возрасту
    def plot_age(self):
        self.figure_age.clear()
        ax = self.figure_age.add_subplot(111)

        ages = [p.age for p in self.patients if p.age is not None]

        if ages:
            ax.hist(
                ages,
                bins=min(10, max(1, len(set(ages)))),
                color="#9FBAF1",
                edgecolor="#3D568F",
                linewidth=1.0,
            )
        else:
            ax.text(
                0.5, 0.5, "Нет данных о возрасте пациентов",
                ha="center", va="center", color="#64748B", fontsize=11
            )

        self._style_axes(
            ax,
            "Распределение по возрасту",
            xlabel="Возраст",
            ylabel="Количество пациентов",
            grid=True,
        )
        self.figure_age.tight_layout()
        self.canvas_age.draw()

    # 3. ИМТ по полу
    def plot_bmi_gender(self):
        self.figure_bmi_gender.clear()
        ax = self.figure_bmi_gender.add_subplot(111)

        genders = sorted({p.gender for p in self.patients if p.gender})
        values = [
            [p.bmi for p in self.patients if p.gender == gender and p.bmi is not None]
            for gender in genders
        ]
        filtered_pairs = [(g, v) for g, v in zip(genders, values) if len(v) > 0]

        if filtered_pairs:
            labels = [g for g, _ in filtered_pairs]
            data = [v for _, v in filtered_pairs]

            box = ax.boxplot(
                data,
                tick_labels=labels,
                patch_artist=True,
                medianprops={"color": "#3D568F", "linewidth": 2.0},
                whiskerprops={"color": "#3D568F", "linewidth": 1.2},
                capprops={"color": "#3D568F", "linewidth": 1.2},
                flierprops={
                    "marker": "o",
                    "markerfacecolor": "#C0B9DD",
                    "markeredgecolor": "#24345C",
                    "markersize": 5,
                },
            )
            for idx, patch in enumerate(box["boxes"]):
                patch.set_facecolor(self.palette[idx % len(self.palette)])
                patch.set_edgecolor("#3D568F")
                patch.set_linewidth(1.2)
        else:
            ax.text(
                0.5, 0.5, "Недостаточно данных об ИМТ по полу",
                ha="center", va="center", color="#64748B", fontsize=11
            )

        self._style_axes(
            ax,
            "ИМТ в зависимости от пола",
            ylabel="ИМТ",
            grid=True,
        )
        self.figure_bmi_gender.tight_layout()
        self.canvas_bmi_gender.draw()

    # 4. ИМТ и возраст
    def plot_bmi_age(self):
        self.figure_bmi_age.clear()
        ax = self.figure_bmi_age.add_subplot(111)

        points = [
            (p.age, p.bmi)
            for p in self.patients
            if p.age is not None and p.bmi is not None
        ]

        if points:
            ages = [pt[0] for pt in points]
            bmis = [pt[1] for pt in points]
            ax.scatter(
                ages,
                bmis,
                color="#3D568F",
                edgecolors="#FDFDF5",
                linewidths=1.0,
                s=55,
                alpha=0.88,
            )
        else:
            ax.text(
                0.5, 0.5, "Недостаточно данных об ИМТ и возрасте",
                ha="center", va="center", color="#64748B", fontsize=11
            )

        self._style_axes(
            ax,
            "Зависимость ИМТ от возраста",
            xlabel="Возраст",
            ylabel="ИМТ",
            grid=True,
        )
        self.figure_bmi_age.tight_layout()
        self.canvas_bmi_age.draw()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if hasattr(self.ui, "applyScale"):
            self.ui.applyScale(self.width(), self.height())

# Окно добавления пациента
class PatientDialog(QDialog):
    patient_saved = Signal(object)
    def __init__(self, patient=None):
        super().__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btn_save.clicked.connect(self.save_patient)
        self.ui.btn_cancel.clicked.connect(self.reject)

        # Если передан пациент, заполняем форму его данными
        if patient:
            self.ui.edit_name.setText(patient.name)
            self.ui.spin_age.setValue(patient.age)
            self.ui.combo_gender.setCurrentText(patient.gender)
            self.ui.spin_height.setValue(patient.height)
            self.ui.spin_weight.setValue(patient.weight)

    def save_patient(self):
        patient = Patient(
            name=self.ui.edit_name.text(),
            age=self.ui.spin_age.value(),
            gender=self.ui.combo_gender.currentText(),
            height=self.ui.spin_height.value(),
            weight=self.ui.spin_weight.value()
        )

        self.patient_saved.emit(patient)
        self.accept()

# Главное окно приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаём интерфейс главного окна
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Подключаем кнопки
        self.add_functions()
        #загружаем пациентов из файла json
        self.patients = load_patients()
        if not self.patients:
            self.patients = generate_patients(30)
            save_patients(self.patients)
        self.refresh_table()

    # Подключение функций к кнопкам
    def add_functions(self):
        self.ui.btn_add_pacient.clicked.connect(self.add_patient)
        self.ui.btn_edit_pacient.clicked.connect(self.edit_patient)
        self.ui.btn_statistics.clicked.connect(self.show_statistics)

    def show_statistics(self):
        self.statistics_window = StatisticsDialog(self.patients)
        self.statistics_window.exec()

    # Открытие окна добавления пациента
    def add_patient(self):
        self.patient_dialog = PatientDialog()
        self.patient_dialog.patient_saved.connect(self.add_patient_to_table)
        self.patient_dialog.exec()

    def add_patient_to_table(self, patient):
        self.patients.append(patient)

        save_patients(self.patients)

        self.refresh_table()

    def refresh_table(self):
        table = self.ui.table_pacients
        cnt = len(self.patients)
        table.setRowCount(0)
        self.ui.label_count.setText("Всего пациентов: " + str(cnt))
        for patient in self.patients:
            row = table.rowCount()
            table.insertRow(row)

            table.setItem(row, 0, QTableWidgetItem(patient.name))
            table.setItem(row, 1, QTableWidgetItem(str(patient.age)))
            table.setItem(row, 2, QTableWidgetItem(patient.gender))
            table.setItem(row, 3, QTableWidgetItem(str(patient.height)))
            table.setItem(row, 4, QTableWidgetItem(str(patient.weight)))
            table.setItem(row, 5, QTableWidgetItem(str(patient.bmi)))

    def edit_patient(self):
        row = self.ui.table_pacients.currentRow()

        if row < 0:
            return

        patient = self.patients[row]

        self.patient_dialog = PatientDialog(patient)
        self.patient_dialog.patient_saved.connect(
            lambda updated_patient: self.update_patient(row, updated_patient)
        )
        self.patient_dialog.exec()

    def update_patient(self, row, updated_patient):
        self.patients[row] = updated_patient

        save_patients(self.patients)
        self.refresh_table()


# Запуск приложения
if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec()
