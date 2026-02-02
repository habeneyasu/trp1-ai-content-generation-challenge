"""Video generation pipeline orchestration."""

from pathlib import Path
from typing import Optional, Dict, Any
from ..providers import get_provider
from ..presets import get_video_preset


class VideoPipeline:
    """
    Pipeline for orchestrating video generation workflows.
    
    The pipeline handles:
    - Provider selection and initialization
    - Preset application
    - Aspect ratio management
    - Image-to-video conversion
    - Output management
    """
    
    def __init__(self, provider_name: str):
        """Initialize video pipeline with a provider."""
        self.provider = get_provider(provider_name)
        if not self.provider.get_capabilities().get("video", False):
            raise ValueError(f"Provider {provider_name} does not support video generation")
    
    def generate(
        self,
        prompt: str,
        duration: int = 5,
        aspect_ratio: str = "16:9",
        style: Optional[str] = None,
        image_path: Optional[Path] = None,
        output_path: Optional[Path] = None,
    ) -> Path:
        """
        Execute the video generation pipeline.
        
        Args:
            prompt: Text description of desired video
            duration: Duration in seconds
            aspect_ratio: Video aspect ratio (e.g., "16:9", "9:16")
            style: Style preset name (optional)
            image_path: Path to input image for image-to-video (optional)
            output_path: Output file path (optional)
            
        Returns:
            Path to generated video file
        """
        # Apply preset if provided
        if style:
            preset = get_video_preset(style)
            if preset:
                if aspect_ratio == "16:9" and preset.get("aspect_ratio"):
                    aspect_ratio = preset.get("aspect_ratio")
                if not prompt or prompt == style:
                    prompt = preset.get("description", prompt)
        
        # Generate video using provider
        return self.provider.generate_video(
            prompt=prompt,
            duration=duration,
            aspect_ratio=aspect_ratio,
            style=style,
            image_path=image_path,
            output_path=output_path,
        )
