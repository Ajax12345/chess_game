#file will inheret from chess_board_pieces
import chess_board_pieces
import piece_moves
import white_piece_moves as wp
import random
import copy
import time
from collections import OrderedDict
import string
import re
#TODO: Add move file output capability

class ChessGame(chess_board_pieces.Board):
    def __init__(self):
        chess_board_pieces.Board.__init__(self)
        #print self.black_place
        self.determine_squares = {"r":[piece_moves.get_rook_moves, wp.get_rook_moves], "b":[piece_moves.get_bishop_moves, wp.get_bishop_moves], "q":[piece_moves.get_queen_moves, wp.get_queen_moves], "k":[piece_moves.get_king_moves, wp.get_king_moves], "kn":[piece_moves.get_knight_moves, wp.get_bishop_moves], "p":[piece_moves.get_pawn_moves, wp.get_pawn_moves]}
        #self.get_possible_moves()
        #self.play_small_game()
        self.piece_values = {"k":20, "q":10, "r":5, "p":1, "kn":3, "b":3}
        self.current_moves = []
        self.move_count = 1
        self.material_score = [0, 0] #white, black


    def get_possible_moves(self):
        #loop through pieces and pass coords to corresponding methods
        possibilites = {}
        other_possibilites = {}
        best_possibilites = OrderedDict()
        for piece in self.black_pieces:

            loc = self.black_place[piece]
            a, b = loc

            moves = []
            if len(piece) == 4:
                #print "piece", piece, " ", self.determine_squares[piece[:2]](self.view_board, a, b)
                moves.extend(self.determine_squares[piece[:2]][0](self.view_board, a, b))



            else:
                #print "piece", piece, " ",self.determine_squares[piece[0]](self.view_board, a, b)

                moves.extend(self.determine_squares[piece[0]][0](self.view_board, a, b))

            for white_piece, location in self.white_places.items():
                if location in moves:
                    #print "can capture ", white_piece
                    best_possibilites[piece] = location



            if moves:
                spot = random.choice(moves)

                result = self.play_small_game(piece, spot)

                if result:
                    possibilites[piece] = spot
                else:
                    other_possibilites[piece] = spot
        #print possibilites
        if len(best_possibilites) > 0:
            #final_piece_to_move = list(best_possibilites)[0]
            while True:
                final_piece_to_move = random.choice(best_possibilites.keys())
                #print "piece chosen: ", final_piece_to_move
                if "pb" in final_piece_to_move:
                    a, b = best_possibilites[final_piece_to_move]
                    current_pos = self.black_place[final_piece_to_move]

                    if b != current_pos[-1]:
                        self.move_piece(final_piece_to_move, best_possibilites[final_piece_to_move])
                        break

                    else:
                        if len(best_possibilites) > 1:
                            continue

                        else:
                            if possibilites:
                                final_piece_to_move = random.choice(possibilites.keys())
                                self.move_piece(final_piece_to_move, possibilites[final_piece_to_move])

                            else:
                                final_piece_to_move = random.choice(other_possibilites.keys())
                                self.move_piece(final_piece_to_move, other_possibilites[final_piece_to_move])

                            break

                else:

                    all_possible_moves = {a:self.determine_squares[a[:2]][1](self.view_board, b[0], b[1]) if len(a) == 4 else self.determine_squares[a[0]][1](self.view_board, b[0], b[1]) for a, b in self.white_places.items()}
                    #print "all_possible_moves", all_possible_moves
                    square_now = best_possibilites[final_piece_to_move]
                    opponents = [a for a, b in all_possible_moves.items() if square_now in b]
                    #print "final_piece_to_move", final_piece_to_move
                    #print "opponents", opponents
                    #print "self.piece_values[final_piece_to_move[0]]", self.piece_values[final_piece_to_move[0]]
                    #print "self.piece_values[i[:2]]", self.piece_values[final_piece_to_move[:1]]
                    #current_piece_value = self.piece_values[final_piece_to_move[0]] if len(final_piece_to_move) != 4 else self.piece_values[i[:2]]
                    current_piece_value = self.piece_values[final_piece_to_move[0]] if len(final_piece_to_move) != 4 else self.piece_values[final_piece_to_move[:2]]

                    if any(self.piece_values[i[0]] < current_piece_value if len(i) != 4 else 3 > current_piece_value for i in opponents):
                        #print "here"
                        if possibilites:
                            final_piece_to_move = random.choice(possibilites.keys())
                            self.move_piece(final_piece_to_move, possibilites[final_piece_to_move])
                            break

                        else:
                            final_piece_to_move = random.choice(other_possibilites.keys())
                            self.move_piece(final_piece_to_move, other_possibilites[final_piece_to_move])
                            break

                    else:

                        self.move_piece(final_piece_to_move, best_possibilites[final_piece_to_move])
                        break




        elif possibilites:
            final_piece_to_move = random.choice(possibilites.keys())
            self.move_piece(final_piece_to_move, possibilites[final_piece_to_move])

        else:
            final_piece_to_move = random.choice(other_possibilites.keys())
            self.move_piece(final_piece_to_move, other_possibilites[final_piece_to_move])



    def user_move(self):
        x = input("Enter the x-corrdinate: ")
        y = input("Enter the y-corrdinate: ")
        piece = raw_input("Enter the piece name: ")
        self.move_piece(piece, (x-1, y-1))

    def user_move_1(self, x, y, piece):
        self.move_piece(piece, (x-1, y-1))


    def record_game(self, piece, location):
        #number:[lowercase, UPPERCASE]
        #(number, letter)
        letters = {i:[a, string.ascii_uppercase[i]] for i, a in zip(range(8), string.ascii_lowercase[:8])}
        #print "location", location
        if piece[0] == "p":
            self.current_moves.append(str(self.move_count)+"."+letters[location[1]][0]+str(location[0]+1))

        else:
            if len(piece) == 4:
                self.current_moves.append(str(self.move_count)+"."+"N"+letters[location[1]][0]+str(location[0]+1))

            else:
                self.current_moves.append(str(self.move_count)+"."+piece[0].upper()+letters[location[1]][0]+str(location[0]+1))

        self.move_count += 1




    def move_piece(self, piece, location):

        self.record_game(piece, location)
        print "self.current_moves", self.current_moves
        if "b" in piece and "w" not in piece: #black move
            a, b = location
            if "w" in self.view_board[a][b]:
                the_enemy_piece = self.view_board[a][b]
                the_enemy_piece_value = self.piece_values[the_enemy_piece[0]] if len(the_enemy_piece) != 4 else 3
                self.material_score[1] += the_enemy_piece_value

                white_piece = self.view_board[a][b]
                try:

                    self.white_pieces.remove(white_piece)
                except:
                    pass
                #if white_piece in self.white_pieces1:
                    #self.white_pieces1.remove(white_piece)
                try:
                    del self.white_places[white_piece]
                except KeyError:
                    pass
                self.view_board[a][b] = piece
                a1, b1 = self.black_place[piece]
                self.view_board[a1][b1] = "-"
                self.black_place[piece] = location

            else:
                a1, b1 = self.black_place[piece]
                self.view_board[a1][b1] = "-"
                self.view_board[a][b] = piece
                self.black_place[piece] = location

        elif "w" in piece: #white move
            a, b = location
            if "b" in self.view_board[a][b] and "w" not in self.view_board[a][b]:
                #self.white_capture_rate += 1
                the_enemy_piece = self.view_board[a][b]
                the_enemy_piece_value = self.piece_values[the_enemy_piece[0]] if len(the_enemy_piece) != 4 else 3
                self.material_score[0] += the_enemy_piece_value
                black_piece = self.view_board[a][b]
                try:
                    self.black_pieces.remove(black_piece)
                except ValueError:
                    pass
                #if black_piece in self.black_pieces1:
                    #self.black_pieces1.remove(black_piece)
                try:
                    del self.black_place[black_piece]
                except KeyError:
                    pass
                a1, b1 = self.white_places[piece]
                self.view_board[a1][b1] = "-"
                self.view_board[a][b] = piece
                self.white_places[piece] = location

            else:
                a1, b1 = self.white_places[piece]
                self.view_board[a1][b1] = "-"
                self.view_board[a][b] = piece
                self.white_places[piece] = location








    def play_small_game(self, piece, to_square): #to_square contains (x, y)
        class SmallGame:
            def __init__(self, board, white_pieces, white_places, black_pieces, black_places):
                self.board_now = board #self.view_board[:]
                self.white_pieces1 = white_pieces #self.white_pieces[:]
                self.white_places1 = white_places #self.white_places
                self.black_pieces1 = black_pieces#self.black_pieces[:]
                self.black_place1 = black_places#self.black_place
                self.black_capture_rate = 0
                self.white_capture_rate = 0



            def move_to(self, piece, location):
                if "b" in piece and "w" not in piece: #black move
                    a, b = location
                    if "w" in self.board_now[a][b]:

                        self.black_capture_rate += 1
                        white_piece = self.board_now[a][b]
                        try:

                            self.white_pieces1.remove(white_piece)
                        except:
                            pass
                        #if white_piece in self.white_pieces1:
                            #self.white_pieces1.remove(white_piece)
                        try:
                            del self.white_places1[white_piece]
                        except KeyError:
                            pass
                        self.board_now[a][b] = piece
                        a1, b1 = self.black_place1[piece]
                        self.board_now[a1][b1] = "-"
                        self.black_place1[piece] = location

                    else:
                        a1, b1 = self.black_place1[piece]
                        self.board_now[a1][b1] = "-"
                        self.board_now[a][b] = piece
                        self.black_place1[piece] = location

                elif "w" in piece: #white move
                    a, b = location
                    if "b" in self.board_now[a][b] and "w" not in self.board_now[a][b]:
                        self.white_capture_rate += 1
                        black_piece = self.board_now[a][b]
                        try:
                            self.black_pieces1.remove(black_piece)
                        except ValueError:
                            pass
                        #if black_piece in self.black_pieces1:
                            #self.black_pieces1.remove(black_piece)
                        try:
                            del self.black_place1[black_piece]
                        except KeyError:
                            pass
                        a1, b1 = self.white_places1[piece]
                        self.board_now[a1][b1] = "-"
                        self.board_now[a][b] = piece
                        self.white_places1[piece] = location

                    else:
                        a1, b1 = self.white_places1[piece]
                        self.board_now[a1][b1] = "-"
                        self.board_now[a][b] = piece
                        self.white_places1[piece] = location

            def determine_results(self):
                return self.black_capture_rate > self.white_capture_rate


        mock_game = SmallGame(copy.deepcopy(self.view_board), copy.deepcopy(self.white_pieces), copy.deepcopy(self.white_places), copy.deepcopy(self.black_pieces), copy.deepcopy(self.black_place)) #may need copy.deepcopy()

        mock_game.move_to(piece, to_square)

        for i in range(25):

            white_possible_moves = {}
            black_possible_moves = {}

            for wpiece in mock_game.white_pieces1:
                loc = mock_game.white_places1[wpiece]

                a, b = loc
                if len(wpiece) == 4:
                    white_possible_moves[wpiece] = self.determine_squares[wpiece[:2]][1](mock_game.board_now, a, b)

                else:
                    white_possible_moves[wpiece] = self.determine_squares[wpiece[0]][1](mock_game.board_now, a, b)
            piece_to_test = None
            place_to_move = None
            while True: #make this rely on a counter
                the_piece = random.choice(white_possible_moves.keys())
                #print "got here:", white_possible_moves
                if white_possible_moves[the_piece]:
                    piece_to_test = the_piece
                    place_to_move = random.choice(white_possible_moves[the_piece])

                    break

            mock_game.move_to(piece_to_test, place_to_move)

            for bpiece in mock_game.black_pieces1:
                loc = mock_game.black_place1[bpiece]
                a, b = loc
                if len(bpiece) == 4:
                    black_possible_moves[bpiece] = self.determine_squares[bpiece[:2]][0](mock_game.board_now, a, b)

                else:
                    black_possible_moves[bpiece] = self.determine_squares[bpiece[0]][0](mock_game.board_now, a, b)

            piece_to_test = None
            place_to_move = None

            while True:
                the_piece = random.choice(black_possible_moves.keys())
                if black_possible_moves[the_piece]:
                    piece_to_test = the_piece
                    place_to_move = random.choice(black_possible_moves[the_piece])

                    break

            mock_game.move_to(piece_to_test, place_to_move)




        return 1 if mock_game.determine_results() else 0



if __name__ == "__main__":

    g = ChessGame()

    while True:
        try:
            for i in range(8):
                print "", i+1, "",
            print
            for row, i in enumerate(g.view_board):
                for b in i:
                    if b == "-":
                        print " "+b+" ",
                    else:
                        print b,
                print row+1
                print
            g.user_move()
            #time.sleep(2)
            for row, i in enumerate(g.view_board):
                for b in i:
                    if b == "-":
                        print " "+b+" ",
                    else:
                        print b,
                print row+1
                print
            g.get_possible_moves()
        except KeyboardInterrupt:
            break


    number_of_games = [int(i.strip('\n')) for i in open('game_numbers.txt')][0]
    f = open('game_numbers.txt', 'w')
    f.write(str(number_of_games + 1)+"\n")
    f.close()
    file_name = "chess game {}.txt".format(number_of_games)
    new_file = open(file_name, 'a')

    for i in g.current_moves:
        new_file.write(i+"\n")

    if g.material_score[0] > g.material_score[1]:
        new_file.write("White wins, {}-{}\n".format(g.material_score[0], g.material_score[-1]))
    elif g.material_score[0] < g.material_score[1]:
        new_file.write("Black wins, {}-{}\n".format(g.material_score[-1], g.material_score[0]))
    else:
        new_file.write("Tie, {}-{}\n".format(g.material_score[-1], g.material_score[0]))
    new_file.close()


