#!/usr/bin/env python
# coding=utf-8
""" Triangle Containment
Three distinct points are plotted at random on a Cartesian plane, for which -1000 ≤ x, y ≤ 1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.

"""
__author__ = 'julenka'

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def contains_origin(self):
        p = Point(0,0)
        alpha = ((self.p2.y - self.p3.y)*(p.x - self.p3.x) + (self.p3.x - self.p2.x)*(p.y - self.p3.y)) /\
                ((self.p2.y - self.p3.y)*(self.p1.x - self.p3.x) + (self.p3.x - self.p2.x)*(self.p1.y - self.p3.y))
        beta = ((self.p3.y - self.p1.y)*(p.x - self.p3.x) + (self.p1.x - self.p3.x)*(p.y - self.p3.y)) /\
            ((self.p2.y - self.p3.y)*(self.p1.x - self.p3.x) + (self.p3.x - self.p2.x)*(self.p1.y - self.p3.y))
        gamma = 1.0 - alpha - beta
        return alpha > 0 and beta > 0 and gamma > 0

triangle_file_path = "p102_triangles.txt"
result = 0
for line in open(triangle_file_path):
    p1x,p1y,p2x,p2y,p3x,p3y = [float(x) for x in line.split(",")]
    p1 = Point(p1x, p1y)
    p2 = Point(p2x, p2y)
    p3 = Point(p3x, p3y)
    t = Triangle(p1, p2, p3)
    print t.p1, t.p2, t.p3
    if t.contains_origin():
        result += 1
print result

