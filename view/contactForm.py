from PyQt5.QtWidgets import *

class ContactForm(QMainWindow):
    def __init__(self, controller, title, contact=None, parent=None):
        super(ContactForm, self).__init__(parent)
        self.controller = controller
        self.contact = contact
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
        if self.contact is not None:
            self.firstnameInput   = QLineEdit(self.contact.firstname)
            self.lastnameInput    = QLineEdit(self.contact.firstname)
            self.numeroInput      = QLineEdit(self.contact.firstname)
            self.departementInput = QLineEdit(str(self.contact.departement))
            self.emailInput       = QLineEdit(self.contact.firstname)
        else:
            self.firstnameInput   = QLineEdit()
            self.lastnameInput    = QLineEdit()
            self.numeroInput      = QLineEdit()
            self.departementInput = QLineEdit()
            self.emailInput       = QLineEdit()

        formLayout.addRow(QLabel("firstname")  , self.firstnameInput)
        formLayout.addRow(QLabel("lastname")   , self.lastnameInput)
        formLayout.addRow(QLabel("numero")     , self.numeroInput)
        formLayout.addRow(QLabel("departement"), self.departementInput)
        formLayout.addRow(QLabel("firstname")  , self.emailInput)

        mainLayout.addLayout(formLayout)

        #Layout des boutons
        btnLayout = QHBoxLayout()

        #Creation des boutons
        btnValidate = QPushButton("Valider")
        btnCancel = QPushButton("Annuler")

        #ajout des evenements
        btnValidate.clicked.connect(self.updContact)
        btnCancel.clicked.connect(self.close)

        #ajout au layout
        btnLayout.addWidget(btnValidate)
        btnLayout.addWidget(btnCancel)

        mainLayout.addLayout(btnLayout)

        window = QWidget()
        window.setLayout(mainLayout)
        self.setCentralWidget(window)

    def updContact(self):
        firstname   = self.firstnameInput.text()
        lastname    = self.lastnameInput.text()
        number      = self.numeroInput.text()
        departement = self.departementInput.text()
        email       = self.emailInput.text()
        #Verifier si le numero existe
        if( self.controller.isNumeroAlreadyTaken( number ) ):
            #si ou modifier le contact
            self.controller.editContact( self.controller.getContactFromNumber(number), firstname, lastname, number, departement, email)
        else:
            #si non ajouter nouveau contact
            self.controller.addContact(  )

        #fermer la modal
        self.close()

