import unittest
import copy 
from ticTacToeGame import *

class ticTacToeTest(unittest.TestCase):
    def test_game_eval_blank(self):
        ''' the game should not be over with a blank board '''
        self.assertEqual(game_eval(board),False)
    
    def test_game_eval_one(self):
        '''the game should not be over if there's only one move on the board'''
        testBoard = ['-','X','-','-','-','-','-','-','-']
        self.assertEqual(game_eval(testBoard), False)
    
    def test_game_eval_three_in_top_row(self):
        ''' If there's 3 in a row  in the top it should return True'''
        testBoard = ['O','O','O','-','-','-','-','-','-']
        self.assertEqual(game_eval(testBoard), True)
        

    def test_play_game_blank(self):
        ''' Should not put in a value if no spot on the board was chosen'''
        mover = "X"
        testMove = " "
        testBoard = ['-','-','-','-','-','-','-','-','-']
        expectedAfterBoard = ['-','-','-','-','-','-','-','-','-']
        moveAccepted = play_game(testBoard, mover, testMove)
        self.assertEqual(moveAccepted, False)
        self.assertListEqual(testBoard, expectedAfterBoard)
    def test_play_game_top_left(self):
        '''Should put an X in the top left'''
        mover = "X"
        testMove = "top left"
        testBoard = ['-','-','-','-','-','-','-','-','-']
        expectedAfterBoard = ['X','-','-','-','-','-','-','-','-']
        moveAccepted = play_game(testBoard, mover, testMove)
        self.assertEqual(moveAccepted, True)
        self.assertListEqual(testBoard, expectedAfterBoard) 