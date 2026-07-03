"""Towers of Hanoi solved and visualized via recursion.

The classic recursive solution: to move n disks from `source` to
`target` using `aux` as a spare peg, move the top n-1 disks out of the
way, move the largest disk directly, then move the n-1 disks back on
top of it. The base case is n == 0 (nothing to move).

The sequence of *which disk* moves on each step turns out to be
self-similar / fractal-like: disk 1 moves every other step, disk 2
every 4th step, disk 3 every 8th, etc. (the same pattern as the
"ruler sequence" / binary carry sequence). We visualize that pattern.
"""


def solve(n, source="A", target="C", aux="B", moves=None):
    """Recursively compute the list of moves to solve Towers of Hanoi."""
    if moves is None:
        moves = []
    if n == 0:
        return moves
    solve(n - 1, source, aux, target, moves)
    moves.append((n, source, target))
    solve(n - 1, aux, target, source, moves)
    return moves


def print_moves(moves):
    for disk, src, dst in moves:
        print(f"Move disk {disk}: {src} -> {dst}")
    print(f"Total moves: {len(moves)}")


def render_image(n=8, path="hanoi.png"):
    """Plot which disk moves on each step, revealing the self-similar pattern."""
    import matplotlib.pyplot as plt

    moves = solve(n)
    steps = list(range(1, len(moves) + 1))
    disks = [disk for disk, _, _ in moves]

    plt.figure(figsize=(10, 4))
    plt.bar(steps, disks, color="darkmagenta", width=1.0)
    plt.gca().invert_yaxis()
    plt.xlabel("Move number")
    plt.ylabel("Disk moved (1 = smallest)")
    plt.title(f"Towers of Hanoi move pattern ({n} disks, {len(moves)} moves)")
    plt.tight_layout()
    plt.savefig(path, dpi=150)
    return path


if __name__ == "__main__":
    print_moves(solve(4))
    render_image()
