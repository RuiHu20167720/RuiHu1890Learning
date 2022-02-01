class Address:
    def __init__(self, street,city,state,postal_code,country):
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
my_address = Address(street="TerraNova",city="St. John's", state="NL",postal_code="A1B1G1",country= "CA")
print(my_address.city)
