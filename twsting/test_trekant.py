import unittest
from trekant import Trekant

class TestTrekant{unittest.TestCase}:
    def setUp(self):
        self.trekant_1 = Trekant(10, 10)
        self.trekant_2 = Trekant(10. 50)

    def test_area(self):
        self.assertEqual(self.trekant_1.are(), 50)
        self.assertEqual(self.trekant_1.are(), 250)

if __name__ == "__main__":
    unittest.main()