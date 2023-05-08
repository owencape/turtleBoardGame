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
# wn.addshape("stack.gif")
# wn.addshape("youTube.gif")


#turtle setup
menu = t.Turtle()
pvc = t.Turtle("pvc.gif")
pvp = t.Turtle("pvp.gif")
connect4 = t.Turtle("connect4.gif")
redChip = t.Turtle("redChip.gif")
blueChip = t.Turtle("blueChip.gif")
# stack = t.Turtle("stack.gif")
# youTube = t.Turtle("youTube.gif")

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
    
def credits():
    #clearing marks
    menu.clear()
    pvc.clear()
    pvp.clear()
    connect4.clear()
    redChip.clear()
    blueChip.clear()
    # #chip border
    # #top row
    # change=-300
    # redChip.penup()
    # blueChip.penup()
    # redChip.goto(-340,340)
    # redChip.stamp()
    # blueChip.goto(-320,340)
    # for x in range(10):
    #     blueChip.pendown()
    #     blueChip.stamp()
    #     blueChip.penup()
    #     change+=35
    #     redChip.penup()
    #     redChip.goto(change,340)
    #     redChip.pendown()
    #     redChip.stamp()
    #     change += 35
    #     blueChip.goto(change,340)
    # #bottom row
    # change=-300
    # redChip.penup()
    # blueChip.penup()
    # redChip.goto(-340,-340)
    # redChip.stamp()
    # blueChip.goto(-320,-340)
    # for x in range(10):
    #     blueChip.pendown()
    #     blueChip.stamp()
    #     blueChip.penup()
    #     change+=35
    #     redChip.penup()
    #     redChip.goto(change,-340)
    #     redChip.pendown()
    #     redChip.stamp()
    #     change += 35
    #     blueChip.goto(change,-340)
    #text
    menu.goto(-150,200)
    menu.color("goldenrod1")
    menu.write("CREDITS", font=("Arial",50,"bold"))
    menu.penup()
    menu.goto(-90,165)
    menu.write("Authors:", font=("Verdana",25,"bold"))
    menu.penup()
    menu.goto(-160,130)
    menu.write("Owen Cape & Ty Tichenor", font=("Times New Roman",20,"bold"))
    menu.penup()
    menu.goto(-125,0)
    menu.write("Sources:", font=("Arial",40,"bold"))
    #logos
    # stack.pendown()
    # stack.goto(-175,-100)
    # stack.stamp()
    # stack.hideturtle()
    # youTube.pendown()
    # youTube.goto(0,-100)
    # youTube.stamp()
    # youTube.hideturtle()
    
        
        
        
    

    
    
# credits()
mainMenu()
    
wn.mainloop()