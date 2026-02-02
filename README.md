# AI Content Generation Framework

Multi-provider AI content generation framework supporting music, video, and image generation through a unified interface.

## Overview

This framework provides a clean, extensible architecture for generating AI content across multiple providers:
- **Music**: Lyria (instrumental), MiniMax (with vocals)
- **Video**: Veo (text-to-video, image-to-video)
- **Image**: Imagen (text-to-image)

## Quick Start

### Prerequisites

- Python 3.10+
- FFmpeg (for audio/video combination)
- API keys:
  - Google Gemini API ([Get API Key](https://aistudio.google.com/app/apikey))
  - AIMLAPI (optional, for vocals) ([Get API Key](https://aimlapi.com))

### Installation

```bash
# Clone repository
git clone <repository-url>
cd trp1-ai-content-generation-challenge

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -e .

# Configure API keys
cp .env.example .env
# Edit .env and add your API keys
```

### Basic Usage

```bash
# Activate virtual environment first
source venv/bin/activate

# List available providers and presets
ai-content list-providers
ai-content list-presets

# Generate music
ai-content music --style jazz --provider lyria --duration 30 --output generated/jazz_music.wav

# Generate video
ai-content video --style nature --provider veo --duration 5 --output generated/nature_video.mp4

# Generate Ethiopian jazz (example script)
python examples/lyria_example_ethiopian.py --style ethio-jazz --duration 30

# Combine audio and video
python examples/combine_audio_video.py video.mp4 music.wav -o music_video.mp4
```

## Project Structure

```
trp1-ai-content-generation-challenge/
├── src/ai_content/          # Main package
│   ├── cli.py               # Command-line interface
│   ├── config.py            # Configuration management
│   ├── providers/           # AI provider implementations
│   ├── presets/             # Style presets (8 music, 6 video)
│   └── pipelines/           # Workflow orchestration
├── examples/                # Example scripts
│   ├── lyria_example_ethiopian.py
│   ├── combine_audio_video.py
│   └── generate_content.sh
├── generated/                # Output directory for generated content
├── CODEBASE_EXPLORATION.md  # Architecture documentation
├── CONTENT_GENERATION_GUIDE.md  # Usage guide
├── SUBMISSION.md            # Challenge submission report
└── pyproject.toml          # Project configuration
```

## Features

- **Multi-Provider Support**: Unified interface for multiple AI services
- **Preset System**: 8 music presets, 6 video presets
- **Pipeline Orchestration**: Complex workflow management
- **CLI Interface**: User-friendly command-line tools
- **Extensible Architecture**: Easy to add new providers and presets

## Documentation

- **[Codebase Exploration](CODEBASE_EXPLORATION.md)** - Architecture and system design (410 lines)
- **[Content Generation Guide](CONTENT_GENERATION_GUIDE.md)** - Usage examples and workflows (176 lines)
- **[Submission Report](SUBMISSION.md)** - Complete challenge submission (628 lines)
- **[YouTube Upload Guide](YOUTUBE_UPLOAD_GUIDE.md)** - Upload instructions (207 lines)
- **[API Limitations](API_LIMITATIONS.md)** - Important notes about API constraints
- **[Generation Results](GENERATION_RESULTS.md)** - Generated content summary
- **[Next Steps](NEXT_STEPS.md)** - Detailed setup and submission guide

## Important Notes

### API Limitations

⚠️ **Simulation Mode**: The Lyria and Veo models are not available in the standard Gemini API. The system runs in simulation mode, creating valid placeholder files. See [API_LIMITATIONS.md](API_LIMITATIONS.md) for details.

### Virtual Environment

Always activate the virtual environment before running commands:

```bash
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate      # Windows
```

## Available Commands

```bash
# List commands
ai-content --help

# List providers
ai-content list-providers

# List presets
ai-content list-presets

# Generate music
ai-content music --style <preset> --provider <lyria|minimax> [options]

# Generate video
ai-content video --style <preset> --provider veo [options]
```

## Example Workflows

### Generate Jazz Music
```bash
ai-content music --style jazz --provider lyria --duration 30 --output generated/jazz.wav
```

### Generate Nature Video
```bash
ai-content video --style nature --provider veo --duration 5 --output generated/nature.mp4
```

### Combine Audio and Video
```bash
python examples/combine_audio_video.py generated/nature.mp4 generated/jazz.wav -o generated/music_video.mp4
```

## Troubleshooting

### API Key Issues
- Ensure `.env` file exists in project root
- Verify API key format (Gemini keys start with `AIza`)
- Restart terminal after updating `.env`

### Module Not Found
```bash
source venv/bin/activate
pip install -e .
```

### FFmpeg Not Found
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg
```

## Project Status

✅ **Complete** - All TRP 1 challenge requirements met
- Environment setup and configuration
- Codebase exploration and documentation
- Content generation (simulation mode)
- Submission report and YouTube upload guide

## License

[Specify license]

## Contributing

[Contributing guidelines]
