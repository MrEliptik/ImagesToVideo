import cv2 as cv
import numpy as np
import os
import re

def tryint(s):
    try:
        return int(s)
    except:
        return s

def alphanum_key(s):
    """ Turn a string into a list of string and number chunks.
        "z23a" -> ["z", 23, "a"]
    """
    return [ tryint(c) for c in re.split('([0-9]+)', s) ]

def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    l.sort(key=alphanum_key)

test_path = 'example/images/'

img_array = []

for subdir, _, files in os.walk(test_path):
    print('[INFO] Working on: ' + str(subdir))
    sort_nicely(files)
    nb_files = len(files)

    # Assume all images are same dimensions
    height, width, layers = cv.imread(os.path.join(subdir, files[0])).shape
    size = (width, height)

    for _file in files:
        img = cv.imread(_file)
        img_array.append(img)

    
out = cv.VideoWriter('example/video/project.mp4', cv.VideoWriter_fourcc('m','p','v','4'), 15, size)

for i in range(len(img_array)):
    out.write(img_array[i])

out.release()
