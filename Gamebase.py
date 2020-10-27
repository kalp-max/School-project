import math
import os


def line(a,b,x,y):

    """
    Draw a line from (a,b) to (x,y)
    """

    import turtle
    turtle.up()
    turtle.goto(a,b)
    turtle.down()
    turtle.goto(x,y)


def square(x,y,sideLength,colourFill):

    """
    Drawing square at '(x,y)' with length of the side as 'sideLength'
    and colour filling as 'colourFill'.
    
    This square will have '(x,y)' at its left bottom corner.
    """

    import turtle
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.color(colourFill)
    turtle.begin_fill()
    turtle.speed(1)

    for _ in range(4):
        turtle.fd(sideLength)
        turtle.lt(90)

    turtle.end_fill()


class vector():

    """
    Two dimensional vector
    """

    precision = 5

    __slots__ = ("_x","_y","_hash")


    def __init__(self,x,y):

        """
        Initialize vector with (x,y)
        """

        self._hash = None
        self._x = round(x,self.precision)
        self._y = round(y,self.precision)


    @property
    def x(self):

        """
        X-axis component of the vector
        """

        return self._x

