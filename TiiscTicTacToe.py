#!/usr/bin/python
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------
# Tic Tac Toe with Minimax Alpha-Beta Pruning in Python
# Author: Oscar Hernandez Diaz
# Email: oscar.hernandez@tiisc.com
# Startup: Tiisc
# Web: tiisc.com
# Date: 06-15-2017
# Inspiration:
# Command-line user interface inspired by: https://github.com/Stepan-Lenevich/Tic-Tac-Toe-Python
# Algorithm used: MINIMAX and ALFA-BETA PRUNING
# Documentation consulted:
# Book: Artificial Intelligence A Systems Approach
# Videos is Spanish:
# AI Graphs – MiniMax: https://www.youtube.com/watch?v=__FPQHKPrVU
# AI Graphs – MiniMax Alpha-Beta Pruning: https://www.youtube.com/watch?v=jYm8eU-N2MA&spfreload=10
# THANK YOU!!!
# ---------------------------------------------------------------------------



# import modules
import sys, random, copy



class TiiscTicTacToe:        
    "Tic-Tac-Toe class. This class holds the user interaction, and game logic"
    def __init__(self):
		self.board = [' '] * 9
		self.player_name = ''
		self.player_marker = ''
		self.bot_name = 'Tiisc Bot'
		self.bot_marker = ''
		self.MAX_INFINITY = 1
		self.DRAW = 0
		self.MIN_INFINITY = -1
		self.winning_combos = ([6, 7, 8], [3, 4, 5], [0, 1, 2], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])
		self.form = '''
           \t| %s | %s | %s |
           \t-------------
           \t| %s | %s | %s |
           \t-------------
           \t| %s | %s | %s |
           '''                    



    # Function for show board on screen
    def print_board(self, board = None):
        "Display board on screen"
        if board is None:
            print self.form % tuple(self.board[6:9] + self.board[3:6] + self.board[0:3])
        else:
            # when the game starts, display numbers on all the grids
            print self.form % tuple(board[6:9] + board[3:6] + board[0:3])



    # Function for get the marker selected for human player
    def get_marker(self):
        marker = raw_input("Would you like your marker to be X or O?: ").upper() 
        while marker not in ["X", "O"]:
            marker = raw_input("Would you like your marker to be X or O? :").upper()
        
        if marker == "X":
            return ('X', 'O')
        else:
            return ('O','X')
    


    # Function for show instructions the game
    def help(self):
        print '''
\n\t The game board has 9 sqaures(3X3).
\n\t Two players take turns in marking the spots/grids on the board.
\n\t The first player to have 3 pieces in a horizontal, vertical or diagonal row wins the game.
\n\t To place your mark in the desired square, simply type the number corresponding with the square
\t on the grid.
\n\t Press Ctrl + C to quit.
'''



    # Function for exit the game
    def quit_game(self):
        "exits game"
        self.print_board
        print "\n\t Thanks for playing :-) \n\t Come play again soon!\n"
        sys.exit()



    # Function for know is winner
    def is_winner(self, board, marker):
        "check if this marker will win the game"
        # order of checks:
        #   1. across the horizontal top
        #   2. across the horizontal middle
        #   3. across the horizontal bottom
        #   4. across the vertical left
        #   5. across the vertical middle
        #   6. across the vertical right
        #   7. across first diagonal
        #   8. across second diagonal
        for combo in self.winning_combos:
            if (board[combo[0]] == board[combo[1]] == board[combo[2]] == marker):
                return True
        return False

    

    # Start Function AI Minimax Alpha-Beta Pruning
	# This function is used in order to understand how to start the AI algorithm
    def get_minimax_ab_bot_move(self, depth, alpha, beta):            
        if (not self.is_board_full(self.board)) or (not self.is_winner(self.board, self.bot_marker)):			
			best_mov = 0
			utility = 0			
			vmax = self.MIN_INFINITY-1
			
			for i in range(0, len(self.board)):
				if self.is_space_free(self.board, i):
					board_copy = copy.deepcopy(self.board)
					self.make_move(board_copy, i, self.bot_marker)
					utility = self.min(board_copy, depth+1, alpha, beta)
					if utility > vmax:
						vmax = utility
						best_mov = i
					if utility > alpha: alpha = utility
					if alpha >= beta: return alpha
			return best_mov



    # Function Min
    def min(self, p_board, depth, alpha, beta):
		utility = 0
		vmin = self.MAX_INFINITY+1
				
		if self.is_winner(p_board, self.bot_marker):
			return self.MAX_INFINITY

		for i in range(0, len(p_board)):
			if self.is_space_free(p_board, i):
				board_copy = copy.deepcopy(p_board)
				self.make_move(board_copy, i, self.player_marker)
				utility = self.max(board_copy, depth+1, alpha, beta)
				if utility < vmin:
					vmin = utility
				if utility < beta: beta = utility
				if alpha >= beta: return beta

		if vmin == self.MAX_INFINITY+1:
			return self.DRAW
		return vmin



    # Function Max
    def max(self, p_board, depth, alpha, beta):
		utility = 0		
		vmax = self.MIN_INFINITY-1
				
		if self.is_winner(p_board, self.player_marker):
			return self.MIN_INFINITY
		
		for i in range(0, len(p_board)):
			if self.is_space_free(p_board, i):
				board_copy = copy.deepcopy(p_board)
				self.make_move(board_copy, i, self.bot_marker)
				utility = self.min(board_copy, depth+1, alpha, beta)
				if utility > vmax:
					vmax = utility				
				if utility > alpha: alpha = utility
				if alpha >= beta: return alpha

		if vmax == self.MIN_INFINITY-1:
			return self.DRAW
		return vmax



    # Function checks for free space of the board
    def is_space_free(self, board, index):
        "checks for free space of the board"        
        return board[index] == ' '



    # Function checks if the board is full
    def is_board_full(self, p_board):
        "checks if the board is full"
        for i in range(0, len(p_board)):
            if self.is_space_free(p_board, i):
                return False
        return True



    # Function for make the move in the board
    def make_move(self, board, index, marker):
        board[index] =  marker



    # Function for start the game
    def start_game(self):
       "welcomes user, prints help message and hands over to the main game loop"
       # welcome user 
       print '''\n\t-------------------------------------------------
                \n\t   TIC-TAC-TOE by Oscar Hernandez Diaz - Tiisc
                \n\t-------------------------------------------------
             '''
       self.print_board(range(1, 10))
       self.help()
       self.player_name = self.get_player_name()

       # get user's preferred marker 
       self.player_marker, self.bot_marker = self.get_marker()
       print "Your marker is: " + self.player_marker
        
       # randomly decide who can play first
       if random.randint(0, 1) == 0:
           print "I will go first"          
           self.enter_game_loop('b')
       else:
           print "You will go first"          
           # now, enter the main game loop
           self.enter_game_loop('h')



    # Function for get human player move
    def get_player_move(self):
        move = int(input("Pick a spot to move (1-9): "))
        while move not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not self.is_space_free(self.board, move-1):
            move = int(input("Invalid move. Please try again (1-9): "))
        return move - 1



    # Function for get player name
    def get_player_name(self):
        return raw_input("Hi, I am %s" % self.bot_name + ". What is your name?: ") 



    # Function for starts the main game loop
    def enter_game_loop(self, turn):
       "starts the main game loop"
       is_running = True
       player = turn # h for human, b for bot
       while is_running:
           if player == 'h':
               user_input = self.get_player_move()               
               self.make_move(self.board, user_input, self.player_marker)
               if(self.is_winner(self.board, self.player_marker)):
                   self.print_board()
                   print "\n\tCONGRATULATIONS %s, YOU HAVE WON THE GAME!!! \t\n" % self.player_name                   
                   is_running = False                   
               else:
                   if self.is_board_full(self.board):
                       self.print_board()
                       print "\n\t-- Match Draw --\t\n"
                       is_running = False     
                   else:
                       self.print_board()
                       player = 'b'
           # bot's turn to play
           else:
               bot_move =  self.get_minimax_ab_bot_move(0, self.MIN_INFINITY-1, self.MAX_INFINITY+1) #Call function minimax alpha-beta
               self.make_move(self.board, bot_move, self.bot_marker)
               if (self.is_winner(self.board, self.bot_marker)):
                   self.print_board()
                   print "\n\t%s HAS WON!!!!\t\n" % self.bot_name                  
                   is_running = False
                   break
               else:
                   if self.is_board_full(self.board):
                       self.print_board()
                       print "\n\t -- Match Draw -- \n\t"
                       is_running = False                   
                   else:
                       self.print_board()
                       player = 'h'

       # when you break out of the loop while, end the game
       self.end_game()



    # Function for ending or re initialization game
    def end_game(self):
       play_again = raw_input("Would you like to play again? (y/n): ").lower()
       if play_again == 'y':
           self.__init__() # necessary for re-initialization of the board etc
           self.start_game()
       else:
           print "\n\t-- GAME OVER!!!--\n\t"
           self.quit_game()



# Start the game with this condition
if __name__ == "__main__":   
     TicTacToe = TiiscTicTacToe()
     TicTacToe.start_game()