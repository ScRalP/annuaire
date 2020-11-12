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
controller.window.show()

sys.exit(app.exec_())