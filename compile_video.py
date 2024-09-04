from moviepy.editor import VideoFileClip, AudioFileClip, ImageClip, TextClip, CompositeVideoClip, concatenate_audioclips
import random
import whisper
# import time

model = whisper.load_model("small")
# def editRedditStory(background_video_path: str, tts_path: str, output_path: str, usr_input: list = {}):
#     with AudioFileClip(tts_path) as audio_clip, VideoFileClip(background_video_path) as video_clip:
#         # Select a random start time for the video subclip
#         rnd_time = random.randint(0, int(video_clip.duration - audio_clip.duration))
#         # Create abclip of the video with the same duration as the audio
#         sub_video_clip = video_clip.subclip(rnd_time, rnd_time + audio_clip.duration)
#         # Set the audio to the subclip
#         final_clip = sub_video_clip.set_audio(audio_clip)
#         # Write the final video to a file using multithreading
#         final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", threads=6)
        

def editRedditStory(background_video_path: str, tts_path: str, output_path: str):
    # Load the Whisper model
    
    # Transcribe the audio and get word-level timestamps
    transcription = model.transcribe(tts_path, word_timestamps=True)

    # Extract word timings from the transcription
    words = []
    for segment in transcription['segments']:
        for word in segment.get('words', []):
            words.append({
                "text": word.get('word', ''),  # Use 'word' key instead of 'text'
                "start": word.get('start', 0),
                "end": word.get('end', 0)
            })

    
    # Load audio and video clips
    with AudioFileClip(tts_path) as audio_clip, VideoFileClip(background_video_path) as video_clip:
        rnd_time = random.randint(0, int(video_clip.duration - audio_clip.duration))
        
        # Create a subclip of the video with the same duration as the audio
        sub_video_clip = video_clip.subclip(rnd_time, rnd_time + audio_clip.duration)
        
        # Create a list of TextClips for each word
        text_clips = []
        for word in words:
            text_clip = (TextClip(word['text'], fontsize=48, color='white', font='Proxima-Nova-Semibold')
                         .set_position(('center', 'center'))
                         .set_start(word['start'])
                         .set_duration(word['end'] - word['start']))
            text_clips.append(text_clip)
        
        # Create a composite video clip that overlays the text clips onto the video
        final_clip = CompositeVideoClip([sub_video_clip] + text_clips)
        
        # Set the audio to the composite clip
        final_clip = final_clip.set_audio(audio_clip)
        
        # Write the final video to a file using multithreading
        final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac", threads=6)

# Example usage
# editRedditStory("resources/parkour_horizontal.mp4", "output.mp3", "output_video1.mp4")

        
def editWYR(tts_files):
    # Load the image
    image = ImageClip("path_to_image.jpg")

    # Load all the audio files
    audio_files = ["audio1.mp3", "audio2.mp3", "audio3.mp3"]  # Replace with your file names
    audio_clips = [AudioFileClip(audio) for audio in audio_files]

    # Concatenate all the audio files
    final_audio = concatenate_audioclips(audio_clips)

    # Set the duration of the image clip to match the total duration of the audio
    image = image.set_duration(final_audio.duration)

    # Set the audio of the image clip to the concatenated audio
    video = image.set_audio(final_audio)

    # Write the result to a file
    video.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac")

    
    
    # Audio files. 
    # Images.
    # Background, Music. Ticking sound. 
    
    # take all audio files in tts / wyr folder with name == {topic}_{topic}_{i+1}
    # Speech to text that audio. Add images when needed. 

# start_time = time.time()  # Record the start time
# editRedditStory("resources/parkour.mp4", "he_reddit_audio.mp3", "output_video.mp4")
# end_time = time.time()  # Record the end time
# elapsed_time = end_time - start_time  
# print(elapsed_time)


