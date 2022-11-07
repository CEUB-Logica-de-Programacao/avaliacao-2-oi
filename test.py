import unittest

from bonus import bonus
from q1 import q1
from q2 import q2
from q3 import q3
from q4 import q4
from q5 import q5


class BaseTestCase(unittest.TestCase):
    def test_q1(self):
        self.assertEqual(q1(["Mary", "John", "Emma"], [180, 165, 170]), ["Mary", "Emma", "John"])
        self.assertEqual(q1(["Alice", "Bob", "Bob"], [155, 185, 150]), ["Bob", "Alice", "Bob"])
        self.assertEqual(q1(["John", "John", "John"], [165, 170, 175]), ["John", "John", "John"])
        self.assertEqual(q1(["John", "Bob", "Ana", "Jose", "Cledison"], [165, 170, 175, 190, 155]),
                         ['Jose', 'Ana', 'Bob', 'John', 'Cledison'])
        self.assertEqual(q1(["John", "Bob", "Ana", "Jose", "Cledison"], [178, 198, 185, 184, 182]),
                         ['Bob', 'Ana', 'Jose', 'Cledison', 'John'])

    def test_q2(self):
        self.assertEqual(q2(1), 1)
        self.assertEqual(q2(2), 2)
        self.assertEqual(q2(3), 3)
        self.assertEqual(q2(4), 5)
        self.assertEqual(q2(5), 8)
        self.assertEqual(q2(6), 13)
        self.assertEqual(q2(7), 21)
        self.assertEqual(q2(8), 34)

    def test_q3(self):
        self.assertEqual(q3([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(q3([7, 6, 4, 3, 1]), 0)
        self.assertEqual(q3([1, 2, 3, 4, 5]), 4)
        self.assertEqual(q3([6223, 2563, 37344, 123, 63342]), 63219)
        self.assertEqual(q3([1, 23, 53, 25, 88, 23]), 87)

    def test_q4(self):
        self.assertEqual(q4('MCMXCIV'), 1994)
        self.assertEqual(q4('LVIII'), 58)
        self.assertEqual(q4('IX'), 9)
        self.assertEqual(q4('III'), 3)
        self.assertEqual(q4('IV'), 4)
        self.assertEqual(q4('DCXXI'), 621)
        self.assertEqual(q4('MCMXC'), 1990)
        self.assertEqual(q4('MMXIV'), 2014)
        self.assertEqual(q4('MCMXCVI'), 1996)
        self.assertEqual(q4('MCMXCVII'), 1997)
        self.assertEqual(q4('MCMXCVIII'), 1998)
        self.assertEqual(q4('MCMXCIX'), 1999)
        self.assertEqual(q4('MM'), 2000)
        self.assertEqual(q4('MMIII'), 2003)
        self.assertEqual(q4('MMIV'), 2004)
        self.assertEqual(q4('MMVII'), 2007)
        self.assertEqual(q4('MXLI'), 1041)
        self.assertEqual(q4('DXCIII'), 593)
        self.assertEqual(q4('CMXCIV'), 994)

    def test_q5(self):
        self.assertEqual(q5([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]), "Sao Paulo")
        self.assertEqual(q5([["B", "C"], ["D", "B"], ["C", "A"]]), "A")
        self.assertEqual(q5([["A", "Z"]]), "Z")
        self.assertEqual(q5([["B", "C"], ["C", "A"], ["D", "B"]]), "A")
        self.assertEqual(q5([["B", "C"], ["E", "F"], ["F", "B"], ["B", "C"], ["C", "A"], ["D", "B"]]), "A")

    def test_bonus(self):
        self.assertEqual(bonus([3, 30, 34, 5, 9, 12]), '953433012')
        self.assertEqual(bonus([3, 30, 34, 5, 9]), '9534330')
        self.assertEqual(bonus([0, 0, 0, 0, 0, 0]), '0')
        self.assertEqual(bonus([0, 0, 0, 0, 0, 1]), '100000')
        self.assertEqual(bonus([10, 2]), '210')
        self.assertEqual(bonus([561, 23342, 99, 4345, 37834, 8438956, 3452, 12, 351, 474, 568, 59, 6, 5, 2]),
                         '9984389566595685615474434537834351345223342212')


if __name__ == '__main__':
    unittest.main()
