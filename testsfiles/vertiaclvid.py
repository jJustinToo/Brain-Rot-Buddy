from moviepy.editor import VideoFileClip, CompositeVideoClip

def create_vertical_video(foreground_clip_path, background_clip_path, output_filename="output.mp4"):
    # Load the foreground and background clips
    foreground_clip = VideoFileClip(foreground_clip_path)
    background_clip = VideoFileClip(background_clip_path)

    # Resize the foreground clip to 1080x1920 and crop it to the top
    resized_foreground = foreground_clip.resize(width=1080).crop(x1=0, y1=0, x2=1080, y2=1920)

    # Resize the background clip to 1080x1920 (maintaining aspect ratio)
    background_clip = background_clip.resize((1080, 1920)).crop(x1=0, y1=0, x2=1080, y2=1920)
    
    # DO THIS HERE

    # Combine the foreground on top of the background
    final_clip = CompositeVideoClip([background_clip, resized_foreground.set_position(("center", "top"))])

    # Write the final video to a file
    final_clip.write_videofile(output_filename, codec="libx264", audio_codec="aac")

# Example usage
create_vertical_video("outputTMP/MyWay.mp4", "outputTMP/output_video.mp4", "final_output.mp4")
