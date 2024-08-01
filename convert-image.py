#!/usr/bin/env python

import os
from PIL import Image

angle = -90         #Enter the angle you want to rotate the image
size = (128, 128)   #Enter the size you want to resize the image

src_dir = "images/"       #Enter your file path to a sauce directory
dst_dir = "/opt/icons/"   #Enter your file path to a destination directory

for infile in os.listdir(src_dir):

    ftitle, fext = os.path.splitext(infile)
    outfile = os.path.join(dst_dir, ftitle)

    if infile != outfile:
        try:
            im = Image.open(src_dir + infile)
            im.rotate(angle).resize(size).convert("RGB").save(outfile, "JPEG")

        except OSError:
                print("cannot convert", infile)
