class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = [""] * capacity
        self.current_index = 1
        self.read_index = 1
        self.is_empty = True

    def __len__(self):
        return self.capacity

    def read(self):
        data_index = self.read_index % self.capacity
        if self.is_empty:
            raise BufferEmptyException("The buffer is empty. |uck off.")
        if self.data[data_index] == "":
            raise BufferEmptyException("We can read items only ones.")
        item = self.data[data_index]
        self.data[data_index] = ""
        self.read_index += 1
        return item

    def write(self, data):
        data_index = self.current_index % self.capacity
        if data_index == 0 and self.data[data_index] != "":
            raise BufferFullException("The buffer is full. |uck off.")
        self.data[data_index] = data
        self.current_index += 1
        self.is_empty = False

    def overwrite(self, data):
        if self.current_index >= self.capacity + 1:
            self.data[self.read_index % self.capacity] = data
            self.read_index += 1
        else:
            self.write(data)

    def clear(self):
        self.current_index = 1
        self.read_index = 1
        self.data = [""] * self.capacity
        self.is_empty = True
