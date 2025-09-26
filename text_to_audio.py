import os
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from config import ELEVENLABS_API_KEY

client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

# Map friendly names to ElevenLabs voice IDs
VOICE_MAP = {
    "adam": "pNInz6obpgDQGcFmaJgB",
    "bella": "EXAVITQu4vr4xnSDxMaL",
    "muthu": "gJvkwI7wGFW2czmyfJhp",
    "custom": "JBFqnCBsd6RMkjVDRZzb" 
}


def text_to_speech_file(text: str, folder: str, voice_name: str = "bella") -> str:
    # Get voice_id from map, fallback to muthu if not found
    voice_id = VOICE_MAP.get(voice_name.lower(), VOICE_MAP["bella"])

    response = client.text_to_speech.convert(
        voice_id=voice_id,
        output_format="mp3_22050_32",
        text=text,
        model_id="eleven_multilingual_v2",  # ✅ multilingual model
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
            speed=1.0,
        ),
    )

    save_file_path = os.path.join(f"user_uploads/{folder}", "audio.mp3")

    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")
    return save_file_path