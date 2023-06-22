CHARACTERS = {
    "Shopkeeper": "A friendly shopkeeper who can give you helpful advice.",
    "Tourist": "A lost tourist who needs your help to find their way.",
    "Police Officer": "A stern police officer who is investigating a crime."
}

class NonPlayerCharacter:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} says: Selamat pagi, Welcome to Singapore.")

    def give_item(self, item):
        print(f"{self.name} gives you {item.name}. Keep the {item.name} till you meet the Merlion.")



