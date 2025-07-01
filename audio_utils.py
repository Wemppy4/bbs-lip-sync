import json
from vosk import Model, KaldiRecognizer
from typing import List, Dict
from pydub import AudioSegment

def open_audio_file(audio_path: str, sample_rates: list) -> AudioSegment:
    """Открывает и валидирует аудиофайл."""
    audio = AudioSegment.from_file(audio_path)
    
    if (audio.channels != 1 or 
        audio.sample_width != 2 or 
        audio.frame_rate not in sample_rates):
        raise ValueError("Аудио должно быть в формате WAV: моно, 16-бит, 8000/16000 Гц")
    return audio

def transcribe_audio(audio: AudioSegment, model_path: str) -> List[Dict]:
    """Транскрибирует аудио через Vosk."""
    model = Model(model_path)
    rec = KaldiRecognizer(model, audio.frame_rate)
    rec.SetWords(True)
    
    results = []
    
    chunk_size = 4000 
    for chunk in audio[::(chunk_size // (audio.frame_width * audio.channels))]:
        if rec.AcceptWaveform(chunk.raw_data):
            results.append(json.loads(rec.Result()))
    
    results.append(json.loads(rec.FinalResult()))
    return results