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

controller = Controller()

sys.exit(app.exec_())