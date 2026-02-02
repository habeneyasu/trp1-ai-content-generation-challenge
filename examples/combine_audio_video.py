#!/usr/bin/env python3
"""Utility script to combine audio and video files into a music video using FFmpeg."""

import argparse
import subprocess
import sys
from pathlib import Path


def check_ffmpeg():
    """Check if FFmpeg is installed."""
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True,
            check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def combine_audio_video(
    video_path: Path,
    audio_path: Path,
    output_path: Path,
    audio_codec: str = "aac",
    video_codec: str = "copy",
):
    """
    Combine audio and video files using FFmpeg.
    
    Args:
        video_path: Path to input video file
        audio_path: Path to input audio file
        output_path: Path to output combined file
        audio_codec: Audio codec to use (default: aac)
        video_codec: Video codec to use (default: copy)
    """
    if not check_ffmpeg():
        raise RuntimeError(
            "FFmpeg is not installed. Please install FFmpeg:\n"
            "  Ubuntu/Debian: sudo apt-get install ffmpeg\n"
            "  macOS: brew install ffmpeg\n"
            "  Windows: Download from https://ffmpeg.org/download.html"
        )
    
    if not video_path.exists():
        raise FileNotFoundError(f"Video file not found: {video_path}")
    
    if not audio_path.exists():
        raise FileNotFoundError(f"Audio file not found: {audio_path}")
    
    # FFmpeg command to combine audio and video
    # -c:v copy: Copy video codec (no re-encoding)
    # -c:a aac: Encode audio as AAC
    # -shortest: Finish when shortest stream ends
    cmd = [
        "ffmpeg",
        "-i", str(video_path),
        "-i", str(audio_path),
        "-c:v", video_codec,
        "-c:a", audio_codec,
        "-shortest",
        "-y",  # Overwrite output file if exists
        str(output_path),
    ]
    
    print(f"Combining audio and video...")
    print(f"  Video: {video_path}")
    print(f"  Audio: {audio_path}")
    print(f"  Output: {output_path}")
    print(f"\nRunning: {' '.join(cmd)}\n")
    
    try:
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=False,
        )
        
        print(f"\n✓ Successfully created music video: {output_path}")
        return output_path
        
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"FFmpeg failed: {str(e)}")


def main():
    """Main function for CLI usage."""
    parser = argparse.ArgumentParser(
        description="Combine audio and video files into a music video"
    )
    parser.add_argument(
        "video",
        type=str,
        help="Path to input video file",
    )
    parser.add_argument(
        "audio",
        type=str,
        help="Path to input audio file",
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        required=True,
        help="Path to output combined file",
    )
    parser.add_argument(
        "--audio-codec",
        type=str,
        default="aac",
        help="Audio codec to use (default: aac)",
    )
    parser.add_argument(
        "--video-codec",
        type=str,
        default="copy",
        help="Video codec to use (default: copy)",
    )
    
    args = parser.parse_args()
    
    try:
        video_path = Path(args.video)
        audio_path = Path(args.audio)
        output_path = Path(args.output)
        
        combine_audio_video(
            video_path=video_path,
            audio_path=audio_path,
            output_path=output_path,
            audio_codec=args.audio_codec,
            video_codec=args.video_codec,
        )
        
        return 0
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
