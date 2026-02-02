"""AI content generation providers."""

from .base import BaseProvider
from .lyria import LyriaProvider
from .minimax import MiniMaxProvider
from .veo import VeoProvider
from .imagen import ImagenProvider

__all__ = [
    "BaseProvider",
    "LyriaProvider",
    "MiniMaxProvider",
    "VeoProvider",
    "ImagenProvider",
]

# Provider registry
PROVIDERS = {
    "lyria": LyriaProvider,
    "minimax": MiniMaxProvider,
    "veo": VeoProvider,
    "imagen": ImagenProvider,
}


def get_provider(name: str) -> BaseProvider:
    """Get a provider instance by name."""
    provider_class = PROVIDERS.get(name.lower())
    if not provider_class:
        raise ValueError(f"Unknown provider: {name}")
    return provider_class()
