#!/usr/bin/env python3
"""Example script for generating Ethiopian music styles using Lyria provider."""

import argparse
import sys
from pathlib import Path

# Add parent directory to path to import ai_content
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.ai_content.pipelines import MusicPipeline


def main():
    """Generate Ethiopian music using Lyria provider."""
    parser = argparse.ArgumentParser(
        description="Generate Ethiopian music styles using Lyria"
    )
    parser.add_argument(
        "--style",
        type=str,
        choices=["ethio-jazz", "tizita-blues", "eskista-dance"],
        default="ethio-jazz",
        help="Ethiopian music style to generate",
    )
    parser.add_argument(
        "--duration",
        type=int,
        default=30,
        help="Duration in seconds (default: 30)",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output file path (optional)",
    )
    parser.add_argument(
        "--provider",
        type=str,
        default="lyria",
        help="Provider to use (default: lyria)",
    )
    
    args = parser.parse_args()
    
    try:
        # Create music pipeline
        pipeline = MusicPipeline(args.provider)
        
        # Generate music
        output_path = args.output or None
        if output_path:
            output_path = Path(output_path)
        
        result_path = pipeline.generate(
            prompt="",
            duration=args.duration,
            style=args.style,
            output_path=output_path,
        )
        
        print(f"\n✓ Successfully generated {args.style} music!")
        print(f"  Output: {result_path}")
        print(f"  Duration: {args.duration} seconds")
        print(f"  Provider: {args.provider}")
        
        return 0
        
    except ValueError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Unexpected error: {str(e)}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
