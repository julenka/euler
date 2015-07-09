__author__ = 'julenka'
from utils import euler

# 70 balls
# 7 colors, 10 per color
# num_balls = 70
num_colors = 7
ball_per_color = 10
max_pick = 20
num_colors_to_count = {x: 0 for x in xrange(num_colors + 1)}

colors = 'roygbiv'


def rcr(colors_left, balls_left, acc, acc2):
    if balls_left < 0:
        return
    if balls_left == 0:
        assert sum(acc.values()) == max_pick
        print acc
        num_colors2 = len(filter(lambda x: x > 0, acc.values()))
        ways = 1
        for _, count in acc.items():
            ways *= euler.choose(10, count)
        num_colors_to_count[num_colors2] += ways
        return
        # num_colors_to_count[acc2] += 1
    if colors_left <= 0:
        return

    for n in xrange(ball_per_color + 1):
        color_idx = num_colors - colors_left
        acc[color_idx] = n
        acc3 = acc2 if n == 0 else acc2 + 1
        rcr(colors_left - 1, balls_left - n, acc, acc3)
        acc[color_idx] = 0

rcr(num_colors, max_pick, {}, 0)

print num_colors_to_count

s = sum(num_colors_to_count.values())

s2 = reduce(lambda y, x: x[0] * x[1] + y, num_colors_to_count.items(), 0)

print s
print s2
print euler.choose(70, 20)
print float(s2) / euler.choose(70, 20)
