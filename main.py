from flask import Flask, render_template, request
import os, shutil, time
from video_generation import make_reddit_story, make_wyr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/library', methods=["POST"])
def return_library():
    video_folder = 'static/output'  # Replace with the path to your folder
    video_list = []

    for filename in os.listdir(video_folder):
        if filename.endswith('.mp4'):  # Check if file is an mp4
            video_list.append(f"output/{filename}")  # Just append the file name, not the full path


    return render_template('library.html', videos=video_list)
    
@app.route('/video', methods=["POST"])
def generate_video():
    start_time = time.time()
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}: Starting video generation...")
    
    video_type = request.form.get("videoType")
    
    if video_type == "reddit":
        topic = request.form.get('topic')
        bg = request.form.get('reddit_bg')
        voice = request.form.get('reddit_voice')
        
        output_video = make_reddit_story(topic, bg, voice)
    elif video_type == "wyr":
        wyr_options_1 = request.form.getlist('wyr_option_1')
        wyr_options_2 = request.form.getlist('wyr_option_2')
        output_video = make_wyr(wyr_options_1, wyr_options_2)
        
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total time to generate function was {round(elapsed_time, 2)} seconds.")
    return render_template('video.html', output=output_video)

def clear_dirs():
    # Clean and recreate 'tts' directory
    if os.path.exists('temp'):
        shutil.rmtree('temp')
    os.makedirs('temp')
    
    # Clean and recreate 'static/output' directory
    if os.path.exists('static/output'):
        shutil.rmtree('static/output')
    os.makedirs('static/output')
    
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}: Successfully deleted all contents in 'temp' and 'static/output' folders.")


if __name__ == '__main__':
    # clear_dirs()
    # app.run(debug=True)
    app.run()
