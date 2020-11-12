#imports
from model.contact import *

class Annuaire():
    def __init__(self, controller):
        #recup du controller
        self.controller = controller
        self.contacts = [Contact("Quentin", "Robard", "06 15 15 15 15", "78420", "quentin.robard@gmail.com"),
                         Contact("Corentin", "Bollaert", "06 12 12 12 12", "16600", "cor_bo@hotmail.fr")]

    def __SaveToJson__(self):
        print("TODO")
    def __LoadJSON__(self):
        print("TODO")
    def __addcontact__(self,contact):
        self.contacts.append(contact)
    def __showcontacts__(self):
        for contact in self.contacts:
            contact.__printInfos__(self)
    def __removecontact__(self, index):
        self.contacts.pop(index)
    def __infocontact__(self, index):
        self.contacts[index].__printInfos__()
    def __getLength__(self):
        return len(self.contacts)
    def __isNumAlreadyTaken__(self, num):
        for contact in self.contacts :
            if num == contact.num:
                return True
            return False

        #Initialisation d'une liste de base
        self.contacts = [Contact("Robard", "quentin.robard@sfr.fr", "78420", "06 15 15 15 15"), Contact("Bollaert", "cor_bo@hotmail.com", "16600", "06 12 12 12 12")]

    def ajouterContact(self, contact):
        self.contacts.append(contact)

    def editerContact(self, contact, nom, email, dep, tel):
        self.contacts.__getitem__(contact).setNom(nom)
        self.contacts.__getitem__(contact).setEmail(email)
        self.contacts.__getitem__(contact).setDep(dep)
        self.contacts.__getitem__(contact).setTel(tel)

    def supprimerContact(self, contact):
        self.contacts.remove(contact)
