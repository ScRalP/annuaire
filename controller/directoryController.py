from model.directory import *
from Tools import trimNumber
from controller.contactController import *
from Tools import SaveFileName
import json

class directoryController():
    def __init__(self):
        self.directory = Directory()
        self.contactController = contactController()
        self.loadJSON(SaveFileName)

    def getDirectory(self):
        return self.directory

    def getWindow(self):
        return self.window

    def saveToJson(self, fileName):
        file = open(fileName, "w")
        file.write(json.dumps(self.directory.getContacts(), default=lambda x: x.__dict__))
        file.close()

    def loadJSON(self, fileName):
        self.directory = Directory()
        file = open(fileName, "r")
        for contact in json.loads(file.read()):
            self.addContact(self.contactController.createContact(contact['firstname'],contact['lastname'],contact['number'],contact['departement'],contact['email'],contact['isFavorite']))
        file.close()

    def addContact(self, contact):
        if self.isNumAlreadyTaken(contact.number):
            return False
        self.directory.getContacts().append(contact)
        return True

    def removeContact(self, contact):
        self.directory.getContacts().remove(contact)

    def isNumAlreadyTaken(self, num):
        for contact in self.directory.getContacts():
            #test non digit char and trim them
            if trimNumber(num) == trimNumber(contact.number):
                return True
                #Numero deja pris
            return False

    def editContact(self, contact, firstname, lastname, number, departement, email, isFavorite):
        if self.isNumAlreadyTaken(number):
            return False
        self.contactController.editContact(contact, firstname, lastname, number, departement, email, isFavorite)
        return True


    def getContactFromNumber(self, number):
        for contact in self.directory.getContacts():
            if(contact.number == number):
                return contact
        return None

    def filteredContacts(self, stringToSearch):
        if (stringToSearch==""):
            return self.directory.getContacts()
        else:
            lower_stringToSearch = stringToSearch.lower()
            contactListToDisplay = []
            for contact in self.directory.getContacts():
                if (lower_stringToSearch in str(contact.firstname).lower() or
                    lower_stringToSearch in str(contact.lastname).lower() or
                    lower_stringToSearch in str(contact.number).lower() or
                    lower_stringToSearch in str(contact.departement).lower() or
                    lower_stringToSearch in str(contact.email).lower()):
                    contactListToDisplay.append(contact)
            return contactListToDisplay