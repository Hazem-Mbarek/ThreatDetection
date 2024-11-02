# Speech-to-Text Transcription App

A Flask web application that converts speech to text using the Vosk speech recognition model.

## Features
- Audio file upload and transcription
- Automatic stereo to mono conversion
- Supports various audio formats
- Real-time transcription display
- Lightweight and fast processing

## Prerequisites
- Python 3.x
- Flask
- Vosk
- SoundFile
- NumPy

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <project-directory>
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Download Vosk model:
- Download [vosk-model-small-en-us-0.15](https://alphacephei.com/vosk/models)
- Extract to project directory as `vosk-model-small-en-us`

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and go to:
```
http://127.0.0.1:5000
```

3. Upload an audio file and click "Transcribe"

## Supported Audio Formats
- WAV
- MP3
- OGG
- FLAC
- And more (supported by SoundFile)

## Project Structure
```
project/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── static/
│   ├── css/
│   │   └── style.css  # Styling
│   └── uploads/       # Temporary audio storage
├── templates/
│   └── index.html     # Web interface
└── vosk-model-small-en-us/  # Speech recognition model
```

## Dependencies
- Flask==2.0.1
- vosk==0.3.45
- soundfile==0.12.1
- numpy==1.21.0

## Notes
- Audio files are automatically converted to mono if needed
- Temporary files are cleaned up after processing
- Best results with clear audio recordings
- Model size: ~40MB

## License
[Your chosen license]

## Contributing
[Your contribution guidelines]

## Acknowledgments
- [Vosk](https://alphacephei.com/vosk/) for the speech recognition model
- [Flask](https://flask.palletsprojects.com/) for the web framework