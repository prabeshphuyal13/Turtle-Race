import turtle
import random

RACERS = 5
WIDTH , HEIGHT = 500 ,550
FINISH_LINE = int((HEIGHT/2)*0.9)
START_LINE = -int((HEIGHT/2)*0.9)
COLORS = ['red', 'green', 'blue', 'yellow', 'pink', 'cyan']

def f():
    pass

def init_screen():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle Racing!")
    screen.bgpic("bg.png")
    screen.bgcolor("grey")
    screen.onkey(f, "Up")
    screen.listen()


def start_finish_line():

    finish_line = turtle.Turtle()
    finish_line.pensize(2) 
    finish_line.pencolor("white") 
    finish_line.speed(5)
    finish_line.hideturtle()  
    finish_line.teleport(-WIDTH/2, FINISH_LINE)  
    finish_line.forward(WIDTH)
    
    start_line = turtle.Turtle()
    start_line.pensize(2)
    start_line.pencolor("white") 
    start_line.speed(5)
    start_line.hideturtle()  
    start_line.teleport(WIDTH/2, START_LINE)  
    start_line.backward(WIDTH) 

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('Enter the number of racers (2 - 6): ')
        if racers.isdigit() and 2 <= int(racers) <= 6 :
            racers = int(racers)
            break
        else:
            print('Invalid input... Try Again!')
            continue
    return racers

def create_turtle(colors):
	turtles = []
	spacingX = WIDTH // (len(colors)+1)
	for i , color in enumerate (colors):
		racer = turtle.Turtle()
		racer.pencolor(color)
		racer.fillcolor(color)
		racer.shape("turtle") 
		racer.left(90)
		racer.penup()
		racer.setpos(-WIDTH/2 + ( i + 1 )*spacingX, START_LINE )
		racer.pendown()
		turtles.append(racer)
	return turtles

def race(colors):
    turtles = create_turtle(colors)
    rank = []

    while True:
        for racer in turtles:
            if racer.ycor() < FINISH_LINE:
                distance = random.randrange(1, 20)
                racer.forward(distance)

            if racer.ycor() >= FINISH_LINE:
                _, fillcolor = racer.color()
                if fillcolor not in rank:
                    rank.append(fillcolor)

            if len(rank) == len(colors):
                return rank
			
			
		
	
racers = RACERS

init_screen()
start_finish_line()

random.shuffle(COLORS)
colors = COLORS[:racers]

rank = race(colors)
print("\nHERE THE RESULT OF THE RACE: ")
for i in rank:
    if rank.index(i) + 1 == 1:
        print(rank.index(i) + 1, i , "🥇")
    elif rank.index(i) + 1 == 2:
        print(rank.index(i) + 1, i , "🥈")
    elif rank.index(i) + 1 == 3:
        print(rank.index(i) + 1, i , "🥉")
    else:
        print(rank.index(i) + 1, i)


input("\npress enter to exit...")
