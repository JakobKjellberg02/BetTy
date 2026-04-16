"""Simple betting bot with bankroll management."""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass
class BetResult:
    outcome: str
    stake: float
    odds: float
    profit: float
    new_balance: float


class BettingBot:
    def __init__(self, starting_balance: float) -> None:
        if starting_balance < 0:
            raise ValueError("Starting balance cannot be negative")
        self.balance = float(starting_balance)

    def place_bet(self, stake: float, odds: float, won: bool) -> BetResult:
        if stake <= 0:
            raise ValueError("Stake must be greater than zero")
        if odds <= 1:
            raise ValueError("Odds must be greater than 1")
        if stake > self.balance:
            raise ValueError("Insufficient balance")

        self.balance -= stake
        if won:
            payout = stake * odds
            self.balance += payout
            profit = payout - stake
            outcome = "win"
        else:
            profit = -stake
            outcome = "lose"

        return BetResult(
            outcome=outcome,
            stake=stake,
            odds=odds,
            profit=round(profit, 2),
            new_balance=round(self.balance, 2),
        )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a single betting simulation")
    parser.add_argument("--balance", type=float, required=True, help="Starting balance")
    parser.add_argument("--stake", type=float, required=True, help="Bet amount")
    parser.add_argument("--odds", type=float, required=True, help="Decimal odds (>1)")
    parser.add_argument(
        "--result",
        choices=["win", "lose"],
        required=True,
        help="Result of the bet",
    )
    return parser


def main() -> None:
    args = _build_parser().parse_args()
    bot = BettingBot(starting_balance=args.balance)
    result = bot.place_bet(stake=args.stake, odds=args.odds, won=args.result == "win")

    print(f"Outcome: {result.outcome}")
    print(f"Profit: {result.profit:.2f}")
    print(f"Balance: {result.new_balance:.2f}")


if __name__ == "__main__":
    main()
