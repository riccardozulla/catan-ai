import Command.commands as commands
import Classes.Game as Game
import unittest


class TestRoadBuilding(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestRoadBuilding, self).__init__(*args, **kwargs)
        self.initializeStuff()

    def initializeStuff(self):
        self.game = Game.Game(2)
        self.Player1 = self.game.players[0]
        self.Player2 = self.game.players[1]

    def test1(self):
        previous = list.copy(self.Player1.ownedStreets)
        self.game.ctr.execute(commands.UseRoadBuildingCardCommand(
            self.Player1, [(0, 1), (0, 8)]))
        self.assertEqual(len(previous) + 2, len(self.Player1.ownedStreets))
        self.assertTrue((0, 1) in self.Player1.ownedStreets)
        self.assertTrue((0, 8) in self.Player1.ownedStreets)

    def test2(self):
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (7, 8)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (0, 8)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (0, 1)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (1, 2)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (2, 3)))

        self.assertEqual([2, 0], [self.Player1.victoryPoints,
                         self.Player2.victoryPoints])

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (4, 5)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (5, 6)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (6, 14)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (14, 15)))

        self.assertEqual([(4, 5), (5, 6), (6, 14), (14, 15)],
                         self.Player2.ownedStreets)
        self.assertEqual([2, 0], [self.Player1.victoryPoints,
                         self.Player2.victoryPoints])

        self.game.ctr.execute(commands.UseRoadBuildingCardCommand(
            self.Player2, ((15, 25), (25, 26))))

        self.assertEqual([(4, 5), (5, 6), (6, 14), (14, 15),
                         (15, 25), (25, 26)], self.Player2.ownedStreets)
        self.assertEqual([0, 2], [self.Player1.victoryPoints,
                         self.Player2.victoryPoints])


if __name__ == '__main__':
    unittest.main()
