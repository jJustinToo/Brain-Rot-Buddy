from moviepy.editor import VideoFileClip, AudioFileClip
import random

def editRedditStory(background_video_path: str, tts_path: str, output_path: str, usr_input: list = {}):
    with AudioFileClip(tts_path) as audio_clip, VideoFileClip(background_video_path) as video_clip:
        
        # Select a random start time for the video subclip
        rnd_time = random.randint(0, int(video_clip.duration - audio_clip.duration))
        
        # Create a subclip of the video with the same duration as the audio
        sub_video_clip = video_clip.subclip(rnd_time, rnd_time + audio_clip.duration)
        
        # Set the audio to the subclip
        final_clip = sub_video_clip.set_audio(audio_clip)
        
        # Write the final video to a file using multithreading
        final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", threads=6)

# editRedditStory("resources/background.mov", "resources/output.mp3", "output/output_video.mp4", 0)

