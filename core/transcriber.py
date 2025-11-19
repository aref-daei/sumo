from typing import List, Dict

import whisper

from settings import WHISPER_MODEL, WHISPER_DEVICE, WHISPER_LANGUAGE
from exceptions.transcriber_exc import *


class Transcriber:
    """Speech to text conversion with OpenAI Whisper"""

    def __init__(self, model_name: str = WHISPER_MODEL, device: str = WHISPER_DEVICE):
        self.model_name = model_name
        self.device = device
        self.model = None

    def load_model(self):
        """Loading the Whisper model"""
        if self.model is None:
            self.model = whisper.load_model(
                self.model_name,
                device=self.device
            )

    def transcribe(self, audio_path: str, language: str = WHISPER_LANGUAGE) -> Dict:
        """Convert voice to text"""
        try:
            self.load_model()

            result = self.model.transcribe(
                audio_path,
                language=language,
                task="transcribe",
                verbose=False,
                word_timestamps=False
            )

            return result

        except Exception as e:
            raise TranscriptionError(f"Transcription failed with error: {e}")

    def get_segments(self, transcription_result: Dict) -> List[Dict]:
        """Extract segments with scheduling"""
        segments = []

        for segment in transcription_result['segments']:
            segments.append({
                'text': segment['text'].strip(),
                'start': segment['start'],
                'end': segment['end']
            })

        return segments
