import random
import sys

#!/usr/bin/env python3
# GitHub Copilot
# Simple ASCII Christmas tree with random decorations


def draw_tree(height=10, deco_prob=0.15):
    for i in range(height):
        width = 2 * i + 1
        row = ''.join(
            random.choice('o*+@') if random.random() < deco_prob else '^'
            for _ in range(width)
        )
        print(' ' * (height - 1 - i) + row)
    trunk_w = max(1, height // 3)
    if trunk_w % 2 == 0:
        trunk_w += 1
    trunk_h = max(2, height // 4)
    trunk = '|' * trunk_w
    for _ in range(trunk_h):
        print(' ' * (height - 1 - trunk_w // 2) + trunk)

if __name__ == "__main__":
    h = 10
    if len(sys.argv) > 1:
        try:
            h = max(3, int(sys.argv[1]))
        except ValueError:
            pass
    draw_tree(h)


    
