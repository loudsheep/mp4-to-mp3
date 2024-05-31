from moviepy.editor import VideoFileClip
from datetime import datetime
import os
import subprocess


def convert():
    inp = input("Enter source file path (.mp4): ")
    now = datetime.now()
    date_time_today = now.strftime("%m_%d_%Y_%H_%M_%S")
    out_dir = "./OUT/" + date_time_today
    mp3_file = os.path.join(out_dir, "out.mp3")

    os.mkdir(out_dir)

    # Load the video clip
    video_clip = VideoFileClip(inp)

    # Extract the audio from the video clip
    audio_clip = video_clip.audio

    # Write the audio to a separate file
    audio_clip.write_audiofile(mp3_file)

    # Close the video and audio clips
    audio_clip.close()
    video_clip.close()
    print("Audio extraction successful!")

    subprocess.Popen(r'explorer /select,"' + os.path.abspath(mp3_file) + '"')


if __name__ == '__main__':
    convert()
