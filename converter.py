import cv2 as cv
import numpy as np
import os
import re
import argparse

codecs = ["mp4v", "xvid", "mjpg", "h264", "avc1"]
extensions = [".mp4", ".mkv", ".avi"]


def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
    """

    def tryint(s):
        try:
            return int(s)
        except:
            return s

    def alphanum_key(s):
        """ Turn a string into a list of string and number chunks.
            "z23a" -> ["z", 23, "a"]
        """
        return [tryint(c) for c in re.split("([0-9]+)", s)]

    l.sort(key=alphanum_key)


def convert(inputs, output, extension, codec, output_size=(None, None)):
    # Assume all images are same dimensions
    height, width, layers = inputs[0].shape
    size = (width, height)

    out = cv.VideoWriter(output + extension, cv.VideoWriter_fourcc(*codec), 15, size)

    # WORKS:
    # out = cv.VideoWriter(output + extension, cv.VideoWriter_fourcc('M','J','P','G'), 15, size) #Big file size
    # out = cv.VideoWriter(output + extension, cv.VideoWriter_fourcc('X','V','I','D'), 15, size)
    # out = cv.VideoWriter(output + '.mp4', cv.VideoWriter_fourcc(*"mp4v"), 15, size)
    # out = cv.VideoWriter(output + '.mp4', cv.VideoWriter_fourcc(*"mp4v"), 15, size)
    # out = cv.VideoWriter('example/video/project.mkv', cv.VideoWriter_fourcc(*"mp4v"), 15, size)

    # MISSING CODEC:
    # out = cv.VideoWriter('example/video/project.mkv', cv.VideoWriter_fourcc(*"h264"), 15, size)
    # out = cv.VideoWriter('example/video/project.mp4', cv.VideoWriter_fourcc(*"avc1"), 15, size)

    for i in range(len(inputs)):
        out.write(inputs[i])

    out.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--inputs",
        type=str,
        required=True,
        help="path to input files (PNG, JPEG, TIFF, JFIF, BMP, JPG)",
    )
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="path to output video",
    )
    parser.add_argument(
        "--container",
        type=str,
        default=".mp4",
        choices=extensions,
        help="container used for video (.mp4, .mkv, .avi), default: .mp4"
    )
    parser.add_argument(
        "--codec",
        type=str,
        default="mp4v",
        choices=codecs,
        help="codec for video encoding (mp4v, xvid, mjpg, h264, avc1), default: mp4v",
    )
    parser.add_argument(
        "--width",
        type=int,
        required=False,
        help="width to reisze the output video"
    )
    parser.add_argument(
        "--height",
        type=int,
        required=False,
        help="height to reisze the output video"
    )

    FLAGS = parser.parse_args()

    img_array = []

    for subdir, _, files in os.walk(FLAGS.inputs):
        print("[INFO] Working on: {}".format(subdir))
        sort_nicely(files)
        nb_files = len(files)
        print("     >>> Found {} files".format(nb_files))

        for _file in files:
            img = cv.imread(os.path.join(subdir, _file))
            img_array.append(img)

    convert(img_array, FLAGS.output, FLAGS.container, FLAGS.codec)
    print("[INFO] Successfully written video: {}".format(FLAGS.output + FLAGS.container))
