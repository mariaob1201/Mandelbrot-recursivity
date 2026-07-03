"""Mandelbrot set rendered as ASCII art using recursion.

The escape-time calculation (how many iterations before a point "escapes"
to infinity) is implemented recursively instead of with a loop, to
demonstrate recursivity: each call either detects escape/max-depth (base
case) or recurses with the next iterate of z = z^2 + c.
"""

CHARS = " .:-=+*#%@"
MAX_ITER = len(CHARS) - 1
ESCAPE_RADIUS_SQ = 4


def escape_iterations(c, z=0j, depth=0, max_iter=MAX_ITER):
    """Recursively compute how many iterations until |z| escapes, or max_iter."""
    if depth == max_iter:
        return depth
    if abs(z) * abs(z) > ESCAPE_RADIUS_SQ:
        return depth
    return escape_iterations(c, z * z + c, depth + 1, max_iter)


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


def render_image(path="mandelbrot.png", width=800, height=600, max_iter=100,
                  x_min=-2.5, x_max=1.0, y_min=-1.2, y_max=1.2):
    """Render the Mandelbrot set to a PNG, reusing the recursive escape_iterations."""
    import numpy as np
    import matplotlib.pyplot as plt

    data = np.empty((height, width))
    for row in range(height):
        y = y_min + (y_max - y_min) * row / (height - 1)
        for col in range(width):
            x = x_min + (x_max - x_min) * col / (width - 1)
            c = complex(x, y)
            data[row, col] = escape_iterations(c, max_iter=max_iter)

    plt.imsave(path, data, cmap="magma")
    return path


if __name__ == "__main__":
    print(render())
    render_image()
