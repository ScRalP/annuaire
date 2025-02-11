from model.contact import *
from Tools import trimNumber

class contactController():

    def __init__(self):
        pass

    def createContact(self, firstname, lastname, number, departement, email, isFavorite):
        return (Contact(firstname, lastname, trimNumber(number), departement, email, isFavorite))

    def editContact(self, contact, firstname, lastname, number, departement, email, isFavorite):
        contact.setFirstname(firstname)
        contact.setLastname(lastname)
        contact.setNumber(number)
        contact.setDepartement(departement)
        contact.setEmail(email)
        contact.setFavorite(isFavorite)
