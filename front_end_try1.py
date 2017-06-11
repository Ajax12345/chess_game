import pygame
#import chess_game2
#from chess_game2 import *
from chess_game2 import Chess

#val = chess_game2.Chess()
#print val.show_board()

class Chessboard:
    def __init__(self):
        self.width = 800
        self.height = 800
        #self.gameDisplay = pygame.display.set_mode((self.width, self.height))
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.rookw = pygame.image.load("/Users/davidpetullo/Desktop/whiteRook.png")
        self.bishopw = pygame.image.load("/Users/davidpetullo/Desktop/bishopw.png")
        self.knightw = pygame.image.load("/Users/davidpetullo/Desktop/knightw.png")
        self.kingw = pygame.image.load("/Users/davidpetullo/Desktop/kingw.png")
        self.queenw = pygame.image.load("/Users/davidpetullo/Desktop/queenw.png")
        self.pawnw = pygame.image.load("/Users/davidpetullo/Desktop/pawnw.png")

        self.kingb = pygame.image.load("/Users/davidpetullo/Desktop/blackKing.png")
        self.rookb = pygame.image.load("/Users/davidpetullo/Desktop/blackRook.png")
        self.bishopb = pygame.image.load("/Users/davidpetullo/Desktop/blackBishop.png")
        self.knightb = pygame.image.load("/Users/davidpetullo/Desktop/blackKnight.png")

        self.queenb = pygame.image.load("/Users/davidpetullo/Desktop/blackQueen.png")
        self.pawnb = pygame.image.load("/Users/davidpetullo/Desktop/blackPawn.png")
        self.alive = True
        self.x = 0
        self.y = 0
        self.first_click = 0
        self.second_click = 0
        #chess = chess_game2.Chess()
        #chess.initialize()
        #self.pieces = chess.white_places
        self.chess = Chess()
        self.chess.initialize()
        self.pieces = self.chess.white_places


        '''
        #self.view_board = [["rb1", "knb1", 'bb1', 'qb', 'kb', 'bb2', 'knb2', 'rb2'],
        #                    ["pb"+str(i+1) for i in range(8)],
        #                    ["-" for i in range(8)],
        #                    ["-" for i in range(8)],
        #                    ["-" for i in range(8)],
        #                    ["-" for i in range(8)],
        #                    ["pw"+str(i+1) for i in range(8)],
        #                    ["rw1", "knw1", 'bw1', 'qw', 'kw', 'bw2', 'knw2', 'rw2']]
        '''

        self.view_board = self.chess.show_board()


    def update_screen(self):
        pygame.display.flip()

    def white_move(self):
        if isinstance(self.first_click, tuple) and isinstance(self.second_click, tuple):
            self.column1 = self.first_click[0]
            self.row1 = self.first_click[1]

            self.column2 = self.second_click[0]
            self.row2 = self.second_click[1]


            self.place1 = (int(str(self.column1)[0]), int(str(self.row1)[0])) #this is the first piece the user selects

            self.place2 = (int(str(self.column2)[0]), int(str(self.row2)[0])) #this is the desired square

            #print self.place2

            #print "pieces", self.pieces

            print self.place1
            print self.place2

            print self.view_board

            self.place1 = self.place1[::-1]
            print "new place1", self.place1


            print [a for a, b in self.pieces.items() if b == self.place1]
            self.piece = "pw2" #have to reverse the corrdinates
            self.chess.user_move(self.piece, self.place2[1], self.place2[0])





    def show_corrds(self):
        #print self.first_click
        #print self.second_click
        if isinstance(self.first_click, tuple) and isinstance(self.second_click, tuple):
            self.column1 = self.first_click[0]
            self.row1 = self.first_click[1]

            self.column2 = self.second_click[0]
            self.row2 = self.second_click[1]

            print "_____________________"
            print (int(str(self.column1)[0]), int(str(self.row1)[0]))

            print (int(str(self.column2)[0]), int(str(self.row2)[0]))

            print "_____________________"



    def draw_board(self):

        for i in range(8):

            for b in range(8):
                if i%2 == 0:
                    if b%2 != 0:
                        pygame.draw.rect(self.screen, (255, 255, 255), (0+self.x, 0+self.y, 100, 100))
                else:
                    if b%2 == 0:
                        pygame.draw.rect(self.screen, (255, 255, 255), (0+self.x, 0+self.y, 100, 100))

                self.x += 100

            self.x = 0
            self.y += 100


    def update_board(self):
        self.x = 0
        self.y = 0

        for i in range(len(self.view_board)):
            for b in range(len(self.view_board[0])):
                if "rw" in self.view_board[i][b]:
                    #self.screen.blit(self.rookw, (i*100, b*100))
                    self.screen.blit(self.rookw, (b*100, i*100))

                elif "pw" in self.view_board[i][b]:
                    self.screen.blit(self.pawnw, (b*100, i*100))

                elif "kw" in self.view_board[i][b]:
                    self.screen.blit(self.kingw, (b*100, i*100))

                elif "qw" in self.view_board[i][b]:
                    self.screen.blit(self.queenw, (b*100, i*100))

                elif "bw" in self.view_board[i][b]:
                    self.screen.blit(self.bishopw, (b*100, i*100))

                elif "knw" in self.view_board[i][b]:
                    self.screen.blit(self.knightw, (b*100, i*100))

                elif "kb" in self.view_board[i][b]:
                    self.screen.blit(self.kingb, (b*100, i*100))

                elif "qb" in self.view_board[i][b]:
                    self.screen.blit(self.queenb, (b*100, i*100))

                elif "rb" in self.view_board[i][b]:
                    self.screen.blit(self.rookb, (b*100, i*100))

                elif "bb" in self.view_board[i][b]:
                    self.screen.blit(self.bishopb, (b*100, i*100))

                elif "knb" in self.view_board[i][b]:
                    self.screen.blit(self.knightb, (b*100, i*100))

                elif "pb" in self.view_board[i][b]:
                    self.screen.blit(self.pawnb, (b*100, i*100))
                else:
                    pass




            #else:
                #pygame.draw.rect(self.screen, (255, 255, 255), (0+self.x, 0+self.y, 100, 100))

            #self.x += 100

        #for i in range(8):


    def board(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Chess game")

        while self.alive:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.alive = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.first_click == 0:
                        self.first_click = pos

                    else:
                        self.second_click = pos




        #for i in range(8):
            #self.draw_board()
            self.draw_board()
            self.white_move()
            self.update_board()

            #self.show_corrds()


            self.update_screen()



        pygame.quit()
        quit()


chess = Chessboard()

chess.board()
