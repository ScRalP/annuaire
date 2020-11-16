from view.contactForm import *

class AddContactForm(ContactForm):
    def __init__(self, language, directoryController, contactController, title, mainwindow):
        ContactForm.__init__(self, language, directoryController, contactController, title, mainwindow)

    def handleOk(self):


        isFavoriteBool = False if self.isFavoriteInput.checkState() == QtCore.Qt.Unchecked else True
        self.directoryController.addContact(self.contactController.createContact(
        self.firstnameInput.text(),
        self.lastnameInput.text(),
        self.numeroInput.text(),
        self.departementInput.text(),
        self.emailInput.text(),
        isFavoriteBool))

        self.mainWindow.updateTable()
        
        self.close()