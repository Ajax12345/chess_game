class Board:
    def __init__(self):

        self.view_board = [["rb1", "knb1", 'bb1', 'qb', 'kb', 'bb2', 'knb2', 'rb2'], ["pb"+str(i+1) for i in range(8)], ["-" for i in range(8)]*4,["pw"+str(i+1) for i in range(8)],
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

        self.initialize()


    def initialize(self):
        for i in range(len(self.view_board)):
            for b in range(len(self.view_board[0])):
                self.piece = self.view_board[i][b]

                if self.piece in self.white_pieces:
                    self.white_places[self.piece] = (i, b)

                elif self.piece in self.black_pieces:
                    self.black_place[self.piece] = (i, b)
