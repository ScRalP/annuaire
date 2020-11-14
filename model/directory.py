#imports
from model.contact import *

class Directory():
    def __init__(self):
        self.contacts=[]

    def getContacts(self):
        return self.contacts

    def getLength(self):
        return len(self.contacts)