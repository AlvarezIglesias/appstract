from moviepy.editor import VideoFileClip
import os

def video_to_audio(video_filename: str):
    """Extract the audio for a given video file."""
    video_path = os.path.join(os.path.abspath("."), video_filename)
    print("Convirtiendo el video a audio")
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(os.path.join(os.path.abspath("."), "tmp", "output.mp3"), codec="libmp3lame")
    return os.path.join(os.path.abspath("."), "tmp", "output.mp3")

# transcribe_file("pum_video.mp4")