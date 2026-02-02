# AI Content Generation Framework

Multi-provider AI content generation framework supporting music, video, and image generation through a unified interface.

## Overview

This framework provides a clean, extensible architecture for generating AI content across multiple providers:
- **Music**: Lyria (instrumental), MiniMax (with vocals)
- **Video**: Veo (text-to-video, image-to-video)
- **Image**: Imagen (text-to-image)

## Quick Start

### Installation

```bash
# Clone repository
git clone <repository-url>
cd trp1-ai-content-generation-challenge

# Setup environment
cp .env.example .env
# Edit .env with your API keys

# Install dependencies
uv sync

# Verify installation
uv run ai-content --help
```

### Basic Usage

```bash
# List available providers
uv run ai-content list-providers

# List available presets
uv run ai-content list-presets

# Generate music
uv run ai-content music --style jazz --provider lyria --duration 30

# Generate video
uv run ai-content video --style nature --provider veo --duration 5
```

## Project Structure

```
trp1-ai-content-generation-challenge/
├── src/ai_content/          # Main package
│   ├── cli.py               # Command-line interface
│   ├── config.py            # Configuration management
│   ├── providers/           # AI provider implementations
│   ├── presets/             # Style presets
│   └── pipelines/           # Workflow orchestration
├── examples/                # Example scripts
├── CODEBASE_EXPLORATION.md  # Architecture documentation
├── CONTENT_GENERATION_GUIDE.md  # Usage guide
├── SUBMISSION.md            # Submission report
└── pyproject.toml          # Project configuration
```

## Documentation

- **[Codebase Exploration](CODEBASE_EXPLORATION.md)** - Architecture and system design
- **[Content Generation Guide](CONTENT_GENERATION_GUIDE.md)** - Usage examples and workflows
- **[Submission Report](SUBMISSION.md)** - Complete challenge submission
- **[YouTube Upload Guide](YOUTUBE_UPLOAD_GUIDE.md)** - Upload instructions
- **[Examples README](examples/README.md)** - Example script documentation

## Features

- **Multi-Provider Support**: Unified interface for multiple AI services
- **Preset System**: 8 music presets, 6 video presets
- **Pipeline Orchestration**: Complex workflow management
- **CLI Interface**: User-friendly command-line tools
- **Extensible Architecture**: Easy to add new providers and presets

## Requirements

- Python 3.10+
- uv (package manager) or pip
- API keys for desired providers:
  - Google Gemini API (for Lyria, Veo, Imagen)
  - AIMLAPI (for MiniMax)

## License

[Specify license]

## Contributing

[Contributing guidelines]
