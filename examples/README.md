# Example Scripts

This directory contains example scripts for generating AI content.

## Ethiopian Music Example

Generate Ethiopian music styles using the Lyria provider.

### Usage

```bash
# Generate ethio-jazz (default)
uv run python examples/lyria_example_ethiopian.py --style ethio-jazz --duration 30

# Generate tizita-blues
uv run python examples/lyria_example_ethiopian.py --style tizita-blues

# Generate eskista-dance
uv run python examples/lyria_example_ethiopian.py --style eskista-dance --duration 45

# Specify custom output path
uv run python examples/lyria_example_ethiopian.py --style ethio-jazz --output my_ethio_jazz.wav
```

### Available Styles

- `ethio-jazz`: Ethiopian jazz fusion with traditional scales (110 BPM, melancholic)
- `tizita-blues`: Tizita mode with blues influences (85 BPM, nostalgic)
- `eskista-dance`: Eskista dance rhythm with traditional instruments (130 BPM, festive)

## Combine Audio and Video

Combine generated audio and video files into a music video using FFmpeg.

### Prerequisites

Install FFmpeg:
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg

# Windows
# Download from https://ffmpeg.org/download.html
```

### Usage

```bash
# Basic usage
uv run python examples/combine_audio_video.py video.mp4 music.wav -o output.mp4

# With custom codecs
uv run python examples/combine_audio_video.py video.mp4 music.wav -o output.mp4 \
    --audio-codec aac --video-codec copy
```

### Direct FFmpeg Command

You can also use FFmpeg directly:

```bash
ffmpeg -i video.mp4 -i music.wav -c:v copy -c:a aac -shortest output.mp4
```

## Example Lyrics File

The `example_lyrics.txt` file contains sample lyrics that can be used with the MiniMax provider:

```bash
uv run ai-content music \
    --prompt "pop ballad style" \
    --provider minimax \
    --lyrics examples/example_lyrics.txt \
    --duration 60
```

## Content Generation Workflow

### 1. Generate Audio (Instrumental)

```bash
# Using preset
uv run ai-content music --style jazz --provider lyria --duration 30

# Using custom prompt
uv run ai-content music --prompt "energetic rock song" --provider lyria --bpm 140

# Using Ethiopian example script
uv run python examples/lyria_example_ethiopian.py --style ethio-jazz --duration 30
```

### 2. Generate Audio with Vocals (MiniMax)

```bash
# Create or use existing lyrics file
uv run ai-content music \
    --prompt "pop ballad" \
    --provider minimax \
    --lyrics examples/example_lyrics.txt \
    --duration 60
```

### 3. Generate Video

```bash
# Using preset
uv run ai-content video --style nature --provider veo --duration 5

# Custom prompt
uv run ai-content video \
    --prompt "sunset over mountains" \
    --provider veo \
    --aspect 16:9 \
    --duration 10

# Image-to-video
uv run ai-content video \
    --image photo.jpg \
    --provider veo \
    --duration 10
```

### 4. Combine into Music Video (Bonus)

```bash
# Generate audio and video first, then combine
uv run ai-content music --style jazz --provider lyria --duration 30 --output music.wav
uv run ai-content video --style nature --provider veo --duration 30 --output video.mp4
uv run python examples/combine_audio_video.py video.mp4 music.wav -o music_video.mp4
```

## Tips

1. **Start with presets**: Presets are optimized for good results
2. **Experiment with durations**: Longer durations may take more time to generate
3. **Use appropriate providers**: 
   - Lyria for instrumental music
   - MiniMax for music with vocals
   - Veo for video generation
4. **Combine strategically**: Match audio and video durations for best results
5. **Check file formats**: Ensure audio/video formats are compatible with FFmpeg
