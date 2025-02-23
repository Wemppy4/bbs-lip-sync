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

def process_results(results: List[dict], file_duration: float, main_mouth_name: str) -> Dict[int, str]:
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
                    result_map[silence_start * 20] = f"{main_mouth_name}.png"

            # Map each letter to the corresponding mouth image
            last_image = f"{main_mouth_name}.png"
            for i, letter in enumerate(text):
                letter_time = start_time + (end_time - start_time) * (i / len(text))
                image = get_mouth_image_for_letter(letter)
                if image and image != last_image:
                    result_map[letter_time * 20] = image
                    last_image = image

            previous_end_time = end_time

    # Check for silence at the end of the file
    if previous_end_time < file_duration:
        silence_start = previous_end_time
        result_map[silence_start * 20] = f"{main_mouth_name}.png"

    return result_map

def get_mouth_image_for_letter(letter: str) -> str:
    """
    Get the corresponding mouth image for a given letter.
    """
    letter_to_image = {
        "б": "b.png", "п": "b.png", "м": "b.png",
        "в": "f.png", "ф": "f.png",
        "г": "ee.png", "к": "ee.png", "х": "ee.png", "и": "ee.png", "й": "ee.png",
        "ш": "ee.png", "щ": "ee.png", "ъ": "ee.png", "ы": "ee.png", "ь": "ee.png",
        "д": "d.png", "т": "d.png", "н": "d.png", "ж": "d.png", "з": "d.png",
        "с": "d.png", "ц": "d.png", "ч": "d.png",
        "е": "a.png", "э": "a.png", "а": "a.png", "я": "a.png",
        "ё": "o.png", "о": "o.png",
        "р": "l.png", "л": "l.png",
        "у": "u.png", "ю": "u.png",

        "b": "b.png", "p": "b.png", "m": "b.png",
        "f": "f.png", "v": "f.png", 
        "g": "ee.png", "k": "ee.png", "h": "ee.png",
        "e": "ee.png","j": "ee.png", "y": "ee.png", "q": "ee.png",
        "s": "d.png", "t": "d.png", "n": "d.png", "z": "d.png",
        "c": "d.png", "d": "d.png", "x": "d.png",
        "i": "a.png", "a": "a.png",
        "o": "o.png", 
        "l": "l.png", "r": "l.png",
        "u": "u.png", "w": "u.png",
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
            "interp": "linear",
            "tick": float(key),
            "value": f"{settings['mouth_shapes_path']}{value}"
        }
        keyframes.append(keyframe)

    result = {
        f"0/texture": {
            "keyframes": keyframes,
            "type": "link"
        }
    }
    return json.dumps(result, indent=4, ensure_ascii=False)

# def generate_result_string(lips_map: Dict[int, str]) -> str:
#     """
#     # Generate a JSON string from the lips map.
#     """
#     result = ''

#     result += '{\n\t\"1/texture\": {\n\t\t\"keyframes\": [\n'

#     for key, value in lips_map.items():
#         # проверка последний ли элемент
#         if key == list(lips_map.keys())[-1]:
#             result += '\t\t\t{\n\t\t\t\t\"duration\": 0.0,\n\t\t\t\t\"interp\": \"linear\",\n\t\t\t\t\"tick\": ' + str(key) + '.0,\n\t\t\t\t\"value\": \"assets:models/Mouth/Pixel shapes/' + value + '\"\n\t\t\t}\n'
#         else:
#             result += '\t\t\t{\n\t\t\t\t\"duration\": 0.0,\n\t\t\t\t\"interp\": \"linear\",\n\t\t\t\t\"tick\": ' + str(key) + '.0,\n\t\t\t\t\"value\": \"assets:models/Mouth/Pixel shapes/' + value + '\"\n\t\t\t},\n'

#     result += '\t\t],\n\t\t\"type\": \"link\"\n\t}\n}'

#     return result

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

    # Get the main mouth image name
    main_mouth_name = input("Enter the main mouth image name (example: Wemppy): ")

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
    
    # Print the recognized words
    print("\nRecognized words:")
    for result in results:
        if "result" in result:
            for word in result["result"]:
                print(word["word"], end=" ")
    print()

    # Process the results and generate the lips map
    file_duration = wf.getnframes() / wf.getframerate()
    lips_map = process_results(results, file_duration, main_mouth_name)

    # Generate and save the result string
    result_string = generate_result_string(lips_map)
    print(result_string)
    
    if not os.path.exists("output"):
        os.makedirs("output")

    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".json"
    with open(f"{OUTPUT_PATH}{filename}", "w", encoding='utf-8') as f:
        f.write(result_string)
    print(f'Result saved to {OUTPUT_PATH}{filename}')

    # Закрываем файл после завершения работы
    wf.close()
    print("Done")

if __name__ == "__main__":
    main()