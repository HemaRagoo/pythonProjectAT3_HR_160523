class Location:
    def __init__(self, name, description, directions, items, locked=False):
        self.name = name
        self.description = description
        self.directions = directions
        self.locked = locked
        self.items = []

    def __str__(self):
        return f"{self.name}, {self.description}"

    def is_locked(self):
        return self.locked


if __name__ == '__main__':
    from items import Key, Drink

    special_key = Key("special")
    merlion_key = Key("Merlion Key")
    singaporean_drink = Drink("Kopi")
    australian_drink = Drink("Beer")
    map_location = {
        (0, 0): Location("Orchard Road", "A bustling shopping district.", [merlion_key], ["north", "west"], False),
        (0, 1): Location("Chinatown", "A cultural enclave with traditional shops.", [singaporean_drink],
                         ["east", "north"], False),
        (1, 0): Location("Little India", "The best place to celebrate Deepavali but it needs special access", [],
                         ["west", "north"], True),
        (1, 1): Location("Bugis Street", "A lively street market.", [special_key], ["east", "south"], False),
    }
    for