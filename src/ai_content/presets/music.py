"""Music generation presets."""

from typing import Dict, Any

MUSIC_PRESETS: Dict[str, Dict[str, Any]] = {
    "jazz": {
        "bpm": 120,
        "mood": "smooth",
        "description": "Smooth jazz with melodic saxophone and piano",
    },
    "rock": {
        "bpm": 140,
        "mood": "energetic",
        "description": "Energetic rock with electric guitars and drums",
    },
    "classical": {
        "bpm": 90,
        "mood": "elegant",
        "description": "Classical orchestral composition",
    },
    "electronic": {
        "bpm": 128,
        "mood": "upbeat",
        "description": "Electronic dance music with synthesizers",
    },
    "ambient": {
        "bpm": 60,
        "mood": "calm",
        "description": "Ambient atmospheric soundscape",
    },
    "ethio-jazz": {
        "bpm": 110,
        "mood": "melancholic",
        "description": "Ethiopian jazz fusion with traditional scales",
    },
    "tizita-blues": {
        "bpm": 85,
        "mood": "nostalgic",
        "description": "Tizita mode with blues influences",
    },
    "eskista-dance": {
        "bpm": 130,
        "mood": "festive",
        "description": "Eskista dance rhythm with traditional instruments",
    },
}


def get_music_preset(name: str) -> Dict[str, Any]:
    """Get a music preset by name."""
    return MUSIC_PRESETS.get(name.lower(), {})


def list_music_presets() -> Dict[str, Dict[str, Any]]:
    """List all available music presets."""
    return MUSIC_PRESETS
