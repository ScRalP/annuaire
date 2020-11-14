from view.contactForm import *

class AddContactForm(ContactForm):
    def __init__(self, parent=None):
        super(ContactForm, self).__init__(parent)

    def addContact(self):
        firstname = self.firstnameInput.text()
        lastname = self.lastnameInput.text()
        number = self.numeroInput.text()
        departement = self.departementInput.text()
        email = self.emailInput.text()

        # Verifier si le numero existe
        if ( not self.controller.createContact( firstname, lastname, number, departement, email ) ):
            QDialog("Ce numéro existe déjà")
            return False

        return True