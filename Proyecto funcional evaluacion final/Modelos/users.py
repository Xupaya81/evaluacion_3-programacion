from Modelos.address import Address
from Modelos.company import Company

class User(Address, Company):
    def __init__(self,
                 id_address=0,
                 id_company=0,
                 id_user=0,
                 name='',
                 username='',
                 email='',
                 phone='',
                 website=''):
        Address.__init__(self, id_address)
        Company.__init__(self, id_company)
        self.id_user = id_user
        self.name = name
        self.username = username
        self.email = email
        self.phone = phone
        self.website = website