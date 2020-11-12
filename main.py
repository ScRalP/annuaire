#import des classes metier & view
import sys
from view.mainWindow import *
from model.annuaire import *

app = QApplication(sys.argv)

class Controller():
    def __init__(self):
        self.annuaire = Annuaire(self)
        self.window = MainWindow(self)

    def getAnnuaire(self):
        return self.annuaire

    def getWindow(self):
        return self.window

controller = Controller(Annuaire(), MainWindow())
controller.annuaire.loadJSON()
controller.window.show()

sys.exit(app.exec_())