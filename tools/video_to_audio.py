from moviepy.editor import VideoFileClip
import os

def video_to_audio(video_filename: str):
    """Extract the audio for a given video file."""

    # Specify the path to your video file (can be any format)
    video_path = os.path.join(os.path.abspath("."), "tmp", video_filename)

    # Load the video file
    print("Convirtiendo el video a audio")
    video = VideoFileClip(video_path)

    # Extract audio from the video and save it as an MP3 file
    video.audio.write_audiofile(os.path.join(os.path.abspath("."), "tmp", "output.mp3"), codec="libmp3lame")
    return os.path.join(os.path.abspath("."), "tmp", "output.mp3")

# transcribe_file("pum_video.mp4")