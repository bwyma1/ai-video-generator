from video_generator import VideoGenerator
from sys import argv

tiktok_generator = VideoGenerator(argv[1])
tiktok_generator.generate_video()
