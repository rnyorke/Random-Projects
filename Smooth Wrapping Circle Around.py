from Tkinter import * 
root = Tk()
# Setting the scene
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=0)
# Creating the circles
circle = drawpad.create_oval(10, 10, 50, 50, fill='blue')
circle2 = drawpad.create_oval(-40, 10, 0, 50, fill='blue')
# Setting speeds
direction = 2
velocity = 0
# Creating animation function
def animate():
    global direction
    global velocity
    # Getting x and y coords of circles
    x1, y1, x2, y2 = drawpad.coords(circle)
    x3, y3, x4, y4 = drawpad.coords(circle2)
    # Making the circle wrap around smoothly
    if x2 > 840: 
        direction = 0
        drawpad.move(circle,-841,0)
        velocity = 2
    if x4 > 840:
        direction = 2
        drawpad.move(circle2,-841, 0 )
        velocity = 0
    # Making the circles move smoothly
    drawpad.move(circle,direction,0)
    drawpad.move(circle2,velocity,0)
    # Waiting then recalling the function
    drawpad.after(1, animate)
# Making the animation work :)
animate()
root.mainloop()
