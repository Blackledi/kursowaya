from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5.QtPrintSupport import QPrinter,QPrintDialog


class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()  #  для инициализации дизайна
        uic.loadUi('untitled.ui', self)
        self.show()

        self.setWindowTitle("MSU-TE-NAI-2021")
        # размеры шрифта
        self.action8pt.triggered.connect(lambda: self.change_size(8))
        self.action9pt.triggered.connect(lambda: self.change_size(9))
        self.action10pt.triggered.connect(lambda: self.change_size(10))
        self.action11pt.triggered.connect(lambda: self.change_size(11))
        self.action12pt.triggered.connect(lambda: self.change_size(12))
        self.action14pt.triggered.connect(lambda: self.change_size(14))
        self.action16pt.triggered.connect(lambda: self.change_size(16))
        self.action18pt.triggered.connect(lambda: self.change_size(18))
        self.action22pt_2.triggered.connect(lambda: self.change_size(22))
        self.action22pt.triggered.connect(lambda: self.change_size(24))
        self.action26pt.triggered.connect(lambda: self.change_size(26))
        self.action28pt.triggered.connect(lambda: self.change_size(28))
        self.action36pt.triggered.connect(lambda: self.change_size(36))
        self.action48pt.triggered.connect(lambda: self.change_size(48))
        self.action72pt.triggered.connect(lambda: self.change_size(72))
        # стили шрифта
        self.actionAlgerian.triggered.connect(lambda: self.change_label("Algerian"))
        self.actionArial_Black.triggered.connect(lambda: self.change_label("Arial Black"))
        self.actionArial.triggered.connect(lambda: self.change_label("Arial"))
        self.actionCourier_New.triggered.connect(lambda: self.change_label("Courier New"))
        self.actionGabriola.triggered.connect(lambda: self.change_label("Gabriola"))
        self.actionGigi.triggered.connect(lambda: self.change_label("Gigi"))
        self.actionGost_type_A.triggered.connect(lambda: self.change_label("Gost type A"))
        self.actionInk_Free.triggered.connect(lambda: self.change_label("Ink Free"))
        self.actionJokerman.triggered.connect(lambda: self.change_label("Jokerman"))
        self.actionMicrosoft_Sans_Serif.triggered.connect(lambda: self.change_label("Microsoft Sans Serif"))
        self.actionMicrosoft_Uighur.triggered.connect(lambda: self.change_label("Microsoft Uighur"))
        self.actionVivaldi.triggered.connect(lambda: self.change_label("Vivaldi"))
        self.actionSitka.triggered.connect(lambda: self.change_label("Sitka"))
        self.actionSimSun.triggered.connect(lambda: self.change_label("SimSun"))
        self.actionTiger.triggered.connect(lambda: self.change_label("Tiger"))
        self.actionTime_New_Romen.triggered.connect(lambda: self.change_label("Time New Romen"))
        self.actionTerminal.triggered.connect(lambda: self.change_label("Terminal"))
        self.actionWingdings_3.triggered.connect(lambda: self.change_label("Wide Latin"))

        self.action.triggered.connect(lambda: self.change_Font_style("Bold"))
        self.action_2.triggered.connect(lambda: self.change_Font_style("Underline"))
        self.action_3.triggered.connect(lambda: self.change_Font_style("Italic"))

        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionClose.triggered.connect(exit)
        self.actionPrint.triggered.connect(self.print_file)




# cтиль текста
    def change_label(self, label):
        self.plainTextEdit.setFont(QFont(label, 10))
# размер текста
    def change_size(self, size):
        self.plainTextEdit.setFont(QFont("Time New Romen", size))
# написание текста
    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files(*.txt);;Python(*.py ",
                                                  options=options)
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())

    def save_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files(*.txt);;All Files (*)",
                                                  options=options)
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())

    def closeEvent(self, event):
        dialog = QMessageBox()
        dialog.setText("Do you want to save your work?")
        dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole)  # 0
        dialog.addButton(QPushButton("No"), QMessageBox.NoRole)  # 1
        dialog.addButton(QPushButton("Cancel"), QMessageBox.RejectRole)  # 2

        answer = dialog.exec_()

        if answer == 0:
            self.save_file()
            event.accept()
        elif answer == 2:
            event.ignore()
# вывод текста на печать
    def print_file(self):

        prnter = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer,self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.plainTextEdit.print_ (printer)



def main():
    app = QApplication([])  # Новый экземпляр QApplication
    window = MyGUI()  # Создаём объект класса MyGUI
    app.exec_()  # запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
