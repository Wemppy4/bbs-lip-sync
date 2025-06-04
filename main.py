import argparse
from datetime import datetime
import os
from typing import Dict, List

# Импорт модулей
from config import load_config, load_poses, load_letter_map
from audio_utils import open_audio_file, transcribe_audio
from mapping_utils import create_mouth_map
from json_utils import generate_standard_json, generate_smooth_json

def process_results(
    words: List[Dict], 
    duration: float, 
    mouth_map: Dict[str, str], 
    mode: str,
    idle_image: str = None
) -> Dict[int, str]:
    """Обрабатывает распознанные слова в таймлайн анимации."""
    result_map = {}
    previous_end_time = 0

    # Преобразуем duration в тики
    duration_ticks = duration * 20

    for result in words:
        if "result" not in result:
            continue

        for word in result["result"]:
            # Преобразуем время слова в тики
            start_time_ticks = word["start"] * 20
            end_time_ticks = word["end"] * 20
            text = word["word"]

            print(f"Обработка слова: '{text}' с {start_time_ticks} по {end_time_ticks}")
            # Обработка пауз между словами
            if start_time_ticks > previous_end_time:
                silence_duration = start_time_ticks - previous_end_time
                silence_ticks = 2 if mode == "smooth" else 5

                result_map[0] = idle_image

                if silence_duration >= silence_ticks:
                    silence_start = previous_end_time

                    result_map[silence_start + 2] = idle_image
                    result_map[start_time_ticks - 2] = idle_image

            # Маппинг букв в кадры анимации
            for i, letter in enumerate(text.lower()):
                if letter not in mouth_map:
                    continue
                letter_time_ticks = start_time_ticks + (end_time_ticks - start_time_ticks) * (i / len(text))
                result_map[letter_time_ticks] = mouth_map[letter]

            previous_end_time = end_time_ticks

    # Обработка паузы в конце аудио
    if previous_end_time < duration_ticks:
        silence_duration = duration_ticks - previous_end_time
        silence_ticks = 2 if mode == "smooth" else 5

        if silence_duration >= silence_ticks:
            silence_start = previous_end_time
            result_map[silence_start + silence_ticks] = idle_image

    return dict(sorted(result_map.items()))

def main():
    # Создание папок, если их нет
    os.makedirs("temp_audio", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    os.makedirs("vosk_models", exist_ok=True)
    os.makedirs("bbs_models", exist_ok=True)
    os.makedirs("json_files", exist_ok=True)

    # CLI аргументы
    parser = argparse.ArgumentParser()
    parser.add_argument("--smooth", action="store_true")
    args = parser.parse_args()

    # Загрузка конфигов
    config = load_config()
    letter_map = load_letter_map(config["language"])
    poses = load_poses() if args.smooth else None

    # Настройки режима
    mouth_map = create_mouth_map(letter_map, "smooth" if args.smooth else "standard", poses)
    idle_image = poses["idle"]["pose"] if args.smooth else input("Основная текстура рта (например, Wemppy): ") + ".png"

    # Обработка аудио
    wf = open_audio_file("temp_audio\converted_audio.wav", [8000, 16000])
    words = transcribe_audio(wf, config["model_path"])
    duration = wf.getnframes() / wf.getframerate()
    wf.close()

    # Генерация анимации
    lips_map = process_results(words, duration, mouth_map, "smooth" if args.smooth else "standard", idle_image)
    json_output = (generate_smooth_json(lips_map) if args.smooth 
                  else generate_standard_json(lips_map, config["mouth_shapes_path"]))

    # Сохранение результата
    output_path = config["output_path"]
    if not output_path:
        output_path = "output"

    filename = os.path.join(output_path, f"{config["language"]}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json_output)

    # Вывод текста в консоль
    print(f"{words[0]['text'] if words else 'Нет распознанного текста.'}")

if __name__ == "__main__":
    main()