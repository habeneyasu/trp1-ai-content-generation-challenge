"""Presets package."""

from .music import MUSIC_PRESETS, get_music_preset, list_music_presets
from .video import VIDEO_PRESETS, get_video_preset, list_video_presets

__all__ = [
    "MUSIC_PRESETS",
    "get_music_preset",
    "list_music_presets",
    "VIDEO_PRESETS",
    "get_video_preset",
    "list_video_presets",
]
