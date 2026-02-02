# Part 3: Content Generation Guide

This guide provides quick reference commands for generating AI content as required in Part 3.

## Required Generations

### 1. Generate Audio Content (Instrumental)

#### Using CLI with Preset
```bash
uv run ai-content music --style jazz --provider lyria --duration 30
```

#### Using Ethiopian Example Script
```bash
# Ethio-jazz style
uv run python examples/lyria_example_ethiopian.py --style ethio-jazz --duration 30

# Tizita-blues style
uv run python examples/lyria_example_ethiopian.py --style tizita-blues

# Eskista-dance style
uv run python examples/lyria_example_ethiopian.py --style eskista-dance
```

#### Using Custom Prompt
```bash
uv run ai-content music --prompt "Your creative prompt here" --provider lyria
```

### 2. Generate Audio with Vocals (MiniMax)

**Step 1**: Create a lyrics file (`.txt` format)

Example: `my_lyrics.txt`
```
Verse 1:
Your lyrics here...

Chorus:
Your chorus here...
```

**Step 2**: Generate music with vocals
```bash
uv run ai-content music \
    --prompt "pop ballad style" \
    --provider minimax \
    --lyrics my_lyrics.txt \
    --duration 60
```

**Note**: Requires `AIMLAPI_KEY` in `.env` file.

### 3. Generate Video

```bash
uv run ai-content video --style nature --provider veo --duration 5
```

**Custom video generation**:
```bash
uv run ai-content video \
    --prompt "sunset over mountains" \
    --provider veo \
    --aspect 16:9 \
    --duration 10
```

**Image-to-video** (Veo only):
```bash
uv run ai-content video \
    --image photo.jpg \
    --provider veo \
    --duration 10
```

### 4. Combine into Music Video (Bonus)

**Option 1: Using Python Script**
```bash
uv run python examples/combine_audio_video.py video.mp4 music.wav -o output.mp4
```

**Option 2: Using FFmpeg Directly**
```bash
ffmpeg -i video.mp4 -i music.wav -c:v copy -c:a aac -shortest output.mp4
```

**Complete Workflow Example**:
```bash
# 1. Generate audio
uv run ai-content music --style jazz --provider lyria --duration 30 --output music.wav

# 2. Generate video
uv run ai-content video --style nature --provider veo --duration 30 --output video.mp4

# 3. Combine
uv run python examples/combine_audio_video.py video.mp4 music.wav -o music_video.mp4
```

## Quick Start Script

Run the automated workflow script:

```bash
bash examples/generate_content.sh
```

This script will:
1. Generate instrumental music (Jazz)
2. Generate Ethiopian jazz music
3. Generate music with vocals (if AIMLAPI_KEY is set)
4. Generate nature video
5. Combine audio and video (if both exist and FFmpeg is installed)

## Artifacts Checklist

For Part 3 submission, ensure you have:

- [ ] At least 1 generated audio file (different styles/providers)
  - Example: `jazz_music.wav`, `ethio_jazz.wav`
- [ ] At least 1 generated video file
  - Example: `nature_video.mp4`
- [ ] (Bonus) 1 combined music video
  - Example: `music_video.mp4`

## Troubleshooting

### API Key Issues
- Ensure `.env` file exists and contains valid API keys
- Check key names: `GEMINI_API_KEY`, `AIMLAPI_KEY`
- Verify keys are not placeholder values

### FFmpeg Not Found
```bash
# Ubuntu/Debian
sudo apt-get install ffmpeg

# macOS
brew install ffmpeg
```

### File Format Issues
- Audio: `.wav`, `.mp3` formats supported
- Video: `.mp4` format recommended
- Ensure audio and video durations match for best results

### Provider Errors
- **Lyria**: Requires `GEMINI_API_KEY`
- **MiniMax**: Requires `AIMLAPI_KEY`
- **Veo**: Requires `GEMINI_API_KEY`
- Check provider status: `uv run ai-content list-providers`

## Example Output Files

After running the generation commands, you should see files like:

```
generated/
├── jazz_music.wav          # Instrumental music
├── ethio_jazz.wav          # Ethiopian jazz style
├── vocal_music.wav         # Music with vocals (if AIMLAPI_KEY set)
├── nature_video.mp4        # Generated video
└── music_video.mp4         # Combined audio+video (bonus)
```

## Next Steps

After generating content:
1. Review generated files
2. Test different styles and prompts
3. Experiment with durations and parameters
4. Combine audio and video for music videos
5. Document your results in `SUBMISSION.md`
