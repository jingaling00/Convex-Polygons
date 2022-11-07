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
    if isinstance(a, P) and isinstance(b, P) and isinstance(c, P): # check if inputs are Point objects
        # Signed area of triangle formed by a,b,c
        s_a = (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)
        
        # Orientation
        if s_a > 0:
            result = 1
        elif s_a < 0:
            result = -1
        else:
            result = 0
        
        return result

class ConvexPolygon:
    """ Creates an n-sided convex polygon with a list of points
        Polygon can be scaled, rotated, translated, etc. 
        using vector and point objects from Vec2D and Point classes"""
        
    def __init__(self, points=[]):
        """
        Parameters
        ----------
        Takes in a list of points as parameter. 
        The default is [].
        Uses the list of points to generate edges,
        which are vectors between the points.

        Raises
        ------
        ValueError is raised when the list of points does not
        form a convex polygon (i.e., the number of points is less than 3,
        the points do not lie in the same orientation, etc.)

        """
        self.verts = points
        
        self.edges = []
        
        if len(self.verts) < 3:
            raise ValueError('Points do not form a convex polygon')
        
        self.nverts = len(self.verts) # total number of points
            
        for i in range(0, self.nverts): # generating the list of edges using Vec2D class
            if i == self.nverts - 1:
                vector = V(self.verts[i], self.verts[0])
                self.edges.append(vector)
            else:
                vector = V(self.verts[i], self.verts[i+1])
                self.edges.append(vector)
        
        for i in range(self.nverts): # checking if points form a convex polygon
            orient_sum = 0
            for j in range(self.nverts):
                orient = orient2d(self.verts[i], self.verts[(i+1) % self.nverts], self.verts[j])
                orient_sum += orient
                
            if math.fabs(orient_sum) != self.nverts - 2:
                raise ValueError('Points do not form a convex polygon')
                     
    def __str__(self):
        """
        Returns
        -------
        str object is returned by formatting the polygon's
        vertices and edges.
        """
        
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
        """
        Parameters
        ----------
        Takes a Vec2D (vector) object as parameter.

        Returns
        -------
        Using vector parameter, the shape is translated along this vector.
        The list of vertices, and edges, is redefined.

        """
        
        new_verts = []
        for n in self.verts:
            n += vec2d
            new_verts.append(n)
        self.verts = new_verts
    
    def centroid(self):
        """
        Returns
        -------
        Returns the Point object denoting the centroid of the polygon.

        """
        a = 0
        cx = 0
        cy = 0
        
        for i in range(0, self.nverts):
            if (i+1) == self.nverts:
                a_mult = (self.verts[i].x * self.verts[0].y) - (self.verts[0].x * self.verts[i].y)
                cx_mult = (self.verts[i].x + self.verts[0].x) * ((self.verts[i].x * self.verts[0].y) - (self.verts[0].x * self.verts[i].y))
                cy_mult = (self.verts[i].y + self.verts[0].y) * ((self.verts[i].x * self.verts[0].y) - (self.verts[0].x * self.verts[i].y))

            else:
                a_mult = (self.verts[i].x * self.verts[i+1].y) - (self.verts[i+1].x * self.verts[i].y)
                cx_mult = (self.verts[i].x + self.verts[i+1].x) * ((self.verts[i].x * self.verts[i+1].y) - (self.verts[i+1].x * self.verts[i].y))
                cy_mult = (self.verts[i].y + self.verts[i+1].y) * ((self.verts[i].x * self.verts[i+1].y) - (self.verts[i+1].x * self.verts[i].y))

            a += a_mult
            cx += cx_mult
            cy += cy_mult

        a *= 0.5
        cx /= (6 * a)
        cy /= (6 * a)
        
        return P(cx, cy)
    
    def rotate(self, angle, pivot=0):
        """
        Rotates shape according to angle and pivot point.
        
        Parameters
        ----------
        angle : angle in radians indicating the extent of rotation.
        pivot : the Point object around which the shape will be rotated. 
                The default is the shape's own centroid.

        """
        
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
                vector = V(self.verts[i], self.verts[0])
                self.edges.append(vector)
            else:
                vector = V(self.verts[i], self.verts[i+1])
                self.edges.append(vector)   
        
    def scale(self, sx, sy):
        """
        The shape is stretched/shrunken according to a stretch constant in parameters.

        Parameters
        ----------
        sx : the factor by which the x-coordinates are stretched/shrunken.
        sy : the factor by which the y-coordinates are streched/shrunken.

        """
        
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
                vector = V(self.verts[i], self.verts[0])
                self.edges.append(vector)
            else:
                vector = V(self.verts[i], self.verts[i+1])
                self.edges.append(vector)
    
    def __and__(self, other):
        """
        Overloads the & operator by using vector projections to analyze
        whether two convex polygons will overlap in a coordinate plane.

        Parameters
        ----------
        self, other are two convex polygon objects.

        Returns
        -------
        bool: True denotes the polygons do overlap. False denotes polygons
        do not overlap.

        """
        
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
        
        return True
