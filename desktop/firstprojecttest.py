#Author: Sina Sadeghi, Top Brains Team
#Special thanks to God
import turtle
import time
import math
from random import randint
wn = turtle.Screen()
wn.title("Top Brains first test application(Developed by Sina Sadeghi)")
MTIME = 6;
WIDTH, HEIGHT = 0.99, 0.99
COLORS = ["#DB6413", "red", "#3A3838", "#548135", "#833C0B", "#002060", "#92D050", "#5b9bd5"]
IS_WAIT = False
circlers = []
for i in range(9):
    circler = turtle.Turtle()
    circler.speed('fastest')
    circler.pu()
    circler.pen(shown=False)
    circlers.append(circler)
trueCircle = 0
results = []
wn.setup(width=WIDTH, height=HEIGHT, startx=1, starty=-1)
RWIDTH, RHEIGHT = wn.window_width()/2-50, wn.window_height()/2-50
bob = turtle.Turtle()
bob.speed('fastest') #bob tabler :)
bob.pu()
bob.pen(shown=False) #hide bob the tabler turtle
texter = turtle.Turtle()
texter.pen(shown=False)
texter.speed('fastest')
texter.pu()

wn.tracer(False) #Turtle becomes MUCH Faster

def square(side):
    for i in range(4):
        bob.forward(side)
        bob.left(90)

def row(n, side):
    for i in range(n):
        square(side)
        bob.forward(side)
    bob.penup()
    bob.left(180)
    bob.forward(n * side)
    bob.left(180)
    bob.pendown()

def row_of_rows(m, n, side):
    for i in range(m):
        row(n, side)
        bob.penup()
        bob.left(90)
        bob.forward(side)
        bob.right(90)
        bob.pendown()
    bob.penup()
    bob.right(90)
    bob.forward(m * side)
    bob.left(90)
    bob.pendown()

def createGrid():
    bob.goto(-RWIDTH, -RHEIGHT)
    bob.pd()
    row_of_rows(12, 21, RWIDTH/12)

def writeOnPage(text):
    texter.clear()
    texter.pu()
    texter.goto(3 * RWIDTH/4 +10, 0)
    texter.pd()
    texter.write(text, font=("Arial", 16, "normal", "bold"))
    texter.pu()

def startTimer():
    global MTIME
    for i in reversed(range(MTIME)):
        texter.clear()
        texter.pu()
        texter.goto(0, 0)
        texter.pd()
        if i > 1:
            texter.write(i, font=("Arial", 24, "normal", "bold"))
        else:
            texter.write("GO", font=("Arial", 24, "normal", "bold"))
        time.sleep(1)
        if i == 0:
            texter.clear()

def isInCircle(x, y):
    global circlers
    for i in circlers:
        if i.distance(x, y) < RWIDTH/6:
            return True
    return False

def handleClickCircle(x, y):
    global results
    print('Hi')
    results.append(circlers[trueCircle].distance(x, y) <= RWIDTH/12)
    wn.onclick(None)
    IS_WAIT = False
    RESULT_AVAILABLE.set()

def createCircles():
    global COLORS, circlers, trueCircle
    for i in range(8):
        circlers[i].fillcolor(COLORS[i])
        x = randint(int(-RWIDTH + RWIDTH/24),  int(RWIDTH/2 - RWIDTH/12))
        y = randint(int(-RHEIGHT), int(RHEIGHT - RWIDTH/4)) + RWIDTH/12
        while isInCircle(x, y):
            x = randint(int(-RWIDTH),  int(RWIDTH/2 - RWIDTH/12))
            y = randint(int(-RHEIGHT), int(RHEIGHT - RWIDTH/6))+RWIDTH/12
        circlers[i].goto(x, y - RWIDTH/12)
        circlers[i].begin_fill()
        circlers[i].pd()
        circlers[i].circle(RWIDTH/12)
        circlers[i].end_fill()
        circlers[i].pu()
        circlers[i].goto(x, y)
    wn.update()
    time.sleep(1.48)
    for i in range(8):
        circlers[i].clear()
    randomCircles = []
    for i in range(4):
        cid = randint(0, 7)
        while cid in randomCircles:
            cid = randint(0, 7)
        randomCircles.append(cid)
    trueCircle = randint(0, 3)
    
    circlers[8].goto(3 * RWIDTH/4 + RWIDTH/6, -RHEIGHT)
    circlers[8].fillcolor(circlers[randomCircles[trueCircle]].fillcolor())
    circlers[8].begin_fill()
    circlers[8].pd()
    circlers[8].circle(RWIDTH/12)
    circlers[8].end_fill()
    circlers[8].pu()
    writeOnPage("Select the circle\nwith the color\nbelow")
    for r in range(len(randomCircles)):
        i = randomCircles[r]
        circlers[i].goto(circlers[i].xcor(), circlers[i].ycor()-RWIDTH/12)
        circlers[i].pd()
        circlers[i].circle(RWIDTH/12)
        circlers[i].pu()
        circlers[i].goto(circlers[i].xcor(), circlers[i].ycor()+RWIDTH/12)
        circlers[i].pd()
        circlers[i].write(r+1, font=("Arial", 24, "normal"))
        circlers[i].pu()
        
    wn.update()
        
    #IS_WAIT = True
    #wn.numinput('Hi', 'Are you Ok?')
    
def cleanCirclers():
    for circler in circlers:
        circler.clear()
        circler.goto(-WIDTH, -HEIGHT)

def mymain():
    global results
    results = []
    turtle.onkey(None, 'space')
    turtle.listen()
    tests = wn.numinput('Welcome to our test!', 'Enter the number of tests:')
    while tests == None or tests < 1:
        tests = wn.numinput('Welcome to our test!', 'Enter the number of tests:')
    tests = int(tests) 
    startTimer()
    createGrid()

    for t in range(tests):
        #IS_WAIT = True
        #taskqueue = deque()
        #taskqueue.append(createCircles())
        #task = taskqueue.pop()
        #while IS_WAIT:
        #    time.sleep(1)
        #wn.numinput('Hi', 'Are you Ok?')
        createCircles()
        userCircle = wn.numinput("Neuroscience project", "Enter the number of the circle you want")
        while userCircle == None or userCircle > 4:
            userCircle = wn.numinput("Neuroscience project", "Enter the number of the circle you want")    
        results.append(userCircle-1 == trueCircle)
        cleanCirclers()
        #turtle.onclick(handleClickCircle)
        #RESULT_AVAILABLE.wait()

    bob.clear()
    texter.clear()
    texter.pu()
    texter.goto(-RWIDTH/3, -RHEIGHT)
    texter.pd()
    txtResult = "Result:\n"
    for i in range(int(math.floor(len(results)/2))):
        txtResult += "Test " + str(2*i+1) + ": " + str(results[2*i]) + "\t"
        if 2*i+1 != len(results):
            txtResult += "Test " + str(2*i+2) + ": " + str(results[2*i+1])
        txtResult += "\n"
    txtResult += "Developed by Sina Sadeghi\nSina.Sadeghi83@gmail.com\nTop Brains Team\nFor exit press space\nFor again test press a"
    texter.write(txtResult, font=("Arial", 18, "normal"))
    texter.pu()
    turtle.onkey(turtle.bye, 'space')
    turtle.onkey(mymain, 'a')
    turtle.listen()
    

texter.pu()
texter.goto(-RWIDTH/4, 0)
texter.pd()
texter.write("Welcome to our test.\nPress space to start\nDeveloped by Sina Sadeghi\nSina.Sadeghi83@gmail.com\nTop Brains Team", font=("Arial", 24, "normal"))
texter.pu()
turtle.listen()
turtle.onkey(mymain, 'space')
turtle.mainloop()
