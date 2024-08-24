from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip
import random

def reddit_story(video, audio, output, usr_input):
    # Load the video file
    
    # with AudioFileClip(audio_file) as audio_clip:
    #     # Get the duration of the audio clip (in seconds)
    #     duration = audio_clip.duration

    audio_clip = AudioFileClip(audio)
    video_clip = VideoFileClip(video)
    
    rnd_time = random.randint(200, int(video_clip.duration) - 200)
    video_clip = video_clip.subclip(rnd_time,rnd_time + audio_clip.duration)
    
    video_clip = video_clip.set_audio(audio_clip)

    # Write the result to a file
    video_clip.write_videofile(output, codec="libx264", audio_codec="aac")

    # Close the clips to release resources
    video_clip.close()
    audio_clip.close()

# reddit_story("resources/parkour.mp4", "resources/output.mp3", "output/output_video.mp4", 0)

