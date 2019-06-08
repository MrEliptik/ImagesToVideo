# ImagesToVideo

Create a video from a series of images. Ideal to make timelapse.

## How to use

**CAREFUL: The script assumes all input images are the same size!**

Call **converter.py** with the path to your images, the output video path, codec and container to use. Example: 

    python converter.py --inputs=example/images/ --output=example/video/example --container=.mp4 --codec=mp4v

By default the output video is going to be encoded at 30fps. Use the `--fps` parameter to change that. Example:

    python converter.py --inputs=example/images/ --output=example/video/example --container=.mp4 --codec=mp4v --fps=15

### Codecs

Codecs are used to encode your video. Before choosing a codec, make sure it's available on your computer. The default ones like: *mjpg, xvid, mp4v* should be available by default. For *avc1, h264* you might need to install dependencies first, see [requirements](##requirements).

Supported codecs are:

- mp4v
- mjpg
- xvid
- avc1
- h264

### Containers

Containers are the extension you'll see at the end of your file. Multiple codecs can use the same container, but some codecs can't be use with certain containers. Use the following table to see what container/codec pair is accepted.

|      | mp4v | mpjg | xvid | avc1 | h264 |
|----- |:----:|:----:|:----:|:----:|:----:|
| .mp4 |   ✔️  |   ❌ |   ❌ |   ✔️  |   ✔️  |
| .avi |   ❌ |   ✔️  |   ✔️  |   ❌ |   ✔️  |
| .mkv |   ✔️  |   ❌ |   ❌ |   ✔️  |   ✔️  |

See the following [benchmark](https://github.com/opencv/opencv/wiki/Video-capture-and-write-benchmark) to help you chose the right combination.

## Requirements

See *requirements.txt* file or run:

    pip install -r requirements.txt