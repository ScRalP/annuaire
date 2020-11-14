#import des classes metier & view
import sys
from view.mainWindow import *
from model.annuaire import *

app = QApplication(sys.argv)

class Controller():
    def __init__(self):
        self.annuaire = Annuaire()
        self.annuaire.loadJSON()
        self.window = MainWindow(self)

    def getAnnuaire(self):
        return self.annuaire

    def getWindow(self):
        return self.window

    def saveToJson(self):
        self.annuaire.saveToJson()

    def loadJSON(self):
        self.annuaire.loadJSON()

    def addContact(self,contact):
        self.annuaire.addContact(contact)

    def editContact(self, contact, firstname, lastname, number, departement, email):
        self.annuaire.editContact(contact, firstname, lastname, number, departement, email)

controller = Controller()

sys.exit(app.exec_())