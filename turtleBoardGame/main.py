import turtle as t

#wn setup
wn=t.Screen()
wn.title("Connect 4")
wn.bgcolor("deepskyblue1")
wn.setup(width=800,height=800)

#add shapes
wn.addshape("pvc.gif")
wn.addshape("pvp.gif")
wn.addshape("connect4.gif")
wn.addshape("redChip.gif")
wn.addshape("blueChip.gif")


#turtle setup
menu = t.Turtle()
pvc = t.Turtle("pvc.gif")
pvp = t.Turtle("pvp.gif")
connect4 = t.Turtle("connect4.gif")
redChip = t.Turtle("redChip.gif")
blueChip = t.Turtle("blueChip.gif")

#starting needs
applied = False
menu.speed(0)
menu.penup()
pvc.hideturtle()
pvc.penup()
pvp.hideturtle()
pvp.penup()
connect4.hideturtle()
redChip.penup()
redChip.hideturtle()
blueChip.penup()
blueChip.hideturtle()



def mainMenu():
    menu.goto(-200,250)
    menu.write("CONNECT 4", font=("Arial",50,"bold"))
    menu.fd(-10)
    menu.left(90)
    menu.color("goldenrod1")
    menu.pensize(5)
    menu.pendown()
    menu.fd(80)
    menu.right(90)
    menu.fd(410)
    menu.right(90)
    menu.fd(80)
    menu.right(90)
    menu.fd(410)
    pvc.goto(0,100)
    pvc.stamp()
    menu.penup()
    menu.right(180)
    menu.goto(-150,0)
    menu.pendown()
    menu.color("black")
    menu.fd(300)
    menu.hideturtle()
    pvp.goto(0,-100)
    pvp.stamp()
    connect4.penup()
    connect4.goto(0,-275)
    connect4.stamp()
    redChip.goto(-290,150)
    redChip.stamp()
    redChip.goto(-290,75)
    redChip.stamp()
    redChip.goto(-290,0)
    redChip.stamp()
    redChip.goto(-290,-75)
    redChip.stamp()
    blueChip.goto(290,150)
    blueChip.stamp()
    blueChip.goto(290,75)
    blueChip.stamp()
    blueChip.goto(290,0)
    blueChip.stamp()
    blueChip.goto(290,-75)
    blueChip.stamp()
    
    
    
mainMenu()
    
wn.mainloop()