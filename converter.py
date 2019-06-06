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
    return [tryint(c) for c in re.split('([0-9]+)', s)]


def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """
    l.sort(key=alphanum_key)


test_path = 'example/images/'


def convert(inputs, output, extension, codec, output_size=(None, None)):
    # Assume all images are same dimensions
    height, width, layers = inputs[0].shape
    size = (width, height)

    # WORKS:
    # out = cv.VideoWriter('example/video/project.avi', cv.VideoWriter_fourcc('M','J','P','G'), 15, size) #Big file size
    out = cv.VideoWriter(output + extension, cv.VideoWriter_fourcc('X','V','I','D'), 15, size)

    # MISSING CODEC:
    # out = cv.VideoWriter('example/video/project.mp4', cv.VideoWriter_fourcc('M','P','V','4'), 15, size)
    # out = cv.VideoWriter('example/video/project.mkv', cv.VideoWriter_fourcc('M','P','V','4'), 15, size)
    # out = cv.VideoWriter('example/video/project.mp4', cv.VideoWriter_fourcc('H','2','6','4'), 15, size)
    # out = cv.VideoWriter('example/video/project.mkv', cv.VideoWriter_fourcc('H','2','6','4'), 15, size)
    # out = cv.VideoWriter('example/video/project.mp4', cv.VideoWriter_fourcc('A','V','C','1'), 15, size)

    for i in range(len(inputs)):
        out.write(inputs[i])

    out.release()


if __name__ == "__main__":
    img_array = []

    for subdir, _, files in os.walk(test_path):
        print('[INFO] Working on: ' + str(subdir))
        sort_nicely(files)
        nb_files = len(files)

        for _file in files:
            img = cv.imread(os.path.join(subdir, _file))
            img_array.append(img)

    convert(img_array, 'example/video/example', '.avi', 'XVID')
