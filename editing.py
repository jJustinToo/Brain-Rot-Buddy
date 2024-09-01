from moviepy.editor import VideoFileClip, AudioFileClip
import random
# import time

def editRedditStory(background_video_path: str, tts_path: str, output_path: str, usr_input: list = {}):
    with AudioFileClip(tts_path) as audio_clip, VideoFileClip(background_video_path) as video_clip:
        # Select a random start time for the video subclip
        rnd_time = random.randint(0, int(video_clip.duration - audio_clip.duration))
        # Create abclip of the video with the same duration as the audio
        sub_video_clip = video_clip.subclip(rnd_time, rnd_time + audio_clip.duration)
        # Set the audio to the subclip
        final_clip = sub_video_clip.set_audio(audio_clip)
        # Write the final video to a file using multithreading
        final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", threads=6)

# start_time = time.time()  # Record the start time
# editRedditStory("resources/parkour.mp4", "he_reddit_audio.mp3", "output_video.mp4")
# end_time = time.time()  # Record the end time
# elapsed_time = end_time - start_time  
# print(elapsed_time)


