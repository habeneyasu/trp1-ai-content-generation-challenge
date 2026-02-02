"""Video generation presets."""

from typing import Dict, Any

VIDEO_PRESETS: Dict[str, Dict[str, Any]] = {
    "nature": {
        "aspect_ratio": "16:9",
        "description": "Natural landscapes and scenery",
    },
    "urban": {
        "aspect_ratio": "16:9",
        "description": "Urban cityscapes and architecture",
    },
    "portrait": {
        "aspect_ratio": "9:16",
        "description": "Portrait-oriented content",
    },
    "cinematic": {
        "aspect_ratio": "21:9",
        "description": "Cinematic widescreen format",
    },
    "square": {
        "aspect_ratio": "1:1",
        "description": "Square format for social media",
    },
    "abstract": {
        "aspect_ratio": "16:9",
        "description": "Abstract visual patterns and colors",
    },
}


def get_video_preset(name: str) -> Dict[str, Any]:
    """Get a video preset by name."""
    return VIDEO_PRESETS.get(name.lower(), {})


def list_video_presets() -> Dict[str, Dict[str, Any]]:
    """List all available video presets."""
    return VIDEO_PRESETS
