# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 11:37:08 2022

@author: jingy
"""

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        string = f'x: {self.x} y: {self.y}'
        return string
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_point = Point(new_x, new_y)
        return new_point
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_point = Point(new_x, new_y)
        return new_point
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

class Vec2D(Point):
    def __init__(self, x=Point(), y=Point()):
        if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
            self.x = x
            self.y = y
            self.final = Point(x, y)
        elif isinstance(x, Point) and isinstance(y, Point):
            self.x = x.x - y.x
            self.y = x.y - y.y
            self.final = Point(self.x, self.y)
    def __str__(self):
        return f'{self.final}'
    def __add__(self, other):
        return Point.__add__(self, other)
    def __sub__(self, other):
        return Point.__sub__(self, other)
    def __mul__(self, other):
        if isinstance(self, Vec2D) and isinstance(other, Vec2D):
            dot = self.x * other.x + self.y * other.y
            return dot
        elif isinstance(other, int):
            scaled = Vec2D(self.x * other, self.y *other)
            return scaled
    def norm(self):
        norm = ((self.x**2)+(self.y**2)) ** 0.5
        return norm
    
        
    