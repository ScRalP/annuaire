class Contact():
    def __init__(self, firstname, lastname, number, departement, email):
        self.number = number
        self.lastname = lastname
        self.firstname = firstname
        self.email = email
        self.departement = departement

    def setNumber(self, number):
        self.number = number

    def setFirstname(self, firstname):
        self.firstname = firstname

    def setLastname(self, lastname):
        self.lastname = lastname

    def setDepartement(self, departement):
        self.departement = departement

    def setEmail(self, email):
        self.email = email

    def toJSON(self):
        return "{"+\
                "\""+ self.firstname +"\","+\
                "\""+ self.lastname +"\","+\
                "\""+ self.number +"\","+\
                "\""+ self.dep +"\","+\
                "\""+ self.email +"\""+\
                "}"