import turtle
import random

# This class is for every individal tile
class Tile:
    COLS = ["cols/empty.gif","cols/white.gif","cols/black.gif","cols/red.gif","cols/orange.gif","cols/yellow.gif","cols/green.gif","cols/blue.gif","cols/indigo.gif","cols/violet.gif",]
    
    def __init__(self, colour, pos_x, pos_y, turtle):
        self.colour = self.COLS[colour]
        # pos_x and pos_y are used for finding the right colour inside the colour board
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.turtle = turtle

    def draw(self, board_cols):
        # Finds the current colour
        self.colour = self.COLS[board_cols[int(self.pos_y)][int(self.pos_x)]]
        # Puts it down and moves forwards
        self.turtle.shape(self.colour)
        self.turtle.stamp()
        self.turtle.forward(50)
        #print(f"drawn {self.colour}, {self.pos_x}, {self.pos_y}")


def main():
    # Instructions
    print("""Hello, welcome to my game! You are going to try to geuss my random series of colours.
R - red, O - orange, Y - yellow, G - green, B - blue, I - indigo, V - violet
In every line you will input a string of length 5 and i will reply whether:
White - the colour is in the right place, Black - There is this colour but it is in the wrong place or, Gray/Empty - This colour is not in my code""")

    # Getting a random secret
    secret = ""
    possible = "ROYGBIV"
    index = 0
    while index < 5:
        secret += possible[random.randint(0, 6)]
        index += 1

    # Making the turtle actually work
    img_turtle = turtle.Turtle()
    img_turtle.speed(0)
    img_turtle.penup()
    img_turtle.backward(100)

    # Defines a 2D array of emptyness
    board = [
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None,None,None,None]
    ]
    # Sets all the colours to the empty one
    board_cols = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
    ]

    # Loops through the colour files and then registers them as shapes
    for file in Tile.COLS:
        turtle.register_shape(file)

    # Fills the Board array with instances of tile with the colours within the colour array
    for row_i in range(len(board)):
        for tile_i in range(10):
            col = int(board_cols[row_i][tile_i])
            board[row_i][tile_i] = Tile(col, tile_i, row_i, img_turtle)
    
    # Draws the board to the screen
    draw_all(board, board_cols, img_turtle)

    done = False

    # Game loop
    for level in range(6):      
        # Gets a geuss and does a round on it            
        geuss = input("Input a geuss\n")
        out = round(secret, geuss)

        #print(board_cols)

        # Makes the geuss into a list of numbers corisponding to the colours
        geuss_list = [0,0,0,0,0]
        for index_g, letter in enumerate(geuss):
            poss = "ROYGBIV"
            for index, curr in enumerate(poss):
                if letter == curr:
                    geuss_list[index_g] = index + 3

        # Sets the colour board layer to the output of the round and the geuss
        board_cols[level] = out[1] + geuss_list
        draw_all(board, board_cols, img_turtle)

        # If the geuss was correct, break the loop and output the win message
        if out[0]:
            print("YOU WINNN")
            done = True
            break

    # If they do not geuss it correctly let them know
    if not done:
        print(f"Sorry, the code was {secret}")
    turtle.done()
        

def draw_all(board, board_cols, img_turtle):
    # Idk what the tracer does, i just know it makes it quick
    img_turtle._tracer(0, 0)
    # Loops through the board
    for row_i in range(len(board)):
        for tile_i in range(10):
            # Adds the gap inbetween the geuss and feedback
            if tile_i == 5:
                img_turtle.forward(25)
            # Draws each tile to the screen
            board[row_i][tile_i].draw(board_cols)

        # Resets the turtle to teh front of the line
        img_turtle.backward(525)
        img_turtle.left(90)
        img_turtle.forward(50)
        img_turtle.right(90)
        #print()

    # puts the turtle into the correct place for the next round
    img_turtle.right(90)
    img_turtle.forward(300)
    img_turtle.left(90)
    # Idk what this does, i just need it for the tracer thing
    img_turtle._update()

def round(SECRET, geuss):
    # Checks if the geuss was correct
    if geuss == SECRET:
        print("Well done! You geussed it!")
        line = [1,1,1,1,1]
        return (True, line)

    else:
        # Defines some things
        used_g = [False, False, False, False, False]
        used_s = [False, False, False, False, False]
        line = [0,0,0,0,0]
        index = 0

        # Loops through and checks for the correct places 
        while index < 5:
            if geuss[index] == SECRET[index]:
                used_g[index] = True
                used_s[index] = True
                line[index] = 1
            index += 1
        index = 0
        # Loops through and checks for the black tiles
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

        # Returns the line and a false to say it was not geussed
        return (False, line)

# Runs the damn thing!
main()
