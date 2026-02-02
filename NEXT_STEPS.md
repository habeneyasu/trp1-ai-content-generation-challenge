# Setup and Submission Guide

Complete guide for TRP 1 challenge setup and submission.

## Quick Setup

1. **Configure API Keys**:
   ```bash
   cp .env.example .env
   nano .env  # Add your Gemini API key (starts with AIza)
   ```

2. **Install Dependencies**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -e .
   ```

3. **Verify Setup**:
   ```bash
   ai-content list-providers  # Should show providers as configured
   ```

## Generate Content

### Basic Generation

```bash
# Activate virtual environment first
source venv/bin/activate

# Generate music
ai-content music --style jazz --provider lyria --duration 30 --output generated/jazz.wav

# Generate video
ai-content video --style nature --provider veo --duration 5 --output generated/nature.mp4

# Generate Ethiopian jazz
python examples/lyria_example_ethiopian.py --style ethio-jazz --duration 30
```

### Combine Audio and Video

```bash
python examples/combine_audio_video.py generated/nature.mp4 generated/jazz.wav -o generated/music_video.mp4
```

**Note**: See [CONTENT_GENERATION_GUIDE.md](CONTENT_GENERATION_GUIDE.md) for detailed examples.

## Upload to YouTube

1. Go to [YouTube Studio](https://studio.youtube.com/)
2. Upload your best generated content
3. Use title format: `[TRP1] Your Name - Content Description`
4. Set visibility to **Unlisted**
5. Add description (see [YOUTUBE_UPLOAD_GUIDE.md](YOUTUBE_UPLOAD_GUIDE.md) for template)

## Update Submission

1. Open `SUBMISSION.md`
2. Add YouTube link(s) in "Part 6: Links" section
3. Update generation log with actual file sizes
4. Document any challenges encountered (see [API_LIMITATIONS.md](API_LIMITATIONS.md))

## Important Notes

- ⚠️ **API Limitations**: Lyria and Veo models are not available in standard Gemini API. System runs in simulation mode. See [API_LIMITATIONS.md](API_LIMITATIONS.md).
- Always activate virtual environment: `source venv/bin/activate`
- FFmpeg required for audio/video combination: `sudo apt-get install ffmpeg`

## Troubleshooting

- **API Key Issues**: Verify `.env` file exists and key starts with `AIza`
- **Module Errors**: Run `pip install -e .` in activated virtual environment
- **FFmpeg Errors**: Install FFmpeg: `sudo apt-get install ffmpeg`

For detailed documentation, see:
- [CONTENT_GENERATION_GUIDE.md](CONTENT_GENERATION_GUIDE.md) - Generation examples
- [YOUTUBE_UPLOAD_GUIDE.md](YOUTUBE_UPLOAD_GUIDE.md) - Upload instructions
- [API_LIMITATIONS.md](API_LIMITATIONS.md) - API constraints
