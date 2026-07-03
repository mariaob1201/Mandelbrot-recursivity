# Mandelbrot Recursivity

Small examples showing recursion through classic math/fractal problems.

## Mandelbrot set (`mandelbrot.py`)

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

Usage:

```bash
python3 mandelbrot.py
```

This prints an ASCII-art rendering of the set to the terminal and also
writes a higher-resolution color PNG to `mandelbrot.png`.

```python
from mandelbrot import render, render_image

print(render(width=120, height=60))          # ASCII art
render_image("zoom.png", x_min=-0.8, x_max=-0.4, y_min=0.4, y_max=0.7)  # zoomed PNG
```

## Towers of Hanoi (`hanoi.py`)

The classic recursive puzzle: to move `n` disks from `source` to
`target` using `aux` as a spare peg, recursively move the top `n-1`
disks out of the way, move the largest disk directly, then recursively
move the `n-1` disks back on top of it. The base case is `n == 0`.

```python
def solve(n, source="A", target="C", aux="B", moves=None):
    if moves is None:
        moves = []
    if n == 0:
        return moves
    solve(n - 1, source, aux, target, moves)
    moves.append((n, source, target))
    solve(n - 1, aux, target, source, moves)
    return moves
```

The sequence of *which disk* moves on each step is itself self-similar
(disk 1 moves every other step, disk 2 every 4th step, disk 3 every
8th, ...) — the same recursive/fractal flavor as the Mandelbrot set,
just in a discrete puzzle instead of the complex plane.

Usage:

```bash
python3 hanoi.py
```

This prints the move list for 4 disks to the terminal and saves a plot
of the move pattern for 8 disks to `hanoi.png`.

## Requirements

- Python 3
- `numpy` and `matplotlib` (only needed for the `render_image` functions
  in `mandelbrot.py` and `hanoi.py`; the ASCII renderer and move solver
  have no dependencies)
