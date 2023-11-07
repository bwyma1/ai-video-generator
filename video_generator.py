from moviepy.editor import *
import whisper_timestamped as whisper

class VideoGenerator(object):
    def __init__(self,movie):
        """ Initialize with a movie (must be .mp4) """
        self.movie = movie
        self.vfc_movie = VideoFileClip(movie)
        self.text_w_timestamps = []
        self.transcript = ''

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
        audio = self.vfc_movie.audio
        if(len(timestamps) == 0):
            raise ValueError("Timestamps can't be empty")
        clips = []
        for i in range(0, len(timestamps)):
            clips.append(audio.subclip(timestamps[i][0], timestamps[i][1]))
        return concatenate_audioclips(clips)
    
    def _generate_text_w_timestamps(self):
        """ Using the whisper_timestamped package from 
            https://github.com/linto-ai/whisper-timestamped the 
            function will create a full timestamped transcript of the movie."""
        audio = whisper.load_audio(self.movie)
        model = whisper.load_model("base")

        result = whisper.transcribe(model, audio, language="en")

        for segment in result['segments']:
            for word in segment['words']:
                self.transcript += ' ' + word['text']
                self.text_w_timestamps.append([word['text'],word['start']])

    def _generate_phrase_audio(self, phrases):
        """ Given phrases (list of string), the function will find and return an 
            AudioFileClip object containing the audio for that phrases """
        timestamps = []
        for phrase in phrases:
            phrase = phrase.split()
            for i in range(0,len(self.text_w_timestamps)-len(phrase)):
                matching = True
                for j in range(0,len(phrase)):
                    if(self.text_w_timestamps[i+j][0] != phrase[j]):
                        matching = False
                if(matching):
                    timestamps.append(self._splice_audio(
                        [self.text_w_timestamps[i][1],
                         self.text_w_timestamps[i+len(phrase)-1][1] ]))
                    break
        return self._splice_audio(timestamps)

    def generate_video(self, outputFile):
        """ Generates an amazing, emotional TikTok short video  using AI
            technology to find the most emotional and aesthetic scenes"""
                         
        