import random
from moviepy.editor import AudioFileClip, VideoFileClip, TextClip, CompositeVideoClip, ImageClip, concatenate_audioclips
from PIL import Image
from text_to_speech import tts
from srt_generation import transcribe
from chat_generation import generate_text
import image_download

def make_reddit_story(topic, bg, voice):
    # Generate Text with Gemma2
    
    generation = generate_text("reddit", topic)
    
    text = "".join(generation)
    tts_file_path = f"temp/reddit_{topic}_audio.mp3"
    tts(text, voice, tts_file_path)  # Generate TTS file
    bg_file = f"resources/{bg}.mp4"
    
    words = transcribe(tts_file_path)

    # Create Actual Video File
    with AudioFileClip(tts_file_path) as audio_clip, VideoFileClip(bg_file, target_resolution=(854,480)) as video_clip:
    
        rnd_time = random.randint(0, int(video_clip.duration - audio_clip.duration))
        sub_video_clip = video_clip.subclip(rnd_time, rnd_time + audio_clip.duration)
        
        
        # image_clip = (ImageClip("resources/reddit_post.png")
        #       .resize(height=50)   # Resize to a height of 200px, width adjusts automatically
        #       .set_duration(5)
        #       .set_position(('center', 0.3))
        #       .set_start(0))
        
        # title = (TextClip(generation[0], fontsize=30, color='Black', font='IBM Plex Sans')
        #                .set_position(('center', 0.8))  # adjust position over the image
        #                .set_duration(5)
        #                .set_start(0))
        
        text_clips = []
        
        for word in words:
            text_clip = (TextClip(word['text'], fontsize=48, color='white', font='Proxima-Nova-Semibold')
                         .set_position(('center', 'center'))
                         .set_start(word['start'])
                         .set_duration(word['end'] - word['start']))
            text_clips.append(text_clip)
        
        final_clip = CompositeVideoClip([sub_video_clip] + text_clips)

        
        # current_phrase = ""
        # current_start = 0  # To track the start time of a phrase
        # phrase_duration = 0  # To track the duration of the current phrase

        # for i, word in enumerate(words):
        #     if current_phrase == "":
        #         # Start a new phrase
        #         current_start = word['start']
            
        #     current_phrase += word['text'] + " "  # Add word to the phrase
        #     phrase_duration = word['end'] - current_start  # Adjust duration for the phrase

        #     # Check if we should end the phrase (either at the end of the sentence or based on timing)
        #     if (i == len(words) - 1) or (words[i + 1]['start'] - word['end'] > 0.5):  # 0.5 seconds gap between phrases
        #         text_clip = (TextClip(current_phrase.strip(), fontsize=48, color='white', font='Proxima-Nova-Semibold')
        #                     .set_position(('center', 'center'))
        #                     .set_start(current_start)
        #                     .set_duration(phrase_duration))
                
        #         text_clips.append(text_clip)
                
        #         # Reset for the next phrase
        #         current_phrase = ""
        #         current_start = 0
        #         phrase_duration = 0

        # # Final composite video
        # final_clip = CompositeVideoClip([sub_video_clip, title] + text_clips)

        
        final_clip = final_clip.set_audio(audio_clip)

        final_clip.write_videofile(f"static/output/reddit_{topic}_video.mp4", codec="libx264", audio_codec="aac", threads=8, fps=24)
    
    return f"output/reddit_{topic}_video.mp4"

def make_wyr(op1_list, op2_list):
    tts_files = []
    image_files = []
    for i in range(len(op1_list)):
        tts(f"Would you rather have {op1_list[i]} or {op2_list[i]}", "en_us_006", f"temp/wyr_{i+1}.mp3")  # Generate TTS file
        tts_files.append(f"temp/wyr_{i+1}.mp3")
        
        # image_download.download_image(op1_list[i])
        # image_files.append(f"temp/images/{op1_list[i]}")
        # image_download.download_image(op2_list[i])
        # image_files.append(f"temp/images/{op2_list[i]}")
        
    
    image = ImageClip("resources/wyr_bg.png")
    
    audio_clips = []
    for i, audio in enumerate(tts_files):
        audio_clips.append(AudioFileClip(audio))
        audio_clips.append(AudioFileClip("resources/ticking.mp3"))
    
    
    final_audio = concatenate_audioclips(audio_clips)

    image = image.set_duration(final_audio.duration)

    video = image.set_audio(final_audio)

    # Write the result to a file
    video.write_videofile("static/output/wyr_output.mp4", codec="libx264", audio_codec="aac", fps=24)
    
    return "output/wyr_output.mp4"
