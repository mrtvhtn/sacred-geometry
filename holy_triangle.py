# -*- coding: utf-8 -*-
"""
Vector Geometry Core Engine
Generates flawless geometric vector mapping based on precise coordinate systems.
"""

def generate_geometry_matrix(filename="holy_triangle.svg"):
    svg_content = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg width="800" height="650" viewBox="0 0 800 650" xmlns="http://w3.org">
    <rect width="100%" height="100%" fill="#F9F6F0" />
    <rect x="50" y="50" width="700" height="500" fill="none" stroke="#1A237E" stroke-width="2" />
    <polygon points="150,450 650,450 400,100" fill="#F48FB1" fill-opacity="0.15" />
    <line x1="150" y1="450" x2="400" y2="100" stroke="#1A237E" stroke-width="3" />
    <line x1="650" y1="450" x2="400" y2="100" stroke="#1A237E" stroke-width="3" />
    <line x1="150" y1="450" x2="650" y2="450" stroke="#1A237E" stroke-width="3" />
    <line x1="400" y1="450" x2="400" y2="200" stroke="#1A237E" stroke-width="3" />
    <circle cx="400" cy="130" r="35" fill="#FFB300" stroke="#FF6F00" stroke-width="2.5" />
</svg>
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"[SUCCESS] Vector file {filename} generated successfully.")

if __name__ == "__main__":
    generate_geometry_matrix()
