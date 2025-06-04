from typing import Dict
import json

def generate_standard_json(lips_map: Dict[int, str], mouth_shapes_path: str) -> str:
    """Генерирует JSON для стандартного режима."""
    keyframes = [
        {
            "duration": 0.0,
            "interp": "linear",
            "tick": float(tick),
            "value": f"{mouth_shapes_path}{image}"
        } for tick, image in lips_map.items()
    ]
    
    return json.dumps({"0/texture": {"keyframes": keyframes, "type": "link"}}, indent=4)

def generate_smooth_json(lips_map: Dict[int, str]) -> str:
    """Генерирует JSON для smooth-режима."""
    keyframes = [
        {
            "duration": 0.0,
            "interp": "cubic_out",
            "tick": float(tick),
            "value": {"static": False, "pose": image}
        } for tick, image in lips_map.items()
    ]
    
    return json.dumps({"0/pose": {"keyframes": keyframes, "type": "pose"}}, indent=4)