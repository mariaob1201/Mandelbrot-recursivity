"""Mandelbrot set rendered as ASCII art using recursion.

The escape-time calculation (how many iterations before a point "escapes"
to infinity) is implemented recursively instead of with a loop, to
demonstrate recursivity: each call either detects escape/max-depth (base
case) or recurses with the next iterate of z = z^2 + c.
"""

CHARS = " .:-=+*#%@"
MAX_ITER = len(CHARS) - 1
ESCAPE_RADIUS_SQ = 4


def escape_iterations(c, z=0j, depth=0):
    """Recursively compute how many iterations until |z| escapes, or MAX_ITER."""
    if depth == MAX_ITER:
        return depth
    if abs(z) * abs(z) > ESCAPE_RADIUS_SQ:
        return depth
    return escape_iterations(c, z * z + c, depth + 1)


def render(width=80, height=40,
           x_min=-2.5, x_max=1.0, y_min=-1.2, y_max=1.2):
    rows = []
    for row in range(height):
        y = y_min + (y_max - y_min) * row / (height - 1)
        line = []
        for col in range(width):
            x = x_min + (x_max - x_min) * col / (width - 1)
            c = complex(x, y)
            iterations = escape_iterations(c)
            line.append(CHARS[iterations])
        rows.append("".join(line))
    return "\n".join(rows)


if __name__ == "__main__":
    print(render())
