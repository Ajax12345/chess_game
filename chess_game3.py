import time
import pickle
class Chess:
    def __init__(self):
        self.view_board = [["rb1", "knb1", 'bb1', 'qb', 'kb', 'bb2', 'knb2', 'rb2'],
                            ["pb"+str(i+1) for i in range(8)],
                            ["-" for i in range(8)],
                            ["-" for i in range(8)],
                            ["-" for i in range(8)],
                            ["-" for i in range(8)],
                            ["pw"+str(i+1) for i in range(8)],
                            ["rw1", "knw1", 'bw1', 'qw', 'kw', 'bw2', 'knw2', 'rw2']]

        self.white_pieces = ["rw1", "knw1", 'bw1', 'qw', 'kw', 'bw2', 'knw2', 'rw2']
        self.white_pieces.extend(["pw"+str(i+1) for i in range(8)])

        self.black_pieces = ["rb2", "knb1", 'bb2', 'qb', 'kb', "bb1", 'knb2', 'rb2']
        self.black_pieces.extend(["pb"+str(i+1) for i in range(8)])

        self.white_places = {}
        self.black_place = {}

        self.value = {"rb1":5, "knb1":3, 'bb1':3, 'qb':10, 'kb':20, 'bb2':3, 'knb2':3, 'rb2':5, "rw1":5, "knw1":3, 'bw1':3, 'qw':10, 'kw':20, 'bw2':3, 'knw2':3, 'rw2':5}

        self.value.update({i:1 for i in ["pb"+str(i+1) for i in range(8)]})

        self.value.update({i:1 for i in ["pw"+str(i+1) for i in range(8)]})

        self.pawns_moved = []
        self.move_count = 0

        self.knight1_move_count = 0

        self.knight2_move_count = 0

    def initialize(self):
        for i in range(len(self.view_board)):
            for b in range(len(self.view_board[0])):
                self.piece = self.view_board[i][b]

                if self.piece in self.white_pieces:
                    self.white_places[self.piece] = (i, b)

                elif self.piece in self.black_pieces:
                    self.black_place[self.piece] = (i, b)
        pickle.dump(self.black_place, open('chess_pieces.txt', 'w'))

        pickle.dump(self.white_places, open('white_pieces.txt', 'w'))



    def user_move(self, piece, x, y):
        self.view_board[self.white_places[piece][0]][self.white_places[piece][1]] = "-"
        self.white_places[piece] = (x-1, y-1)
        if self.view_board[x-1][y-1] == "-":
            self.view_board[x-1][y-1] = piece
        else:
            print "capturing ", self.view_board[x-1][y-1]

            del self.black_place[self.view_board[x-1][y-1]]

            self.view_board[x-1][y-1] = piece

    def pawn_capture(self):
        #vulnerable white piece and position list
         #flag is false, we are just checking, may not actually need this if we just return self.vulnerable
        self.vulnerable = {} #dictionary that stores {blackpiece:[vulnerable_white_piece, (new_location), (old_locations)]}
        for i in self.pawns_moved:
            if i in self.black_place:
                self.current_square = self.black_place[i]
                if int(i[len(i)-1]) == 1:
                    if self.view_board[self.black_place[i][0]+1][self.black_place[i][1]+1] in self.white_places.keys():
                        self.vulnerable[i] = [self.view_board[self.black_place[i][0]+1][self.black_place[i][1]+1], (self.black_place[i][0]+1, self.black_place[i][1]+1), (self.black_place[i][0], self.black_place[i][1])]

                    elif int(i[len(i)-1]) == 8:
                        if self.view_board[self.black_place[i][0]+1][self.black_place[i][1]-1] in self.white_places.keys():
                            self.vulnerable[i] = [self.view_board[self.black_place[i][0]+1][self.black_place[i][1]-1], (self.black_place[i][0]+1, self.black_place[i][1]-1), (self.black_place[i][0], self.black_place[i][1])]

                else:
                    if self.view_board[self.black_place[i][0]+1][self.black_place[i][1]+1] in self.white_places.keys():
                        self.vulnerable[i] = [self.view_board[self.black_place[i][0]+1][self.black_place[i][1]+1], (self.black_place[i][0]+1, self.black_place[i][1]+1), (self.black_place[i][0], self.black_place[i][1])]

                    elif self.view_board[self.black_place[i][0]+1][self.black_place[i][1]-1] in self.white_places.keys():
                        self.vulnerable[i] = [self.view_board[self.black_place[i][0]+1][self.black_place[i][1]-1], (self.black_place[i][0]+1, self.black_place[i][1]-1), (self.black_place[i][0], self.black_place[i][1])]

        #new list of pawns, those that have not been moved, to check if they are threatened
        self.other_pawns = [i for i in self.view_board[1] if i not in self.pawns_moved and i != "-"]
        #print self.other_pawns
        self.other_vulnerable = {}
        for i in self.other_pawns:
            if i in self.black_place:
                self.current_square = self.black_place[i]
                if int(i[len(i)-1]) == 1: #will need to make it so that moves the pawns that make the most logical sense, not just by number order
                    #try might be the way to go, so we do not have to check if our pieces are out of range
                    try:
                        if self.view_board[self.black_place[i][0]+1][self.black_place[i][1]+1] in self.white_places.keys():
                            self.other_vulnerable[i] = [self.view_board[self.black_place[i][0]+1][self.black_place[i][1]+1], (self.black_place[i][0]+1, self.black_place[i][1]+1), (self.black_place[i][0], self.black_place[i][1])]

                        elif int(i[len(i)-1]) == 8:
                            if self.view_board[self.black_place[i][0]+1][self.black_place[i][1]-1] in self.white_places.keys():
                                self.other_vulnerable[i] = [self.view_board[self.black_place[i][0]+1][self.black_place[i][1]-1], (self.black_place[i][0]+1, self.black_place[i][1]-1), (self.black_place[i][0], self.black_place[i][1])]
                    except:
                        pass

                else:
                    try:
                        if self.view_board[self.black_place[i][0]+1][self.black_place[i][1]+1] in self.white_places.keys():
                            self.other_vulnerable[i] = [self.view_board[self.black_place[i][0]+1][self.black_place[i][1]+1], (self.black_place[i][0]+1, self.black_place[i][1]+1), (self.black_place[i][0], self.black_place[i][1])]

                        elif self.view_board[self.black_place[i][0]+1][self.black_place[i][1]-1] in self.white_places.keys():
                            self.other_vulnerable[i] = [self.view_board[self.black_place[i][0]+1][self.black_place[i][1]-1], (self.black_place[i][0]+1, self.black_place[i][1]-1), (self.black_place[i][0], self.black_place[i][1])]
                    except:
                        pass

        return self.vulnerable, self.other_vulnerable

    def knight_capture(self, knight): #need to check in main moves that the knight you want exists



        self.k1_loc_now = self.black_place[knight]


        #just return possible moves for knight
        self.posibilites = []
        #changing everything to +3

        #worst case senarios
        try:
            self.test = self.view_board[self.k1_loc_now[0]+2][0]
            #self.posibilites.append((self.k1_loc_now[0]+3, self.k1_loc_now[1]+1)) #this stuff just appends, it will give negative corrdinates

        except IndexError:
            try:
                self.new_test = self.view_board[0][self.k1_loc_now[1]+1]
            except IndexError:

                self.posibilites.append((self.k1_loc_now[0]-2, self.k1_loc_now[1]-1))

            else:
                self.posibilites.append((self.k1_loc_now[0]-2, self.k1_loc_now[1]+1))
                self.posibilites.append((self.k1_loc_now[0]-2, self.k1_loc_now[1]-1))

        else:
            try:
                self.new_test = self.view_board[0][self.k1_loc_now[1]+1]
            except IndexError:
                self.posibilites.append((self.k1_loc_now[0]+2, self.k1_loc_now[1]-1))

                self.posibilites.append((self.k1_loc_now[0]-2, self.k1_loc_now[1]-1))

            else:
                self.posibilites.append((self.k1_loc_now[0]+2, self.k1_loc_now[1]+1))
                self.posibilites.append((self.k1_loc_now[0]+2, self.k1_loc_now[1]-1))
                self.posibilites.append((self.k1_loc_now[0]-2, self.k1_loc_now[1]-1))
                self.posibilites.append((self.k1_loc_now[0]-2, self.k1_loc_now[1]+1))







        #now, filter self.posibilites so that bad moves are avoided
        self.posibilites = [i for i in self.posibilites if i[0] >= 0 and i[1] >= 0]
        print self.posibilites
        self.posibilites = [i for i in self.posibilites if self.view_board[i[0]][i[1]] not in self.black_place.keys()]

        self.should_capture = [i for i in self.posibilites if "w" in self.view_board[i[0]][i[1]]] #was not here before

        print "self.should_capture:", self.should_capture
        try:

            self.posibilites = [i for i in self.posibilites if "pw" not in self.view_board[i[0]+1][i[1]+1] or "w" not in self.view_board[i[0]+1][i[1]-1]]

        except IndexError:
            self.posibilites = self.posibilites

        #self.should_capture = [i for i in self.posibilites if "w" in self.view_board[i[0]][i[1]]]

        return self.should_capture, self.posibilites




    def pawn_move(self):
        if self.move_count == 0:
            self.original = self.black_place["pb5"]
            self.view_board[self.original[0]][self.original[1]] = "-"
            self.view_board[self.original[0]+2][self.original[1]] = "pb1"

            self.black_place["pb1"] = (self.original[0]+2, self.original[1])

            self.move_count += 1
            self.pawns_moved.append("pb1")

        else:
            self.posibilites, self.last_resort = self.pawn_capture()

            if len(self.posibilites) > 0:
                self.piece_to_move = self.posibilites.keys()[0]

                print "Capturing: "

                self.view_board[self.posibilites[self.piece_to_move][2][0]][self.posibilites[self.piece_to_move][2][1]] = "-"
                self.white_pieces.remove(self.view_board[self.posibilites[self.piece_to_move][1][0]][self.posibilites[self.piece_to_move][1][1]])

                self.view_board[self.posibilites[self.piece_to_move][1][0]][self.posibilites[self.piece_to_move][1][1]] = self.piece_to_move

                del self.white_places[self.posibilites[self.piece_to_move][0]]

                self.black_place[self.piece_to_move] = self.posibilites[self.piece_to_move][1]

            else:

                if len(self.last_resort) > 0:
                    self.piece_to_move = self.last_resort.keys()[0]

                    print "Capturing: "

                    self.view_board[self.last_resort[self.piece_to_move][2][0]][self.last_resort[self.piece_to_move][2][1]] = "-"
                    self.white_pieces.remove(self.view_board[self.last_resort[self.piece_to_move][1][0]][self.last_resort[self.piece_to_move][1][1]])

                    self.view_board[self.last_resort[self.piece_to_move][1][0]][self.last_resort[self.piece_to_move][1][1]] = self.piece_to_move

                    del self.white_places[self.last_resort[self.piece_to_move][0]]

                    self.black_place[self.piece_to_move] = self.last_resort[self.piece_to_move][1]


                else:
                    #need to make sure piece has not been captured
                    self.new_piece = ''
                    self.new_counter = self.move_count
                    while True:

                        self.new_piece = "pb"+str(5-self.new_counter)
                        if self.new_piece in self.black_place:
                            break
                        else:
                            self.new_counter -= 1
                    #self.new_piece = "pb"+str(5-self.move_count)
                    print self.new_piece
                    self.original = self.black_place[self.new_piece]
                    print self.original
                    self.view_board[self.original[0]][self.original[1]] = "-"

                    if self.view_board[self.original[0]+3][self.original[1]+1][:2] == "pw" or self.view_board[self.original[0]+3][self.original[1]-1][:2]== "pw":
                        self.view_board[self.original[0]+1][self.original[1]] = self.new_piece
                        self.black_place[self.new_piece] = (self.original[0]+1, self.original[1])

                    else:
                        self.view_board[self.original[0]+2][self.original[1]] = self.new_piece

                        self.black_place[self.new_piece] = (self.original[0]+2, self.original[1])


                #self.move_count += 1
                    self.pawns_moved.append(self.new_piece)

    def knight_move(self):
        if "knb1" in self.black_place.keys():
            print "Got to here"
            self.can_capture, self.safe_alternative = self.knight_capture("knb1")
            print "Can capture", self.can_capture
            print "Safe alternatives", self.safe_alternative

        elif "knb2" in self.black_place.keys():
            print "Got to here"
            self.can_capture2, self.safe_alternative2 = self.knight_capture("knb2")


        self.vuln1, self.vuln2 = self.pawn_capture()



        if len(self.vuln2) > 0:
            self.pawn_move() #check if we have any threatened pawns

        else:
            if self.knight1_move_count < 3:
                if "knb1" in self.black_place.keys():
                    if len(self.can_capture) > 0:
                        self.corrd = self.can_capture[0]
                        print "self.cord", self.corrd

                        print "Capturing: "

                        self.view_board[self.black_place["knb1"][0]][self.black_place["knb1"][1]] = "-"
                        try:
                            self.white_pieces.remove(self.view_board[self.corrd[0]][self.corrd[1]])

                        except ValueError:
                            pass

                        del self.white_places[self.view_board[self.corrd[0]][self.corrd[1]]]

                        self.view_board[self.corrd[0]][self.corrd[1]] = "knb1"

                        self.black_place["knb1"] = self.corrd

                        self.knight1_move_count += 1

                    elif len(self.safe_alternative) > 0:
                        self.corrd = self.safe_alternative[0]
                        self.view_board[self.black_place["knb1"][0]][self.black_place["knb1"][1]] = "-"




                        self.view_board[self.corrd[0]][self.corrd[1]] = "knb1"

                        self.black_place["knb1"] = self.corrd

                        self.knight1_move_count += 1

                elif "knb2" in self.black_place.keys():
                    if len(self.can_capture2) > 0:
                        self.corrd = self.can_capture2[0]

                        print "Capturing: "

                        self.view_board[self.black_place["knb2"][0]][self.black_place["knb2"][1]] = "-"
                        try:
                            self.white_pieces.remove(self.view_board[self.corrd[0]][self.corrd[1]])

                        except ValueError:
                            pass

                        del self.white_places[self.view_board[self.corrd[0]][self.corrd[1]]]

                        self.view_board[self.corrd[0]][self.corrd[1]] = "knb2"

                        self.black_place["knb2"] = self.corrd

                        self.knight2_move_count += 1

                    elif len(self.safe_alternative2) > 0:
                        self.corrd = self.safe_alternative2[0]
                        self.view_board[self.black_place["knb2"][0]][self.black_place["knb2"][1]] = "-"




                        self.view_board[self.corrd[0]][self.corrd[1]] = "knb2"

                        self.black_place["knb2"] = self.corrd

                        self.knight2_move_count += 1



                else:
                    self.pawn_move()

            else:
                self.can_capture, self.safe_alternative = self.knight_capture("knb2")
                if "knb2" in self.black_place.keys():
                    self.can_capture, self.safe_alternative = self.knight_capture("knb2")
                    if len(self.can_capture) > 0:
                        self.corrd = self.can_capture[0]
                        print "self.cord", self.corrd

                        print "Capturing: "

                        self.view_board[self.black_place["knb2"][0]][self.black_place["knb2"][1]] = "-"
                        try:
                            self.white_pieces.remove(self.view_board[self.corrd[0]][self.corrd[1]])

                        except ValueError:
                            pass

                        del self.white_places[self.view_board[self.corrd[0]][self.corrd[1]]]

                        self.view_board[self.corrd[0]][self.corrd[1]] = "knb2"

                        self.black_place["knb2"] = self.corrd

                        self.knight1_move_count += 1

                    elif len(self.safe_alternative) > 0:
                        self.corrd = self.safe_alternative[0]
                        self.view_board[self.black_place["knb2"][0]][self.black_place["knb2"][1]] = "-"




                        self.view_board[self.corrd[0]][self.corrd[1]] = "knb2"

                        self.black_place["knb2"] = self.corrd

                        self.knight1_move_count += 1

                else:
                    self.pawn_move()

    def bishop_move(self):
        #del self.black_place["bb1"]

        self.flag1 = "bb1" in self.black_pieces

        self.flag2 = "bb2" in self.black_pieces

        if self.flag1:
            try:
                self.bishop1_loc_now = self.black_place["bb1"]
            except:
                pass

        if self.flag2:
            try:

                self.bishop2_loc_now = self.black_place["bb2"]

            except:
                pass

        if self.flag1:

            self.possible_squares = []
            self.counter1 = 1
            self.counter2 = 1
            self.y1 = self.bishop1_loc_now[1]
            self.x1 = 1

            self.y2 = self.bishop1_loc_now[0]
            self.x2 = self.bishop1_loc_now[1]

            self.y3 = 1
            self.x3 = self.bishop1_loc_now[0]
            while True:
                try:
                    self.sequence = (self.bishop1_loc_now[0]+self.counter1, self.bishop1_loc_now[1]+self.counter2)
                    self.returned = self.view_board[self.sequence[0]][self.sequence[1]]

                except IndexError:
                    break

                else:
                    self.possible_squares.append(self.sequence)
                    self.counter1 += 1
                    self.counter2 += 1


            while True:
                try:
                    self.sequence = (self.bishop1_loc_now[0]+self.x1, self.bishop1_loc_now[1]-self.y1)
                    self.returned = self.view_board[self.sequence[0]][self.sequence[1]]



                except IndexError:
                    break

                else:
                    self.possible_squares.append(self.sequence)
                    self.y1 -= 1
                    self.x1 += 1


            while self.bishop1_loc_now[0]-self.x2 >= 0 and self.bishop1_loc_now[1] - self.y2 >= 0:
                self.sequence = (self.bishop1_loc_now[0]-self.x2, self.bishop1_loc_now[1] - self.y2)
                self.possible_squares.append(self.sequence)

                self.x2 += 1

                self.y2 += 1

            print self.possible_squares

        #-----------------------bishop 2 -------------------------

        if self.flag2:

            self.possible_squares1 = []
            self.counter1 = 1
            self.counter2 = 1
            self.y1 = self.bishop2_loc_now[1]
            self.x1 = 1

            self.y2 = self.bishop2_loc_now[0]
            self.x2 = self.bishop2_loc_now[1]

            self.y3 = 1
            self.x3 = self.bishop2_loc_now[0]
            while True:
                try:
                    self.sequence = (self.bishop2_loc_now[0]+self.counter1, self.bishop2_loc_now[1]+self.counter2)
                    self.returned = self.view_board[self.sequence[0]][self.sequence[1]]

                except IndexError:
                    break

                else:
                    self.possible_squares1.append(self.sequence)
                    self.counter1 += 1
                    self.counter2 += 1


            while True:
                try:
                    self.sequence = (self.bishop2_loc_now[0]+self.x1, self.bishop2_loc_now[1]-self.y1)
                    self.returned = self.view_board[self.sequence[0]][self.sequence[1]]



                except IndexError:
                    break

                else:
                    self.possible_squares1.append(self.sequence)
                    self.y1 -= 1
                    self.x1 += 1


            while self.bishop2_loc_now[0]-self.x2 >= 0 and self.bishop2_loc_now[1] - self.y2 >= 0:
                self.sequence = (self.bishop2_loc_now[0]-self.x2, self.bishop2_loc_now[1] - self.y2)
                self.possible_squares1.append(self.sequence)

                self.x2 += 1

                self.y2 += 1

            if self.flag1:
                self.can_capture1 = {self.value[self.view_board[i[0]][i[1]]]:i for i in self.possible_squares if self.view_board[i[0]][i[1]] in self.white_places}

            if self.flag2:
                self.can_capture2 = {self.value[self.view_board[i[0]][i[1]]]:i for i in self.possible_squares1 if self.view_board[i[0]][i[1]] in self.white_places}

            print self.can_capture1

            print self.can_capture2

            if self.flag1:
                if len(self.can_capture1) > 0:

                    self.square_to_move = [i for a, i in self.can_capture1.items() if a == max(self.can_capture1.keys())][0]

                    print "Capturing:"

                    self.view_board[self.black_place["bb1"][0]][self.black_place['bb1'][1]] = "-"

                    self.piece_to_capture = self.view_board[self.square_to_move[0]][self.square_to_move[1]]
                    del self.white_places[self.piece_to_capture]


                    self.view_board[self.square_to_move[0]][self.square_to_move[1]] = "bb1"

                else:
                    if len(self.can_capture2) > 0:
                        self.square_to_move = [i for a, i in self.can_capture2.items() if a == max(self.can_capture2.keys())][0]

                        print "Capturing:"

                        self.view_board[self.black_place["bb2"][0]][self.black_place['bb2'][1]] = "-"

                        self.piece_to_capture = self.view_board[self.square_to_move[0]][self.square_to_move[1]]
                        del self.white_places[self.piece_to_capture]


                        self.view_board[self.square_to_move[0]][self.square_to_move[1]] = "bb2"

                    else:
                        self.best_square = self.node(self.possible_squares)
                        self.view_board[self.black_place["bb1"][0]][self.black_place['bb1'][1]] = "-"
                        self.place_to_move = self.view_board[self.best_square[0]][self.best_square[1]]

                        self.view_board[self.place_to_move[0]][self.place_to_move[1]] = "bb1"

            else:
                self.knight_move()






    def node(self, squares):
        self.best_squares = squares
        #self.not_good = []

        for i in squares:
            #check for pawns:
            try:
                self.val = self.view_board[i[0]+1][i[1]+1]
                self.val2 = self.view_board[i[0]+1][i[1]-1]

                if "pb" in self.val:
                    self.best_squares.remove(i)

                if "pb" in self.val2:
                    self.best_squares.remove(i)

            except IndexError:
                pass
        return self.best_squares[0]






    def computer_move(self):
        #need to check if self.move_count < 3
        #need to scan entire board and see if any pawn can capture any enemy pawn
        #this is the first stage of the game: The Pawns advance:
        if self.move_count < 4:
            self.pawn_move()

                #self.white_pieces.remove()
                #To do: put the above in a function, that way it can be called in any other section
        #-----------------------------------End of Pawn Stage ----------------------------
        #-----------------------------------Beginning of knight stage ----------------------------
        #elif self.move_count > 3 and self.move_count < 10:
        elif self.move_count >= 4 and self.move_count < 10:
            #must move knights and pawns
            #if knights cannot be moved, try to attack with the pawn code above
            #try to involve the bishops as well

            #two lists returned: [(x1, y1), etc], [(x1, y1), etc], first for capture, second for safe move
            self.knight_move()

        else:
            self.bishop_move()

        #-----------------------------------End of knight stage ----------------------------
        #-----------------------------------Beginning of Bishop stage ----------------------------

        self.move_count += 1






    def show_board(self):
        return self.view_board





the_game = Chess()
the_game.initialize()

for i in range(10):
    for i in range(8):
        print str(i+1)+"  ",
    print
    for row, i in enumerate(the_game.show_board()):
        for b in i:
            if b == "-":
                print " "+b+" ",
            else:
                print b,
        print row+1
        print
    x = input("Enter the x-corrdinate: ")
    y = input("Enter the y-corrdinate: ")
    piece = raw_input("Enter the piece: ")
    the_game.user_move(piece, x, y)
    for row, i in enumerate(the_game.show_board()):
        for b in i:
            if b == "-":
                print " "+b+" ",
            else:
                print b,
        print row+1
        print
    #time.sleep(2)
    the_game.computer_move()

    for row, i in enumerate(the_game.show_board()):
        for b in i:
            if b == "-":
                print " "+b+" ",
            else:
                print b,
        print row+1
        print
