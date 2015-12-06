import unittest
from app.board import Board

class TestBoard(unittest.TestCase):
    def test_new_board(self):
        board = Board(raws=10, cols=20)
        self.assertEqual(board.raws, 10)
        self.assertEqual(board.cols, 20)
