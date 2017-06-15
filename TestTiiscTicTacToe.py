#!/usr/bin/python
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------
# Test Tic Tac Toe with Minimax Alpha-Beta Pruning in Python
# Author: Oscar Hernandez Diaz
# Email: oscar.hernandez@tiisc.com
# Startup: Tiisc
# Web: tiisc.com
# Date: 06-15-2017
# Note: Some unit tests are included
# ---------------------------------------------------------------------------



import unittest
from TiiscTicTacToe import TiiscTicTacToe

class Test_TiiscTicTacToe(unittest.TestCase):
    def test_is_winner_x(self):
		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 6, "X")
		test_g.make_move(test_g.board, 7, "X")
		test_g.make_move(test_g.board, 8, "X")
		test_g.make_move(test_g.board, 0, "O")
		test_g.make_move(test_g.board, 4, "O")
		test_g.make_move(test_g.board, 2, "O")
		self.assertTrue(test_g.is_winner(test_g.board, "X"))

		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 3, "X")
		test_g.make_move(test_g.board, 4, "X")
		test_g.make_move(test_g.board, 5, "X")
		test_g.make_move(test_g.board, 0, "O")
		test_g.make_move(test_g.board, 1, "O")
		test_g.make_move(test_g.board, 8, "O")
		self.assertTrue(test_g.is_winner(test_g.board, "X"))

		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 0, "X")
		test_g.make_move(test_g.board, 1, "X")
		test_g.make_move(test_g.board, 2, "X")
		test_g.make_move(test_g.board, 5, "O")
		test_g.make_move(test_g.board, 3, "O")
		test_g.make_move(test_g.board, 8, "O")
		self.assertTrue(test_g.is_winner(test_g.board, "X"))

		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 0, "X")
		test_g.make_move(test_g.board, 3, "X")
		test_g.make_move(test_g.board, 6, "X")
		test_g.make_move(test_g.board, 1, "O")
		test_g.make_move(test_g.board, 4, "O")
		test_g.make_move(test_g.board, 8, "O")
		self.assertTrue(test_g.is_winner(test_g.board, "X"))

		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 1, "X")
		test_g.make_move(test_g.board, 4, "X")
		test_g.make_move(test_g.board, 7, "X")
		test_g.make_move(test_g.board, 2, "O")
		test_g.make_move(test_g.board, 0, "O")
		test_g.make_move(test_g.board, 3, "O")
		self.assertTrue(test_g.is_winner(test_g.board, "X"))

		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 2, "X")
		test_g.make_move(test_g.board, 5, "X")
		test_g.make_move(test_g.board, 8, "X")
		test_g.make_move(test_g.board, 6, "O")
		test_g.make_move(test_g.board, 0, "O")
		test_g.make_move(test_g.board, 7, "O")
		self.assertTrue(test_g.is_winner(test_g.board, "X"))

		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 0, "X")
		test_g.make_move(test_g.board, 4, "X")
		test_g.make_move(test_g.board, 8, "X")
		test_g.make_move(test_g.board, 6, "O")
		test_g.make_move(test_g.board, 3, "O")
		test_g.make_move(test_g.board, 2, "O")
		self.assertTrue(test_g.is_winner(test_g.board, "X"))

		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 2, "X")
		test_g.make_move(test_g.board, 4, "X")
		test_g.make_move(test_g.board, 6, "X")
		test_g.make_move(test_g.board, 0, "O")
		test_g.make_move(test_g.board, 5, "O")
		test_g.make_move(test_g.board, 8, "O")
		self.assertTrue(test_g.is_winner(test_g.board, "X"))
		
		

    def test_is_winner_o(self):
		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 6, "O")
		test_g.make_move(test_g.board, 7, "O")
		test_g.make_move(test_g.board, 8, "O")
		test_g.make_move(test_g.board, 0, "X")
		test_g.make_move(test_g.board, 4, "X")
		test_g.make_move(test_g.board, 2, "X")
		self.assertTrue(test_g.is_winner(test_g.board, "O"))

		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 3, "O")
		test_g.make_move(test_g.board, 4, "O")
		test_g.make_move(test_g.board, 5, "O")
		test_g.make_move(test_g.board, 0, "X")
		test_g.make_move(test_g.board, 1, "X")
		test_g.make_move(test_g.board, 8, "X")
		self.assertTrue(test_g.is_winner(test_g.board, "O"))

		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 0, "O")
		test_g.make_move(test_g.board, 1, "O")
		test_g.make_move(test_g.board, 2, "O")
		test_g.make_move(test_g.board, 5, "X")
		test_g.make_move(test_g.board, 3, "X")
		test_g.make_move(test_g.board, 8, "X")
		self.assertTrue(test_g.is_winner(test_g.board, "O"))

		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 0, "O")
		test_g.make_move(test_g.board, 3, "O")
		test_g.make_move(test_g.board, 6, "O")
		test_g.make_move(test_g.board, 1, "X")
		test_g.make_move(test_g.board, 4, "X")
		test_g.make_move(test_g.board, 8, "X")
		self.assertTrue(test_g.is_winner(test_g.board, "O"))

		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 1, "O")
		test_g.make_move(test_g.board, 4, "O")
		test_g.make_move(test_g.board, 7, "O")
		test_g.make_move(test_g.board, 2, "X")
		test_g.make_move(test_g.board, 0, "X")
		test_g.make_move(test_g.board, 3, "X")
		self.assertTrue(test_g.is_winner(test_g.board, "O"))

		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 2, "O")
		test_g.make_move(test_g.board, 5, "O")
		test_g.make_move(test_g.board, 8, "O")
		test_g.make_move(test_g.board, 6, "X")
		test_g.make_move(test_g.board, 0, "X")
		test_g.make_move(test_g.board, 7, "X")
		self.assertTrue(test_g.is_winner(test_g.board, "O"))

		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 0, "O")
		test_g.make_move(test_g.board, 4, "O")
		test_g.make_move(test_g.board, 8, "O")
		test_g.make_move(test_g.board, 6, "X")
		test_g.make_move(test_g.board, 3, "X")
		test_g.make_move(test_g.board, 2, "X")
		self.assertTrue(test_g.is_winner(test_g.board, "O"))

		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 2, "O")
		test_g.make_move(test_g.board, 4, "O")
		test_g.make_move(test_g.board, 6, "O")
		test_g.make_move(test_g.board, 0, "X")
		test_g.make_move(test_g.board, 5, "X")
		test_g.make_move(test_g.board, 8, "X")
		self.assertTrue(test_g.is_winner(test_g.board, "O"))		



    def test_is_space_free(self):
		test_g = TiiscTicTacToe()
		self.assertTrue(test_g.is_space_free(test_g.board, 0))
		self.assertTrue(test_g.is_space_free(test_g.board, 1))
		self.assertTrue(test_g.is_space_free(test_g.board, 2))
		self.assertTrue(test_g.is_space_free(test_g.board, 3))
		self.assertTrue(test_g.is_space_free(test_g.board, 4))
		self.assertTrue(test_g.is_space_free(test_g.board, 5))
		self.assertTrue(test_g.is_space_free(test_g.board, 6))
		self.assertTrue(test_g.is_space_free(test_g.board, 7))
		self.assertTrue(test_g.is_space_free(test_g.board, 8))

		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 2, "O")
		test_g.make_move(test_g.board, 4, "O")
		test_g.make_move(test_g.board, 6, "O")
		test_g.make_move(test_g.board, 0, "X")
		test_g.make_move(test_g.board, 5, "X")
		test_g.make_move(test_g.board, 8, "X")
		self.assertFalse(test_g.is_space_free(test_g.board, 2))
		self.assertFalse(test_g.is_space_free(test_g.board, 4))
		self.assertFalse(test_g.is_space_free(test_g.board, 6))
		self.assertFalse(test_g.is_space_free(test_g.board, 0))
		self.assertFalse(test_g.is_space_free(test_g.board, 5))
		self.assertFalse(test_g.is_space_free(test_g.board, 8))

				

    def test_is_board_full(self):
		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 0, "O")
		test_g.make_move(test_g.board, 1, "O")
		test_g.make_move(test_g.board, 2, "X")
		test_g.make_move(test_g.board, 3, "0")
		test_g.make_move(test_g.board, 4, "0")
		test_g.make_move(test_g.board, 5, "X")
		test_g.make_move(test_g.board, 6, "X")
		test_g.make_move(test_g.board, 7, "X")
		test_g.make_move(test_g.board, 8, "X")
		self.assertTrue(test_g.is_board_full(test_g.board))

		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 0, "O")
		test_g.make_move(test_g.board, 1, "O")
		test_g.make_move(test_g.board, 2, "X")
		test_g.make_move(test_g.board, 3, "0")
		test_g.make_move(test_g.board, 4, "0")
		test_g.make_move(test_g.board, 5, "X")		
		test_g.make_move(test_g.board, 7, "X")
		test_g.make_move(test_g.board, 8, "X")
		self.assertFalse(test_g.is_board_full(test_g.board))



    def test_make_move(self):
		test_g = TiiscTicTacToe()
		test_g.make_move(test_g.board, 0, "X")
		self.assertEqual(test_g.board[0], "X")

		test_g.make_move(test_g.board, 1, "0")
		self.assertEqual(test_g.board[1], "0")

		test_g.make_move(test_g.board, 8, "X")
		self.assertEqual(test_g.board[8], "X")

if __name__ == '__main__':
    unittest.main()
