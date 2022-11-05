# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 15:06:11 2022

@author: jingy
"""
from vec2d import Vec2D as V
from vec2d import Point as P
import math

def orient2d(a, b, c):
    '''
    Parameters
    ----------
        a : Point object
        b : Point object
        c : Point object
        
    Returns
    --------
        Integer 1/1/0
        Returns 1 if points are oriented in the 
        counter clockwise direction -1 if clockwise
        and 0 if collinear
        
    '''

    # Signed area of triangle formed by a,b,c
    s_a = (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)
    
    # Orientation
    result = 1 if s_a > 0 else -1 if s_a < 0 else 0
    
    return result

class ConvexPolygon:
    def __init__(self, points=[]):
        self.nverts = len(points)
        if self.nverts < 3:
            raise ValueError('Points do not form a convex polygon')
        
        self.verts = points
        
        self.edges = []
        
        for i in range(0, self.nverts):
            if i == self.nverts - 1:
                vector = V(self.verts[0], self.verts[i])
                self.edges.append(vector)
            else:
                vector = V(self.verts[i+1], self.verts[i])
                self.edges.append(vector)
            
        for point in self.verts:
             a = self.verts[0]
             b = self.verts[1]
             for i in range(2, len(self.verts)):
                 orient = orient2d(a, b, self.verts[i])
                 if orient == -1 or orient == 0:
                     raise ValueError('Points do not form a convex polygon')
                     
    def __str__(self):
        verts = []
        for i in self.verts:
            verts.append(P.__str__(i))
        vert_str = ', '.join(verts)
        
        edges = []
        for i in self.edges:
            edges.append(V.__str__(i))
        edges_str = ', '.join(edges)
        return f'No. of Vertices: {self.nverts}\nVertices {vert_str}\nEdges {edges_str}'

    def translate(self, vec2d):
        new_verts = []
        for n in self.verts:
            n += vec2d
            new_verts.append(n)
        self.verts = new_verts
        
    
    def centroid(self):
        a = 0
        for i in range(0, self.nverts):
            if (i+1) == self.nverts:
                vertex_mult = (self.verts[i].x * self.verts[0].y) - (self.verts[0].x * self.verts[i].y)
            else:
                vertex_mult = (self.verts[i].x * self.verts[i+1].y) - (self.verts[i+1].x * self.verts[i].y)
            a += vertex_mult
        a *= 0.5
        
        cx = 0
        for i in range(0, self.nverts):
            if (i+1) == self.nverts:
                vertex_mult = (self.verts[i].x + self.verts[0].x) * ((self.verts[i].x * self.verts[0].y) - (self.verts[0].x * self.verts[i].y))
            else:   
                vertex_mult = (self.verts[i].x + self.verts[i+1].x) * ((self.verts[i].x * self.verts[i+1].y) - (self.verts[i+1].x * self.verts[i].y))
            cx += vertex_mult
        cx /= (6 * a)
        
        cy = 0
        for i in range(0, self.nverts):
            if (i+1) == self.nverts:
                vertex_mult = (self.verts[i].y + self.verts[0].y) * ((self.verts[i].x * self.verts[0].y) - (self.verts[0].x * self.verts[i].y))
            else:
                vertex_mult = (self.verts[i].y + self.verts[i+1].y) * ((self.verts[i].x * self.verts[i+1].y) - (self.verts[i+1].x * self.verts[i].y))
            cy += vertex_mult
        cy /= (6 * a)
        
        centroid = P(cx, cy)
        
        return centroid
    
    def rotate(self, angle, pivot=0):
        if pivot == 0:
            pivot = self.centroid()
        verts = []
        cos = math.cos(angle)
        sin = math.sin(angle)
        for v in self.verts:
            x = (cos * (v.x - pivot.x)) - (sin * (v.y - pivot.y)) + pivot.x
            y = (sin * (v.x - pivot.x)) + (cos * (v.y - pivot.y)) + pivot.y
            v = P(x, y)
            verts.append(v)
        self.verts = verts
        
        self.edges = []
        for i in range(0, self.nverts):
            if i == self.nverts - 1:
                vector = V(self.verts[0], self.verts[i])
                self.edges.append(vector)
            else:
                vector = V(self.verts[i+1], self.verts[i])
                self.edges.append(vector)   
        
    def scale(self, sx, sy):
        centroid = self.centroid()
        verts = []
        for v in self.verts:
            x = sx * (v.x - centroid.x) + centroid.x
            y = sy * (v.y - centroid.y) + centroid.y
            v = P(x, y)
            verts.append(v)
        self.verts = verts
        
        self.edges = []
        for i in range(0, self.nverts):
            if (i+1) == self.nverts:
                vector = V(self.verts[0], self.verts[i])
                self.edges.append(vector)
            else:
                vector = V(self.verts[i+1], self.verts[i])
                self.edges.append(vector)
    
    def __and__(self, other):
        total_edges = self.edges + other.edges
        
        for edge in total_edges:
            polyA_projs = []
            polyB_projs = []
            
            orthog = V(-edge.y, edge.x)
            
            for vertA in self.verts:
                vec = V(vertA.x, vertA.y)
                proj = vec * orthog
                polyA_projs.append(proj)
            for vertB in other.verts:
                vec = V(vertB.x, vertB.y)
                proj = vec * orthog
                polyB_projs.append(proj)
                
            min_A = min(polyA_projs)
            max_A = max(polyA_projs)
            
            min_B = min(polyB_projs)
            max_B = max(polyB_projs)
            
            if max_A < min_B or max_B < min_A:
                return False
            else:
                continue
        
        return True
            
        

        

        