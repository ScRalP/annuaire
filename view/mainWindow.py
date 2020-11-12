from PyQt5.QtWidgets import *
from view.contactForm import *

class MainWindow(QMainWindow):
    def __init__(self, controller):
        super(MainWindow, self).__init__()

        #Récupération du controller
        self.controller = controller

        #Init de la fenetre
        self.setWindowTitle("Annuaire")
        self.setGeometry(800,200,1000,650)
        #empecher le resize
        self.setFixedSize(self.size())
        self.statusBar().setSizeGripEnabled(False)

        self.initMenu()
        self.initUi()
        self.show()

    #Initialise la barre de menu
    def initMenu(self):
        #Actions du fileMenu
        exitMenu = QAction("&Quitter", self)
        exitMenu.setShortcut("Ctrl+Q")
        exitMenu.triggered.connect(qApp.quit)
        #Actions du actionMenu
        addMenu = QAction("&Ajouter", self)
        addMenu.setShortcut("Ctrl+N")
        addMenu.triggered.connect(self.addContact)
        updMenu = QAction("&Editer", self)
        updMenu.setShortcut("Ctrl+E")
        #addMenu.triggered.connect(self.updContact)
        delMenu = QAction("&Supprimer", self)
        delMenu.setShortcut("Ctrl+D")
        #addMenu.triggered.connect(self.delContact)

        #Ajout du menu
        self.statusBar()
        menu = self.menuBar()
        fileMenu = menu.addMenu("&Fichier")
        fileMenu.addAction(exitMenu)
        actionMenu = menu.addMenu("&Action")
        actionMenu.addAction(addMenu)
        actionMenu.addAction(updMenu)
        actionMenu.addAction(delMenu)

    #Initialise la fenetre avec les composants
    def initUi(self):
        mainLayout = QVBoxLayout()

        #--- Creation du layout de la barre de recherche ---#
        barLayout = QHBoxLayout()

        #Creation des composants
        barLabel = QLabel("Rechercher")
        barInput = QLineEdit()

        #Ajout des composants au layout
        barLayout.addWidget(barLabel)
        barLayout.addWidget(barInput)

        mainLayout.addLayout(barLayout)

        #--- Creation du tableau de contact ---#
        self.table = QTableWidget()

        #Ajout d'une ligne
        self.table.insertRow(0)
        self.table.setItem(0,0,QTableWidgetItem("yes"))

        mainLayout.addWidget(self.table)

        #--- Creation du Layout des boutons ---#
        btnLayout = QHBoxLayout()

        #Creation des boutons
        btnAdd = QPushButton('Ajouter', self)
        btnUpd = QPushButton('Editer', self)
        btnDel = QPushButton('Supprimer', self)

        #ajout des boutons dans le layout
        btnLayout.addWidget(btnAdd)
        btnLayout.addWidget(btnUpd)
        btnLayout.addWidget(btnDel)

        mainLayout.addLayout(btnLayout)


        window = QWidget()
        window.setLayout(mainLayout)

        #set central widget
        self.setCentralWidget(window)
        self.updateTable()

    def updateTable(self):
        annuaire = self.controller.getAnnuaire()
        #On vide la table
        self.table.clear()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['firstname', 'lastname', 'number', 'departement', 'email'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #On remplis la table
        i = 0
        for contact in annuaire.contacts:
            self.table.insertRow(i)

            self.table.setItem(i,0,QTableWidgetItem(contact.firstname))
            self.table.setItem(i,1,QTableWidgetItem(contact.lastname))
            self.table.setItem(i,2,QTableWidgetItem(contact.number))
            self.table.setItem(i,3,QTableWidgetItem(str(contact.departement)))
            self.table.setItem(i,4,QTableWidgetItem(contact.email))

            i+=1

    def addContact(self):
        ContactForm(self)
