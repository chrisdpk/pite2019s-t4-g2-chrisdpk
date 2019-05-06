import unittest
from Matrix import Matrix

class MatrixTest(unittest.TestCase):
    def test_init(self):
        m1 = Matrix(1,1)
        for i in range(m1.m):
            for j in range(m1.n):
                self.assertEqual(0, m1[i,j])
    def test_init2(self):
        m2 = Matrix(1,2)
        self.assertIsNotNone(m2)
    def test_set(self):
        m1 = Matrix(1,1)
        m1[0,0] = 44
        self.assertEqual(44, m1[0,0])
    def test_fromList(self):
        m3 = Matrix.fromList( [[1, 2]] )
        self.assertEqual(1, m3.values[0][0])
    def test_add_matrices(self):
        m1 = Matrix(4,4)
        m2 = Matrix.fromList([ [1,2,3,4], [4,3,2,1], [2,3,4,1], [3,4,1,2]])
        m3 = m1 + m2
        self.assertEqual(m3,m2)
    def test_add_int(self):
        m1 = Matrix(4,4)
        m3 = m1 + 4
        self.assertEqual(Matrix.fromList([[4,4,4,4], [4,4,4,4], [4,4,4,4], [4,4,4,4]]), m3)
    def test_add_float(self):
        m1 = Matrix(4,4)
        m3 = m1 + 3.14
        self.assertEqual(Matrix.fromList([[3.14, 3.14, 3.14, 3.14],[3.14, 3.14, 3.14, 3.14],[3.14, 3.14, 3.14, 3.14],[3.14, 3.14, 3.14, 3.14],]), m3)
    def test_mul_matrices(self):
        m1 = Matrix(4,4)
        m1[0,0] = 10
        m1[1,0] = 9
        m1[3,2] = 5
        m2 = Matrix.fromList([ [1,2,3,4], [4,3,2,1], [2,3,4,1], [3,4,1,2]])
        m_act = m1*m2
        m_exp = Matrix.fromList([ [10, 20, 30, 40], [9, 18, 27, 36], [0,0,0,0], [10, 15, 20, 5] ])
        self.assertEqual(m_exp, m_act)
    def test_mul_scalar(self):
        m2 = Matrix.fromList([ [2,2], [2,2]])
        m_act = m2 * 4
        m_exp = Matrix.fromList([ [8,8], [8,8]])
        self.assertEqual(m_exp, m_act)
    def test_transpose(self):
        m2 = Matrix.fromList([[2,2,2], [3,3,3]])
        m_act = m2.transpose()
        m_exp = Matrix.fromList([[2,3],[2,3],[2,3]])
        self.assertEqual(m_exp, m_act)
    def test_mul_neg_scalar(self):
        m_act = Matrix.fromList([[2,2,2], [3,3,3]])
        m_act *= -1
        m_exp = Matrix.fromList([[-2,-2,-2],[-3,-3,-3]])
        self.assertEqual(m_exp, m_act)
    def test_sub(self):
        m_act = Matrix.fromList([ [2,2], [2,2]])
        m_act -= 1
        m_exp = Matrix.fromList([[1,1],[1,1]])
        self.assertEqual(m_act, m_exp)
    def test_sub_matrices(self):
        m2 = Matrix.fromList([ [2,2], [2,2]])
        m1 = Matrix.fromList([ [1,1], [1,1]])
        m_exp = Matrix.fromList( [[-1,-1], [-1,-1]] )
        m_act = m1-m2
        self.assertEqual(m_exp, m_act)
if __name__ == '__main__':
    unittest.main()
