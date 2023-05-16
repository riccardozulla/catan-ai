import unittest
from Classes.Game import Game
from Classes.Player import Player
from Classes.Bank import Bank
from Command import commands


class TestCommands(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.game = Game()

    def testTradeBank(self):
        player = Player(1, self.game)
        player.resources["wood"] = 4

        previousWood = Bank().resources["wood"]
        previousCrop = Bank().resources["crop"]

        self.game.ctr.execute(
            commands.TradeBankCommand(player, ("crop", "wood")))

        self.assertEqual(player.resources["wood"], 0)
        self.assertEqual(player.resources["crop"], 1)

        self.assertEqual(previousWood+4, Bank().resources["wood"])
        self.assertEqual(previousCrop-1, Bank().resources["crop"])


if __name__ == '__main__':
    unittest.main()
