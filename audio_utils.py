import wave
import json
from vosk import Model, KaldiRecognizer
from typing import List, Dict

def open_audio_file(audio_path: str, sample_rates: list) -> wave.Wave_read:
    """Открывает и валидирует WAV-файл."""
    wf = wave.open(audio_path, "rb")
    if (wf.getnchannels() != 1 or 
        wf.getsampwidth() != 2 or 
        wf.getframerate() not in sample_rates):
        wf.close()
        raise ValueError("Аудио должно быть в формате WAV: моно, 16-бит, 8000/16000 Гц")
    return wf

def transcribe_audio(wf: wave.Wave_read, model_path: str) -> List[Dict]:
    """Транскрибирует аудио через Vosk."""
    model = Model(model_path)
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)
    
    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            results.append(json.loads(rec.Result()))
    
    results.append(json.loads(rec.FinalResult()))
    return results