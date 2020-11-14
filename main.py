#import des classes metier & view
import sys
from view.mainWindow import *
from controller.directoryController import *

app = QApplication(sys.argv)

MainWindow = MainWindow()

sys.exit(app.exec_())