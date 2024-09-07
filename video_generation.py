import random
from moviepy.editor import AudioFileClip, VideoFileClip, TextClip, CompositeVideoClip, ImageClip, concatenate_audioclips
from text_to_speech import tts
from srt_generation import transcribe
from chat_generation import generate_text

def make_reddit_story(topic, bg, voice):
    # Generate Text with Gemma2
    
    generation = generate_text("reddit", topic)
    text = "".join(generation)
    tts_file_path = f"tts/reddit_{topic}_audio.mp3"
    tts(text, voice, tts_file_path)  # Generate TTS file
    bg_file = f"resources/{bg}.mp4"
    
    words = transcribe(tts_file_path)

    # Create Actual Video File
    with AudioFileClip(tts_file_path) as audio_clip, VideoFileClip(bg_file) as video_clip:
        rnd_time = random.randint(0, int(video_clip.duration - audio_clip.duration))
        sub_video_clip = video_clip.subclip(rnd_time, rnd_time + audio_clip.duration)
        
        text_clips = []
        for word in words:
            text_clip = (TextClip(word['text'], fontsize=48, color='white', font='Proxima-Nova-Semibold').set_position(('center', 'center')).set_start(word['start']).set_duration(word['end'] - word['start']))
            text_clips.append(text_clip)
        
        final_clip = CompositeVideoClip([sub_video_clip] + text_clips)
        
        final_clip = final_clip.set_audio(audio_clip)
        
        final_clip.write_videofile(f"static/output/reddit_{topic}_video.mp4", codec="libx264", audio_codec="aac", threads=8)
    
    return f"output/reddit_{topic}_video.mp4"

def make_wyr(op1_list, op2_list):
    tts_files = []
    for i in range(len(op1_list)):
        tts(f"Would you rather have {op1_list[i]} or {op2_list[i]}", "en_us_006", f"tts/wyr_{i+1}.mp3")  # Generate TTS file
        tts_files.append(f"tts/wyr_{i+1}.mp3")
    
    image = ImageClip("path_to_image.jpg")
    
    audio_clips = []
    for audio in tts_files:
        audio_clips.append(AudioFileClip(audio))
        audio_clips.append(AudioFileClip(ticking.mp3))
        audio_clips.append(AudioFileClip())
    
    
    final_audio = concatenate_audioclips(audio_clips)

    # Set the duration of the image clip to match the total duration of the audio
    image = image.set_duration(final_audio.duration)

    # Set the audio of the image clip to the concatenated audio
    video = image.set_audio(final_audio)

    # Write the result to a file
    video.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac")
    
    # Text shows up when WOULD YOU RATHER lengths.
    # Text shows up when WOULD YOU RAHTER + OP1 + OR
    
    
    return # returns file loc

# make_reddit_story("fortntie", "bg", "en_us_006")