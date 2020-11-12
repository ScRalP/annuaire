#imports
from model.contact import *

class Annuaire():
    def __init__(self):
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
