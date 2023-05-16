import Classes.Player as Player
import Classes.Board as Board
import Classes.Bank as Bank
import Command.commands as commands
import Classes.Game as Game
import unittest


class TestStreetOwner(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestStreetOwner, self).__init__(*args, **kwargs)
        self.initializeStuff()

    def initializeStuff(self):
        self.game = Game.Game(2)
        self.Player1 = self.game.players[0]
        self.Player2 = self.game.players[1]

    #     self.results = [5, 5, 11, 5, 10, 10, 5, 7, 6, 10, 5, 10, 5, 5]

    def setUp(self):
        Board.Board().reset()

    def test_0(self):
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (41, 49)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 40)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (40, 41)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (41, 42)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (42, 43)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (43, 44)))

        self.assertEqual(self.game.longestStreetLength, 5)

    def test1(self):
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 40)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (40, 41)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (41, 42)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (42, 43)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (43, 44)))
        self.assertEqual(self.game.longestStreetLength, 5)

    def test2(self):
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 40)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (40, 41)))

        self.game.ctr.execute(commands.PlaceFreeStreetCommand(
            self.Player1, (41, 49)))  # quello in mezzo

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (41, 42)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (42, 43)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (43, 51)))

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (50, 51)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (49, 50)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (48, 49)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (47, 48)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 47)))

        self.assertEqual(self.game.longestStreetLength, 11)

    def test3(self):
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (28, 38)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (38, 39)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 40)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (40, 41)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (41, 42)))
        self.game.ctr.execute(commands.PlaceInitialColonyCommand(
            self.Player2, Board.Board().places[42]))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (42, 43)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (43, 44)))
        self.assertEqual(self.game.longestStreetLength, 5)

    def test4(self):
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 40)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (40, 41)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (41, 49)))
        self.game.ctr.execute(commands.PlaceFreeStreetCommand(
            self.Player2, (41, 42)))  # Player2
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (42, 43)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (43, 51)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (50, 51)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (49, 50)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (48, 49)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (47, 48)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 47)))
        self.assertEqual(self.game.longestStreetLength, 10)

    def test5(self):
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 40)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (40, 41)))
        self.game.ctr.execute(commands.PlaceFreeStreetCommand(
            self.Player2, (41, 49)))  # Player2
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (41, 42)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (42, 43)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (43, 51)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (50, 51)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (49, 50)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (48, 49)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (47, 48)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 47)))
        self.assertEqual(self.game.longestStreetLength, 10)

    def test6(self):
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 40)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (40, 41)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (41, 42)))
        self.game.ctr.execute(commands.PlaceInitialColonyCommand(
            self.Player2, Board.Board().places[42]))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (42, 43)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (43, 44)))

        self.assertEqual(self.game.longestStreetLength, 4)

    def test7(self):
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 40)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (40, 41)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (41, 49)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (48, 49)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (47, 48)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 47)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (30, 40)))

        self.assertEqual(self.game.longestStreetLength, 7)

    def test8(self):
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 40)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (40, 41)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (41, 49)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (48, 49)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (47, 48)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 47)))

        self.assertEqual(self.game.longestStreetLength, 6)

    def test9(self):
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 40)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (40, 41)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (41, 49)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (48, 49)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (47, 48)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 47)))

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (22, 23)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (23, 24)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (24, 35)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (34, 35)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (33, 34)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (22, 33)))

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (19, 20)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (20, 21)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (11, 21)))

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (9, 19)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (21, 22)))

        self.assertEqual(self.game.longestStreetLength, 10)

    def test10(self):
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (4, 5)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (5, 6)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (6, 14)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (15, 25)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (25, 26)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (26, 37)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (36, 37)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (36, 46)))

        self.assertEqual(self.game.longestStreetLength, 5)

    def test11(self):
        # print('Step 0 --------- Owner: ', self.game.longestStreetOwner.id, ' length: ', self.game.longestStreetLength)
        # for p in self.game.players:
        #     print('player: ', p.id, ' points: ', p.victoryPoints)

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (4, 5)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (5, 6)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (6, 14)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (15, 25)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (25, 26)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (26, 37)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (36, 37)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (36, 46)))

        # print('Step 1 --------- Owner: ', self.game.longestStreetOwner.id, ' length: ', self.game.longestStreetLength)
        # for p in self.game.players:
        #     print('player: ', p.id, ' points: ', p.victoryPoints)

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 40)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (40, 41)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (41, 49)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (48, 49)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (47, 48)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 47)))

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (22, 23)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (23, 24)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (24, 35)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (34, 35)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (33, 34)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (22, 33)))

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (19, 20)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (20, 21)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (11, 21)))

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (9, 19)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (21, 22)))

        # print('Step 2 --------- Owner: ', self.game.longestStreetOwner.id, ' length: ', self.game.longestStreetLength)
        # for p in self.game.players:
        #     print('player: ', p.id, ' points: ', p.victoryPoints)

        self.assertEqual(self.game.longestStreetLength, 10)

    def test12(self):
        # print('Step 0 --------- Owner: ', self.game.longestStreetOwner.id, ' length: ', self.game.longestStreetLength)
        # for p in self.game.players:
        #     print('player: ', p.id, ' points: ', p.victoryPoints)

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (4, 5)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (5, 6)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (6, 14)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (15, 25)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (25, 26)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (26, 37)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (36, 37)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (36, 46)))

        # print('Step 1 --------- Owner: ', self.game.longestStreetOwner.id, ' length: ', self.game.longestStreetLength)
        # for p in self.game.players:
        #     print('player: ', p.id, ' points: ', p.victoryPoints)

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 40)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (40, 41)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (41, 49)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (48, 49)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (47, 48)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 47)))

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (22, 23)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (23, 24)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (24, 35)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (34, 35)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (33, 34)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (22, 33)))

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (19, 20)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (20, 21)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (11, 21)))

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (9, 19)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (21, 22)))

        # print('Step 2 --------- Owner: ', self.game.longestStreetOwner.id, ' length: ', self.game.longestStreetLength)
        # for p in self.game.players:
        #     print('player: ', p.id, ' points: ', p.victoryPoints)

        self.game.ctr.execute(commands.PlaceInitialColonyCommand(
            self.Player2, Board.Board().places[21]))
        self.game.ctr.execute(commands.PlaceInitialColonyCommand(
            self.Player2, Board.Board().places[33]))
        self.game.ctr.execute(commands.PlaceInitialColonyCommand(
            self.Player2, Board.Board().places[23]))
        self.game.ctr.execute(commands.PlaceInitialColonyCommand(
            self.Player2, Board.Board().places[40]))
        self.game.ctr.execute(commands.PlaceInitialColonyCommand(
            self.Player2, Board.Board().places[48]))

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (3, 4)))

        # print('Step 3 --------- Owner: ', self.game.longestStreetOwner.id, ' length: ', self.game.longestStreetLength)
        # for p in self.game.players:
        #     print('player: ', p.id, ' points: ', p.victoryPoints)

        self.assertEqual(self.game.longestStreetLength, 5)

    def test13(self):
        # print('Step 0 --------- Owner: ', self.game.longestStreetOwner.id, ' length: ', self.game.longestStreetLength)
        # for p in self.game.players:
        #     print('player: ', p.id, ' points: ', p.victoryPoints)

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (29, 30)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (30, 31)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (31, 32)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (32, 33)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player2, (33, 34)))

        # print('Step 1 --------- Owner: ', self.game.longestStreetOwner.id, ' length: ', self.game.longestStreetLength)
        # for p in self.game.players:
        #     print('player: ', p.id, ' points: ', p.victoryPoints)

        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (39, 40)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (40, 41)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (41, 42)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (42, 43)))
        self.game.ctr.execute(
            commands.PlaceFreeStreetCommand(self.Player1, (43, 44)))

        # print('Step 2 --------- Owner: ', self.game.longestStreetOwner.id, ' length: ', self.game.longestStreetLength)
        # for p in self.game.players:
        #     print('player: ', p.id, ' points: ', p.victoryPoints)

        self.assertEqual(self.game.longestStreetLength, 5)


if __name__ == '__main__':
    unittest.main()
