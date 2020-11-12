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
        

    def toJSON(self):
        return "{"+\
                "\""+ self.firstname +"\","+\
                "\""+ self.lastname +"\","+\
                "\""+ self.number +"\","+\
                "\""+ self.dep +"\","+\
                "\""+ self.email +"\""+\
                "}"