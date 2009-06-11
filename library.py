"""  Library database creation code """

from __future__ import division
import sqlite3
import os
import re
import hashlib
import Image
from scipy.ndimage import *
from scipy import *
import pylab


imagepattern = "jpg$"
R, G, B = 0, 1, 2
ndiv = 25

path="."
dirList=os.listdir(path)
for fname in dirList:

    if re.search(imagepattern, fname, re.I):
        print ("match --> %s"  % (fname))
        data = Image.open(fname)
        source = data.split()
        chR = misc.fromimage(source[R])
        chG = misc.fromimage(source[G])
        chB = misc.fromimage(source[B])
        (dx, dy) = chR.shape
        print "Size: %d x %d" % (dx,dy)
        values = ""
        for i in range(0,ndiv):
            minx = round(i*dx/ndiv)
            maxx = round((i+1)*dx/ndiv)
            for j in range(0, ndiv):
                miny = round(j*dy/ndiv)
                maxy = round((j+1)*dy/ndiv)
                chR[minx:maxx,miny:maxy] = (0*chR[minx:maxx,miny:maxy]) + mean(chR[minx:maxx,miny:maxy])
                values += (" %f" % (mean(chR[minx:maxx,miny:maxy])))
        print values
        pylab.imshow(chR)
        pylab.show()
    else:
        print ("x: %s"  % (fname))
