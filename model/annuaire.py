#imports
from model.contact import *
import json

class Annuaire():
    def __init__(self):
        self.contacts=[]
        
    def saveToJson(self):
        for contact in self.contacts:
            contact.toJSON(self)

    def loadJSON(self):
        file = open("contacts.json", "r")
        for contact in json.loads(file.read()):
            __addcontact__(Contact(contact['firstname'],contact['lastname'],contact['number'],contact['departement'],contact['email']))
        file.close()

    def addContact(self,contact):
        self.contacts.append(contact)
        
    def showContacts(self):
        for contact in self.contacts:
            contact.__printInfos__(self)

    # def removeContact(self, index):
    #     self.contacts.pop(index)

    def removeContact(self, contact):
        self.contacts.remove(contact)

    def infoContact(self, index):
        
        self.contacts[index].__printInfos__()
    def getLength(self):
        return len(self.contacts)

    def isNumAlreadyTaken(self, num):
        for contact in self.contacts :
            if num.strip() == contact.num.strip():
                return True
            return False

    def editContact(self, firstname, lastname, number, departement, email):
        contactToEdit = self.contacts.__getitem__(contact)
        contactToEdit.setFirstname(firstname)
        contactToEdit.setLastname(lastname)
        contactToEdit.setNumber(number)
        contactToEdit.setDepartement(departement)
        contactToEdit.setEmail(email)

