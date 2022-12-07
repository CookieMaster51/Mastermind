import turtle
import random


class Tile:
    COLS = ["cols/empty.gif","cols/white.gif","cols/black.gif","cols/red.gif","cols/orange.gif","cols/yellow.gif","cols/green.gif","cols/blue.gif","cols/indigo.gif","cols/violet.gif",]
    
    def __init__(self, colour, pos_x, pos_y, turtle):
        self.colour = self.COLS[colour]
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.turtle = turtle

    def draw(self, board_cols):
        self.colour = self.COLS[board_cols[int(self.pos_y)][int(self.pos_x)]]
        self.turtle.shape(self.colour)
        self.turtle.stamp()
        self.turtle.forward(50)
        #print(f"drawn {self.colour}, {self.pos_x}, {self.pos_y}")


def main():
    print("""Hello, welcome to my game! You are going to try to geuss my random series of colours.
R - red, O - orange, Y - yellow, G - green, B - blue, I - indigo, V - violet
In every line you will input a string of length 5 and i will reply whether:
White - the colour is in the right place, Black - There is this colour but it is in the wrong place or, Gray/Empty - This colour is not in my code""")

    secret = ""
    possible = "ROYGBIV"
    index = 0
    while index < 5:
        secret += possible[random.randint(0, 6)]
        index += 1

    img_turtle = turtle.Turtle()
    img_turtle.speed(0)
    img_turtle.penup()
    img_turtle.backward(100)

    board = [
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None]
    ]
    board_cols = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
    ]

    for file in Tile.COLS:
        turtle.register_shape(file)

    for row_i in range(len(board)):
        for tile_i in range(10):
            col = int(board_cols[row_i][tile_i])
            board[row_i][tile_i] = Tile(col, tile_i, row_i, img_turtle)
    
    draw_all(board, board_cols, img_turtle)

    
    done = False

    for level in range(6):                  
        geuss = input("Input a geuss\n")
        out = round(secret, geuss)

        #print(board_cols)

        geuss_list = [0,0,0,0,0]
        for index_g, letter in enumerate(geuss):
            poss = "ROYGBIV"
            for index, curr in enumerate(poss):
                if letter == curr:
                    geuss_list[index_g] = index + 3

        board_cols[level] = out[1] + geuss_list
        draw_all(board, board_cols, img_turtle)

        if out[0]:
            print("YOU WINNN")
            done = True
            break

    if not done:
        print(f"Sorry, the code was {secret}")
    turtle.done()
        

def draw_all(board, board_cols, img_turtle):
    for row_i in range(len(board)):
        for tile_i in range(10):
            if tile_i == 5:
                img_turtle.forward(25)
            board[row_i][tile_i].draw(board_cols)

        img_turtle.backward(525)
        img_turtle.left(90)
        img_turtle.forward(50)
        img_turtle.right(90)
        #print()

    img_turtle.right(90)
    img_turtle.forward(300)
    img_turtle.left(90)

def round(SECRET, geuss):
    #geuss = input("Input a geuss\n")
    if geuss == SECRET:
        print("Well done! You geussed it!")
        line = [1,1,1,1,1]
        return (True, line)
    else:
        used_g = [False, False, False, False, False]
        used_s = [False, False, False, False, False]
        line = [0,0,0,0,0]
        index = 0
        while index < 5:
            if geuss[index] == SECRET[index]:
                used_g[index] = True
                used_s[index] = True
                line[index] = 1
            index += 1
        index = 0
        while index < 5:
            if not used_g[index]:
                index_s = 0
                brek = False
                while index_s < 5 and not brek:
                    if geuss[index] ==  SECRET[index_s] and not used_s[index_s]:
                        used_g[index] = True
                        used_s[index_s] = True
                        line[index] = 2
                        brek = True
                        
                    index_s += 1
            index += 1

        return (False, line)

main()
