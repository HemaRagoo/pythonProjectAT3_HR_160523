class BackPack:
    """
    BackPack Class



    ToDo: [X] Instantiate backpack
    ToDo: [X] Add Item
    ToDo: [X] Remove Item
    ToDo: [ ] List Items
    ToDo: [X] Count items
    ToDo: [X] in backpack (Search for Item - Student to do)
    ToDo: [X] Sort Items

    """

    def __init__(self, items: list):
        self._backpack = []
        if items is None:
            items = []
        for item in items:
            self._backpack.append(item)
        self.sort()

    def __repr__(self):
        return f"{self._backpack!r}"

    def __getitem__(self, index):
        return self._backpack[index]

    def sort(self):
        self._backpack.sort()

    def count(self):
        return len(self._backpack)

    def list(self):
        """no need to implement-not relevant to my game"""
        pass

    def remove(self, item):
        if item is not None:
            self._backpack.remove(item)

    def add(self, item):
        if item is not None:
            self._backpack.append(item)
            self.sort()

    def in_backpack(self, item) -> int:
        """
        Complete this method using a binary search
        returns -1 or False if not found
        returns position if found
        :param item:
        :return: -1 | False | integer
        """
        low: int = 0
        high: int = len(self._backpack) - 1
        return self._binary_search(item, low, high)

    def _binary_search(self, item, low: int, high: int) -> int:
        if low > high:
            return -1

        mid: int = (low + high) // 2
        if self._backpack[mid] == item:
            return mid
        elif self._backpack[mid] < item:
            return self._binary_search(item, mid + 1, high)
        else:
            return self._binary_search(item, low, mid - 1)
