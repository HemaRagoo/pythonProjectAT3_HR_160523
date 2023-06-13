from player import Player
from world import Map
from location import Location
from items import Key, Drink

# Write the gameplay here, like menu function and move function decision function as well
map_location = {
    (0, 0): Location("Orchard Road", "A bustling shopping district.", ["north", "west"], False),
    (1, 0): Location("Chinatown", "A night street market.", ["west", "north"], True),
    (1, 1): Location("Bugis Street", "A lively street market.", ["east", "south"], True),
}
game_map = Map(map_location)

killer_key = Key("Killer Key")
merlion_key = Key("Merlion Key")

player = Player("hema", [merlion_key], 2)

player.current_location = [1, 1]

player.move('N')
print(game_map.locations[(0, 0)].is_accessible)
print(game_map.locations[(1, 1)].is_accessible)

game_map.locations[(1, 0)].item.append(killer_key)
game_map.locations[(1,1)].item.append(merlion_key)

print(game_map.locations[(1, 0)].item)
