from Tkinter import *
root = Tk()
drawpad = Canvas(root, width = 800, height = 600, background = "white")
drawpad.grid(row=0, column=0)

circle = drawpad.create_oval(300, 500, 400, 600, fill = "blue")
xdirection = 1
ydirection = 2
def animate():
    global xdirection
    global ydirection
    x1,y1,x2,y2 = drawpad.coords(circle)
    if x2 > 800:
        xdirection = -2
    if x1 < 0:
        xdirection = 2
    if y2 > 600:
        ydirection = -2
    if y1 < 0:
        ydirection = 2
    drawpad.move(circle,xdirection,ydirection)
    drawpad.after(1, animate)
animate()
root.mainloop()