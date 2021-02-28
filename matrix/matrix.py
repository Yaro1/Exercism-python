class Matrix:
    def __init__(self, matrix_string):
        self.dataRow = []
        self.dataColumn = []

        for i in matrix_string.split('\n'):
            i_split = i.split()
            self.dataRow.append(list())
            for j in i_split:
                self.dataRow[-1].append(int(j))

        for i in range(len(self.dataRow[0])):
            self.dataColumn.append(list())
            for j in range(len(self.dataRow)):
                self.dataColumn[-1].append(self.dataRow[j][i])

    def row(self, index):
        return self.dataRow[index - 1]

    def column(self, index):
        return self.dataColumn[index - 1]


