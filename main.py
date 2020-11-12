import sys
from PyQt5.QtWidgets import *

#import des classes metier & view
from view.mainWindow import *
from model.annuaire import *

app = QApplication(sys.argv)

window = MainWindow()

sys.exit(app.exec_())