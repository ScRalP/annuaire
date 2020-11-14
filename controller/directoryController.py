
from model.directory import *

class directoryController():
    def __init__(self):
        self.directory = Directory()
        self.directory.loadJSON()

    def getDirectory(self):
        return self.directory

    def getWindow(self):
        return self.window

    def saveToJson(self):
        self.directory.saveToJson()

    def loadJSON(self):
        self.directory.loadJSON()

    def createContact(self,firstname, lastname, number, departement, email):
        self.directory.createContact(firstname, lastname, number, departement, email)

    def editContact(self, contact, firstname, lastname, number, departement, email):
        self.directory.editContact(contact, firstname, lastname, number, departement, email)

    def isNumAlreadyTaken(self, num):
        self.directory.isNumAlreadyTaken(num)
    
    def getContactFromNumber(self, number):
        self.directory.getContactFromNumber(number)
