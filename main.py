from video_generator import VideoGenerator
from sys import argv
import whisper_timestamped as whisper


tiktok_generator = VideoGenerator(argv[1])
tiktok_generator.generate_video(argv[2])
