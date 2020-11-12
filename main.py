import sys
from PyQt5.QtWidgets import *

#import des classes metier & view
from view.mainWindow import *
from model.annuaire import *

app = QApplication(sys.argv)

class Controller():
    def __init__(self, annuaire, window):
        self.annuaire = annuaire
        self.window = window

    def getAnnuaire(self):
        return self.annuaire

    def getWindow(self):
        return self.window

controller = Controller(Annuaire(), MainWindow())

sys.exit(app.exec_())