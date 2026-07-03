# Mandelbrot Recursivity

A small example showing recursion by computing the Mandelbrot set.

## The recursion

The Mandelbrot set is defined by iterating `z = z^2 + c` starting from
`z = 0`. A point `c` belongs to the set if that sequence never escapes
to infinity. Traditionally this "escape-time" check is written with a
loop; here it's written recursively instead, in
[`escape_iterations`](mandelbrot.py):

```python
def escape_iterations(c, z=0j, depth=0, max_iter=MAX_ITER):
    if depth == max_iter:        # base case: never escaped
        return depth
    if abs(z) * abs(z) > ESCAPE_RADIUS_SQ:  # base case: escaped
        return depth
    return escape_iterations(c, z * z + c, depth + 1, max_iter)
```

Each call either hits a base case (escaped, or reached the iteration
limit) or recurses with the next iterate of `z`. The recursion depth at
which a point escapes determines how it's shaded.

## Usage

```bash
python3 mandelbrot.py
```

This prints an ASCII-art rendering of the set to the terminal and also
writes a higher-resolution color PNG to `mandelbrot.png`.

You can call the rendering functions directly for custom output:

```python
from mandelbrot import render, render_image

print(render(width=120, height=60))          # ASCII art
render_image("zoom.png", x_min=-0.8, x_max=-0.4, y_min=0.4, y_max=0.7)  # zoomed PNG
```

## Requirements

- Python 3
- `numpy` and `matplotlib` (only needed for `render_image`; the ASCII
  renderer has no dependencies)
