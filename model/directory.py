#imports
from model.contact import *
import json

class Directory():
    def __init__(self):
        self.contacts=[]

    def saveToJson(self):
        file = open("export.json", "a")
        file.write(json.dumps(self.contacts, default=lambda x: x.__dict__))
        file.close()

    def loadJSON(self):
        file = open("contacts.json", "r")
        for contact in json.loads(file.read()):
            self.createContact(contact['firstname'],contact['lastname'],contact['number'],contact['departement'],contact['email'])
        file.close()

    def createContact(self, firstname, lastname, number, departement, email):
        trimedNumber = str(self.trimNumber(number))
        if self.isNumAlreadyTaken(trimedNumber):
            return False
        self.contacts.append(Contact(firstname, lastname, trimedNumber, departement, email))
        return True
        
    def trimNumber(self, number):
        trimmedNum = number.strip()
        for c in ".- ":
            trimmedNum = trimmedNum.replace(c, "")
        return trimmedNum

    def showContacts(self):
        for contact in self.contacts:
            contact.printInfos(self)

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
            if self.trimNumber(num) == self.trimNumber(contact.number):
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