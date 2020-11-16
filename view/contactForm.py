from PyQt5 import QtCore
from PyQt5.QtWidgets import *


class ContactForm(QMainWindow):
    def __init__(self, language, directoryController, contactController, title, mainwindow):
        super(ContactForm, self).__init__(None)

        #
        self.mainWindow = mainwindow
        #Traduction
        self.translation= language
        #
        self.directoryController = directoryController
        self.contactController = contactController
        # Init de la fenetre
        self.setWindowTitle(title)
        self.setGeometry(1000, 300, 500, 400)
        # empecher le resize
        self.setFixedSize(self.size())
        self.statusBar().setSizeGripEnabled(False)

        self.initUi()

    def initUi(self):
        mainLayout = QVBoxLayout()

        #Layout du formulaire
        formLayout = QFormLayout()

        #Ajout des lignes
        self.firstnameInput   = QLineEdit()
        self.lastnameInput    = QLineEdit()
        self.numeroInput      = QLineEdit()
        self.departementInput = QLineEdit()
        self.emailInput       = QLineEdit()
        self.isFavoriteInput  = QCheckBox()

        formLayout.addRow(QLabel(self.translation["Firstname"])  , self.firstnameInput)
        formLayout.addRow(QLabel(self.translation["Lastname"])   , self.lastnameInput)
        formLayout.addRow(QLabel(self.translation["Number"])     , self.numeroInput)
        formLayout.addRow(QLabel(self.translation["Departement"]), self.departementInput)
        formLayout.addRow(QLabel(self.translation["Email"])      , self.emailInput)
        formLayout.addRow(QLabel(self.translation["IsFavorite"]) , self.isFavoriteInput)

        mainLayout.addLayout(formLayout)

        #Layout des boutons
        btnLayout = QHBoxLayout()

        #Creation des boutons
        btnValidate = QPushButton(self.translation["Ok"])
        btnCancel = QPushButton(self.translation["Cancel"])

        #ajout des evenements
        btnValidate.clicked.connect(self.handleOk)
        btnCancel.clicked.connect(self.close)

        #ajout au layout
        btnLayout.addWidget(btnValidate)
        btnLayout.addWidget(btnCancel)

        mainLayout.addLayout(btnLayout)

        window = QWidget()
        window.setLayout(mainLayout)
        self.setCentralWidget(window)

