import configparser
import json
from typing import Dict, Any

def load_config() -> Dict[str, str]:
    """Загружает настройки из config.ini"""
    config = configparser.ConfigParser()
    config.read("config.ini")
    
    return {
        "model_path": config.get("Settings", "model_path"),
        "mouth_shapes_path": config.get("Settings", "mouth_shapes_path"),
        "output_path": config.get("Settings", "output_path"),
        "language": config.get("Settings", "language", fallback="ru"),
    }

def load_poses() -> Dict[str, Any]:
    """Загружает poses.json для smooth-режима"""
    with open("json_files\poses.json", "r", encoding="utf-8") as f:
        return json.load(f)

def load_letter_map(language: str) -> Dict[str, str]:
    """Загружает маппинг букв для языка"""
    path = f"json_files/maps/{language}.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)