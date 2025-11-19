from pathlib import Path

# Project name
PROJECT_NAME = "SUMO.AI"
PROJECT_LICENSE = "(c) 2025 Aref Daei - MIT License"
PROJECT_VERSION = "1.0.0"

# Project paths
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
TEMP_DIR = OUTPUT_DIR / "temp"

DEBUG = True

# Whisper settings
WHISPER_MODEL = "base"  # tiny, base, small, medium, large
WHISPER_DEVICE = "cpu"  # or "cuda" for GPU
WHISPER_LANGUAGE = "en"

# Translate settings
TRANSLATION_MODEL = "Helsinki-NLP/opus-mt-en-fa"
# or "facebook/m2m100_418M" for quality better
MAX_TRANSLATION_LENGTH = 512
BATCH_SIZE = 8
TRANSLATION_CHUNK_SIZE = 500  # تعداد کاراکتر در هر درخواست
TRANSLATION_DELAY = 0.5  # تاخیر بین درخواست‌ها (ثانیه)

# ffmpeg settings
AUDIO_FORMAT = "wav"
AUDIO_CODEC = "pcm_s16le"
AUDIO_RATE = 16000

# Subtitle settings
SRT_ENCODING = "utf-8"
MAX_SUBTITLE_LENGTH = 42  # Maximum character in a line

DIRS = [
    TEMP_DIR,
    OUTPUT_DIR,
    OUTPUT_DIR / "subtitles",
    OUTPUT_DIR / "videos",
]

# Create directories
for directory in DIRS:
    directory.mkdir(parents=True, exist_ok=True)
