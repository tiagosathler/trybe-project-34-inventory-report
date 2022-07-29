from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data: list):
        self._data = data
        self._index = 0

    def __next__(self):
        try:
            product = self._data[self._index]
        except IndexError:
            raise StopIteration()
        else:
            self._index += 1
            return product
