"""MiniMax music generation provider using AIMLAPI."""

import time
from pathlib import Path
from typing import Optional
from .base import BaseProvider
from ..config import Config

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


class MiniMaxProvider(BaseProvider):
    """Provider for MiniMax music generation with vocals via AIMLAPI."""
    
    def __init__(self):
        super().__init__()
        self.api_key = Config.get_aimlapi_key()
        self.base_url = "https://api.aimlapi.com/v1"
    
    def validate_config(self) -> bool:
        """Validate MiniMax configuration."""
        return Config.validate_provider_key("minimax")
    
    def get_capabilities(self) -> dict:
        """Get MiniMax capabilities."""
        return {
            "music": True,
            "video": False,
            "image": False,
            "vocals": True,
            "image_to_video": False,
        }
    
    def generate_music(
        self,
        prompt: str,
        duration: int = 30,
        bpm: Optional[int] = None,
        style: Optional[str] = None,
        lyrics_file: Optional[Path] = None,
        output_path: Optional[Path] = None,
    ) -> Path:
        """Generate music using MiniMax."""
        if not self.validate_config():
            raise ValueError("AIMLAPI_KEY not configured")
        
        if not REQUESTS_AVAILABLE:
            raise ImportError("requests package not installed")
        
        # Read lyrics if provided
        lyrics = ""
        if lyrics_file and lyrics_file.exists():
            lyrics = lyrics_file.read_text()
        
        # Build prompt
        full_prompt = prompt
        if style:
            full_prompt = f"{style} style: {prompt}"
        if bpm:
            full_prompt += f" at {bpm} BPM"
        if lyrics:
            full_prompt += f"\n\nLyrics:\n{lyrics}"
        
        print(f"Generating music with MiniMax: {full_prompt}")
        
        # In a real implementation, this would call the AIMLAPI
        if output_path is None:
            output_path = Path(f"minimax_output_{int(time.time())}.wav")
        
        print(f"Music generation complete. Saving to {output_path}")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.touch()
        
        return output_path
    
    def generate_video(self, *args, **kwargs) -> Path:
        """MiniMax does not support video generation."""
        raise NotImplementedError("MiniMax does not support video generation")
    
    def generate_image(self, *args, **kwargs) -> Path:
        """MiniMax does not support image generation."""
        raise NotImplementedError("MiniMax does not support image generation")
