pipes = {}
with open('input/day12.txt') as f:
    for line in f:
        src, _, dsts = line.split(maxsplit=2)
        pipes[int(src)] = set(map(int, dsts.split(', ')))

def find_group(seed):
    group = {seed}
    new = {seed}
    while new:
        next_new = set()
        for item in new:
            next_new.update(pipes[item])
        new = next_new - group
        group.update(next_new)
    return group
print('Part 1:', len(find_group(0)))

remaining = set(pipes)
groups = 0
while remaining:
    groups += 1
    group = find_group(remaining.pop())
    remaining -= group
print('Part 2:', groups)