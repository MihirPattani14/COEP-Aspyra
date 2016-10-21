__author__ = 'pshubham'
import os
import moviepy.editor as mp
import subprocess
def convert(updir,filename):
    clip = mp.VideoFileClip(os.path.join(updir, filename))
    clip.write_videofile(os.path.join(updir, filename.split('.')[0]+'.mp4'))
    subprocess.call('rm '+os.path.join(updir, filename),shell=True)

