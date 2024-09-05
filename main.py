from flask import Flask, render_template, request
import os
import shutil
import time
from text_to_speech import tts
from compile_video import editRedditStory, editWYR
from chat_generation import generateRedditStory

# Define video types
videoTypes = {
    "reddit": "Reddit Story",
    "movieClip": "Movie Clip",
    "wyr": "Would You Rather"
}

def setup_directories():
    """Set up the necessary directories for video processing."""
    # # Clean and recreate 'tts' directory
    # if os.path.exists('tts'):
    #     shutil.rmtree('tts')
    # os.makedirs('tts')
    
    # # Clean and recreate 'static/output' directory
    # if os.path.exists('static/output'):
    #     shutil.rmtree('static/output')
    # os.makedirs('static/output')
    
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}: Successfully deleted all contents in 'tts' and 'static/output' folders.")


def process_reddit_story(topic, userInput):
    """Generate a Reddit story video."""
    text = generateRedditStory(topic)
    tts(text, "en_us_006", f"tts/reddit_audio.mp3")  # Generate TTS file
    editRedditStory("resources/parkour_horizontal.mp4", f"tts/reddit_audio.mp3", f"static/output/reddit_video.mp4")  # Generate video
    return f"output/reddit_video.mp4"


def process_wyr(op1_list, op2_list):
    """Generate a Would You Rather video."""
    
    tts_files = []
    for i in range(len(op1_list)):
        tts(f"Would you rather have {op1_list[i]} or {op2_list[i]}", "en_us_006", f"tts/wyr_{i+1}.mp3")  # Generate TTS file
        tts_files.append(f"tts/wyr_{i+1}.mp3")
        
    # editWYR(tts_files)  # Edit WYR video
    return # returns file loc

app = Flask(__name__)

@app.route('/')
def index():
    """Render the index page."""
    setup_directories()
    return render_template('index.html', videoTypes=videoTypes)
    
@app.route('/video', methods=["POST"])
def generate_video():
    """Handle video generation based on user input."""
    videoType = request.form.get("videoType")
    topic = request.form.get('topic')
    
    # Record start time
    start_time = time.time()
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}: Starting video generation...")

    if videoType == "reddit":
        userInput = {
            "red_story": request.form.get("red_story"),
            "promoGoal": request.form.get("promoGoal")
        }
        output = process_reddit_story(topic, userInput)
    elif videoType == "movieClip":
        # Placeholder for movie clip processing
        pass
    elif videoType == 'wyr':
        wyr_options_1 = request.form.getlist('wyr_option_1')
        wyr_options_2 = request.form.getlist('wyr_option_2')
        output = process_wyr(wyr_options_1, wyr_options_2)
        
    # Record end time
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total time to generate function was {round(elapsed_time, 2)} seconds.")
    # output = f"output/{topic}_{videoType}.mp4"
    # Return the path to the generated video
    return render_template('video.html', output=output)

if __name__ == '__main__':
    setup_directories()
    # app.run(debug=True)
    app.run()
