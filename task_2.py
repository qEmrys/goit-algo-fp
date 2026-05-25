import matplotlib.pyplot as plt
import argparse
import math


def draw_tree(ax, x, y, length, angle, level):
    if level == 0:
        return

    x_end = x + length * math.cos(math.radians(angle))
    y_end = y + length * math.sin(math.radians(angle))

    ax.plot([x, x_end], [y, y_end], color="darkred", linewidth=level * 0.5)

    draw_tree(ax, x_end, y_end, length * 0.7, angle + 45, level - 1)
    draw_tree(ax, x_end, y_end, length * 0.7, angle - 45, level - 1)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("level", type=int, nargs="?", default=7)
    args = parser.parse_args()

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(f"Дерево Піфагора - рівень {args.level}")

    draw_tree(ax, 0, -200, 100, 90, args.level)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
