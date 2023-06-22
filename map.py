class Map:
    def __init__(self, map_size):
        self.map_size = map_size
        self.matrix = [[None for _ in range(self.map_size)] for _ in range(self.map_size)]


if __name__ == '__main__':
    map1 = Map(2)
    print(map1.matrix)
