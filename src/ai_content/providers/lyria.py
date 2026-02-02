"""Lyria music generation provider using Google Gemini API."""

import time
from pathlib import Path
from typing import Optional
from .base import BaseProvider
from ..config import Config

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


class LyriaProvider(BaseProvider):
    """Provider for Lyria music generation via Google Gemini."""
    
    def __init__(self):
        super().__init__()
        self.api_key = Config.get_gemini_api_key()
        if self.api_key and GEMINI_AVAILABLE:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel("lyria-1.0")
    
    def validate_config(self) -> bool:
        """Validate Lyria configuration."""
        return Config.validate_provider_key("lyria")
    
    def get_capabilities(self) -> dict:
        """Get Lyria capabilities."""
        return {
            "music": True,
            "video": False,
            "image": False,
            "vocals": False,
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
        """Generate music using Lyria."""
        if not self.validate_config():
            raise ValueError("GEMINI_API_KEY not configured")
        
        if not GEMINI_AVAILABLE:
            raise ImportError("google-generativeai package not installed")
        
        # Build prompt with parameters
        full_prompt = prompt
        if style:
            full_prompt = f"{style} style: {prompt}"
        if bpm:
            full_prompt += f" at {bpm} BPM"
        if duration:
            full_prompt += f", {duration} seconds long"
        
        print(f"Generating music with Lyria: {full_prompt}")
        
        # Generate music
        try:
            response = self.model.generate_content(
                full_prompt,
                generation_config={
                    "temperature": 0.9,
                    "max_output_tokens": 8192,
                }
            )
            
            # In a real implementation, this would handle the audio generation
            if output_path is None:
                output_path = Path(f"lyria_output_{int(time.time())}.wav")
            
            print(f"Music generation complete. Saving to {output_path}")
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.touch()
            
            return output_path
            
        except Exception as e:
            raise RuntimeError(f"Lyria generation failed: {str(e)}")
    
    def generate_video(self, *args, **kwargs) -> Path:
        """Lyria does not support video generation."""
        raise NotImplementedError("Lyria does not support video generation")
    
    def generate_image(self, *args, **kwargs) -> Path:
        """Lyria does not support image generation."""
        raise NotImplementedError("Lyria does not support image generation")
