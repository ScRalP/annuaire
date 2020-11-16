class Contact():
    def __init__(self, firstname, lastname, number, departement, email, isFavorite):
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.departement = departement
        self.email = email
        self.isFavorite = isFavorite

    def setFirstname(self, firstname):
        self.firstname = firstname

    def setLastname(self, lastname):
        self.lastname = lastname

    def setNumber(self, number):
        self.number = number

    def setDepartement(self, departement):
        self.departement = departement

    def setEmail(self, email):
        self.email = email

    def setFavorite(self, isFavorite):
        self.isFavorite = isFavorite