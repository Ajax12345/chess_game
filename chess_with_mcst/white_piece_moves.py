def get_pawn_moves(view_board, x, y):
    to_move = []
    if x == 6:
        to_move.append((x-2, y))
        to_move.append((x-1, y))

    else:
        try:
            a1, b1 = (x-1, y-1)
            a2, b2 = (x-1, y+1)
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
        a, b = (x-2, y-1) #-
                              #-
                              #- -
        if view_board[a][b] == "-" or "b" in view_board[a][b]:
            to_return.append((a, b))

    except:
        pass

    try:
        a, b = (x-2, y+1) #-
                        #-
                        #- -


        if view_board[a][b] == "-" or "b" in view_board[a][b]:
            to_return.append((a, b))

    except:
        pass

    try:
        a, b = (x-1, y-2) #- - -
                                  #-
        if view_board[a][b] == "-" or "b" in view_board[a][b]:
            to_return.append((a, b))

    except:
        pass

    try:
        a, b = (x+1, y-2)   #-
                            #- - -
        if a > 0:

            if view_board[a][b] == "-" or "b" in view_board[a][b]:
                to_return.append((a, b))

    except:
        pass

    try:
        a, b = (x-1, y+2)
        if view_board[a][b] == "-" or "b" in view_board[a][b]: #used to be : "w" in view_board[a][b]:
            to_return.append((a, b))

    except:
        pass

    try:
        a, b = (x+1, y+2)
        if a > 0:
            if view_board[a][b] == "-" or "b" in view_board[a][b]:
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
        print "here 1"
        if new_y - 1 >= 0 and new_x - 1 >= 0:
            new_y -= 1
            new_x -= 1
            if view_board[new_x][new_y] == "-":
                to_return.append((new_x, new_y))

            else:
                to_return.append((new_x, new_y))
                break

        else:
            break



    new_y = y
    new_x = x

    while True:
        print "here 2"
        if new_y + 1 < 8 and new_x - 1 >= 0:
            new_y += 1
            new_x -= 1
            if view_board[new_x][new_y] == "-":
                to_return.append((new_x, new_y))

            else:
                to_return.append((new_x, new_y))
                break
        else:
            break


    new_y = y
    new_x = x

    while True:
        print "here 3"
        if new_y + 1  < 8 and new_x + 8 < 8:
            new_y += 1
            new_x += 1
            if view_board[new_x][new_y] == "-":
                to_return.append((new_x, new_y))
            else:
                to_return.append((new_x, new_y))
                break
        else:
            break

    new_y = y
    new_x = x

    while True:
        
        if new_y - 1 >= 0 and new_x + 1 < 8:
            new_y -= 1
            new_x += 1
            print (new_x, new_y)
            if view_board[new_x][new_y] == "-":
                to_return.append((new_x, new_y))
            else:
                to_return.append((new_x, new_y))
                break
        else:
            break




    #return to_return
    return [i for i in to_return if i != (x, y)]



def get_rook_moves(view_board, x, y):
    to_return = []

    for i in range(1, x):
        a, b = (x-i, y)

        if view_board[a][b] == "-":
            to_return.append((a, b))

        else:
            to_return.append((a, b))
            break

    for i in range(x, 8):
        a, b = (i, y)
        if view_board[a][b] == "-":
            to_return.append((a, b))

        else:
            to_return.append((a, b))
            break

    for i in range(y, 8):
        a, b = (x, i)
        if view_board[a][b] == "-":
            to_return.append((a, b))

        else:
            to_return.append((a, b))
            break

    for i in range(1, y):
        a, b = (x, y-i)
        if view_board[a][b] == "-":
            to_return.append((a, b))

        else:
            to_return.append((a, b))
            break

    return to_return


def get_queen_moves(view_board, x, y):
    ranks = get_rook_moves(view_board, x, y)
    diags = get_bishop_moves(view_board, x, y)

    return ranks + diags

def get_king_moves(self, x, y):
    to_return = []

    try:
        a = x+1
        b = y + 1
        if view_board[a][b] == "-":
            to_return.append((a, b))
    except:
        pass

    try:
        a = x+1
        b = y
        if view_board[a][b] == "-":
            to_return.append((a, b))
    except:
        pass

    try:
        a = x
        b = y + 1
        if view_board[a][b] == "-":
            to_return.append((a, b))
    except:
        pass

    try:
        a = x+1
        b = y + 1
        if view_board[a][b] == "-":
            to_return.append((a, b))
    except:
        pass

    try:
        if y - 1 < 0:
            a = x + 1
            b = y - 1

            if view_board[a][b] == "-":
                to_return.append((a, b))

    except:
        pass
    try:
        if y - 1 < 0:
            a = x
            b = y - 1
            if view_board[a][b] == "-":
                to_return.append((a, b))

    except:
        pass

    try:
        if x - 1 < 0:
            a = x - 1
            b = y + 1

            if view_board[a][b] == "-":
                to_return.append((a, b))

    except:
        pass

    try:
        if x - 1 < 0:
            a = x - 1
            b = y

            if view_board[a][b] == "-":
                to_return.append((a, b))

    except:
        pass
    return to_return
