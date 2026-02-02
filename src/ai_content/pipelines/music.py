"""Music generation pipeline orchestration."""

from pathlib import Path
from typing import Optional, Dict, Any
from ..providers import get_provider
from ..presets import get_music_preset


class MusicPipeline:
    """
    Pipeline for orchestrating music generation workflows.
    
    The pipeline handles:
    - Provider selection and initialization
    - Preset application
    - Parameter validation
    - Output management
    """
    
    def __init__(self, provider_name: str):
        """Initialize music pipeline with a provider."""
        self.provider = get_provider(provider_name)
        if not self.provider.get_capabilities().get("music", False):
            raise ValueError(f"Provider {provider_name} does not support music generation")
    
    def generate(
        self,
        prompt: str,
        duration: int = 30,
        bpm: Optional[int] = None,
        style: Optional[str] = None,
        lyrics_file: Optional[Path] = None,
        output_path: Optional[Path] = None,
    ) -> Path:
        """
        Execute the music generation pipeline.
        
        Args:
            prompt: Text description of desired music
            duration: Duration in seconds
            bpm: Beats per minute (optional)
            style: Style preset name (optional)
            lyrics_file: Path to lyrics file (optional)
            output_path: Output file path (optional)
            
        Returns:
            Path to generated audio file
        """
        # Apply preset if provided
        if style:
            preset = get_music_preset(style)
            if preset:
                if bpm is None and preset.get("bpm"):
                    bpm = preset.get("bpm")
                if not prompt or prompt == style:
                    prompt = preset.get("description", prompt)
        
        # Generate music using provider
        return self.provider.generate_music(
            prompt=prompt,
            duration=duration,
            bpm=bpm,
            style=style,
            lyrics_file=lyrics_file,
            output_path=output_path,
        )
