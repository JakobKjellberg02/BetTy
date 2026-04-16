import unittest

from betting_bot import BettingBot


class BettingBotTests(unittest.TestCase):
    def test_win_updates_balance_and_profit(self):
        bot = BettingBot(100)
        result = bot.place_bet(stake=10, odds=2.5, won=True)

        self.assertEqual(result.outcome, "win")
        self.assertEqual(result.profit, 15.0)
        self.assertEqual(result.new_balance, 115.0)

    def test_loss_updates_balance_and_profit(self):
        bot = BettingBot(100)
        result = bot.place_bet(stake=25, odds=3.0, won=False)

        self.assertEqual(result.outcome, "lose")
        self.assertEqual(result.profit, -25.0)
        self.assertEqual(result.new_balance, 75.0)

    def test_stake_cannot_exceed_balance(self):
        bot = BettingBot(10)
        with self.assertRaisesRegex(ValueError, "Insufficient balance"):
            bot.place_bet(stake=50, odds=2.0, won=True)

    def test_invalid_bet_inputs_raise(self):
        bot = BettingBot(50)

        with self.assertRaisesRegex(ValueError, "Stake must be greater than zero"):
            bot.place_bet(stake=0, odds=2.0, won=True)

        with self.assertRaisesRegex(ValueError, "Odds must be greater than 1"):
            bot.place_bet(stake=5, odds=1.0, won=True)


if __name__ == "__main__":
    unittest.main()
