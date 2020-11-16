from view.contactForm import *

class EditContactForm(ContactForm):
    def __init__(self, language, directoryController, contactController, title, mainwindow, contact):
        ContactForm.__init__(self,language, directoryController, contactController, title, mainwindow)

        self.contactController= contactController
        self.contact= contact
        
        self.firstnameInput.setText(contact.firstname)
        self.lastnameInput.setText(contact.lastname)
        self.numeroInput.setText(contact.number)
        self.departementInput.setText(str(contact.departement))
        self.emailInput.setText(contact.email)
        if contact.isFavorite == False:
            self.isFavoriteInput.setCheckState(QtCore.Qt.Unchecked)
        else :
            self.isFavoriteInput.setCheckState(QtCore.Qt.Checked)

    def handleOk(self):

        isFavoriteBool = False if self.isFavoriteInput.checkState() == QtCore.Qt.Unchecked else True
        self.contactController.editContact(
        self.contact,
        self.firstnameInput.text(),
        self.lastnameInput.text(),
        self.numeroInput.text(),
        self.departementInput.text(),
        self.emailInput.text(),
        isFavoriteBool)

        self.mainWindow.updateTable()
        
        self.close()