##file = input("Enter file name: ")

WALL = 1
SIDE = 10
BEG_X = -200
BEG_Y = 200

def readMaze(file):
    f = open(file, 'r')
    read = f.readlines()
    matrix = []
    row = []
    for i in range(0,len(read)): #outer list
        for k in range(0,len(read[i])-1): #nested list
            if read[i][k] == "#":
                row.append(1)
            else:
                row.append(0)
        matrix.append(row)
        row = []
    return matrix

def drawSquare(i,j,t,side=10,col="black"):
    t.color(col)
    t.penup()
    t.goto(i,j)
    t.pendown()
    t.begin_fill()
    for d in range(0, 4):
        t.forward(10)
        t.left(90)
    t.end_fill()
    t.penup()


def drawMaze(maze,t,col):
    for i in range(0,(len(maze))):
        for j in range(0,len(maze[i])):
            if maze[i][j] == WALL:
                drawSquare(j*SIDE + BEG_X,-i*SIDE + BEG_Y,t)
    t.ht()


def followLeftWall(maze, t, col):
    i = 1 #beginning of the maze
    j = 0
    drawSquare(j*SIDE + BEG_X,-i*SIDE + BEG_Y, t, side=10, col="yellow")
    direction = "east"
    while i <= len(maze)-2 and j < len(maze[i])-1: #goes to exit of maze
        direction = nextMove(maze,i,j,direction)
        if direction == "east":
            j = j + 1
        elif direction == "north":
            i = i - 1
        elif direction == "west":
            j = j - 1
        elif direction == "south":
            i = i + 1
        drawSquare(j*SIDE + BEG_X,-i*SIDE + BEG_Y,t,side=10, col="yellow")

def nextMove(maze,i,j,currDirection):
    if currDirection == "east":
        if maze[i-1][j] != WALL: #left
            direction = "north"
            return direction
        elif maze[i][j+1] != WALL: #straight
            direction = "east"
            return direction
        elif maze[i+1][j] != WALL: #right
            direction = "south"
            return direction
        elif maze[i][j-1] != WALL: #backwards
            direction = "west"
            return direction
        
    elif currDirection == "north":
        if maze[i][j-1] != WALL: #left
            direction = "west"
            return direction
        elif maze[i-1][j] != WALL: #straight
            direction = "north"
            return direction
        elif maze[i][j+1] != WALL: #right
            direction = "east"
            return direction
        elif maze[i+1][j] != WALL: #backwards
            direction = "south"
            return direction
        
    elif currDirection == "west":
        if maze[i+1][j] != WALL: #left
            direction = "south"
            return direction
        elif maze[i][j-1] != WALL: #straight
            direction = "west"
            return direction
        elif maze[i-1][j] != WALL: #right
            direction = "north"
            return direction
        elif maze[i][j+1] != WALL: #backwards
            direction = "east"
            return direction
        
    elif currDirection == "south":
        if maze[i][j+1] != WALL: #left
            direction = "east"
            return direction
        elif maze[i+1][j] != WALL: #straight
            direction = "south"
            return direction
        elif maze[i][j-1] != WALL: #right
            direction = "west"
            return direction
        elif maze[i-1][j] != WALL: #backwards
            direction = "north"
            return direction


def main(filename,algorithm):
    matrix = readMaze(filename)
    import turtle
    wn = turtle.Screen()
    wilfred = turtle.Turtle()
    wn.tracer(0)
    drawMaze(matrix,wilfred,"black")
    wn.update()
    wn.tracer(10)
    followLeftWall(matrix,wilfred,"yellow")
    wn.update() 

main("testMaze2.txt", " ")
