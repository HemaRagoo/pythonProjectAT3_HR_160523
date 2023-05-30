from location import Location

class Map:
    def __init__(self, location):
        self.locations = location
        self.start_location = self.locations[(0, 0)]
        self.player_location = self.start_location

    def __repr__(self):
        map_str = ""
        for x in range(2):
            for y in range(2):
                location = self.locations.get((x, y))
                if location == self.player_location:
                    map_str += "[X]"
                elif location:
                    map_str += "[ ]"
                else:
                    map_str += "[ ]"
            map_str += "\n"
        return map_str

    def trace_player(self, file_path, player):
        file = open(file_path)
        position = player.current_location
        # print(file.readlines())
        row_length = len(file.readline())
        #[0, 1]
        file.close()
        player_location = player.current_location[0] + player.current_location[1] * row_length
        print(player_location)
        file = open(file_path, 'rb+')
        file.seek(player_location)
        file.write(b'X')

        # print(row_length)

if __name__ == '__main__':
    map_location = {
        (0, 0): Location("Orchard Road", "A bustling shopping district.", ["north", "west"]),
        (1, 1): Location("Bugis Street", "A lively street market.", ["east", "south"]),
        # (0, 2): Location("Chinatown", "A cultural enclave with traditional shops."),
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
    game_map = Map(map_location)
    print(game_map)
    print(game_map.locations[(0, 0)].name,":",game_map.locations[(0, 0)].description)
    from player import Player
    from items import Key, Drink
    special_key = Key("special")
    door_key = Key("door")
    singaporean_drink = Drink("Kopi")
    australian_drink = Drink("Beer")
    player = Player("hema", [door_key, singaporean_drink])
    player.current_location = [1,1]
    game_map.trace_player('map.txt', player)

    # print(game_map.locations[(0, 0)].directions)