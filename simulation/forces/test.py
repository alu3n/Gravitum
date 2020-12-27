from noise import *

n = noise()

for x in n.field:
    print(x.direction.data[0])
    print(x.pos.data[0])
# print(n.field)
