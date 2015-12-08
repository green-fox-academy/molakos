import unittest
from wizard import Wizard

class TestWizard(unittest.TestCase):
    def test_existance(self):
        wizard = Wizard('Merlin', 40, 10, 20)

    def test_inheritance(self):
        wizard = Wizard('Merlin', 40, 10, 20)
        self.assertEqual(wizard.hp, 40)

    def test_mana(self):
        wizard = Wizard('Merlin', 40, 10, 20)
        self.assertEqual(wizard.mana, 20)

    def test_strike(self):
        wizard = Wizard('Merlin', 40, 10, 20)
        opponent = Wizard('Gandalf', 40, 10, 20)
        wizard.strike(opponent)
        self.assertEqual(opponent.hp, 10)
        self.assertEqual(wizard.mana, 15)

    def test_strike_without_mana(self):
        wizard = Wizard('Merlin', 40, 9, 0)
        opponent = Wizard('Gandalf', 30, 10, 20)
        wizard.strike(opponent)
        self.assertEqual(opponent.hp, 27)


unittest.main()
