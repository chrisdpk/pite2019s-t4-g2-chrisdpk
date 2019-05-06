class Matrix():
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.values = [[0] * n for _x in range(m)]

    @classmethod
    def fromList(self, list):
        n = len(list[0])
        for i in list:
            if len(i) != n:
                return None
        new = Matrix(m=len(list), n=len(list[0]))
        new.values = list
        return new

    def __eq__(self, other):
        if self.m == other.m and self.n == other.n:
            for i in range(self.m):
                for j in range(self.n):
                    if self[i, j] != other[i, j]:
                        return False
            return True
        else:
            return False

    def __getitem__(self, tup):
        y, x = tup
        return self.values[y][x]

    def __setitem__(self, tup, item):
        y, x = tup
        self.values[y][x] = item

    def __mul__(self, other):
        if(isinstance(other, Matrix)):
            return self.product(other)
        elif(isinstance(other, (int, float))):
            return self.scalar(other)

    def __add__(self, other):
        if(isinstance(other, Matrix)):
            return self.add(other)
        elif(isinstance(other, (int, float))):
            new = Matrix(n=self.n, m=self.m)
            for i in range(self.n):
                for j in range(self.m):
                    new[i, j] = self[i, j] + other
            return new

    def __sub__(self, other):
        return self + (other * -1)

    def __repr__(self):
        s = ''
        for i in range(self.m):
            s += ' '.join(map(str, self.values[i]))
            s += '\n'
        return s

    def add(self, m2):
        if m2.n == self.n and m2.m == self.m:
            sum = Matrix(self.n, self.m)
            for i in range(self.m):
                for j in range(self.m):
                    sum[i, j] = self.values[i][j] + m2.values[i][j]
            return sum
        else:
            return None

    def product(self, m2):
        new = Matrix(m=self.m, n=m2.n)
        for i in range(self.m):
            for j in range(m2.n):
                s = 0
                for r in range(m2.n):
                    s += self[i, r] * m2[r, j]
                new[i, j] = s
        return new

    def scalar(self, scalar):
        new = Matrix(m=self.m, n=self.n)
        for i in range(self.m):
            for j in range(self.n):
                new[i, j] = self[i, j] * scalar
        return new

    def transpose(self):
        new = Matrix(n=self.m, m=self.n)
        for j in range(new.m):
            for i in range(new.n):
                new[j, i] = self[i, j]
        return new


if __name__ == '__main__':
    pass
