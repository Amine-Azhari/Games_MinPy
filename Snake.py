import tkinter as tk
import random as rd

WIDTH = 600
HEIGHT = 600
SIZE = 25
PERIODE = 50
BODY_SIZE = 4
BG_COLOR = "#8da259"
SNAKE_COLOR = "#2c311d"
SCORE = 0
direction = "right"


class Snake:
    def __init__(self):
        self.score = SCORE
        self.cordinates = [(0,0) for i in range(BODY_SIZE)]
        self.squares = []

        for x,y in self.cordinates :
            square = canvas.create_rectangle(x,y,x + SIZE, y + SIZE, fill=SNAKE_COLOR, tag= 'snake')
            self.squares.append(square)



class Food:
    def __init__(self):
        xf = rd.randint(0,(WIDTH // SIZE)-1) * SIZE
        yf = rd.randint(0,(HEIGHT // SIZE)-1) * SIZE

        self.cordinates = (xf,yf)

        canvas.create_oval(xf,yf,xf + SIZE, yf + SIZE, fill = SNAKE_COLOR, tag = 'food')
        



def next_turn(snake, food):
    
    xh, yh = snake.cordinates[0] 
    xf, yf = food.cordinates

    if direction == 'down':
        yh += SIZE
    elif direction == 'up':
        yh -= SIZE
    elif direction == 'left':
        xh -= SIZE
    elif direction == 'right':
        xh += SIZE
    
    if xh<0 : 
        xh = WIDTH - SIZE
    elif xh>WIDTH:
        xh = 0
    if yh<0 : 
        yh = HEIGHT - SIZE
    elif yh> HEIGHT:
        yh = 0

    snake.cordinates.insert(0,(xh,yh))
    square = canvas.create_rectangle(xh,yh,xh + SIZE, yh + SIZE, fill=SNAKE_COLOR, tag= 'snake')
    snake.squares.insert(0,square)    

    if xh == xf and yh == yf:
        snake.score += 1
        label.config(text=f"SCORE : {snake.score}")

        canvas.delete("food")
        food = Food()

    else:
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]
        del snake.cordinates[-1]

    window.after(PERIODE,next_turn,snake, food)



def change_direction(new_direction):
    global direction
    if new_direction == 'down':
        if direction != 'up':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'left':
        if direction != 'right':
            direction = new_direction


window = tk.Tk()

canvas = tk.Canvas(window, bg=BG_COLOR, height=HEIGHT, width= WIDTH, )
canvas.pack()

snake = Snake()
food = Food()

label = tk.Label(window, text=(f"SCORE : {snake.score}"))
label.pack()

window.bind("<Up>", lambda event:change_direction('up'))
window.bind("<Down>", lambda event:change_direction('down'))
window.bind("<Right>", lambda event:change_direction('right'))
window.bind("<Left>", lambda event:change_direction('left'))

next_turn(snake,food)

window.mainloop()
