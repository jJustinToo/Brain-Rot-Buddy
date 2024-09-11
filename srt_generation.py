import whisper

model = whisper.load_model("base")

def transcribe(file_path): 
    transcription = model.transcribe(file_path, word_timestamps=True)

    # Extract word timings from the transcription
    words = []
    for segment in transcription['segments']:
        for word in segment.get('words', []):
            words.append({
                "text": word.get('word', ''),  # Use 'word' key instead of 'text'
                "start": word.get('start', 0),
                "end": word.get('end', 0)
            })
        
    print("Script has been transcribed")
    return words