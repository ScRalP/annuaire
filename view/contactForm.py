from PyQt5.QtWidgets import *


class ContactForm(QMainWindow):
    def __init__(self, controller, title, parent=None):
        super(ContactForm, self).__init__(parent)

        # Init de la fenetre
        self.setWindowTitle(title)
        self.setGeometry(1000, 300, 300, 200)
        # empecher le resize
        self.setFixedSize(self.size())
        self.statusBar().setSizeGripEnabled(False)

        self.initUi()

    def initUi(self):
        mainLayout = QVBoxLayout()

        #Layout du formulaire
        formLayout = QFormLayout()

        #Ajout des lignes
        formLayout.addRow(QLabel("firstname"), QLineEdit())
        formLayout.addRow(QLabel("lastname"), QLineEdit())
        formLayout.addRow(QLabel("number"), QLineEdit())
        formLayout.addRow(QLabel("departement"), QLineEdit())
        formLayout.addRow(QLabel("email"), QLineEdit())

        mainLayout.addLayout(formLayout)

        #Layout des boutons
        btnLayout = QHBoxLayout()

        #Ajout des boutons
        self.validate = QPushButton("Valider")
        self.cancel = QPushButton("Annuler")
        btnLayout.addWidget(self.validate)
        btnLayout.addWidget(self.cancel)

        mainLayout.addLayout(btnLayout)

        window = QWidget()
        window.setLayout(mainLayout)
        self.setCentralWidget(window)
