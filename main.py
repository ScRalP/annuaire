#import des classes metier & view
import sys
from view.mainWindow import *
from controller.directoryController import *

app = QApplication(sys.argv)

MainWindow = MainWindow("en") if (len(sys.argv) <= 1) else MainWindow(str(sys.argv[1]))

sys.exit(app.exec_())
