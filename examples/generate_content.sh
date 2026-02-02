#!/bin/bash
# Example script demonstrating content generation workflow

set -e  # Exit on error

echo "=== AI Content Generation Workflow ==="
echo ""

# Create output directory
OUTPUT_DIR="generated"
mkdir -p "$OUTPUT_DIR"

echo "1. Generating instrumental music (Jazz style)..."
uv run ai-content music \
    --style jazz \
    --provider lyria \
    --duration 30 \
    --output "$OUTPUT_DIR/jazz_music.wav" || echo "Note: Requires GEMINI_API_KEY"

echo ""
echo "2. Generating Ethiopian jazz music..."
uv run python examples/lyria_example_ethiopian.py \
    --style ethio-jazz \
    --duration 30 \
    --output "$OUTPUT_DIR/ethio_jazz.wav" || echo "Note: Requires GEMINI_API_KEY"

echo ""
echo "3. Generating music with vocals (if AIMLAPI_KEY is set)..."
if [ -n "$AIMLAPI_KEY" ]; then
    uv run ai-content music \
        --prompt "pop ballad style" \
        --provider minimax \
        --lyrics examples/example_lyrics.txt \
        --duration 60 \
        --output "$OUTPUT_DIR/vocal_music.wav" || echo "Note: AIMLAPI may require additional setup"
else
    echo "Skipping: AIMLAPI_KEY not set"
fi

echo ""
echo "4. Generating video (Nature style)..."
uv run ai-content video \
    --style nature \
    --provider veo \
    --duration 5 \
    --output "$OUTPUT_DIR/nature_video.mp4" || echo "Note: Requires GEMINI_API_KEY"

echo ""
echo "5. Combining audio and video (if both exist)..."
if [ -f "$OUTPUT_DIR/jazz_music.wav" ] && [ -f "$OUTPUT_DIR/nature_video.mp4" ]; then
    uv run python examples/combine_audio_video.py \
        "$OUTPUT_DIR/nature_video.mp4" \
        "$OUTPUT_DIR/jazz_music.wav" \
        -o "$OUTPUT_DIR/music_video.mp4" || echo "Note: Requires FFmpeg to be installed"
else
    echo "Skipping: Required audio or video files not found"
fi

echo ""
echo "=== Generation Complete ==="
echo "Check the '$OUTPUT_DIR' directory for generated files"
