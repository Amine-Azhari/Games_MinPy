import tkinter as tk
import random as rd

WIDTH = 300
HEIGHT = 600
SIZE = 30
PERIODE = 600
BG_COLOR = "#1f1e55"
COLORS =  ["#E73C53", "#F9B738", "#B068F6",
           "#C7CBD3", "#19DFEA", "#4AE16A",
           "#FBE43D" ]
FIGURES  = [
    [(-1, 1), (-2, 1), (0, 1), (1, 1)],
    [(0, 0), (-1, 0), (-1, 1), (0, 1)],
    [(-1, 0), (0, -1), (0, 0), (-1, 1)],
    [(0, 0), (-1, 0), (-1, -1), (0, 1)],
    [(0, 0), (0, -1), (-1, -1), (0, 1)],
    [(0, 0), (0, -1), (1, -1), (0, 1)],
    [(0, 0), (0, -1), (-1, 0), (0, 1)]]

score = 0 
direction = None
rotation = False
grid = [['0' for i in range(WIDTH//SIZE)] for j in range(HEIGHT//SIZE)]

class Tetris:
    def __init__(self):
        self.figure = rd.choice(FIGURES)
        self.color = rd.choice(COLORS)
        self.squares = []
        for x,y in self.figure:
            xc = x * SIZE + WIDTH//2
            yc = y * SIZE  + 2 * SIZE
            square = canvas.create_rectangle(xc ,yc , xc + SIZE, yc + SIZE, fill= self.color, tag = "tetris")
            self.squares.append(square)

def next_turn(tetris):
    global grid
    figure = tetris.figure.copy()
    color = tetris.color

    def move(tetris):
        nonlocal figure  
        global direction
        global rotation
        stop = False
        new_figure = []
        #print("figure: ", figure)

        # Rotate
        if rotation: 
            test_figure = rotate(figure)
            can_rotate = True
            for x,y in test_figure:
                x_grid = x + WIDTH // (2 * SIZE)
                y_grid = y + 3 
                if not ( 0 <= x_grid <= WIDTH // SIZE and 0 <= y_grid <= HEIGHT // SIZE) or grid[y_grid][x_grid] == '1':
                    can_rotate = False
                    break
            if can_rotate:
                figure = test_figure
            rotation = False

        for i in range(4):
            x, y = figure[i]
            # move x
            if direction == 'right' and x + 1 < WIDTH // SIZE // 2:
                x += 1
            elif direction == 'left' and x - 1 >= -WIDTH // SIZE // 2:
                x -= 1

            new_figure.append((x, y))

        figure = new_figure
        direction = None

        # move y attempt
        for x, y in figure:
            x_grid = x + WIDTH // (2 * SIZE)
            y_grid = y + 3  # +2 pour décalage initial, +1 pour voir dessous
            if y_grid >= HEIGHT // SIZE or grid[y_grid][x_grid] == '1':
                stop = True
                break

        if not stop:
            new_figure = []
            for i in range(4):
                x, y = figure[i]
                x_canvas = x * SIZE + WIDTH // 2
                y_canvas = (y + 1) * SIZE + 2 * SIZE
                canvas.delete(tetris.squares[i])
                tetris.squares[i] = canvas.create_rectangle(x_canvas, y_canvas, x_canvas + SIZE, y_canvas + SIZE, fill=color)
                new_figure.append((x, y + 1))
            figure = new_figure
            window.after(PERIODE, move, tetris)

        else:
            for i in range(4):
                x, y = figure[i]
                grid_x = x + WIDTH // (2 * SIZE)
                grid_y = y + 2
                grid[grid_y][grid_x] = '1'
            next_turn(Tetris())

    move(tetris)

        
"""
def next_turn(tetris):
    global grid
    figure = tetris.figure.copy()
    color = tetris.color
    def move(tetris):

        ycf = max(figure[0][1],figure[1][1],figure[2][1],figure[3][1]) + 2 
        xcf_max = max(figure[0][0],figure[1][0],figure[2][0],figure[3][0])* SIZE + WIDTH//2
        xcf_min = min(figure[0][0],figure[1][0],figure[2][0],figure[3][0])* SIZE + WIDTH//2

        global direction
        if direction:
            for i in range(4):
                    x,y = figure[i]
                    xc = x * SIZE + WIDTH//2
                    yc = y * SIZE  + 2 * SIZE
                    #move x
                    if direction == 'right':
                        if ycf <= HEIGHT//SIZE - 4 and xcf_max < WIDTH - SIZE:
                            xc += SIZE
                            x += 1
                    elif direction == 'left':
                        if ycf <= HEIGHT//SIZE - 4 and xcf_min >= SIZE:
                            xc -= SIZE
                            x -= 1
                    figure[i] = x,y
                    canvas.delete(tetris.squares[i])
                    del tetris.squares[i]
                    square = canvas.create_rectangle(xc ,yc , xc + SIZE, yc + SIZE, fill= color, tag = "tetris")
                    tetris.squares.insert(i, square)


        if ycf <= HEIGHT//SIZE - 2 :
            for i in range(4):
                x,y = figure[i]
                xc = x * SIZE + WIDTH//2
                yc = y * SIZE  + 2 * SIZE
                #move y
                print(grid[y+3][x + WIDTH//(2* SIZE)])
                if grid[y+4][x + WIDTH//(2* SIZE)]=='0':
                    if direction == 'down':
                        yc += 2*SIZE
                        y += 2
                    else : 
                        yc += SIZE
                        y += 1
                    figure[i] = x,y
                    canvas.delete(tetris.squares[i])
                    del tetris.squares[i]
                    square = canvas.create_rectangle(xc ,yc , xc + SIZE, yc + SIZE, fill= color, tag = "tetris")
                    tetris.squares.insert(i, square)
                else: break
            window.after(PERIODE, move, tetris)
        else : 
            for i in range(4):
                x,y = figure[i]
                xc = x + WIDTH//(2* SIZE)
                yc = y + 2
                grid[yc][xc] = "1"
            window.after(0, lambda: next_turn(Tetris()))


        direction = None
    move(tetris)
""" 

def change_direction(new_direction):
    global direction
    if new_direction == 'right':
        direction = new_direction
    elif new_direction == 'left':
        direction = new_direction
    elif new_direction == 'down':
        direction = new_direction


def rotate_condition():
    global rotation
    rotation = True


def rotate(figure):
    xi_0, yi_0 = figure[0]
    new_figure = []
    for x,y in figure:
        x -= xi_0
        y -= yi_0 
        x, y = y, -x 
        x += xi_0
        y += yi_0
        new_figure.append((x,y))
    figure = new_figure
    return figure

        

window = tk.Tk()

canvas = tk.Canvas(window, bg= BG_COLOR, width=WIDTH, height=HEIGHT)
canvas.pack()

label = tk.Label(window, text=f"SCORE : {score}")
label.pack()

window.bind("<Right>", lambda event: change_direction('right'))
window.bind("<Left>", lambda event: change_direction('left'))
window.bind("<Down>", lambda event: change_direction('down'))
window.bind("<Escape>", lambda event: window.destroy())
window.bind("<a>", lambda event: rotate_condition())

tetris = Tetris()

next_turn(tetris)

window.mainloop()