import unittest
import q1_f, q2_f, q3_f, q4_f, q5_f, q6_f, q7_f, q8_f, q9_f, q10_f

class TestQ1(unittest.TestCase):

    def test_maxi(self):
        result = q1_f.maxi(45, 23, 65)
        self.assertTrue(result, 65)


class TestQ2(unittest.TestCase):

    def test_listsum(self):
        result = q2_f.listsum([8, 2, 3, -10, 7])
        self.assertEqual(result, 10)


class TestQ3(unittest.TestCase):
    def test_product(self):
        result = q3_f.product([8, 2, 3, -10, 7])
        self.assertEqual(result, -3360)


class TestQ4(unittest.TestCase):
    def test_reverse(self):
        result = q4_f.reverse("45sdfg99f")
        self.assertEqual(result, "f99gfds54")


class TestQ5(unittest.TestCase):
    def test_fact(self):
        result = q5_f.fact(7)
        self.assertEqual(result, 5040)


class TestQ6(unittest.TestCase):
    def test_range_check(self):
        result = q6_f.range_check(20)
        self.assertEqual(result, "The number is out of range")


class TestQ7(unittest.TestCase):
    def test_func(self):
        result = q7_f.func("Hello World")
        self.assertEqual(result, (2,8))


class TestQ8(unittest.TestCase):
    def test_uniq(self):
        result = q8_f.uniq([1,1,1,2,2,2,3,3,3,4,4,4])
        self.assertEqual(result, [1,2,3,4])


class TestQ9(unittest.TestCase):
    def test_isprime(self):
        result = q9_f.isprime(197)
        self.assertEqual(result, "Prime")


class TestQ10(unittest.TestCase):
    def test_iseven(self):
        result = q10_f.iseven([23,43,12,44,23,60])
        self.assertEqual(result, [12,44,60])



if __name__ == '__main__':
    unittest.main()