class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [""] * capacity
        self.current_index = 0
        self.read_index = 0
        self.is_empty = True

    def __len__(self):
        return self.capacity

    def read(self):
        if self.is_empty:
            raise BufferEmptyException("The buffer is empty. |uck off.")
        if self.data[self.read_index % self.capacity] == "":
            raise BufferEmptyException("We can read items only ones.")
        item = self.data[self.read_index % self.capacity]
        self.data[self.read_index % self.capacity] = ""
        self.read_index += 1
        return item

    def write(self, data):
        if self.current_index % self.capacity == 0 and self.current_index != 0 and self.data[self.current_index % self.capacity] != "":
            raise BufferFullException("The buffer is full. |uck off.")
        self.data[self.current_index % self.capacity] = data
        self.current_index += 1
        self.is_empty = False

    def overwrite(self, data):
        if self.current_index >= self.capacity:
            self.data[self.read_index % self.capacity] = data
            self.read_index += 1
        else:
            self.write(data)

    def clear(self):
        self.current_index = 0
        self.read_index = 0
        self.data = [""] * self.capacity
        self.is_empty = True
