# Codebase Exploration Documentation

## Part 2: Understanding the AI Content Generation Framework

This document provides a comprehensive exploration of the codebase structure, capabilities, and usage patterns.

---

## 1. Package Structure

### Main Modules in `src/ai_content/`

The package is organized into the following main modules:

```
src/ai_content/
├── __init__.py          # Package initialization and version
├── config.py            # Configuration management (API keys, environment)
├── cli.py               # Command-line interface implementation
├── providers/           # AI provider implementations
│   ├── __init__.py      # Provider registry and factory
│   ├── base.py          # Base provider abstract class
│   ├── lyria.py         # Lyria music provider (Google Gemini)
│   ├── minimax.py       # MiniMax music provider (AIMLAPI)
│   ├── veo.py           # Veo video provider (Google Gemini)
│   └── imagen.py        # Imagen image provider (Google Gemini)
├── presets/             # Style presets for music and video
│   ├── __init__.py      # Preset exports
│   ├── music.py         # Music style presets
│   └── video.py         # Video style presets
└── pipelines/           # Orchestration pipelines
    ├── __init__.py      # Pipeline exports
    ├── music.py         # Music generation pipeline
    └── video.py         # Video generation pipeline
```

### Module Responsibilities

- **`config.py`**: Manages environment variables, API key loading, and provider configuration validation
- **`cli.py`**: Implements the Click-based CLI with commands for listing providers/presets and generating content
- **`providers/`**: Contains all AI provider implementations, each inheriting from `BaseProvider`
- **`presets/`**: Defines reusable style presets with parameters (BPM, mood, aspect ratios)
- **`pipelines/`**: Orchestrates complex workflows combining providers, presets, and parameter handling

### How Providers are Organized

Providers follow a consistent architecture:

1. **Base Class** (`providers/base.py`):
   - Defines abstract interface for all providers
   - Requires implementation of `generate_music()`, `generate_video()`, `generate_image()`
   - Provides `validate_config()` and `get_capabilities()` methods

2. **Provider Registry** (`providers/__init__.py`):
   - Maps provider names (strings) to provider classes
   - Provides `get_provider(name)` factory function
   - Exports all provider classes

3. **Individual Providers**:
   - Each provider (Lyria, MiniMax, Veo, Imagen) implements the base interface
   - Handles provider-specific API calls and configuration
   - Validates API keys and capabilities

### Purpose of the `pipelines/` Directory

The `pipelines/` directory contains orchestration modules that:

1. **Simplify Complex Workflows**: Combine provider selection, preset application, and parameter management
2. **Abstract Provider Details**: Users can work with pipelines without directly instantiating providers
3. **Enable Extensibility**: Easy to add preprocessing, post-processing, or multi-step workflows
4. **Provide Reusable Patterns**: Common workflows can be encapsulated in pipeline classes

**Example Usage**:
```python
from ai_content.pipelines import MusicPipeline

pipeline = MusicPipeline("lyria")
result = pipeline.generate(
    prompt="smooth jazz",
    style="jazz",
    duration=30
)
```

---

## 2. Provider Capabilities

### Music Providers

#### Lyria (via Google Gemini)
- **Provider Name**: `lyria`
- **API**: Google Gemini API
- **Capabilities**:
  - ✅ Music generation (instrumental only)
  - ❌ Vocals/lyrics support
  - ❌ Video generation
  - ❌ Image generation
- **Key Features**:
  - High-quality instrumental music generation
  - Supports BPM and style customization
  - Requires `GEMINI_API_KEY`
- **Best For**: Instrumental music, background tracks, ambient soundscapes

#### MiniMax (via AIMLAPI)
- **Provider Name**: `minimax`
- **API**: AIMLAPI.com
- **Capabilities**:
  - ✅ Music generation
  - ✅ **Vocals/lyrics support** (unique feature)
  - ❌ Video generation
  - ❌ Image generation
- **Key Features**:
  - Supports lyrics files for vocal generation
  - Can generate music with singing
  - Requires `AIMLAPI_KEY`
- **Best For**: Songs with vocals, music with lyrics, vocal tracks

### Video Providers

#### Veo (via Google Gemini)
- **Provider Name**: `veo`
- **API**: Google Gemini API
- **Capabilities**:
  - ✅ Video generation
  - ✅ **Image-to-video conversion** (unique feature)
  - ❌ Music generation
  - ❌ Image generation
- **Key Features**:
  - Text-to-video generation
  - Image-to-video conversion (can animate static images)
  - Supports custom aspect ratios and durations
  - Requires `GEMINI_API_KEY`
- **Best For**: Video content, animated sequences, image-to-video transformations

### Image Providers

#### Imagen (via Google Gemini)
- **Provider Name**: `imagen`
- **API**: Google Gemini API
- **Capabilities**:
  - ✅ Image generation
  - ❌ Music generation
  - ❌ Video generation
- **Key Features**:
  - High-quality image generation
  - Supports various aspect ratios
  - Requires `GEMINI_API_KEY`
- **Best For**: Static image generation, artwork, visual content

### Provider Comparison Summary

| Provider | Music | Video | Image | Vocals | Image-to-Video | API Key Required |
|----------|-------|-------|-------|--------|----------------|------------------|
| **Lyria** | ✅ | ❌ | ❌ | ❌ | ❌ | GEMINI_API_KEY |
| **MiniMax** | ✅ | ❌ | ❌ | ✅ | ❌ | AIMLAPI_KEY |
| **Veo** | ❌ | ✅ | ❌ | ❌ | ✅ | GEMINI_API_KEY |
| **Imagen** | ❌ | ❌ | ✅ | ❌ | ❌ | GEMINI_API_KEY |

---

## 3. Preset System

### Music Presets

All music presets include BPM (beats per minute) and mood information:

| Preset Name | BPM | Mood | Description |
|-------------|-----|------|-------------|
| **jazz** | 120 | smooth | Smooth jazz with melodic saxophone and piano |
| **rock** | 140 | energetic | Energetic rock with electric guitars and drums |
| **classical** | 90 | elegant | Classical orchestral composition |
| **electronic** | 128 | upbeat | Electronic dance music with synthesizers |
| **ambient** | 60 | calm | Ambient atmospheric soundscape |
| **ethio-jazz** | 110 | melancholic | Ethiopian jazz fusion with traditional scales |
| **tizita-blues** | 85 | nostalgic | Tizita mode with blues influences |
| **eskista-dance** | 130 | festive | Eskista dance rhythm with traditional instruments |

**Usage Example**:
```bash
uv run ai-content music --style jazz --provider lyria --duration 30
```

### Video Presets

All video presets include aspect ratio information:

| Preset Name | Aspect Ratio | Description |
|-------------|--------------|-------------|
| **nature** | 16:9 | Natural landscapes and scenery |
| **urban** | 16:9 | Urban cityscapes and architecture |
| **portrait** | 9:16 | Portrait-oriented content (mobile/social) |
| **cinematic** | 21:9 | Cinematic widescreen format |
| **square** | 1:1 | Square format for social media |
| **abstract** | 16:9 | Abstract visual patterns and colors |

**Usage Example**:
```bash
uv run ai-content video --style nature --provider veo --duration 5
```

### How to Add a New Preset

#### Adding a Music Preset

1. Open `src/ai_content/presets/music.py`
2. Add a new entry to the `MUSIC_PRESETS` dictionary:

```python
MUSIC_PRESETS: Dict[str, Dict[str, Any]] = {
    # ... existing presets ...
    "your-preset-name": {
        "bpm": 100,  # Beats per minute
        "mood": "your-mood",  # Mood descriptor
        "description": "Description of the music style",
    },
}
```

3. The preset will automatically be available via CLI and pipeline

#### Adding a Video Preset

1. Open `src/ai_content/presets/video.py`
2. Add a new entry to the `VIDEO_PRESETS` dictionary:

```python
VIDEO_PRESETS: Dict[str, Dict[str, Any]] = {
    # ... existing presets ...
    "your-preset-name": {
        "aspect_ratio": "16:9",  # Aspect ratio
        "description": "Description of the video style",
    },
}
```

3. The preset will automatically be available via CLI and pipeline

**Example: Adding a "lofi" Music Preset**

```python
# In src/ai_content/presets/music.py
"lofi": {
    "bpm": 80,
    "mood": "chill",
    "description": "Lo-fi hip hop beats with vinyl crackle",
},
```

Then use it:
```bash
uv run ai-content music --style lofi --provider lyria
```

---

## 4. CLI Commands

### Available Commands

The CLI provides the following commands:

1. `ai-content --help` - Show help message
2. `ai-content list-providers` - List all available providers
3. `ai-content list-presets` - List all available presets
4. `ai-content music` - Generate music
5. `ai-content video` - Generate video

### Command: `list-providers`

**Usage**: `uv run ai-content list-providers`

**Description**: Lists all available AI providers with their capabilities and configuration status.

**Output Example**:
```
Available Providers:
==================================================

LYRIA
  Status: ✓ Configured
  Capabilities:
    - music

MINIMAX
  Status: ✗ Not configured
  Capabilities:
    - music
    - vocals
```

### Command: `list-presets`

**Usage**: `uv run ai-content list-presets`

**Description**: Lists all available music and video presets with their parameters.

**Output Example**:
```
Music Presets:
==================================================

jazz
  BPM: 120
  Mood: smooth
  Description: Smooth jazz with melodic saxophone and piano

Video Presets:
==================================================

nature
  Aspect Ratio: 16:9
  Description: Natural landscapes and scenery
```

### Command: `music`

**Usage**: `uv run ai-content music [OPTIONS]`

**Description**: Generate music using a specified provider.

#### Options

| Option | Short | Required | Description | Example |
|--------|-------|----------|-------------|---------|
| `--provider` | `-p` | ✅ Yes | Provider name (lyria, minimax) | `--provider lyria` |
| `--style` | `-s` | ❌ No | Preset style name | `--style jazz` |
| `--prompt` | | ❌ No | Custom prompt for generation | `--prompt "smooth jazz"` |
| `--duration` | `-d` | ❌ No | Duration in seconds (default: 30) | `--duration 60` |
| `--bpm` | | ❌ No | Beats per minute | `--bpm 120` |
| `--lyrics` | | ❌ No | Path to lyrics file (.txt) | `--lyrics lyrics.txt` |
| `--output` | `-o` | ❌ No | Output file path | `--output my_music.wav` |

#### Examples

```bash
# Using a preset
uv run ai-content music --style jazz --provider lyria --duration 30

# Custom prompt
uv run ai-content music --prompt "energetic rock song" --provider lyria --bpm 140

# With lyrics (MiniMax only)
uv run ai-content music --style rock --provider minimax --lyrics song_lyrics.txt

# Custom output path
uv run ai-content music --style jazz --provider lyria --output jazz_track.wav
```

#### Notes

- If `--style` is provided, preset BPM and description are automatically applied
- If both `--style` and `--prompt` are provided, the prompt is enhanced with preset description
- `--lyrics` option only works with MiniMax provider
- If `--output` is not specified, a timestamped filename is generated

### Command: `video`

**Usage**: `uv run ai-content video [OPTIONS]`

**Description**: Generate video using a specified provider.

#### Options

| Option | Short | Required | Description | Example |
|--------|-------|----------|-------------|---------|
| `--provider` | `-p` | ✅ Yes | Provider name (veo) | `--provider veo` |
| `--style` | `-s` | ❌ No | Preset style name | `--style nature` |
| `--prompt` | | ❌ No | Custom prompt for generation | `--prompt "sunset over mountains"` |
| `--duration` | `-d` | ❌ No | Duration in seconds (default: 5) | `--duration 10` |
| `--aspect` | `-a` | ❌ No | Aspect ratio (default: 16:9) | `--aspect 9:16` |
| `--image` | | ❌ No | Path to input image for image-to-video | `--image photo.jpg` |
| `--output` | `-o` | ❌ No | Output file path | `--output my_video.mp4` |

#### Examples

```bash
# Using a preset
uv run ai-content video --style nature --provider veo --duration 5

# Custom prompt with aspect ratio
uv run ai-content video --prompt "urban cityscape at night" --provider veo --aspect 16:9

# Image-to-video conversion
uv run ai-content video --image photo.jpg --provider veo --duration 10

# Portrait format
uv run ai-content video --style portrait --provider veo --duration 5
```

#### Notes

- If `--style` is provided, preset aspect ratio is automatically applied
- `--image` option enables image-to-video conversion (Veo only)
- If `--output` is not specified, a timestamped filename is generated

---

## Summary

This codebase provides a flexible, extensible framework for AI content generation with:

- **4 Providers**: Lyria (music), MiniMax (music with vocals), Veo (video), Imagen (images)
- **8 Music Presets**: jazz, rock, classical, electronic, ambient, ethio-jazz, tizita-blues, eskista-dance
- **6 Video Presets**: nature, urban, portrait, cinematic, square, abstract
- **Pipeline Architecture**: Orchestration layer for complex workflows
- **CLI Interface**: User-friendly command-line tools for all operations

The system is designed to be easily extensible - new providers, presets, and pipelines can be added by following the established patterns.
