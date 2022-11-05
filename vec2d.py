# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:37:08 2022

@author: jingy
"""

class Point:
    """
    Creates points in a Cartesian plane and 
    manipulates multiple points in various arithmetic methods.
    """
    def __init__(self, x=0, y=0):
        """ Default Point at (0,0) """
        self.x = x
        self.y = y
    def __str__(self):
        """
        Returns
        -------
        string : Composition of the point in a formatted manner.

        """
        string = f'x: {self.x} y: {self.y}'
        return string
    def __add__(self, other):
        """
        Parameters
        ----------
        self, other: two Point objects.

        Returns
        -------
        new_point : overloads + operator to sum the components of the Point objects.

        """
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_point = Point(new_x, new_y)
        return new_point
    def __iadd__(self, other):
        """
        Parameters
        ----------
        self, other: two Point objects.

        Returns
        -------
        Overloads += operator to sum components of Point objects.

        """
        self.x += other.x
        self.y += other.y
        return self
    def __sub__(self, other):
        """
        Parameters
        ----------
        self, other: two Point objects.

        Returns
        -------
        Overloads - operator to find difference of components of Point objects.

        """
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_point = Point(new_x, new_y)
        return new_point
    def __isub__(self, other):
        """
        Parameters
        ----------
        self, other: two Point objects.

        Returns
        -------
        Overloads -= operator to find difference of components of Point objects.

        """
        self.x -= other.x
        self.y -= other.y
        return self

class Vec2D(Point):
    """
    Creates vectors in a 2D Cartesian plane and 
    manipulates multiple points in various arithmetic methods.
    """
    def __init__(self, x=Point(), y=Point()):
        if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
            self.x = x
            self.y = y
            self.final = Point(x, y)
        elif isinstance(x, Point) and isinstance(y, Point):
            self.x = y.x - x.x
            self.y = y.y - x.y
            self.final = Point(self.x, self.y)
    def __str__(self):
        return f'{self.final}'
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_vec = Vec2D(new_x, new_y)
        return new_vec
    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_vec = Vec2D(new_x, new_y)
        return new_vec
    def __mul__(self, other):
        if (isinstance(self, Vec2D) or isinstance(self, Point)) and (isinstance(other, Vec2D) or isinstance(other, Point)):
            dot = self.x * other.x + self.y * other.y
            return dot
        elif isinstance(self, int) or isinstance(self, float):
            scaled = Vec2D(self * other.x, self * other.y)
            return scaled
        elif isinstance(other, int) or isinstance(other, float):
            scaled = Vec2D(self.x * other, self.y * other)
            return scaled
    def norm(self):
        norm = ((self.x**2)+(self.y**2)) ** 0.5
        return norm
