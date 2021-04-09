from converter import (ImageConverter, VideoConverter)
import asyncio
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("-img", "--image", help="Convert Image", action="store_true")
parser.add_argument("-vid", "--video", help="Convert Video", action="store_true")

parser.add_argument("-f", "--file", help="Path To File | File Name", type=str)
parser.add_argument("-rgb", "--color", help="RGB", action="store_true")

arguments = parser.parse_args()


if arguments.image and arguments.video:
    raise Exception("Choose from two options: video or image")

if not arguments.file:
    raise Exception("File not specified")

if arguments.image:
    asyncio.run(
        ImageConverter().convert(
            arguments.file, 
            RGB=arguments.color or False
        )
    )
elif arguments.video:
    asyncio.run(
        VideoConverter().convert(
            arguments.file, 
            convert_gs=not arguments.color if arguments.color is not None else False
        )
    )

else:
    raise Exception("The conversion method is not specified")
