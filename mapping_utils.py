from typing import Dict

def create_mouth_map(letter_map: Dict[str, str], mode: str, poses: Dict = None) -> Dict[str, str]:
    """Создает маппинг букв в текстуры (.png) или позы (smooth)."""
    if mode == "smooth":
        return {k: poses[v]["pose"] for k, v in letter_map.items()}
    else:
        return {k: f"{v}.png" for k, v in letter_map.items()}