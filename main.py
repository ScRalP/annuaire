#import des classes metier & view
from view.mainWindow import *
from model.annuaire import *

app = QApplication(sys.argv)

class Controller():
    def __init__(self):
        self.annuaire = Annuaire()
        self.window = MainWindow(self)

    def getAnnuaire(self):
        return self.annuaire

    def getWindow(self):
        return self.window

controller = Controller()
controller.annuaire.loadJSON()
controller.annuaire.infoContacts()
controller.window.show()

sys.exit(app.exec_())