"""
This script defines the Ball class, which is a subclass of the Turtle class from the turtle module. The Ball class represents a ball in a game, with methods to move the ball, bounce it off walls, and reset its position. The ball moves in a 2D space and can change direction when it bounces. The speed of the ball increases each time it bounces off a paddle.

this is a simple showcase of how to use a customized shape (in this case, a circle) and how to implement movement and collision logic for a game. The Ball class can be used in a larger game context, such as a Pong game, where the ball interacts with paddles and walls.
"""
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.color("white")
        self.penup()
        self.got(0, 0)
        self.dx = 10
        self.dy = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)


    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1
        self.move_speed *= 0.9     # Increase speed by reducing the move speed

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()             # Change direction after resetting position