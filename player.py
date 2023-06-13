from backpack import BackPack
from items import Key, Drink


class Player:
    def __init__(self, name, items, map_size):
        self.name = name
        self.current_location = [0, 0]
        self.backpack = BackPack(items)
        self.map_size = map_size

    def __repr__(self):
        return self.name

    def move(self, direction):
        x, y = self.current_location
        if direction == "N" and y > 0:
            self.current_location = (x, y - 1)
        elif direction == "S" and y < self.map_size - 1:
            self.current_location = (x, y + 1)
        elif direction == "W" and x > 0:
            self.current_location = (x - 1, y)
        elif direction == "E" and x < self.map_size - 1:
            self.current_location = (x + 1, y)
        else:
            print("You cannot move in that direction from here.")
            return

        print("You move to", self.current_location)


    # def move(self, direction):
    #     x, y = self.current_location
    #     if direction == "N" and y > 0:
    #         self.current_location = (x, y - 1)
    #     elif direction == "S" and y < MAP_SIZE - 1:
    #         self.current_location = (x, y + 1)
    #     elif direction == "W" and x > 0:
    #         self.current_location = (x - 1, y)
    #     elif direction == "E" and x < MAP_SIZE - 1:
    #         self.current_location = (x + 1, y)
    #     else:
    #         print("You cannot move in that direction from here.")
    #         return
    #
    #     print("You move to", self.get_current_location())
    #
    # def get_current_location(self):
    #     x, y = self.current_location
    #     for location, coords in LOCATIONS.items():
    #         if coords == (x, y):
    #             return location

    # def add_item_to_backpack(self, item):
    #     self.backpack.append(item)
    #     print(f"You have added {item.name} to your backpack.")
    #
    # def remove_item_from_backpack(self, item):
    #     if item in self.backpack:
    #         self.backpack.remove(item)
    #         print(f"You have removed {item.name} from your backpack.")
    #     else:
    #         print(f"{item.name} is not in your backpack.")
    #
    # def show_backpack_contents(self):
    #     if self.backpack:
    #         print("Your backpack contains:")
    #         for item in self.backpack:
    #             print(item.name)
    #     else:
    #         print("Your backpack is empty.")
    #
    # def pick_up_item(self, item):
    #     self.backpack.append(item)
    #     print(f"You have picked up {item.name}.")
    #
    # def drop_item(self, item):
    #     if item in self.backpack:
    #         self.backpack.remove(item)
    #         print(f"You have dropped {item.name}.")
    #     else:
    #         print(f"{item.name} is not in your backpack.")


if __name__ == "__main__":
    special_key = Key("special")
    door_key = Key("door")
    singaporean_drink = Drink("Kopi")
    australian_drink = Drink("Beer")
    player = Player("hema", [door_key, singaporean_drink])

    print(player)
    print(player.backpack)
    print(player.backpack.in_backpack(door_key))
    print(player.backpack[1])