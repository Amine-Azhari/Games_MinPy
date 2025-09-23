import tkinter as tk

w = 7
h = 6

class Puissance_4:
    def __init__(self):
        self.grid = [['' for i in range(w)]for j in range(h)]
        self.window = tk.Tk()
        self.create_canvas()
        self.window.bind('<Escape>', lambda event: self.window.destroy())
        self.quit = tk.Button(self.window, text ='quit' ,command = lambda: self.window.destroy())
        self.quit.pack()
        self.window.mainloop()
    def create_canvas(self):
        self.h = 600
        self.w = 700
        self.game_over = False
        self.canvas = tk.Canvas(self.window, bg = 'blue', width = self.w, height = self.h)
        self.canvas.pack()
        self.turn = 0
        self.window.bind('<Button-1>',self.on_click)
        
        for i in range(7):
            for j in range(6):
                x = (i+0.5)*(self.w/w)
                y = (j+0.5)*(self.h/h)
                r = 40
                self.canvas.create_oval(x-r,y-r,x+r,y+r,outline ='black',fill='white')
    
    def player(self,turn):
        if turn %2 == 0 : return 'PLAYER_1'
        else : return 'PLAYER_2'
    
    def find_row(self,col,grid):
        row = h -1
        while grid[row][col] != '' and row>0:
            row -= 1
        return row 
        
    def win(self):
        s_1 = 0 
        s_2 = 0
        grid = self.grid
        for i in range(h-1, -1,-1):
            j = 0
            while j<w and (s_1< 4 and s_2 <4):
                if grid[i][j] == 'a': 
                    s_1 += 1
                    s_2 = 0
                elif grid[i][j] == 'b': 
                    s_1 = 0
                    s_2 += 1
                else: 
                    s_1 = 0
                    s_2 = 0
                j += 1
            if s_1 == 4 or s_2 == 4: return True

        s_1 = 0 
        s_2 = 0
        for j in range(w):
             i = h-1
             while i>=0 and (s_1< 4 and s_2 <4):
                 if grid[i][j] == 'a': 
                     s_1 += 1
                     s_2 = 0
                 elif grid[i][j] == 'b': 
                     s_1 = 0
                     s_2 += 1
                 else: 
                     s_1 = 0
                     s_2 = 0
                 i -= 1
             if s_1 == 4 or s_2 == 4: return True
        else : return False
        
        
    def on_click(self,event):
        if self.game_over: return
        grid = self.grid
        col = event.x//(self.w//w)
        row = self.find_row(col, grid)
        x = (col+0.5)*(self.w//w)
        y = (row+0.5)*(self.h//h)
        r = 40
        if grid[row][col] == '':
            if self.turn%2 == 0:
                self.canvas.create_oval(x-r,y-r,x+r,y+r,outline ='black',fill='red')
                grid[row][col]='a'
            else:
                self.canvas.create_oval(x-r,y-r,x+r,y+r,outline ='black',fill='orange')
                grid[row][col]='b'
                
            if self.win() : 
                self.label = tk.Label(self.window, font = 'Calibri',text = f'{self.player(self.turn)} is the winner')
                self.label.pack()
                self.game_over = True
                
            self.turn += 1
        
    """
    def on_click(self,event):
        if self.game_over: return
        grid = self.grid
        col = event.x//(self.w//w)
        row = self.find_row(col, grid)
        x = (col+0.5)*(self.w//w)
        y = (row+0.5)*(self.h//h)
        r = 40
        if grid[row][col] == '':
            if self.turn%2 == 0:
                self.canvas.create_oval(x-r,y-r,x+r,y+r,outline ='black',fill='red')
                self.turn += 1
                grid[row][col]='a'
                if self.win() : 
                    self.label = tk.Label(self.window, font = 'Calibri',text = f'{self.player(self.turn)} is the winner')
                    self.label.pack()
                    self.game_over == True
            else:
                self.canvas.create_oval(x-r,y-r,x+r,y+r,outline ='black',fill='orange')
                self.turn += 1
                grid[row][col]='b'
                if self.win() : 
                    self.label = tk.Label(self.window, font = 'Calibri',text =f'{self.player(self.turn)} is the winner')
                    self.label.pack()
                    self.game_over = True
                """


test = Puissance_4()