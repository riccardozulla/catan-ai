import Classes.Player as Player
import Classes.Board as Board
import Classes.Bank as Bank
import Command.commands as commands
import Classes.Game as Game
import os
import unittest


class TestLargestArmy(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.game = Game.Game(3)
        b = Board.Board()

        self.largestArmyPlayer = Player.Player(0, self.game)

        self.Player1 = self.game.players[0]
        self.Player2 = self.game.players[1]
        self.Player3 = self.game.players[2]

        self.results = [0, 1]

    # def __init__(self, test):
    #     print("Evaluating test: ", test)
    #     self.game = Game.Game(3)
    #     b = Board.Board()

    #     self.largestArmyPlayer = Player.Player(0, self.game)

    #     self.Player1 = self.game.players[0]
    #     self.Player2 = self.game.players[1]
    #     self.Player3 = self.game.players[2]

    #     self.results = [0, 1]

    def test_0(self):
        self.game.ctr.execute(commands.UseKnightCommand(self.Player1, 1))
        self.assertEqual(0, self.game.largestArmyPlayer.id)

    def test_1(self):
        previousPoints = self.Player1.victoryPoints
        previousOwner = self.game.largestArmyPlayer.id

        self.game.ctr.execute(commands.UseKnightCommand(self.Player1, 1))
        self.game.ctr.execute(commands.UseKnightCommand(self.Player1, 2))
        self.game.ctr.execute(commands.UseKnightCommand(self.Player1, 3))

        self.assertEqual(previousPoints+2, self.Player1.victoryPoints)
        self.assertNotEqual(previousOwner, self.game.largestArmyPlayer.id)

    def test_2(self):
        self.assertEqual(
            [0, 0, 0], [p.victoryPoints for p in self.game.players])
        self.assertEqual(0, self.game.largestArmyPlayer.id)

        self.game.ctr.execute(commands.UseKnightCommand(self.Player1, 1))
        self.game.ctr.execute(commands.UseKnightCommand(self.Player1, 1))
        self.game.ctr.execute(commands.UseKnightCommand(self.Player1, 1))

        self.assertEqual(
            [2, 0, 0], [p.victoryPoints for p in self.game.players])
        self.assertEqual(1, self.game.largestArmyPlayer.id)

        self.game.ctr.execute(commands.UseKnightCommand(self.Player2, 1))
        self.game.ctr.execute(commands.UseKnightCommand(self.Player2, 2))
        self.game.ctr.execute(commands.UseKnightCommand(self.Player2, 3))
        self.game.ctr.execute(commands.UseKnightCommand(self.Player2, 4))

        self.assertEqual(
            [0, 2, 0], [p.victoryPoints for p in self.game.players])
        self.assertEqual(2, self.game.largestArmyPlayer.id)
