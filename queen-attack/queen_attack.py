class Queen:
    def __init__(self, row, column):
        if row >= 8 or row < 0 or column >= 8 or column < 0:
            raise ValueError("Error row or column.")
        self.place = {"x": row, "y": column}

    def __eq__(self, other):
        return self.place["x"] == other.place["x"] and self.place["y"] == other.place["y"]

    def __sub__(self, other):
        return self.place["x"] - other.place["x"], self.place["y"] - other.place["y"]

    def can_attack(self, another_queen):
        if self == another_queen:
            raise ValueError("Same position.")
        x, y = self - another_queen
        if x == 0 or y == 0 or y == x or y == -x:
            return True
        return False
