from view.addContactForm import *
from view.editContactForm import *
from controller import directoryController,contactController
from Tools import formatTelNumberDisplay
from Tools import SaveFileName

import json

from PyQt5 import *
from pathlib import Path


class MainWindow(QMainWindow):
    def __init__(self, language):
        super(MainWindow, self).__init__()

        #Liste à afficher
        self.displayedContacts = []

        #chargement du fichier de traduction
        file = open("translations/translation"+language.upper()+".json", "r")
        self.translation = json.loads(file.read())
        file.close()

        #Récupération des controllers
        self.directoryController = directoryController.directoryController()
        self.contactController = contactController.contactController()

        #Init de la fenetre
        self.setWindowTitle(self.translation['Title'])
        self.setGeometry(500,200,800,800)
        #empecher le resize
        self.setFixedSize(self.size())
        self.statusBar().setSizeGripEnabled(False)

        self.initMenu()
        self.initUi()
        self.show()

    #Initialise la barre de menu
    def initMenu(self):
        #Actions du fileMenu
        exitMenu = QAction("&"+self.translation['Quit'], self)
        exitMenu.setShortcut("Ctrl+Q")
        exitMenu.triggered.connect(qApp.quit)

        loadMenu = QAction("&"+self.translation['Load'], self)
        loadMenu.setShortcut("Ctrl+O")
        loadMenu.triggered.connect(lambda: self.loadJSON())

        saveMenu = QAction("&"+self.translation['Save'], self)
        saveMenu.setShortcut("Ctrl+S")
        saveMenu.triggered.connect(lambda: self.directoryController.saveToJson(SaveFileName))

        saveAsMenu = QAction("&"+self.translation['SaveAs'], self)
        saveAsMenu.triggered.connect(self.saveAs)

        #Actions du actionMenu
        addMenu = QAction("&"+self.translation['Add'], self)
        addMenu.setShortcut("Ctrl+N")
        addMenu.triggered.connect(self.addContact)

        updMenu = QAction("&"+self.translation['Edit'], self)
        updMenu.setShortcut("Ctrl+E")
        updMenu.triggered.connect(self.editContact)

        delMenu = QAction("&"+self.translation['Delete'], self)
        delMenu.setShortcut("Ctrl+D")
        delMenu.triggered.connect(self.delContact)

        #Actions de langue
        frMenu = QAction("&"+self.translation['French'], self)
        #frMenu.triggered.connect(self.reopen(self.translation['French']))
        enMenu = QAction("&"+self.translation['English'], self)
        #enMenu.triggered.connect(self.reopen(self.translation['English']))
        monkeyMenu = QAction("&"+self.translation['Monkey'], self)
        #monkeyMenu.triggered.connect(self.reopen(self.translation['Monkey']))

        #Ajout du menu
        self.statusBar()
        menu = self.menuBar()
        fileMenu = menu.addMenu("&"+self.translation['File'])
        fileMenu.addAction(exitMenu)
        fileMenu.addAction(loadMenu)
        fileMenu.addAction(saveMenu)
        fileMenu.addAction(saveAsMenu)
        actionMenu = menu.addMenu("&"+self.translation['Action'])
        actionMenu.addAction(addMenu)
        actionMenu.addAction(updMenu)
        actionMenu.addAction(delMenu)
        languageMenu = menu.addMenu("&"+self.translation['Languages'])
        languageMenu.addAction(frMenu)
        languageMenu.addAction(enMenu)
        languageMenu.addAction(monkeyMenu)

    #Initialise la fenetre avec les composants
    def initUi(self):
        mainLayout = QVBoxLayout()

        #--- Creation du layout de la barre de recherche ---#
        barLayout = QHBoxLayout()

        #Creation des composants
        barLabel = QLabel(self.translation['Search'])
        barInput = QLineEdit()
        barInput.textChanged[str].connect(self.updateFilter)

        #Ajout des composants au layout
        barLayout.addWidget(barLabel)
        barLayout.addWidget(barInput)

        mainLayout.addLayout(barLayout)

        #--- Creation du tableau de contact ---#
        self.table = QTableWidget()
        self.table.setSelectionBehavior(QTableView.SelectRows)
        self.table.setSelectionMode(QTableView.SingleSelection)

        # #Ajout d'une ligne
        # self.table.insertRow(0)
        # self.table.setItem(0,0,QTableWidgetItem("yes"))

        mainLayout.addWidget(self.table)

        #--- Creation du Layout des boutons ---#
        btnLayout = QHBoxLayout()

        #Creation des boutons
        btnAdd = QPushButton("&"+self.translation['Add'], self)
        btnUpd = QPushButton("&"+self.translation['Edit'], self)
        btnDel = QPushButton("&"+self.translation['Delete'], self)

        #ajout des evenement
        btnAdd.clicked.connect(self.addContact);
        btnUpd.clicked.connect(self.editContact);
        btnDel.clicked.connect(self.delContact);

        #ajout des boutons dans le layout
        btnLayout.addWidget(btnAdd)
        btnLayout.addWidget(btnUpd)
        btnLayout.addWidget(btnDel)

        mainLayout.addLayout(btnLayout)

        window = QWidget()
        window.setLayout(mainLayout)

        #set central widget
        self.setCentralWidget(window)
        self.updateTable("")

    def updateTable(self, stringFilter=""):
        self.displayedContacts = self.directoryController.filteredContacts(stringFilter)

        directory = self.directoryController.getDirectory()
        #On vide la table
        self.table.setRowCount(0)
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            self.translation['Firstname'],
            self.translation['Lastname'],
            self.translation['Number'],
            self.translation['Departement'],
            self.translation['Email'],
            self.translation['IsFavorite']
            ])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        self.table.setSortingEnabled(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableView.SelectRows)

        #On remplis la table
        i = 0
        for contact in self.displayedContacts :
            self.table.insertRow(i)

            self.table.setItem(i,0,QTableWidgetItem(contact.firstname))
            self.table.setItem(i,1,QTableWidgetItem(contact.lastname))
            self.table.setItem(i,2,QTableWidgetItem(formatTelNumberDisplay(contact.number)))
            self.table.setItem(i,3,QTableWidgetItem(str(contact.departement)))
            self.table.setItem(i,4,QTableWidgetItem(contact.email))            

            if (contact.isFavorite == True):
                self.table.setItem(i,5,QTableWidgetItem("✔"))
            else:
                self.table.setItem(i,5,QTableWidgetItem(""))
            i+=1

    def loadJSON(self):
        name = QFileDialog.getOpenFileName(self,self.translation['Load'], "", "JSON (*.json)")
        if not (name[0] == None or name[0] == ""):
            self.directoryController.loadJSON(Path(name[0]))
        self.updateTable()

    def saveAs(self):
        name = QFileDialog.getSaveFileName(self,self.translation['SaveAs'], "", "JSON (*.json)")
        if not (name[0] == None or name[0] == ""):
            self.directoryController.saveToJson(Path(name[0]))

    def addContact(self):
        self.dialog = AddContactForm(self.translation, self.directoryController,self.contactController, self.translation['AddContact'], self)
        self.dialog.show()

    def editContact(self):
        if (len(self.table.selectedIndexes()) > 0):
            self.dialog = EditContactForm(self.translation, self.directoryController,self.contactController, self.translation['EditContact'], self, self.displayedContacts[self.table.selectedIndexes()[0].row()])
            self.dialog.show()

    def delContact(self):
        if len(self.table.selectedIndexes()) > 0:
            self.directoryController.removeContact(self.displayedContacts[self.table.selectedIndexes()[0].row()])
            self.updateTable()

    def updateFilter(self, stringFilter):
        self.updateTable(stringFilter)
