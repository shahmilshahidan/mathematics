import unittest
import number_speller as ns

class spellerTest(unittest.TestCase):
    def test_singleDigit(self):
        self.assertEqual(ns.spellNum(0), 'zero')
        self.assertEqual(ns.spellNum(5), 'five')

    def test_doubleDigit(self):
        self.assertEqual(ns.spellNum(17), 'seventeen')
        self.assertEqual(ns.spellNum(61), 'sixty one')

    def test_tripleDigit(self):
        self.assertEqual(ns.spellNum(400), 'four hundred')
        self.assertEqual(ns.spellNum(304), 'three hundred four')
        self.assertEqual(ns.spellNum(713), 'seven hundred thirteen')
        self.assertEqual(ns.spellNum(192), 'one hundred ninety two')

    def test_quadDigit(self):
        self.assertEqual(ns.spellNum(2000), 'two thousand')
        self.assertEqual(ns.spellNum(3008), 'three thousand eight')
        self.assertEqual(ns.spellNum(6015), 'six thousand fifteen')
        self.assertEqual(ns.spellNum(8387), 'eight thousand three hundred eighty seven')

    def test_quinDigit(self):
        self.assertEqual(ns.spellNum(70000), 'seventy thousand')
        self.assertEqual(ns.spellNum(20002), 'twenty thousand two')
        self.assertEqual(ns.spellNum(80019), 'eighty thousand ninteen')
        self.assertEqual(ns.spellNum(83870), 'eighty three thousand eight hundred seventy')
        self.assertEqual(ns.spellNum(51629), 'fifty one thousand six hundred twenty nine')

if __name__ == "__main__":
    unittest.main()
