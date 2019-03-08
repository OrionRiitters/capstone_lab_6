from board import Board
from player import Player
from rule_manager import RuleManager
from ui import UI
from unittest import TestCase
from unittest.mock import patch, call
from constant import BOARD_SIZE

class TestBoard(TestCase):

    def test_get_rects_correct_input(self):

        board = Board()

        rectX = board.getRectX('23')
        self.assertEqual(20, rectX)

        rectY = board.getRectY('23')
        self.assertEqual(3, rectY)


    def test_get_rects_incorrect_input(self):

        board = Board()

        with self.assertRaises(ValueError):
            rect_1 = board.getRectX('No')
            rect_2 = board.getRectX(None)
            rect_3 = board.getRectX('@#$')
        with self.assertRaises(ValueError):
            rect_1 = board.getRectY('No')
            rect_2 = board.getRectY(None)
            rect_3 = board.getRecty('@#$')

    def test_fill_coordinate(self):

        board = Board()
        player_1 = Player('Human')
        player_2 = Player('Computer')

        board.fillCoordinate(34, player_1)
        self.assertEqual(' [X] ', board.boardGraphic[BOARD_SIZE - 4][3])

        board.fillCoordinate(43, player_2)
        self.assertEqual(' [O] ', board.boardGraphic[BOARD_SIZE - 3][4])

    def test_check_column_full(self):

        board = Board()

        board.filledRects = ['20', '21', '22', '23', '24', '25', '26']
        full_column_1 = board.checkColumnFull(2)

        board.filledRects = ['20', '21', '22', '23', '24', '25', '54']
        full_column_2 = board.checkColumnFull(2)

        self.assertTrue(full_column_1)
        self.assertFalse(full_column_2)

    def test_find_column_top_rect(self):

        board = Board()

        board.filledRects = ['20', '21', '22', '23', '24', '25']
        top_rect_1 = board.findColumnTopRect(2)

        board.filledRects = []
        top_rect_2 = board.findColumnTopRect(4)

        self.assertEqual(26, top_rect_1)
        self.assertEqual(40, top_rect_2)


class TestUI(TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_prompt_input(self, mock_input):
        ui = UI()
        user_input = ui.promptInput(4, 'Blah')

        self.assertEqual(1, user_input)


class TestRuleManager(TestCase):

    def test_locate_possible_connects(self):
        rule_manager = RuleManager()
        board = Board()
        player = Player('Human')
        player.filledRects = [
            '00', '01', '02', '03'
        ]
        connect_four = rule_manager.locatePossibleConnects(board, player, '00')
        self.assertTrue(connect_four)
