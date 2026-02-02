"""Configuration management for AI content generation."""

import os
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

# Load environment variables
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(env_path)


class Config:
    """Configuration class for API keys and settings."""
    
    @staticmethod
    def get_gemini_api_key() -> Optional[str]:
        """Get Google Gemini API key from environment."""
        return os.getenv("GEMINI_API_KEY")
    
    @staticmethod
    def get_aimlapi_key() -> Optional[str]:
        """Get AIMLAPI key from environment."""
        return os.getenv("AIMLAPI_KEY")
    
    @staticmethod
    def get_klingai_key() -> Optional[str]:
        """Get KlingAI key from environment."""
        return os.getenv("KLINGAI_API_KEY")
    
    @staticmethod
    def validate_provider_key(provider: str) -> bool:
        """Validate that required API key exists for provider."""
        key_map = {
            "lyria": "GEMINI_API_KEY",
            "veo": "GEMINI_API_KEY",
            "imagen": "GEMINI_API_KEY",
            "minimax": "AIMLAPI_KEY",
            "klingai": "KLINGAI_API_KEY",
        }
        
        key_name = key_map.get(provider.lower())
        if not key_name:
            return False
        
        key_value = os.getenv(key_name)
        return key_value is not None and key_value != "" and key_value != f"your_{key_name.lower()}_here"
