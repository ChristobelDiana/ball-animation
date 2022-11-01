from tkinter import *

W, H = 600, 500
tk = Tk()
canvas = Canvas(tk,width=W,height=H)
canvas.pack()

class Ball:
    def __init__(self,size,speedx, speedy, color):
        self.ball = canvas.create_oval(0,0,size,size,fill=color)
        self.speedx = speedx
        self.speedy = speedy
        self.movement()

    def movement(self):
        canvas.move(self.ball,self.speedx,self.speedy)
        pos = canvas.coords(self.ball)
        if pos[2]>=W or pos[0]<=0:
            self.speedx *= -1
        if pos[3]>=H or pos[1]<=0:
            self.speedy *= -1
        tk.after(40,self.movement)

ball1 = Ball(100,3,3,'brown')
ball2 = Ball(75,4,3,'yellow')
ball3 = Ball(60,4,5,'green')
ball4 = Ball(90,5,5,'blue')
tk.mainloop()

