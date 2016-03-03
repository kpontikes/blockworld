import json


grass = []
stone = []
brick = []
sand = []
n = 80  # 1/2 width and height of world
s = 1  # step size
y = 0  # initial y height
for x in xrange(-n, n + 1, s):
   for z in xrange(-n, n + 1, s):
   # create a layer stone and grass everywhere.
      grass.append((x, y-2, z))
      stone.append((x, y-3, z))
      if x in (-n, n) or z in (-n, n):
         # create outer walls.
         for dy in xrange(-2, 3):
            stone.append((x, y+dy, z))
   
world = [grass,stone,brick,sand]
generate_file = open("generate_world.json", "w")
json.dump(world, generate_file)
