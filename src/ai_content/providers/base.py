"""Base provider interface for AI content generation."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Optional, Dict, Any


class BaseProvider(ABC):
    """Base class for all AI content generation providers."""
    
    def __init__(self):
        self.name = self.__class__.__name__
    
    @abstractmethod
    def generate_music(
        self,
        prompt: str,
        duration: int = 30,
        bpm: Optional[int] = None,
        style: Optional[str] = None,
        lyrics_file: Optional[Path] = None,
        output_path: Optional[Path] = None,
    ) -> Path:
        """
        Generate music based on prompt.
        
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
        pass
    
    @abstractmethod
    def generate_video(
        self,
        prompt: str,
        duration: int = 5,
        aspect_ratio: str = "16:9",
        style: Optional[str] = None,
        image_path: Optional[Path] = None,
        output_path: Optional[Path] = None,
    ) -> Path:
        """
        Generate video based on prompt.
        
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
        pass
    
    @abstractmethod
    def generate_image(
        self,
        prompt: str,
        aspect_ratio: str = "1:1",
        style: Optional[str] = None,
        output_path: Optional[Path] = None,
    ) -> Path:
        """
        Generate image based on prompt.
        
        Args:
            prompt: Text description of desired image
            aspect_ratio: Image aspect ratio
            style: Style preset name (optional)
            output_path: Output file path (optional)
            
        Returns:
            Path to generated image file
        """
        pass
    
    def validate_config(self) -> bool:
        """Validate provider configuration (API keys, etc.)."""
        return True
    
    def get_capabilities(self) -> Dict[str, Any]:
        """Get provider capabilities."""
        return {
            "music": False,
            "video": False,
            "image": False,
            "vocals": False,
            "image_to_video": False,
        }
