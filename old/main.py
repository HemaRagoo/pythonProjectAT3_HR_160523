from player import Player
from world import Map
from items import Key, Drink
from location import Location

# Write the gameplay here, like menu function and move function decision function as well
special_key = Key("special key")
door_key = Key("door key")
singaporean_drink = Drink("Kopi")
australian_drink = Drink("Beer")

map_location = {
    (0, 0): Location("Orchard Road", "A bustling shopping district.", ["north", "west"], False),
    (0, 1): Location("Chinatown", "A cultural enclave with traditional shops.", ["east", "north"], False),
    (1, 0): Location("Little India", "The best place to celebrate Deepavali but it needs special access", ["west", "north"], True),
    (1, 1): Location("Bugis Street", "A lively street market.", ["east", "south"], False),
}
player = Player("hema", [door_key, singaporean_drink], map_location)

game_map = Map(map_location, player)

game_map.locations[(0, 1)].items = [special_key, door_key]
game_map.locations[(0, 0)].items = [singaporean_drink]
game_map.locations[(1, 1)].items = [australian_drink]





# print(game_map.locations[tuple(player.current_location)])
# player.move('west')

# print(game_map.locations[(0, 1)].items)

while True:
    direction = input("Hi kindly choose where you would like to go: North, East, South, West?: ").lower()
    player.move(direction)
    x, y = player.current_location




