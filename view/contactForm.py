from PyQt5.QtWidgets import QMainWindow


class ContactForm(QMainWindow):
    def __init__(self, controller, title, parent=None):
        super(ContactForm, self).__init__(parent)

        # Init de la fenetre
        self.setWindowTitle(title)
        self.setGeometry(1000, 300, 300, 500)
        # empecher le resize
        self.setFixedSize(self.size())
        self.statusBar().setSizeGripEnabled(False)

        self.initUi()



    def initUi(self):
        print('yo')
