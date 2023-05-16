import Classes.Player as Player
import Classes.Board as Board
import Classes.Bank as Bank
import Command.commands as commands
import Classes.Game as Game
import unittest


class TestMonopoly(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestMonopoly, self).__init__(*args, **kwargs)
        self.initializeStuff()

    def initializeStuff(self):
        self.game = Game.Game(4)

        self.activePlayer = self.game.players[0]
        self.otherPlayers = [self.game.players[1],
                             self.game.players[2],
                             self.game.players[3]]

    def givePlayersResources(self):
        for op in self.otherPlayers:
            self.game.ctr.execute(
                commands.BankGiveResourceCommand(op, "crop"))
            self.game.ctr.execute(
                commands.BankGiveResourceCommand(op, "iron"))
            self.game.ctr.execute(
                commands.BankGiveResourceCommand(op, "sheep"))
            self.game.ctr.execute(
                commands.BankGiveResourceCommand(op, "clay"))
            self.game.ctr.execute(
                commands.BankGiveResourceCommand(op, "wood"))

    def test_1(self):
        self.givePlayersResources()
        self.game.ctr.execute(
            commands.UseMonopolyCardCommand(self.activePlayer, "crop"))
        self.game.ctr.execute(
            commands.UseMonopolyCardCommand(self.activePlayer, "iron"))
        for op in self.otherPlayers:
            self.assertEquals(op.resources["crop"], 0)
            self.assertEquals(op.resources["iron"], 0)
        self.assertEquals(self.activePlayer.resources["crop"], 3)
        self.assertEquals(self.activePlayer.resources["iron"], 3)

    def test_2(self):
        self.game.ctr.execute(
            commands.UseMonopolyCardCommand(self.activePlayer, "crop"))
        self.game.ctr.execute(
            commands.UseMonopolyCardCommand(self.activePlayer, "iron"))
        self.assertEquals(self.activePlayer.resources["crop"], 0)
        self.assertEquals(self.activePlayer.resources["iron"], 0)


if __name__ == '__main__':
    unittest.main()
