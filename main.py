from flask import Flask, render_template, request, jsonify
import config
from editing import * 
from tiktok_voice_tts import tts
# import urllib.parse

videoTypes = {"reddit": "Reddit Story", "familyGuy": "Family Guy Clip"}

def main():
    input = ""
    # print(config.api_key)

    #with open("./text.txt") as file: 
        # print(file.readline())

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', videoTypes=videoTypes)
    
@app.route('/video', methods=["POST"])
def videos():
    videoType = request.form.get("videoType")
    
    topic = request.form.get('topic')
    if videoType == "reddit":
        red_story = request.form.get("red_story")
        promoGoal = request.form.get("promoGoal")
        # return f"hello VIDEO TYPE is {videoTypes[videoType]}. TOPIC is {topic} RED STORY is {red_story}. PROMO GOAL is {promoGoal}"
        
    #return f"hello {videoTypes[videoType]}"
    text = f"Hi you want a video that is about {topic} and a video that is a {videoTypes[videoType]}" # RUN texst = CHATGPT(USR INPUT) or whatever in future
    tts(text, "en_us_006", f"tts/{topic}_{videoType}_audio.mp3")
    reddit_story("resources/parkour.mp4", f"tts/{topic}_{videoType}_audio.mp3", f"static/output/{topic}_{videoType}.mp4", 0)
    
    # urllib.parse.quote(f"output/{topic}_{videoType}.mp4")
    return render_template('video.html', output=f"output/{topic}_{videoType}.mp4")
    # return f"hello {topic}. You chose a {videoType}. {red_story} and {promoGoal}  I have generated a video. /Users/j.jh.toh/Desktop/Software Development/Automated Shorts Creator/output/{topic}_{videoType}.mp4"

if __name__ == '__main__':
    main()
    app.run(debug=True)