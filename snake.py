from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments_lst = []
        self.distance = MOVE_DISTANCE
        self.create()
        self.head = self.segments_lst[0]

    def create(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segment.setposition(position)
        self.segments_lst.append(segment)

    def extend(self):
        # Add a new segment at the position of the current last segment.
        self.add_segment(self.segments_lst[-1].position())

    def move(self):
        # Move each segment to the position of the segment in front of it,
        # starting from the tail so positions aren't overwritten too early.
        for segment in range(len(self.segments_lst) - 1, 0, -1):
            new_x = self.segments_lst[segment - 1].xcor()
            new_y = self.segments_lst[segment - 1].ycor()
            self.segments_lst[segment].goto(new_x, new_y)
        self.head.forward(self.distance)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
