

class Map:
    """Create a map class that contains the location and player to ensure the player is able to start from the
    first location and be able to view player in the grid by 2 by 2"""
    def __init__(self, location, player):
        """
        :param location: dict
        :param player: Player
        """
        self.locations = location
        self.player = player
        self.current_location = [0, 0]

    def trace_player(self, file_path):
        """Trace player by reading the binary file to show player's position. Random access technique is used to access
        visibility on player's location"""
        file = open(file_path)
        position = self.player.current_location
        row_length = len(file.readline())
        file.close()
        player_location = position[0] + position[1] * row_length
        print(player_location)
        file = open(file_path, 'rb+')
        file.seek(player_location)
        file.write(b'X')


if __name__ == '__main__':
    # pass
    from player import Player
    from items import Key, Drink
    from location import Location
    map_location = {
        (0, 0): Location("Orchard Road", "A bustling shopping district.", ["north", "west"]),
        (1, 1): Location("Bugis Street", "A lively street market.", ["east", "south"]),
        (0, 2): Location("Chinatown", "A cultural enclave with traditional shops.", ["east", "south"]),
        # (0, 3): Location("Little India", "A vibrant neighborhood with Indian restaurants and shops."),
        # (1, 0): Location("Lavender", "A mix of residential and commercial buildings."),
        # (1, 1): Location("Pasir Ris", "A coastal town with a park and beach."),
        # (1, 2): Location("Jurong East", "A major transportation hub and commercial district."),
        # (1, 3): Location("Jurong West", "A residential town with parks and schools."),
        # (2, 0): Location("Marsiling", "A quiet residential neighborhood."),
        # (2, 1): Location("Sembawang", "A coastal town with a naval base."),
        # (2, 2): Location("Somerset", "A shopping district with high-end stores."),
        # (2, 3): Location("Tiong Bahru", "A trendy neighborhood with cafes and boutiques.")
    }


    special_key = Key("special")
    door_key = Key("door")
    singaporean_drink = Drink("Kopi")
    australian_drink = Drink("Beer")
    player = Player("hema", [door_key, singaporean_drink])
    game_map = Map(map_location, player)

    print(game_map)
    print(game_map.locations[(0, 0)].name, ":", game_map.locations[(0, 0)].description)



    game_map.trace_player('map.txt')