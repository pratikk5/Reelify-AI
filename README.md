# Reelify AI - Instagram Reel Generator

Reelify AI is a Flask-based web application that allows users to create engaging Instagram reels using AI-powered voice synthesis and smart video stitching. Users can upload images, add custom text (converted to audio), and generate reels automatically.

## Features

- **AI-Powered Voiceover:** Converts user text to natural-sounding audio using ElevenLabs API.
- **Smart Image Stitching:** Combines uploaded images into a video reel using FFmpeg.
- **Modern UI:** Responsive interface for uploading images and entering text.
- **Gallery:** Browse generated reels in a gallery view.

## Project Structure

```
config.py
main.py
generate_process.py
text_to_audio.py
requirements.txt
static/
    css/
    reels/
templates/
    base.html
    index.html
    create.html
    gallery.html
user_uploads/
    <uuid>/
        input.txt
        desc.txt
        audio.mp3
done.txt
```

## Setup

1. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

2. **Set ElevenLabs API Key:**
    - Edit `config.py` and add your ElevenLabs API key.

3. **Run the Flask app:**
    ```sh
    python main.py
    ```

4. **Start the reel generation process:**
    ```sh
    python generate_process.py
    ```

## Usage

- Visit `http://localhost:5000` in your browser.
- Go to **Create Reel** to upload images and enter text.
- Generated reels appear in the **Gallery**.

## How It Works

- **main.py:** Handles web routes, file uploads, and user interactions.
- **generate_process.py:** Monitors uploads, generates audio from text, and stitches images/audio into reels.
- **text_to_audio.py:** Converts text to audio using ElevenLabs.
- **FFmpeg:** Used for video creation (must be installed and available in your PATH).

## Requirements

- Python 3.8+
- FFmpeg installed
- ElevenLabs API key



**Made with ❤️ using Flask and AI! for Content Creators**
