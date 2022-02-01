# describe the idea/concept of a house
class house:
    """
    data items : address(str) , #_of_rooms(int), price(float), is_for_sale(bool)
    behaviour: open_garage_door(), mow_lawn(), clean_up()
    """

    def __init__(self, street_address, room_count, house_price, is_for_sale):
        self.address = street_address
        self.rooms = room_count
        self.price = house_price
        self.for_sale = is_for_sale


# my_house is a n object of type house
my_house = house(street_address="1 ppd", room_count=10, house_price=3000000, is_for_sale=True)
my_shed = house(street_address="2ppd", room_count=0, house_price=20000, is_for_sale=False)
print(type(my_house))
print(my_house.price)
print(my_shed.price)
