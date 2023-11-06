from moviepy.editor import *
from PIL import Image

class VideoGenerator(object):
    def __init__(self,movie):
        """ Initialize with a movie (must be .mp4) """
        self.movie = movie
        self.audio = movie.audio

    def _splice_movie(self, timestamps):
        """ Using the timestamps, the function will splice together
            the movie clips. Timestamps is a list of lists."""
        if(len(timestamps) == 0):
            raise ValueError("Timestamps can't be empty")
        clips = []
        for i in range(0, len(timestamps)):
            clips.append(self.movie.subclip(timestamps[i][0], timestamps[i][1]))
        return concatenate_videoclips(clips)

    def _splice_audio(self, timestamps):
        """ Using the timestamps, the function will splice together
            the audio clips. Timestamps is a list of lists."""
        if(len(timestamps) == 0):
            raise ValueError("Timestamps can't be empty")
        clips = []
        for i in range(0, len(timestamps)):
            clips.append(self.audio.subclip(timestamps[i][0], timestamps[i][1]))
        return concatenate_audioclips(clips)
    
    def generate_video(self):
        """ Generates an amazing, emotional TikTok short video  using AI
            technology to find the most emotional and aesthetic scenes"""
                         
        