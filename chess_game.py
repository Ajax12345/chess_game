#some things for later: game log, with each move written to a file
import time
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

        self.black_pieces = ["rb2", "knb2", 'bb2', 'qb', 'kb', "bb2", 'knb2', 'rb2']
        self.black_pieces.extend(["pb"+str(i+1) for i in range(8)])

        self.white_places = {}
        self.black_place = {}

        self.value = {"rb1":5, "knb1":3, 'bb1':3, 'qb':10, 'kb':20, 'bb2':3, 'knb2':3, 'rb2':5, "rw1":5, "knw1":3, 'bw1':3, 'qw':10, 'kw':20, 'bw2':3, 'knw2':3, 'rw2':5}

        self.value.update({i:1 for i in ["pb"+str(i+1) for i in range(8)]})

        self.value.update({i:1 for i in ["pw"+str(i+1) for i in range(8)]})
        self.move_count = 0



    def rook(self, position):
        '''
        may not need this stuff: flawed logic
        self.danger_squares = [(position[0], position[1]+i) for i in range(1, 7-position[1]) if (position[0], position[1]+i) not in self.white_places.values()]
        self.danger_squares.extend([([position[0], position[1]-i]) for i in range(1, position[1]+1) if (position[0], position[1]-i) not in self.white_places.values()])
        self.danger_squares.extend([(position[0]+i, position[1]) for i in range(1, position[0]+1) if (position[0], position[1]-i) not in self.white_places.values()])
        self.danger_squares.extend([(position[0]-i, position[1]) for i in range(1, position[0]+1) if (position[0], position[1]-i) not in self.white_places.values()])
        '''
        self.danger_squares = [(position[0], position[1]+i) if (position[0], position[1]+i) not in self.white_places.values() else None for i in range(1, 7-position[1])]
        self.danger_squares.extend([([position[0], position[1]-i]) if ([position[0], position[1]-i]) not in self.white_places.values() else None for i in range(1, position[1]+1)])
        self.danger_squares.extend([([position[0]+i, position[1]]) if ([position[0]+i, position[1]]) not in self.white_places.values() else None for i in range(1, position[1]+1)])
        self.danger_squares.extend([([position[0]-i, position[1]]) if ([position[0]-i, position[1]]) not in self.white_places.values() else None for i in range(1, position[1]+1)])

        self.danger_squares = [i[:i.index(None)] if None in i else i for i in self.danger_squares]


        self.threatened = [a for a, b in self.black_place.items() if b in self.danger_squares]

        self.maxes = {i:self.value[i] for i in self.threatened}

        return [(a, b) for a, b in self.maxes.items() if b == max(self.maxes.values())][0]


    def bishop(self, position):
        #self.danger_squares = [(position[0]+i, position[1]+i) for i in range(1, min([position[0], position[1]])) if (position[0]+i, position[1]+i) not in self.white_places.values()]

        #self.danger_squares.extend([(position[0]-i, position[1]-i) for i in range(1, min([position[0], position[1]])) if (position[0]+i, position[1]+i) not in self.white_places.values()])
        #self.danger_squares.extend([(position[0]+i, position[1]-i) for i in range(1, min([position[0], position[1]])) if (position[0]+i, position[1]+i) not in self.white_places.values()])
        #self.danger_squares.extend([(position[0]-i, position[1]+i) for i in range(1, min([position[0], position[1]])) if (position[0]+i, position[1]+i) not in self.white_places.values()])


        self.danger_squares = [(position[0]+i, position[1]+i) if (position[0]+i, position[1]+i) not in self.white_places.values() else None for i in range(1, min([position[0], position[1]]))]
        self.danger_squares.extend([(position[0]-i, position[1]-i) if (position[0]-i, position[1]-i) not in self.white_places.values() else None for i in range(1, min([position[0], position[1]]))])
        self.danger_squares.extend([(position[0]+i, position[1]-i) if (position[0]+i, position[1]-i) not in self.white_places.values() else None for i in range(1, min([position[0], position[1]]))])
        self.danger_squares.extend([(position[0]-i, position[1]+i) if (position[0]-i, position[1]+i) not in self.white_places.values() else None for i in range(1, min([position[0], position[1]]))])

        self.danger_squares = [i[:i.index(None)] if None in i else i for i in self.danger_squares]

        self.threatened = [a for a, b in self.black_place.items() if b in self.danger_squares]

        self.maxes = {i:self.value[i] for i in self.threatened}

        return [(a, b) for a, b in self.maxes.items() if b == max(self.maxes.values())][0]


    def queen(self, position):

        self.danger_squares = [(position[0], position[1]+i) if (position[0], position[1]+i) not in self.white_places.values() else None for i in range(1, 7-position[1])]
        self.danger_squares.extend([([position[0], position[1]-i]) if ([position[0], position[1]-i]) not in self.white_places.values() else None for i in range(1, position[1]+1)])
        self.danger_squares.extend([([position[0]+i, position[1]]) if ([position[0]+i, position[1]]) not in self.white_places.values() else None for i in range(1, position[1]+1)])
        self.danger_squares.extend([([position[0]-i, position[1]]) if ([position[0]-i, position[1]]) not in self.white_places.values() else None for i in range(1, position[1]+1)])

        self.danger_squares = [(position[0]+i, position[1]+i) if (position[0]+i, position[1]+i) not in self.white_places.values() else None for i in range(1, min([position[0], position[1]]))]
        self.danger_squares.extend([(position[0]-i, position[1]-i) if (position[0]-i, position[1]-i) not in self.white_places.values() else None for i in range(1, min([position[0], position[1]]))])
        self.danger_squares.extend([(position[0]+i, position[1]-i) if (position[0]+i, position[1]-i) not in self.white_places.values() else None for i in range(1, min([position[0], position[1]]))])
        self.danger_squares.extend([(position[0]-i, position[1]+i) if (position[0]-i, position[1]+i) not in self.white_places.values() else None for i in range(1, min([position[0], position[1]]))])

        #self.danger_squares = [i[:i.index(None)] if None in i else i for i in self.danger_squares] #need to change this
        if None in self.danger_squares:
            self.danger_squares = self.danger_squares[:self.danger_squares.index(None)]

        self.threatened = [a for a, b in self.black_place.items() if b in self.danger_squares]
        self.maxes = {i:self.value[i] for i in self.threatened}

        #return [(a, b) for a, b in self.maxes.items() if b == max(self.maxes.values())][0]
        if len([(a, b) for a, b in self.maxes.items()]) > 0:
            return [(a, b) for a, b in self.maxes.items()][0]

        else:
            return []


    def king(self, position):
        self.danger_squares = []
        if position[0]+ 1 > 7:
            self.danger_squares.append((position[0]-1, position[1]))
            if position[1]+1 > 7:
                self.danger_squares.append(position)

            else:
                self.danger_squares.append((position[0], position[1]+1))

        else:
            self.danger_squares.append((position[0]+1, position[1]))
            if position[1]+1 > 7:
                self.danger_squares.append((position[0]+1, position[1]))

            else:
                self.danger_squares.append((position[0]+1, position[1]+1))

        if position[0]-1 >= 0:
            self.danger_squares.append((position[0]-1, position[1]))
            if position[1] - 1 >= 0:
                self.danger_squares.append((position[0]-1, position[1]-1))

            else:
                self.danger_squares.append((position[0]-1, position[1]))

        self.threatened = [a for a, b in self.black_place.items() if b in self.danger_squares]
        self.maxes = {i:self.value[i] for i in self.threatened}

        return [(a, b) for a, b in self.maxes.items() if b == max(self.maxes.values())][0]

    def knight(self, position):
        self.danger_squares = []
        if position[0]+2 <= 7:
            if position[1]+1 <=7:
                self.danger_squares.append((position[0]+2, position[1]+1))

            else:
                self.danger_squares.append((position[0]+2, position[1]-1))


        else:
            if position[1]+1 <=7:
                self.danger_squares.append((position[0]-2, position[1]+1))

            else:
                self.danger_squares.append((position[0]-2, position[1]-1))

        if position[0]-2 >= 0:

            if position[1] + 1 <= 7:
                self.danger_squares.append((position[0]-2, position[1]+1))

            else:
                self.danger_squares.append((position[0]-2, position[1]-1))

        self.threatened = [a for a, b in self.black_place.items() if b in self.danger_squares]
        self.maxes = {i:self.value[i] for i in self.threatened}

        return [(a, b) for a, b in self.maxes.items() if b == max(self.maxes.values())][0] #returning name of black piece threatened and its value


    def attack_rook(self, position):
        self.danger_squares = [(position[0], position[1]+i) if (position[0], position[1]+i) not in self.black_place.values() else None for i in range(1, 7-position[1])]
        self.danger_squares.extend([([position[0], position[1]-i]) if ([position[0], position[1]-i]) not in self.black_place.values() else None for i in range(1, position[1]+1)])
        self.danger_squares.extend([([position[0]+i, position[1]]) if ([position[0]+i, position[1]]) not in self.black_place.values() else None for i in range(1, position[1]+1)])
        self.danger_squares.extend([([position[0]-i, position[1]]) if ([position[0]-i, position[1]]) not in self.black_place.values() else None for i in range(1, position[1]+1)])

        self.danger_squares = [i[:i.index(None)] if None in i else i for i in self.danger_squares]
        return self.danger_squares
        '''
        self.threatened = [a for a, b in self.white_places.items() if b in self.danger_squares]
        self.maxes = {i:self.value[i] for i in self.threatened}

        return [(a, b) for a, b in self.maxes.items() if b == max(self.maxes.values())][0]      #returning name of white piece threatened and its value
        '''
    def attack_bishop(self, position):
        self.danger_squares = [(position[0]+i, position[1]+i) if (position[0]+i, position[1]+i) not in self.black_place.values() else None for i in range(1, min([position[0], position[1]]))]
        self.danger_squares.extend([(position[0]-i, position[1]-i) if (position[0]-i, position[1]-i) not in self.black_place.values() else None for i in range(1, min([position[0], position[1]]))])
        self.danger_squares.extend([(position[0]+i, position[1]-i) if (position[0]+i, position[1]-i) not in self.black_place.values() else None for i in range(1, min([position[0], position[1]]))])
        self.danger_squares.extend([(position[0]-i, position[1]+i) if (position[0]-i, position[1]+i) not in self.black_place.values() else None for i in range(1, min([position[0], position[1]]))])

        self.danger_squares = [i[:i.index(None)] if None in i else i for i in self.danger_squares]
        return self.danger_squares
        '''
        self.threatened = [a for a, b in self.white_places.items() if b in self.danger_squares]

        self.maxes = {i:self.value[i] for i in self.threatened}

        return [(a, b) for a, b in self.maxes.items() if b == max(self.maxes.values())][0]
        '''
    def attack_knight(self, position):
        self.danger_squares = []
        if position[0]+2 <= 7:
            if position[1]+1 <=7:
                self.danger_squares.append((position[0]+2, position[1]+1))

            else:
                self.danger_squares.append((position[0]+2, position[1]-1))


        else:
            if position[1]+1 <=7:
                self.danger_squares.append((position[0]-2, position[1]+1))

            else:
                self.danger_squares.append((position[0]-2, position[1]-1))

        if position[0]-2 >= 0:

            if position[1] + 1 <= 7:
                self.danger_squares.append((position[0]-2, position[1]+1))

            else:
                self.danger_squares.append((position[0]-2, position[1]-1))

        self.threatened = [a for a, b in self.white_places.items() if b in self.danger_squares]
        return self.threatened
        '''
        self.maxes = {i:self.value[i] for i in self.threatened}

        return [(a, b) for a, b in self.maxes.items() if b == max(self.maxes.values())][0]
        '''
    #need attack queen:

    def attack_queen(self, postion):
        #need to convert white_places to black_place
        self.danger_squares = [(position[0], position[1]+i) if (position[0], position[1]+i) not in self.black_place.values() else None for i in range(1, 7-position[1])]
        self.danger_squares.extend([([position[0], position[1]-i]) if ([position[0], position[1]-i]) not in self.black_place.values() else None for i in range(1, position[1]+1)])
        self.danger_squares.extend([([position[0]+i, position[1]]) if ([position[0]+i, position[1]]) not in self.white_places.values() else None for i in range(1, position[1]+1)])
        self.danger_squares.extend([([position[0]-i, position[1]]) if ([position[0]-i, position[1]]) not in self.white_places.values() else None for i in range(1, position[1]+1)])

        self.danger_squares = [(position[0]+i, position[1]+i) if (position[0]+i, position[1]+i) not in self.white_places.values() else None for i in range(1, min([position[0], position[1]]))]
        self.danger_squares.extend([(position[0]-i, position[1]-i) if (position[0]-i, position[1]-i) not in self.white_places.values() else None for i in range(1, min([position[0], position[1]]))])
        self.danger_squares.extend([(position[0]+i, position[1]-i) if (position[0]+i, position[1]-i) not in self.white_places.values() else None for i in range(1, min([position[0], position[1]]))])
        self.danger_squares.extend([(position[0]-i, position[1]+i) if (position[0]-i, position[1]+i) not in self.white_places.values() else None for i in range(1, min([position[0], position[1]]))])

        self.danger_squares = [i[:i.index(None)] if None in i else i for i in self.danger_squares]
        return self.danger_squares
        '''
        self.threatened = [a for a, b in self.black_place.items() if b in self.danger_squares]
        self.maxes = {i:self.value[i] for i in self.threatened}

        return [(a, b) for a, b in self.maxes.items() if b == max(self.maxes.values())][0]
        '''

    def regular_rook(self, piece_to_attack):
        self.danger_squares = [(position[0], position[1]+i) if (position[0], position[1]+i) not in self.black_place.values() else None for i in range(1, 7-position[1])]
        self.danger_squares.extend([([position[0], position[1]-i]) if ([position[0], position[1]-i]) not in self.black_place.values() else None for i in range(1, position[1]+1)])
        self.danger_squares.extend([([position[0]+i, position[1]]) if ([position[0]+i, position[1]]) not in self.black_place.values() else None for i in range(1, position[1]+1)])
        self.danger_squares.extend([([position[0]-i, position[1]]) if ([position[0]-i, position[1]]) not in self.black_place.values() else None for i in range(1, position[1]+1)])

        self.danger_squares = [i[:i.index(None)] if None in i else i for i in self.danger_squares]

        return list(self.value[piece_to_attack]) in self.danger_squares


    def regular_bishop(self, piece_to_attack):
        self.danger_squares = [(position[0]+i, position[1]+i) if (position[0]+i, position[1]+i) not in self.black_place.values() else None for i in range(1, min([position[0], position[1]]))]
        self.danger_squares.extend([(position[0]-i, position[1]-i) if (position[0]-i, position[1]-i) not in self.black_place.values() else None for i in range(1, min([position[0], position[1]]))])
        self.danger_squares.extend([(position[0]+i, position[1]-i) if (position[0]+i, position[1]-i) not in self.black_place.values() else None for i in range(1, min([position[0], position[1]]))])
        self.danger_squares.extend([(position[0]-i, position[1]+i) if (position[0]-i, position[1]+i) not in self.black_place.values() else None for i in range(1, min([position[0], position[1]]))])

        self.danger_squares = [i[:i.index(None)] if None in i else i for i in self.danger_squares]

        return list(self.value[piece_to_attack]) in self.danger_squares #need to get its position tuple from dict

    def regular_queen(self, piece_to_attack):
        self.danger_squares = [(position[0], position[1]+i) if (position[0], position[1]+i) not in self.black_place.values() else None for i in range(1, 7-position[1])]
        self.danger_squares.extend([([position[0], position[1]-i]) if ([position[0], position[1]-i]) not in self.black_place.values() else None for i in range(1, position[1]+1)])
        self.danger_squares.extend([([position[0]+i, position[1]]) if ([position[0]+i, position[1]]) not in self.black_place.values() else None for i in range(1, position[1]+1)])
        self.danger_squares.extend([([position[0]-i, position[1]]) if ([position[0]-i, position[1]]) not in self.black_place.values() else None for i in range(1, position[1]+1)])
        self.danger_squares = [(position[0]+i, position[1]+i) if (position[0]+i, position[1]+i) not in self.black_place.values() else None for i in range(1, min([position[0], position[1]]))]
        self.danger_squares.extend([(position[0]-i, position[1]-i) if (position[0]-i, position[1]-i) not in self.black_place.values() else None for i in range(1, min([position[0], position[1]]))])
        self.danger_squares.extend([(position[0]+i, position[1]-i) if (position[0]+i, position[1]-i) not in self.black_place.values() else None for i in range(1, min([position[0], position[1]]))])
        self.danger_squares.extend([(position[0]-i, position[1]+i) if (position[0]-i, position[1]+i) not in self.black_place.values() else None for i in range(1, min([position[0], position[1]]))])
        self.danger_squares = [i[:i.index(None)] if None in i else i for i in self.danger_squares]

        return list(self.value[piece_to_attack]) in self.danger_squares #need to get its position tuple for dict

    def regular_knight(self, piece_to_attack):
        self.danger_squares = []
        if position[0]+2 <= 7:
            if position[1]+1 <=7:
                self.danger_squares.append((position[0]+2, position[1]+1))

            else:
                self.danger_squares.append((position[0]+2, position[1]-1))


        else:
            if position[1]+1 <=7:
                self.danger_squares.append((position[0]-2, position[1]+1))

            else:
                self.danger_squares.append((position[0]-2, position[1]-1))

        if position[0]-2 >= 0:

            if position[1] + 1 <= 7:
                self.danger_squares.append((position[0]-2, position[1]+1))

            else:
                self.danger_squares.append((position[0]-2, position[1]-1))
        self.danger_squares = [i[:i.index(None)] if None in i else i for i in self.danger_squares]
        print self.danger_squares

        return list(self.value[piece_to_attack]) in self.danger_squares



    def user_move(self, piece, x, y):
        self.view_board[self.white_places[piece][0]][self.white_places[piece][1]] = "-"
        self.white_places[piece] = (x-1, y-1)
        if self.view_board[x-1][y-1] == "-":
            self.view_board[x-1][y-1] = piece
        else:
            print "capturing ", self.view_board[x-1][y-1]

            del self.black_place[self.view_board[x-1][y-1]]

            self.view_board[x-1][y-1] = piece #was not here before
            #self.black_pieces.remove(self.view_board[x-1][y-1])

    def move_black_piece_to_capture(self, black, white):
        print "Capturing:"
        self.white_piece = self.view_board[self.value[white][0]][self.value[white][1]]
        self.view_board[self.value[white][0]][self.value[white][1]] = black
        del self.view[self.white_piece]
        self.view_board[self.value[black][0]][self.value[black][1]] = "-"

    def retreat_piece(self, black):
        self.options = []
        self.location = self.value[black]
        if black[:2] == "rb":
            self.options = self.regular_rook(self.location)

        elif black[:2] == "qb":
            self.options = self.regular_queen(self.location)

        elif black[:2] == "kn":
            self.options = self.regular_knight(self.location)

        elif black[:2] == "bb":
            self.options = self.regular_bishop(self.location)

        self.square = self.options[0]
        self.old_postition = self.value[black]

        self.view_board[self.square[0]][self.square[1]] = black

        self.view_board[self.old_postition[0]][self.old_postition[1]] = "-"

    def initial_moves(self):
        '''
        self.position = self.black_place["pb"+str(self.move_count+1)]
        print self.position
        self.view_board[self.position[0]][self.position[1]] = "-"

        self.view_board[self.position[0]+2][self.position[1]] = "pb"+str(self.move_count+1) #may need to switch all x and y corrdinates from now on
        '''
        #need a capture feature here





    def computer_move(self):
        if self.move_count > 4:
            self.pieces_attacked = []
        #--------------------Black pieces potentially threatened--------------------------------------------------------------------------------
            for a, b in self.white_places.items():
                if len(a) == 3:
                    if a[:2] == "rw":
                    #if len(self.)
                        self.pieces_attacked.append(self.rook(b))

                    elif a[:2] == 'bw':
                        self.pieces_attacked(self.bishop(b))

                elif len(a) == 2:
                    if a[0] == 'q':
                        if len(self.queen(b)) > 0:

                            self.pieces_attacked.append(self.queen(b))
                    elif len(a) == 4:
                        self.pieces_attacked.append(self.knight(b))


                    else:
                        self.pieces_attacked.append(self.king(b))



            self.at_risk = {i:self.value[i] for i in self.pieces_attacked}

            self.under_attack = [a for a, b in self.at_risk.items() if b == max(self.at_risk.values())][0]


            self.can_attack = []
        #----------------------black squares for attacking------------------------------------------------------------------------------
        #need to convert all to self.attack_rook, attack_queen, etc
        #need exact black piece name
            for a, b in self.black_place.items():
                if len(a) == 3:
                    if a[:2] == "rb":
                        self.can_attack.append((a, self.attack_rook(b))) #(blackpeice, (white_piece, whitepiecevalue))

                    elif a[:2] == 'bb':
                        self.can_attack.append((a, self.attack_bishop(b)))

                elif len(a) == 2:
                    if a[0] == 'q':
                        self.can_attack.append((a, self.attack_queen(b)))


                elif len(a) == 4:
                    self.can_attack.append((a, self.attack_knight(position))) #may not need this



            #do we stand to loose or gain more material?
            #do not need the regular___ piece methods.

            self.could_lose = max([list(i)[1] for i in self.pieces_attacked])

            self.could_gain = max([list(i)[1][1] for i in self.can_attack])

            if self.could_gain > self.could_lose:

                self.enemy = [(a, b[0]) for a, b in dict(self.can_attack).items() if b[1] == self.could_gain][0] #returns black white piece name

                self.move_black_piece_to_capture(self.enemy[0], self.enemy[1])






            elif self.could_gain <= self.could_lose:
                self.must_move = [a for a, b in dict(self.pieces_attacked).items() if b == self.could_lose][0] #returns black piece name

                self.retreat_piece(self.must_move)

        else:
            self.initial_moves()

        self.move_count += 1



    def show_board(self):
        return self.view_board

    def iskingwhite(self):
        return "kw" in self.white_pieces

    def iskingblack(self):
        return "kb" in self.black_pieces

    def initialize(self):
        for i in range(len(self.view_board)):
            for b in range(len(self.view_board[0])):
                self.piece = self.view_board[i][b]

                if self.piece in self.white_pieces:
                    self.white_places[self.piece] = (i, b)

                elif self.piece in self.black_pieces:
                    self.black_place[self.piece] = (i, b)



    def show_pieces(self):
        print self.white_places
        print "-----------------------"
        print self.black_place




game = Chess()
game.initialize()
#game.show_pieces()
flag = True

while flag:
    for i in range(8):
        print str(i+1)+"  ",
    print
    for row, i in enumerate(game.show_board()):
        for b in i:
            if b == "-":
                print " "+b+" ",
            else:
                print b,
        print row+1
        print

    x = input("Enter the x-corrdinate: ")
    y = input('Enter the y-corrdinate: ')
    the_piece = raw_input("Enter the piece: ")
    game.user_move(the_piece, x, y)
    #time.sleep(3)
    game.computer_move()

    for row, i in enumerate(game.show_board()):
        for b in i:
            if b == "-":
                print " "+b+" ",
            else:
                print b,
        print row+1
        print

    if game.iskingwhite() and game.iskingblack():
        continue

    elif not game.iskingwhite():
        print "You lost"
        flag = False

    elif not game.iskingblack():
        print "You won!"
        flag = False
