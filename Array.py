class Array:
    def __init__(self, capacity):
    # """ Capacity is the static size of the array. Each index is initialized
    # to None """
        self._items = []
        self._logical_size = 0
        for i in range(capacity):
            self._items.append(None)


    def __len__(self):
    # """ Returns the capacity of this Array """
        return len(self._items)
    def __str__(self):
    # """ Returns a string representation of this Array """
        return str(self._items)
    def __iter__(self):
    # """ Returns an iterator over the Array """
        return iter(self._items)
    def __getitem__(self, index):
    # """ Return the item at the given index """
        return self._items[index]
    def __getter__(self):
        return self._logical_size
    def __setitem__(self, index, new_item):
    # """ Adds the value 'new_item' to the array at the given index """
        try:
            self._items[index] = new_item
            self._logical_size += 1
        except IndexError:
            raise IndexError("Array does not have an index " + str(index))
        if index >= self._logical_size:
            raise IndexError("Attempting to update an index further than first logically empty index of the array.")
        if new_item == None and index < (self._logical_size - 1):
            raise IndexError("Cannot set index to None unless it's the last logically filled index of array")
    def __eq__(self, other):
        if self._logical_size == other._logical_size and len(self._items) == len(other._items):
            other_index = 0
            for i in self._items:
                if i == other._items[other_index]:
                    other_index += 1
                else:
                    return False
            return True
        return False
