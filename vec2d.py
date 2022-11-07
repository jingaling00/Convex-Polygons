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
    Inherited from Point class.
    
    """
    
    def __init__(self, x=Point(), y=Point()):
        """
        Takes two objects to create a vector. This could be
        two point objects, or two integer/float objects.

        Parameters
        ----------
        x : Could be integer/float or Point object. Default is  (0,0).
        y : Could be integer/float or Point object. Default is (0,0).

        """
        
        if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
            self.x = x
            self.y = y
            self.final = Point(x, y)
        elif isinstance(x, Point) and isinstance(y, Point):
            self.x = y.x - x.x
            self.y = y.y - x.y
            self.final = Point(self.x, self.y)
    
    def __add__(self, other):
        """
        Overloads + operator to perform vector addition.

        Parameters
        ----------
        self, other are Vector objects.

        Returns
        -------
        new_vec is the sum of the two vectors.

        """
        
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_vec = Vec2D(new_x, new_y)
        return new_vec
    
    def __sub__(self, other):
        """
        Overloads - operator to perform vector subtraction.

        Parameters
        ----------
        self, other are Vector objects.

        Returns
        -------
        new_vec is the difference of the two vectors.

        """
        
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_vec = Vec2D(new_x, new_y)
        return new_vec

    def __mul__(self, other):
        """
        Overloads * operator to perfrom scalar-vector multiplication,
        or find the inner product between two vectors.

        Parameters
        ----------
        self, other are either two vector objects,
        or one scalar and one vector object.

        Returns
        -------
        Returns new, scaled vector if multiplying between scalar and vector.
        Returns a scalar if finding the inner product between 2 vectors.

        """
        
        if isinstance(self, int) or isinstance(self, float):
            scaled = Vec2D(self * other.x, self * other.y)
            return scaled
        elif isinstance(other, int) or isinstance(other, float):
            scaled = Vec2D(self.x * other, self.y * other)
            return scaled
        else:
            dot = self.x * other.x + self.y * other.y
            return dot
        
    def norm(self):
        """
        Find the magnitude of the vector.

        Returns
        -------
        No arguments required; use vector components to find magnitude.

        """
        
        norm = ((self.x**2)+(self.y**2)) ** 0.5
        return norm
