from flask import Flask, request, jsonify, render_template
from vosk import Model, KaldiRecognizer
import soundfile as sf
import numpy as np
import wave
import os
import json
from openai import OpenAI
from moderation import check_violence_threat
from plyer import notification
import threading
import logging

logging.getLogger('vosk').setLevel(logging.ERROR)

app = Flask(__name__)

# Load the model once at startup
vosk_model = Model("vosk-model-small-en-us")

def show_notification(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            timeout=5
        )
    except Exception as e:
        print(f"Failed to show notification: {str(e)}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save-audio', methods=['POST'])
def save_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file received'})
    
    audio_file = request.files['audio']
    
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    
    # Save the file
    filepath = os.path.join('uploads', 'recording.wav')
    audio_file.save(filepath)
    
    try:
        # Use the pre-loaded model
        wf = wave.open(filepath, "rb")
        recognizer = KaldiRecognizer(vosk_model, wf.getframerate())
        
        while True:
            data = wf.readframes(4000)
            if len(data) == 0:
                break
            recognizer.AcceptWaveform(data)
        
        result = recognizer.FinalResult()
        
        # Extract the text from Vosk result (it returns a JSON string)
        transcribed_text = json.loads(result)['text']
        
        # Check for violent content
        threat_assessment = check_violence_threat(transcribed_text)
        
        # Send notification if threat is detected
        if threat_assessment.lower() == 'no':
            # Run notification in a separate thread
            threading.Thread(
                target=show_notification,
                args=("⚠️ Threat Detected!", f'Threatening content detected in audio: "{transcribed_text}"')
            ).start()
            print(f"Threat detected in text: {transcribed_text}")  # Debug print
        
        # Return both the transcription and the threat assessment
        return jsonify({
            'transcription': transcribed_text,
            'contains_threat': threat_assessment
        })
        
    except Exception as e:
        print(f"Error processing audio: {str(e)}")
        return jsonify({'error': str(e)})

@app.route('/page1')
def page1():
    return render_template('page1.html')

if __name__ == '__main__':
    app.run(debug=True)

