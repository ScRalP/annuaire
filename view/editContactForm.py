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

    def handleOk(self):

        self.contactController.editContact(self.contact,
        self.firstnameInput.text(),
        self.lastnameInput.text(),
        self.numeroInput.text(),
        self.departementInput.text(),
        self.emailInput.text())

        self.mainWindow.updateTable()
        
        self.close()