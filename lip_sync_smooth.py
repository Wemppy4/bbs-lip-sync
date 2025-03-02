import os
import json
from vosk import Model, KaldiRecognizer
import wave
from typing import Dict, List
import configparser
from datetime import datetime

# Config
config = configparser.ConfigParser()
config.read("config.ini")

settings = {
    "model_path": config.get("Settings", "model_path"),
    "mouth_shapes_path": config.get("Settings", "mouth_shapes_path"),
    "output_path": config.get("Settings", "output_path"),
}

# Constants
AUDIO_FILE = "converted_audio.wav"
MODEL_PATH = settings["model_path"]
OUTPUT_PATH = settings["output_path"]
SAMPLE_RATES = [8000, 16000]

def process_results(results: List[dict], file_duration: float, poses: Dict) -> Dict[int, str]:
    """
    Process the results from the recognizer and generate a map of timestamps to mouth images.
    """
    previous_end_time = 0
    result_map = {}

    for result in results:
        if "result" not in result:
            continue

        for word in result["result"]:
            start_time = word["start"]
            end_time = word["end"]
            text = word["word"]

            # Check for silence before the current word
            if start_time > previous_end_time:
                silence_duration = (start_time - previous_end_time) * 20

                # Если пауза длится больше 5 тиков, добавляем молчание
                if silence_duration >= 5:
                    silence_start = previous_end_time
                    if previous_end_time == 0:
                        result_map[silence_start * 20] = poses["idle"]["pose"]
                        result_map[start_time * 20 - 2] = poses["idle"]["pose"]
                    else:
                        result_map[silence_start * 20 + 1] = poses["b"]["pose"]
                        result_map[silence_start * 20 + 2] = poses["idle"]["pose"]
                        result_map[start_time * 20 - 2] = poses["idle"]["pose"]

            # Map each letter to the corresponding mouth image
            for i, letter in enumerate(text):
                letter_time = start_time + (end_time - start_time) * (i / len(text))
                image = get_mouth_image_for_letter(letter, poses)
                result_map[letter_time * 20] = image

            previous_end_time = end_time

    # Check for silence at the end of the file
    if previous_end_time < file_duration:
        silence_duration = file_duration - previous_end_time
        silence_duration_ticks = silence_duration * 20

        # Если пауза длится больше 5 тиков, добавляем молчание
        if silence_duration_ticks >= 5:
            silence_start = previous_end_time
            result_map[silence_start * 20 + 1] = poses["b"]["pose"]
            result_map[silence_start * 20 + 2] = poses["idle"]["pose"]

        

    return result_map

def get_mouth_image_for_letter(letter: str, poses: Dict) -> str:
    """
    Get the corresponding mouth image for a given letter.
    """
    letter_to_image = {
        "б": poses["b"]["pose"], "п": poses["b"]["pose"], "м": poses["b"]["pose"],
        "в": poses["f"]["pose"], "ф": poses["f"]["pose"],
        "г": poses["ee"]["pose"], "к": poses["ee"]["pose"], "х": poses["ee"]["pose"], "и": poses["ee"]["pose"], "й": poses["ee"]["pose"],
        "ш": poses["ee"]["pose"], "щ": poses["ee"]["pose"], "ъ": poses["ee"]["pose"], "ы": poses["ee"]["pose"], "ь": poses["ee"]["pose"],
        "д": poses["d"]["pose"], "т": poses["d"]["pose"], "н": poses["d"]["pose"], "ж": poses["d"]["pose"], "з": poses["d"]["pose"],
        "с": poses["d"]["pose"], "ц": poses["d"]["pose"], "ч": poses["d"]["pose"],
        "е": poses["a"]["pose"], "э": poses["a"]["pose"], "а": poses["a"]["pose"], "я": poses["a"]["pose"],
        "ё": poses["o"]["pose"], "о": poses["o"]["pose"],
        "р": poses["l"]["pose"], "л": poses["l"]["pose"],
        "у": poses["u"]["pose"], "ю": poses["u"]["pose"],

        "b" : poses["b"]["pose"], "p" : poses["b"]["pose"], "m" : poses["b"]["pose"],
        "f" : poses["f"]["pose"], "v" : poses["f"]["pose"],
        "g" : poses["ee"]["pose"], "k" : poses["ee"]["pose"], "h" : poses["ee"]["pose"], "e" : poses["ee"]["pose"], "j" : poses["ee"]["pose"],
        "y" : poses["ee"]["pose"], "q" : poses["ee"]["pose"],
        "s" : poses["d"]["pose"], "t" : poses["d"]["pose"], "n" : poses["d"]["pose"], "z" : poses["d"]["pose"],
        "c" : poses["d"]["pose"], "d" : poses["d"]["pose"], "x" : poses["d"]["pose"],
        "i" : poses["a"]["pose"], "a" : poses["a"]["pose"],
        "o" : poses["o"]["pose"],
        "l" : poses["l"]["pose"], "r" : poses["l"]["pose"],
        "u" : poses["u"]["pose"], "w" : poses["u"]["pose"],
    }
    return letter_to_image.get(letter, "")

def generate_result_string(lips_map: Dict[int, str]) -> str:
    """
    Generate a JSON string from the lips map.
    """

    keyframes = []
    for key, value in lips_map.items():
        keyframe = {
            "duration": 0.0,
            "interp": "cubic_out",
            "tick": float(key),
            "value": {
                "static": False,
                "pose": value
            }
        }
        keyframes.append(keyframe)

    result = {
        f"1/pose": {
            "keyframes": keyframes,
            "type": "pose"
        }
    }
    return json.dumps(result, indent=4, ensure_ascii=False)

def read_audio_file(wf: wave.Wave_read, rec: KaldiRecognizer) -> List[dict]:
    """
    Read the audio file and process it with the recognizer.
    """
    results = []
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            results.append(result)
    return results

def open_audio_file() -> wave.Wave_read:
    """
    Open the audio file and validate its format.
    """
    wf = wave.open(AUDIO_FILE, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getframerate() not in SAMPLE_RATES:
        wf.close()  # Закрываем файл, если формат неверный
        raise ValueError("The audio file must be in WAV format, mono, 16-bit, 8000 or 16000 Hz")
    return wf

def main():
    # Check if the model exists
    if not os.path.exists(MODEL_PATH):
        print(f"Model {MODEL_PATH} not found. Download it from https://alphacephei.com/vosk/models")
        exit(1)

    # Load the model
    model = Model(MODEL_PATH)

    # Open poses json file

    with open("poses.json", "r", encoding="utf-8") as file:
        poses_data = json.load(file)

    # Open and validate the audio file
    try:
        wf = open_audio_file()
    except ValueError as e:
        print(e)
        exit(1)

    # Initialize the recognizer
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    # Read and process the audio file
    results = read_audio_file(wf, rec)
    final_result = json.loads(rec.FinalResult())
    results.append(final_result)

    # Process the results and generate the lips map
    file_duration = wf.getnframes() / wf.getframerate()
    lips_map = process_results(results, file_duration, poses_data)

    # Generate and save the result string
    result_string = generate_result_string(lips_map)
    print(result_string)
    
    if not os.path.exists("output"):
        os.makedirs("output")
    
    # Print the recognized words
    print("\nRecognized words:")
    for result in results:
        if "result" in result:
            for word in result["result"]:
                print(word["word"], end=" ")
    print()

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".json"
    with open(f"{OUTPUT_PATH}{filename}", "w", encoding='utf-8') as f:
        f.write(result_string)
    print(f'Result saved to {OUTPUT_PATH}{filename}')

    # Закрываем файл после завершения работы
    wf.close()
    print("Done")

if __name__ == "__main__":
    main()