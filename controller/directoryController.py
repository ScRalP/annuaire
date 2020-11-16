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
        file = open(fileName+".json", "a")
        file.write(json.dumps(self.directory.getContacts(), default=lambda x: x.__dict__))
        file.close()

    def loadJSON(self, fileName):
        file = open(fileName+".json", "r")
        for contact in json.loads(file.read()):
            self.addContact(self.contactController.createContact(contact['firstname'],contact['lastname'],contact['number'],contact['departement'],contact['email']))
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
    
    def getContactFromNumber(self, number):
        for contact in self.directory.getContacts():
            if(contact.number == number):
                return contact
        return None

    def filteredContacts(self, stringToSearch):
        if (stringToSearch==""):
            return self.directory.getContacts()
        else :
            contactListToDisplay = []
            for contact in self.directory.getContacts():
                if (contact.searchByString(stringToSearch)):
                    contactListToDisplay.append(contact)
            return contactListToDisplay