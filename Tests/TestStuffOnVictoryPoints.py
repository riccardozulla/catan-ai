import Classes.Player as Player
import Classes.Board as Board
import Classes.Bank as Bank
import Command.commands as commands
import Classes.Game as Game
import unittest


class TestVictoryPoints(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestVictoryPoints, self).__init__(*args, **kwargs)
        self.initializeStuff()

    def initializeStuff(self):
        self.game = Game.Game(2)

        self.Player1 = self.game.players[0]
        self.Player2 = self.game.players[1]

    def testUndoColony(self):
        action = commands.PlaceInitialColonyCommand(
            self.Player1, Board.Board().places[0])
        self.game.ctr.execute(action)
        self.game.ctr.undo()
        self.assertEqual(self.Player1.victoryPoints, 0)

    def testUndoCity(self):
        self.game.ctr.execute(
            commands.BankGiveResourceCommand(self.Player1, "crop"))
        self.game.ctr.execute(
            commands.BankGiveResourceCommand(self.Player1, "crop"))
        self.game.ctr.execute(
            commands.BankGiveResourceCommand(self.Player1, "iron"))
        self.game.ctr.execute(
            commands.BankGiveResourceCommand(self.Player1, "iron"))
        self.game.ctr.execute(
            commands.BankGiveResourceCommand(self.Player1, "iron"))
        action = commands.PlaceCityCommand(
            self.Player1, Board.Board().places[0])
        self.game.ctr.execute(action)
        self.game.ctr.undo()
        self.assertEqual(self.Player1.victoryPoints, 0)

    def testColony(self):
        self.game.ctr.execute(commands.PlaceInitialColonyCommand(
            self.Player1, Board.Board().places[0]))
        self.assertEqual(self.Player1.victoryPoints, 1)

    def testCity(self):
        self.game.ctr.execute(
            commands.BankGiveResourceCommand(self.Player1, "crop"))
        self.game.ctr.execute(
            commands.BankGiveResourceCommand(self.Player1, "clay"))
        self.game.ctr.execute(
            commands.BankGiveResourceCommand(self.Player1, "wood"))
        self.game.ctr.execute(
            commands.BankGiveResourceCommand(self.Player1, "sheep"))

        self.game.ctr.execute(commands.PlaceColonyCommand(
            self.Player1, Board.Board().places[0]))
        self.game.ctr.execute(commands.PlaceInitialColonyCommand(
            self.Player1, Board.Board().places[3]))
        self.game.ctr.execute(
            commands.BankGiveResourceCommand(self.Player1, "crop"))
        self.game.ctr.execute(
            commands.BankGiveResourceCommand(self.Player1, "crop"))
        self.game.ctr.execute(
            commands.BankGiveResourceCommand(self.Player1, "iron"))
        self.game.ctr.execute(
            commands.BankGiveResourceCommand(self.Player1, "iron"))
        self.game.ctr.execute(
            commands.BankGiveResourceCommand(self.Player1, "iron"))
        self.game.ctr.execute(commands.PlaceCityCommand(
            self.Player1, Board.Board().places[0]))
        self.assertEqual(self.Player1.victoryPoints, 3)


if __name__ == '__main__':
    unittest.main()
