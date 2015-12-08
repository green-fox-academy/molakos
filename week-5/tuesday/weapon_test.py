import unittest
from weapon import Bow

class TestBow(unittest.TestCase):
    def test_bow_effect(self):
        weapon = Bow(TestWeapon())
        self.assertEqual(10, weapon.damage())

class TestWeapon:
    def damage(self):
        return 10

if __name__ == '__main__':
    unittest.main()
