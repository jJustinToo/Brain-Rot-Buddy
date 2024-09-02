from flask import Flask, render_template, request, jsonify
import config
from text_to_speech import tts
from editing import * 
from chatbot import *
import os, shutil, time

videoTypes = {"reddit": "Reddit Story", "movieClip": "Movie Clip", "wyr": "Would You Rather"}
loading_video = []

def main():
    if os.path.exists('tts'):
        shutil.rmtree('tts')
    os.makedirs('tts')
    os.makedirs('tts/wyr')
    
    if os.path.exists('static/output'):
        shutil.rmtree('static/output')
    os.makedirs('static/output')
    
    print(f"{(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))}: " + colored('Successfully deleted all contents in "tts" folder and "static/output" folder.', "red"))
    
    input = ""
    # print(config.api_key)
        
        
def redditStory(videoType, topic, userInput):
    text = generateRedditStory(topic)
    # text = f"Hi you want a video that is about {topic} and a video that is a {videoTypes[videoType]}" # RUN texst = CHATGPT(USR INPUT) or whatever in future
    tts(text, "en_us_006", f"tts/{topic}_{videoType}_audio.mp3") # Generate TTS file
    editRedditStory("resources/parkour.mp4", f"tts/{topic}_{videoType}_audio.mp3", f"static/output/{topic}_{videoType}.mp4", userInput) # Generate video


def movieClip():
    pass


def wyr(op1_list, op2_list):
    print(op1_list)
    for i in range(len(op1_list)):
        text = f"Would you rather {op1_list[i]}. . . . . or Would you rather {op2_list[i]}"
        tts(text, "en_us_006", f"tts/wyr/audio_{i+1}.mp3") # Generate TTS file
        
    editWYR()
    pass
    # GENERATE TEX

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', videoTypes=videoTypes)
    
@app.route('/video', methods=["POST"])
def videos():
    videoType = request.form.get("videoType")
    topic = request.form.get('topic')
    
    # videoTypes[videoType]
    
    start_time = time.time()  # Record the start time
    print(f"{(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))}: Starting video generation...")
    if videoType == "reddit":
        userInput = {"red_story": request.form.get("red_story"), "promoGoal": request.form.get("promoGoal")}
        redditStory(videoType, topic, userInput)
    elif videoType == "familyGuy":
        movieClip()
    elif videoType == 'wyr':
        wyr_options_1 = request.form.getlist('wyr_option_1')
        wyr_options_2 = request.form.getlist('wyr_option_2')
        
        print(wyr_options_1)
        wyr(wyr_options_1, wyr_options_2)
        
    
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  
    print(f"Total time to generate function was {elapsed_time} seconds.")
    return render_template('video.html', output=f"output/{topic}_{videoType}.mp4") # THIS IS JUST EXAMPLE. EACH TYPE SHOULD RETURN ITS OWN FILE. I NEED BETTER FILE MANAGAEMENT.
    
    
if __name__ == '__main__':
    main()
    # app.run()
    app.run(debug=True)