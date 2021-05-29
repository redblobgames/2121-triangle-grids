#!/usr/bin/env python3

"""
From https://www.redblobgames.com/x/2121-triangle-grids/
@license CC0-1.0 https://github.com/BorisTheBrave/grids/blob/main/LICENSE
"""

from third_party import updown_tri
from browser import document, html, svg

diagram = document["drawing-area"]

grid = []
for q in range(-7, 8):
    for r in range(-4, 5):
        grid.append((q, r, 1-q-r))
        grid.append((q, r, 2-q-r))

def draw():
    """Return a map from triangle to polygon svg object"""
    svg_objects = {}
    for triangle in grid:
        (a, b, c) = triangle
        corners = updown_tri.tri_corners(*triangle)
        (center_x, center_y) = updown_tri.tri_center(*triangle)
        if updown_tri.points_up(*triangle):
            center_y -= 0.0
        else:
            center_y += 0.2

        text = svg.text(x=center_x, y=center_y, text_anchor="middle")
        text <= svg.tspan(triangle[0], fill="hsl( 90, 100%, 35%)")
        text <= svg.tspan(",")
        text <= svg.tspan(triangle[1], fill="hsl(300,  80%, 50%)")
        text <= svg.tspan(",")
        text <= svg.tspan(triangle[2], fill="hsl(200, 100%, 45%)")

        polygon = svg.polygon(fill="none", stroke="black", stroke_width="0.02",
                               points = " ".join([str(x)+","+str(y) for (x,y) in corners]))
        diagram <= polygon
        diagram <= text
        svg_objects[triangle] = polygon

    return svg_objects

# global
svg_objects = draw()

def recolor_handler(selected_triangle):
    def handler(event):
        for (triangle, polygon) in svg_objects.items():
            fill = "none"
            if selected_triangle[0] == triangle[0]: fill = "hsl(90, 40%, 87%)"
            if selected_triangle[1] == triangle[1]: fill = "hsl(200, 35%, 90%)"
            if selected_triangle[2] == triangle[2]: fill = "hsl(300, 30%, 90%)"
            if selected_triangle == triangle: fill = "hsl(60, 100%, 85%)"
            polygon.attrs["fill"] = fill
        
    return handler

def add_interactivity():
    for (triangle, polygon) in svg_objects.items():
        polygon.bind("pointerenter", recolor_handler(triangle))

add_interactivity()


