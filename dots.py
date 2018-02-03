import os, sys
import Image
png = Image.open(sys.argv[1]).convert('RGBA')
pixels = png.load()
width, height = png.size

all_pixels = []
maxx = float(sys.argv[2])
dispx = float(sys.argv[4])
realx = maxx - dispx
lx = float(sys.argv[6])
maxy = float(sys.argv[3])
dispy = float(sys.argv[5])
realy = maxy - dispy
ly = float(sys.argv[7])
dx = float(sys.argv[8])
dy = float(sys.argv[9])
rc = int(sys.argv[10])
gc = int(sys.argv[11])
bc = int(sys.argv[12]) 
k = 0


f = open(sys.argv[13], 'w')
tempx = -1
for x in range(width):
    for y in range(height):
        t = height-y-1
        cpixel = pixels[x, t]
        color = tuple (cpixel)
        r, g, b, a = color
        if (r == rc) and (g == gc) and (b == bc):
            if tempx != x: 
                tempx = x
                f.write(str((x-dispx) * lx/ realx + dx) + ' ' + str((maxy-t)* ly/realy+dy)+'\n')
        all_pixels.append(cpixel)
f.close