#This throws an error, but still works so ¯\_(ツ)_/¯.
from moviepy.editor import *

clip = (VideoFileClip("video.mp4")
        .subclip((3),(5))
        .resize(0.3))
clip.write_gif("mesmerising.gif")
