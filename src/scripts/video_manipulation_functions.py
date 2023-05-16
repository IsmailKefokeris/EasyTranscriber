import ffmpeg
import os
import subprocess

def video_to_mp3(video, filename, output_ext="mp3"):
    subprocess.run(["ffmpeg", "-y", "-i", video, f"{filename}.{output_ext}"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

    return f"{filename}.{output_ext}"

def delete_video(video):
    pass