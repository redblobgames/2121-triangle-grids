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

def redraw():
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

        fill = "none"
        if a == 2: fill = "hsl(90, 40%, 87%)"
        if b == 2: fill = "hsl(200, 35%, 90%)"
        if c == 2: fill = "hsl(300, 30%, 90%)"
        if a == 2 and b == 2 and c == 2: fill = "hsl(60, 100%, 85%)"

        diagram <= svg.polygon(fill=fill, stroke="black", stroke_width="0.02",
                               points = " ".join([str(x)+","+str(y) for (x,y) in corners]))
        diagram <= text

redraw()

# TODO: on mouseover, set the "current" position, and redraw
# TODO: need to hold on to the polygons so that we can go back and update         polygon.attrs["fill"] = …
