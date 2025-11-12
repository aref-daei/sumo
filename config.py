import os
from pathlib import Path

# Project Paths
BASE_DIR = Path()
TEMP_DIR = BASE_DIR / "temp"
OUTPUT_DIR = BASE_DIR / "output"
MODELS_DIR = BASE_DIR / "models" / "cache"
DIRS = [
    TEMP_DIR,
    OUTPUT_DIR,
    MODELS_DIR,
    OUTPUT_DIR / "subtitles",
    OUTPUT_DIR / "videos",
]

# Create directories
for directory in DIRS:
    directory.mkdir(parents=True, exist_ok=True)

# Whisper settings
WHISPER_MODEL = "base"  # tiny, base, small, medium, large
WHISPER_DEVICE = "cpu"  # or "cuda" for GPU

# Translate settings
TRANSLATION_MODEL = "Helsinki-NLP/opus-mt-en-fa"
# or "facebook/m2m100_418M" for quality better
MAX_TRANSLATION_LENGTH = 512
BATCH_SIZE = 8

# ffmpeg settings
FFMPEG_AUDIO_CODEC = "pcm_s16le"
FFMPEG_AUDIO_RATE = 16000

# Subtitle settings
SRT_ENCODING = "utf-8"
MAX_SUBTITLE_LENGTH = 42  # Maximum character in a line
