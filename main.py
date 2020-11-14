#import des classes metier & view
import sys
from view.mainWindow import *
from controller.directoryController import *

app = QApplication(sys.argv)

directoryController = directoryController()

sys.exit(app.exec_())