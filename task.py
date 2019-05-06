from Matrix import Matrix

m1 = Matrix(4, 4)
m1[0, 0] = 10
m1[1, 0] = 9
m1[3, 2] = 5
print(m1)
m2 = Matrix.fromList([[1, 2, 3, 4], [4, 3, 2, 1], [2, 3, 4, 1], [3, 4, 1, 2]])
print(m2)

print(m1+8)
print(m2-4)
print(m2*8)
print(m2*(-5))
print(m1+m2)
print(m1*m2)
print(m2.transpose())
