class Location:
    def __init__(self, name, description, directions, lock_condition):
        self.name = name
        self.description = description
        self.item = []
        self.directions = directions
        self.locked = lock_condition

    def __str__(self):
        return f"{self.name}, {self.description}"
