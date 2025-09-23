import tkinter as tk
import random as rd

class Pong:
    def __init__(self):
        
        self.window = tk.Tk()
        self.window.title('mouvement de la boule')
        self.w = 720
        self.h = 480
        self.canvas = tk.Canvas(self.window, bg ='black',width = self.w,height = self.h)
        self.canvas.pack()
            
        self.xc,self.yc = (self.w//2,self.h//2)
        self.size = 30
        coordinates = self.w//2,0,self.w//2,self.h
        self.canvas.create_line(coordinates,fill ='white', dash=(5,1))
        self.ball = self.canvas.create_oval(self.xc-self.size//2,self.yc-self.size//2,self.xc+self.size//2,
                                       self.yc+self.size//2,outline ='orange' , fill='red')
        self.gk1 = self.canvas.create_rectangle(self.w -20,self.h//2 + 40,self.w -10,self.h//2 - 40, 
                                           fill = 'cyan')
        self.gk2 = self.canvas.create_rectangle(10,self.h//2 + 40,20,self.h//2 - 40, 
                                           fill = 'cyan')
        
        self.score1 = 0
        self.score2 = 0
        
        self.score_1 = self.canvas.create_text(self.w//4,40, font = 'Calibri',
                                              text = f'Player_1: {self.score1} ', fill='white')
        self.score_2 = self.canvas.create_text(3*self.w//4,40, font = 'Calibri',
                                              text = f'{self.score2} :Player_2', fill='white')
        self.leave = tk.Button(self.window, text = 'Leave',command = self.window.destroy )
        self.leave.pack()
        
        self.window.bind('<Up>',self.move_up1)
        self.window.bind('<Down>',self.move_down1)
        self.window.bind('<a>',self.move_up2)
        self.window.bind('<q>',self.move_down2)
        self.window.bind('<A>',self.move_up2)
        self.window.bind('<Q>',self.move_down2)
        self.window.bind('<Escape>',self.quitt)
        self.dx,self.dy = rd.choice([(2,2),(-2,2),(-2,-2),(2,-2)])
        self.move_ball()
        self.label = tk.Label(self.window, font = 'Calibri',
                               text = 'Use ↑/↓ and a/q to move (Esc to quit)')
        self.label.pack()
        self.window.mainloop()
    
    def move_ball(self):
        self.canvas.move(self.ball,self.dx,self.dy)
        coords_ball = self.canvas.coords(self.ball)
        coords_gk1 = self.canvas.coords(self.gk1)
        coords_gk2 = self.canvas.coords(self.gk2)
        if coords_ball[3]>=self.h or coords_ball[1]<=0: self.dy= -self.dy
        if coords_ball[2]>=coords_gk1[0] :
            if coords_gk1[1]<=coords_ball[1]<=coords_gk1[3]\
                or coords_gk1[1]<=coords_ball[3]<=coords_gk1[3]:
                    self.dx = -abs(self.dx +1)
            else: 
                self.reset_2()
        if coords_ball[0]<=coords_gk2[2] :
            if coords_gk2[1]<=coords_ball[1]<=coords_gk2[3]\
                or coords_gk2[1]<=coords_ball[3]<=coords_gk2[3]:
                    self.dx = -self.dx +1
            else: 
                self.reset_1()
        
        self.window.after(10,self.move_ball)

    def reset_1(self):
        self.canvas.coords(self.ball,
                           self.xc-self.size//2,
                           self.yc-self.size//2,
                           self.xc+self.size//2,
                           self.yc+self.size//2)
        self.score2 += 1
        self.canvas.itemconfig(self.score_2, text= f'{self.score2} :Player_2')
        self.dx,self.dy = rd.choice([(2,2),(-2,2),(-2,-2),(2,-2)])
    
    def reset_2(self):
        self.canvas.coords(self.ball,
                                         self.xc-self.size//2,
                                         self.yc-self.size//2,
                                         self.xc+self.size//2,
                                         self.yc+self.size//2)
        self.score1 += 1
        self.canvas.itemconfig(self.score_1, text= f'Player_1: {self.score1}')
        self.dx,self.dy = rd.choice([(2,2),(-2,2),(-2,-2),(2,-2)])
        
    def move_up1(self,event):
        coords_gk1 = self.canvas.coords(self.gk1)
        self.canvas.move(self.gk1, 0, -20)
        coords_gk1[1] -= 20
        coords_gk1[3] -= 20
    def move_down1(self,event):
        coords_gk1 = self.canvas.coords(self.gk1)
        self.canvas.move(self.gk1, 0, 20)
        coords_gk1[1] += 20
        coords_gk1[3] += 20
    def move_up2(self,event):
        coords_gk2 = self.canvas.coords(self.gk2)
        self.canvas.move(self.gk2, 0, -20)
        coords_gk2[1] -= 20
        coords_gk2[3] -= 20
    def move_down2(self,event):
        coords_gk2 = self.canvas.coords(self.gk2)
        self.canvas.move(self.gk2, 0, 20)
        coords_gk2[1] += 20
        coords_gk2[3] += 20
    def quitt(self,event):
        self.window.destroy()
    
    
    
pong = Pong()
pong.move_ball()