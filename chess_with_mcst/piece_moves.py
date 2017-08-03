def get_pawn_moves(view_board, x, y):
    to_move = []
    if x == 1:
        to_move.append((x+2, y))
        to_move.append((x+1, y))

    else:
        try:
            a1, b1 = (x+1, y+1)
            a2, b2 = (x+1, y-1)
            space1 = view_board[a1][b1]
            space2 = view_board[a2][b2]
            if "w" in space1:
                to_move.append((a1, b1))

            if "w" in space2:
                to_move.append((a2, b2))
        except:
            pass
    return to_move



def get_knight_moves(view_board, x, y):
    to_return = []

    try:
        a, b = (x+2, y+1) #-
                              #-
                              #- -
        if view_board[a][b] == "-" or "w" in view_board[a][b]:
            to_return.append((a, b))

    except:
        pass

    try:
        a, b = (x+2, y-1) #-
                        #-
                        #- -


        if view_board[a][b] == "-" or "w" in view_board[a][b]:
            to_return.append((a, b))

    except:
        pass

    try:
        a, b = (x+1, y+2) #- - -
                                  #-
        if view_board[a][b] == "-" or "w" in view_board[a][b]:
            to_return.append((a, b))

    except:
        pass

    try:
        a, b = (x-1, y+2)   #-
                            #- - -
        if a > 0:

            if view_board[a][b] == "-" or "w" in view_board[a][b]:
                to_return.append((a, b))

    except:
        pass

    try:
        a, b = (x+1, y-2)
        if view_board[a][b] == "-" or "w" in view_board[a][b]:
            to_return.append((a, b))

    except:
        pass

    try:
        a, b = (x-1, y-2)
        if a > 0:
            if view_board[a][b] == "-" or "w" in view_board[a][b]:
                to_return.append((a, b))

    except:
        pass

    #return to_return
    return [i for i in to_return if all(b >= 0 for b in i)]



def get_bishop_moves(view_board, x, y):
    to_return = []
    new_y = y
    new_x = x
    while True:

        if new_y +1 < 8 and new_x + 1 < 8:
            #print "got here"
            new_y += 1
            new_x += 1
            if view_board[new_x][new_y] == "-" or "w" in view_board[new_x][new_y]:
                #print "got here"
                to_return.append((new_x, new_y))


            else:
                break

        else:
            break
    new_y = y
    new_x = x

    while True:

        if new_y - 1 >=0 and new_x - 1 >= 0:
            new_y -= 1
            new_x -= 1
            if view_board[new_x][new_y] == "-" or "w" in view_board[new_x][new_y]:
                #print "got here"
                to_return.append((new_x, new_y))


            else:
                break

        else:
            break

    new_y = y
    new_x = x

    while True:

        if new_y + 1 < 8 and new_x -1 >= 0:
            new_y += 1
            new_x -= 1
            if view_board[new_x][new_y] == "-" or "w" in view_board[new_x][new_y]:
                #print "got here"
                to_return.append((new_x, new_y))


            else:
                break

        else:
            break

    new_y = y
    new_x = x

    while True:
        if new_y -1 >= 0 and new_x + 1 < 8:
            new_y -= 1
            new_x += 1
            if view_board[new_x][new_y] == "-" or "w" in view_board[new_x][new_y]:
                #print "got here"
                to_return.append((new_x, new_y))


            else:
                break

        else:
            break

    return to_return



def get_rook_moves(view_board, x, y):
    to_return = []

    for i in range(x+1, 8):
        a, b = (i, y)
        try:
            if view_board[a][b] == "-" or "w" in view_board[a][b]:
                to_return.append((a, b))

            else:
                break

        except:
            pass

    for i in range(x):
        a, b = (i, y)
        if view_board[a][b] == "-" or "w" in view_board[a][b]:
            to_return.append((a, b))

        else:
            break

    for i in range(y+1, 8):

        a, b = (x, i)
        if view_board[a][b] == "-" or "w" in view_board[a][b]:
            to_return.append((a, b))

        else:
            break

    for i in range(y):

        a, b = (x, i)
        if view_board[a][b] == "-" or "w" in view_board[a][b]:
            to_return.append((a, b))

        else:
            break

    return to_return


def get_queen_moves(view_board, x, y):
    ranks = get_rook_moves(view_board, x, y)
    diags = get_bishop_moves(view_board, x, y)

    return ranks + diags

def get_king_moves(view_board, x, y):
    to_return = []

    if x + 1 < 8 and y + 1 < 8:
        if view_board[x+1][y+1] == "-" or "w" in view_board[x+1][y+1]:
            to_return.append((x+1, y+1))

    if x + 1 <8 and y - 1 >= 0:
        if view_board[x+1][y-1] == "-" or "w" in view_board[x+1][y-1]:
            to_return.append((x+1, y-1))

    if x - 1 >= 0 and y - 1 >= 0:
        if view_board[x-1][y-1] == "-" or "w" in view_board[x-1][y-1]:
            to_return.append((x-1, y-1))

    if x - 1 >= 0 and y + 1 < 8:
        if view_board[x-1][y+1] == "-" or "w" in view_board[x-1][y+1]:
            to_return.append((x-1, y+1))

    return to_return
