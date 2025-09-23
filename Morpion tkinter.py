import tkinter as tk
import numpy as np

class Morpion:
    def __init__(self):
        self.window = tk.Tk()
        self.create_canvas()
        self.window.bind('<Escape>',lambda event : self.window.destroy())
        
        
        #self.label.config(text = f'Turn {self.turn + 1}: {self.player(self.turn)} win: {self.win()}')
                          
        self.window.mainloop()
    
    def create_canvas(self):
            self.w = 500
            self.h = 500
            self.canvas = tk.Canvas(self.window,bg = 'white', width= self.w, height = self.h)
            self.canvas.pack()
            self.canvas.create_line(self.w//3,0,self.w//3,self.h, fill='black',width = 4)
            self.canvas.create_line(2*self.w//3,0,2*self.w//3,self.h, fill='black',width = 4)
            self.canvas.create_line(0,self.h//3,self.w,self.h//3, fill='black',width = 4)
            self.canvas.create_line(0,2*self.h//3,self.w,2*self.h//3, fill='black',width = 4)
            self.leave = tk.Button(self.window, text = 'leave', command= lambda :self.window.destroy())
            self.leave.pack()
            self.new = tk.Button(self.window, text = 'New game', command= lambda :self.new_game())
            self.new.pack()
            self.grid = np.array([['' for i in range(3)] for j in range(3)])
            self.turn = 0
            self.window.bind('<Button-1>',self.on_click)
            self.label = tk.Label(self.window, font = 'Calibri',text = f'Turn {self.turn+1}: {self.player(self.turn)}')
            self.label.pack()
            self.game_over = False
            
    def new_game(self):
        self.turn = 0
        #destroy all widgets in the window so we can create new ones
        for widget in self.window.winfo_children():
            widget.destroy()
        self.create_canvas()
        for i in range(3):
            for j in range(3):
                self.grid[i,j] = '' 
                
    def win(self): 
        grid = self.grid
        for i in range(3):
            if grid[i,0] == grid[i,1] == grid[i,2] and grid[i,0]!='' : return True
        for j in range(3):
            if grid[0,j] == grid[1,j] == grid[2,j] and grid[0,j]!='' : return True
        
        if grid[0,0] == grid[1,1] == grid[2,2] and grid[0,0]!='' : return True 
        if grid[2,0] == grid[1,1] == grid[0,2] and grid[2,0]!='' : return True
        else: return False
    
    def player(self,turn):
        if turn %2 == 0 : return 'PLAYER_X'
        else : return 'PLAYER_O'
        
    def create_shape(self,turn,x,y):
        if turn%2 == 0:
            self.canvas.create_text(x,y,font =('Calibri',40), text= 'X',fill = 'black')
        else :
            self.canvas.create_text(x,y,font =('Calibri',40), text= 'O',fill = 'black')
        
    
    def on_click(self,event):
        if self.game_over :
            return
        row = event.y//(self.w//3)
        col = event.x//(self.h//3)
        
        
        x = (col * self.w//3) + self.w//6
        y = (row * self.h//3) + self.h//6
        
        if self.grid[row][col] == '':
            if self.turn%2 == 0:
                self.grid[row,col] = 'x'
            else: self.grid[row,col] = 'o'
            self.create_shape(self.turn,x,y)

        
            if self.win():
                self.label.config(text = f"{self.player(self.turn-1)} is the winner!")
                self.game_over = True
                return
        
            self.turn += 1
            self.label.config(text = f'Turn {self.turn + 1}: {self.player(self.turn)} win: {self.win()}')
            
            if self.turn == 9:
                self.label.config(text = "Tie")
            
    """
    def on_click(self,event):
        row = event.y//(self.w//3)
        col = event.x//(self.h//3)
        
        
        x = (col * self.w//3) + self.w//6
        y = (row * self.h//3) + self.h//6
        if self.win() == True and  self.turn <=9 :
            self.label.config(text = f"{self.player(self.turn-1)} is the winner!")
        elif self.win() == False :
            if self.turn<=9:
                if self.grid[row][col] == '':
                    if self.turn%2 == 0:
                        self.grid[row,col] = 'x'
                    else: self.grid[row,col] = 'o'
                    self.create_shape(self.turn,x,y)
                    self.turn += 1
                    self.label.config(text = f'Turn {self.turn + 1}: {self.player(self.turn)} win: {self.win()}')
        elif self.turn <=9 :
                 self.label.config(text = f"{self.player(self.turn-1)} is the winner!")
        else:
                 self.label.config(text = "Tie")
                 """
    
            
    








a = Morpion()