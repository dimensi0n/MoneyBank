import unittest
import src.main as bank
class TestBank(unittest.TestCase):
    def testPayThree(self):
        moneyBank = bank.MoneyBank([1], [])
        self.assertEqual(moneyBank.pay([2,2], [],3), (0, [],[1]))
    def testPayFourFifty(self):
        moneyBank = bank.MoneyBank([0.5], [])
        self.assertEqual(moneyBank.pay([5], [],4.5),(0, [],[0.5]))
    def testPayFourtyTwoWithBills(self):
        moneyBank = bank.MoneyBank([2, 1], [5])
        self.assertEqual(moneyBank.pay([], [50], 42), (0, [5], [2, 1]))
    def testCantGiveBack(self):
        moneyBank = bank.MoneyBank([], [])
        self.assertEqual(moneyBank.pay([1,2,2,2], [],6.5), (0.5, [],[]))
    def testIsExactlyWhatYouHaveToGive(self):
        moneyBank = bank.MoneyBank([], [])
        self.assertEqual(moneyBank.pay([], [10], 10), (0))

if __name__ == '__main__':
    unittest.main()
