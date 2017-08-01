#file will inheret from chess_board_pieces
import chess_board_pieces
import piece_moves
import random

class ChessGame(chess_board_pieces.Board):
    def __init__(self):
        chess_board_pieces.Board.__init__(self)
        print self.black_place

    def get_possible_moves(self):
        #loop through pieces and pass coords to corresponding methods
        pass






if __name__ == "__main__":
    g = ChessGame()
