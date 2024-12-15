from Modelos.geos import Geo


class Address(Geo):
    def __init__(self,
                 id_geo=0,
                 id_address=0,
                 street='',
                 suite='',
                 city='',
                 zipcode=''):
        Geo.__init__(self, id_geo)
        self.id_address = id_address
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode