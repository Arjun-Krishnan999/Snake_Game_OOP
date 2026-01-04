from turtle import Turtle
starting_pos = [(0, 0), (-20, 0), (-40, 0)]
move_dist=20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in starting_pos:
            self.add_seg(pos)

    def add_seg(self,pos):
        new_seg = Turtle("square")
        new_seg.color("white")
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]

    def extend(self):
        self.add_seg(self.segments[-1].position())

    def move(self,segments):
        for seg in range(len(self.segments) - 1, 0, -1):
            next_x = self.segments[seg - 1].xcor()
            next_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(next_x, next_y)
        self.head.forward(move_dist)

    def up(self):
        if self.head.heading()==270:
            pass
        else:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()==90:
            pass
        else:
            self.head.setheading(270)
    def left(self):
        if self.head.heading()==0:
            pass
        else:
            self.head.setheading(180)
    def right(self):
        if self.head.heading()==180:
            pass
        else:
            self.head.setheading(0)