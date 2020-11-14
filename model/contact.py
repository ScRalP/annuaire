class Contact():
    def __init__(self, firstname, lastname, number, departement, email):
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.departement = departement
        self.email = email

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

    def searchByString(self, stringToSearch):
        if (stringToSearch in str(self.firstname) or
        stringToSearch in str(self.lastname) or
        stringToSearch in str(self.number) or
        stringToSearch in str(self.departement) or
        stringToSearch in str(self.email)):
            return True
        return False