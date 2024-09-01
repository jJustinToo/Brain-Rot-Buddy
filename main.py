from flask import Flask, render_template, request, jsonify
import config
from text_to_speech import tts
from editing import * 
from chatbot import *
import os, shutil

videoTypes = {"reddit": "Reddit Story", "movieClip": "Movie Clip"}
loading_video = []

def main():
    if os.path.exists('tts'):
        shutil.rmtree('tts')
    os.makedirs('tts')
    
    if os.path.exists('static/output'):
        shutil.rmtree('static/output')
    os.makedirs('static/output')
    
    print('Successfully deleted all contents in "tts" folder and "static/output" folder.')
    
    input = ""
    # print(config.api_key)
        
        
def redditStory(videoType, topic, userInput):
    text = generateRedditStory(topic)
    # text = f"Hi you want a video that is about {topic} and a video that is a {videoTypes[videoType]}" # RUN texst = CHATGPT(USR INPUT) or whatever in future
    tts(text, "en_us_006", f"tts/{topic}_{videoType}_audio.mp3") # Generate TTS file
    editRedditStory("resources/parkour.mp4", f"tts/{topic}_{videoType}_audio.mp3", f"static/output/{topic}_{videoType}.mp4", userInput) # Generate video


def movieClip():
    pass


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', videoTypes=videoTypes)
    
@app.route('/video', methods=["POST"])
def videos():
    videoType = request.form.get("videoType")
    topic = request.form.get('topic')
    
    # videoTypes[videoType]
    
    if videoType == "reddit":
        userInput = {"red_story": request.form.get("red_story"), "promoGoal": request.form.get("promoGoal")}
        redditStory(videoType, topic, userInput)
    elif videoType == "familyGuy":
        movieClip()
    
    return render_template('video.html', output=f"output/{topic}_{videoType}.mp4")
    
    
if __name__ == '__main__':
    main()
    app.run(debug=True)