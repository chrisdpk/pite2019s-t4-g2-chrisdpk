class Matrix():
    def __init__(self, a1, a2, b1, b2):
        self.values = [a1, a2, b1, b2]
        
    def add(self, m2):
        return Matrix(self.values[0] + m2.values[0],
                    self.values[1] + m2.values[1],
                    self.values[2] + m2.values[2],
                    self.values[3] + m2.values[3])
    def product(self, m2):
        return Matrix(self.values[0] * m2.values[0] + self.values[1] * m2.values[2],
                    self.values[0] * m2.values[1] + self.values[1] * m2.values[3],
                    self.values[2] * m2.values[0] + self.values[3] * m2.values[2],
                    self.values[2] * m2.values[1] + self.values[3] * m2.values[3])

    def scalar(self, scalar):
        return Matrix(scalar * self.values[0],
                    scalar * self.values[1],
                    scalar * self.values[2],
                    scalar * self.values[3])
    def transpose(self):
        return Matrix(self.values[0], self.values[2], self.values[1], self.values[3])

    def __repr__(self):
        return "{} {} \n{} {}".format(self.values[0], self.values[1],
                                    self.values[2], self.values[3])

if __name__ == '__main__':
    matrix_1 = Matrix(4,5,6,7)
    matrix_2 = Matrix(2,2,2,1)
    matrix_3 = matrix_2.add(matrix_1)
    product =  matrix_1.product(matrix_2)
    print("... Matrix A ...")
    print(matrix_1)
    print("... Matrix B ...")
    print(matrix_2)
    print("... A + B ... ")
    print(matrix_3)
    print("... A * B...")
    print(product)
    print(" ... 3 * A ...")
    print(matrix_1.scalar(3))
    print("... A transposed ... ")
    print(matrix_1.transpose())
    print(".. ((A transposed) + B) * B ... ")
    print(matrix_1.transpose().add(matrix_2).product(matrix_2))
