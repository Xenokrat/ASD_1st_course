import ctypes


class DynArray:
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self, i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2 * self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self, i, itm):
        # add object imt to "i" position, starts with 0, end with self.count
        # if add in tail
        if i == self.count:
            self.append(itm)
            return

        # out of bounds
        if i > self.count or i < 0:
            raise IndexError('Index is out of bounds')

        # resize capacity if it's not enough
        if self.count == self.capacity:
            self.resize(2 * self.capacity)

        # insertion
        for ind in range(self.count, i, -1):
            self.array[ind] = self.array[ind - 1]

        self.array[i] = itm
        self.count += 1

    def delete(self, i):
        # is there need to resize?
        is_arr_too_big = (self.count - 1) / self.capacity < 0.5
        if is_arr_too_big:
            self.resize(int(self.capacity / 1.5))
        if self.capacity < 16:
            self.capacity = 16

        # out of bounds
        if i >= self.count or i < 0:
            raise IndexError('Index is out of bounds')

        # del
        for ind in range(i, self.count - 1):
            self.array[ind] = self.array[ind + 1]

        self.count -= 1
        self.array[self.count] = ctypes.py_object()  # dunno if this needed
