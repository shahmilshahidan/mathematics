import unittest
import prime_multiplier as pf 

class PrimeTest(unittest.TestCase):
    def test_prime_factors(self):
        self.assertEqual(pf.primeFactors(1000), [2,2,2,5,5,5])

    def test_prime_factors_with_count(self):
        self.assertEqual(pf.primeFactorsWithCount(1000), [[3,3],[2,5]])

    def test_prime_factors_with_pow(self):
        self.assertEqual(pf.powPrimeFactors(1000), [4,25])


if __name__ == "__main__":
    unittest.main()

