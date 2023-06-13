class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def __lt__(self, other):
        return self.name < other.name


class Key(Item):
    def __init__(self, name):
        super().__init__(name)


class Drink(Item):
    def __init__(self, name):
        super().__init__(name)



if __name__ == "__main__":
    killer_key = Key("Killer Key")
    merlion_key = Key("Merlion Key")
    singaporean_drink = Drink("Kopi")
    australian_drink = Drink("Beer")
    print(special_key, merlion_key, singaporean_drink, australian_drink)