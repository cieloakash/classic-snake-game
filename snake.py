from turtle import Turtle
START_POSITION = [(0,0),(-20,0),(-40,0)]
STEP = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments= []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color('green')
    
    def create_snake(self):
        for pos in START_POSITION:
            self.add_segment(pos)
    

    def add_segment(self,pos):
        new_seg= Turtle('square')
        new_seg.color('white')
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.color('green')
    

    def extends(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments)-1, 0 ,-1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.head.forward(STEP)
        

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() !=UP :
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        