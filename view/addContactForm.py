from view.contactForm import *

class AddContactForm(ContactForm):
    def __init__(self, language, directoryController, contactController, title, mainwindow):
        ContactForm.__init__(self, language, directoryController, contactController, title, mainwindow)

    def handleOk(self):

        self.directoryController.addContact(self.contactController.createContact(
        self.firstnameInput.text(),
        self.lastnameInput.text(),
        self.numeroInput.text(),
        self.departementInput.text(),
        self.emailInput.text()))

        self.mainWindow.updateTable()
        
        self.close()