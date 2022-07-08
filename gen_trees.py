import re
import os

x = []
with open('trees.txt') as f:
    for line in f.readlines():
        y = re.findall(r'\(.+\)', line)
        if y:
            x.append(y[0]+';')

xs = x[1:len(x)]

for val in range(len(xs)):
    with open(f'new_trees/tree{val}.tree','w') as out:
        out.write(xs[val])

with open('p3_out_TRUE.phy', 'r') as phy:
    phys = re.split(r'\n+\s{5}',phy.read()) 

for val in (range(len(phys))):
    with open(f'phys/phy{val}.phy', 'w') as out:
        out.write(phys[val])


files = [f'phys/phy{val}.phy' for val in range(len(phys))]

i = 0
for file in files:
    os.system(f"./FastTree {file} > est_tree/est{i}.tree")
    i += 1