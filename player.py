from location import Location
from map import Map
from backpack import BackPack


class Player:
    def __init__(self, name, starting_location):
        self.name = name
        self.current_location = starting_location
        self.backpack = BackPack([])

    def move(self, direction, game_map):
        available_exits = game_map.get_available_exits()
        if direction in available_exits:
            row, col = self.current_location
            if direction == 'N':
                row -= 1
            elif direction == 'S':
                row += 1
            elif direction == 'W':
                col -= 1
            elif direction == 'E':
                col += 1

            if 0 <= row < game_map.map_size and 0 <= col < game_map.map_size:
                self.current_location = (row, col)
                game_map.visit_location(self.current_location)
                return True
            else:
                print("Warning: Out of bounds!")
        else:
            print("Warning: Invalid direction!")

        return False

    def pick_up_item(self, item):
        self.backpack.add(item)


if __name__ == '__main__':
    map1 = Map(2)
