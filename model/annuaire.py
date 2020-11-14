#imports
from model.contact import *
import json

class Annuaire():
    def __init__(self):
        self.contacts=[]

    def saveToJson(self):
        file = open("export.json", "a")
        file.write(json.dumps(self.contacts, default=lambda x: x.__dict__))
        file.close()

    def loadJSON(self):
        file = open("contacts.json", "r")
        for contact in json.loads(file.read()):
            self.addContact(Contact(contact['firstname'],contact['lastname'],contact['number'],contact['departement'],contact['email']))
        file.close()

    def addContact(self, contact):
        contact.trimNumber()

        if(not self.isNumAlreadyTaken(contact.number)):
            self.contacts.append(contact)
        
    def showContacts(self):
        for contact in self.contacts:
            contact.printInfos(self)

    # def removeContact(self, index):
    #     self.contacts.pop(index)

    def removeContact(self, contact):
        self.contacts.remove(contact)

    def infoContacts(self):
        for contact in self.contacts:
            contact.printInfos()

    def getLength(self):
        return len(self.contacts)

    def isNumAlreadyTaken(self, num):
        for contact in self.contacts:
            #test non digit char and trim them
            if num.strip(" .-") == contact.number.strip(" .-"):
                return True
                #Numero deja pris
            return False

    def editContact(self, contact, firstname, lastname, number, departement, email):
        contactToEdit = self.contacts.__getitem__(contact)
        contactToEdit.setFirstname(firstname)
        contactToEdit.setLastname(lastname)
        contactToEdit.setNumber(number)
        contactToEdit.setDepartement(departement)
        contactToEdit.setEmail(email)

    def getContactFromNumber(self, number):
        for contact in self.contacts:
            if(contact.number == number):
                return contact
        return None

    def filteredContacts(self, stringToSearch):
        if (stringToSearch==""):
            return self.contacts
        else :
            contactListToDisplay = []
            for contact in self.contacts:
                if (contact.searchByString(stringToSearch)):
                    contactListToDisplay.append(contact)
            return contactListToDisplay