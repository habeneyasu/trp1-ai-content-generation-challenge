"""Command-line interface for AI content generation."""

import click
from pathlib import Path
from typing import Optional

from .providers import PROVIDERS, get_provider
from .presets import list_music_presets, list_video_presets, get_music_preset, get_video_preset
from .config import Config


@click.group()
@click.version_option(version="0.1.0")
def main():
    """AI Content Generation Framework - Multi-provider AI content generation."""
    pass


@main.command()
def list_providers():
    """List all available providers."""
    click.echo("Available Providers:")
    click.echo("=" * 50)
    
    for name, provider_class in PROVIDERS.items():
        try:
            provider = provider_class()
            capabilities = provider.get_capabilities()
            has_key = provider.validate_config()
            
            status = "✓ Configured" if has_key else "✗ Not configured"
            
            click.echo(f"\n{name.upper()}")
            click.echo(f"  Status: {status}")
            click.echo(f"  Capabilities:")
            for cap, enabled in capabilities.items():
                if enabled:
                    click.echo(f"    - {cap}")
        except Exception as e:
            click.echo(f"\n{name.upper()}")
            click.echo(f"  Status: Error - {str(e)}")


@main.command()
def list_presets():
    """List all available presets."""
    click.echo("Music Presets:")
    click.echo("=" * 50)
    music_presets = list_music_presets()
    for name, preset in music_presets.items():
        click.echo(f"\n{name}")
        click.echo(f"  BPM: {preset.get('bpm', 'N/A')}")
        click.echo(f"  Mood: {preset.get('mood', 'N/A')}")
        click.echo(f"  Description: {preset.get('description', 'N/A')}")
    
    click.echo("\n\nVideo Presets:")
    click.echo("=" * 50)
    video_presets = list_video_presets()
    for name, preset in video_presets.items():
        click.echo(f"\n{name}")
        click.echo(f"  Aspect Ratio: {preset.get('aspect_ratio', 'N/A')}")
        click.echo(f"  Description: {preset.get('description', 'N/A')}")


@main.command()
@click.option("--style", "-s", help="Preset style name")
@click.option("--provider", "-p", required=True, help="Provider name (lyria, minimax)")
@click.option("--prompt", help="Custom prompt for generation")
@click.option("--duration", "-d", type=int, default=30, help="Duration in seconds")
@click.option("--bpm", type=int, help="Beats per minute")
@click.option("--lyrics", type=click.Path(exists=True), help="Path to lyrics file (.txt)")
@click.option("--output", "-o", type=click.Path(), help="Output file path")
def music(style, provider, prompt, duration, bpm, lyrics, output):
    """Generate music using specified provider."""
    try:
        # Get provider
        provider_instance = get_provider(provider)
        
        # Validate provider supports music
        if not provider_instance.get_capabilities().get("music", False):
            click.echo(f"Error: {provider} does not support music generation", err=True)
            return
        
        # Get preset if style provided
        preset = None
        if style:
            preset = get_music_preset(style)
            if not preset:
                click.echo(f"Warning: Unknown preset '{style}', ignoring", err=True)
            else:
                # Use preset BPM if not specified
                if bpm is None and preset.get("bpm"):
                    bpm = preset.get("bpm")
                # Enhance prompt with preset description
                if prompt and preset.get("description"):
                    prompt = f"{preset['description']}, {prompt}"
                elif not prompt:
                    prompt = preset.get("description", "")
        
        # Use style as prompt if no prompt provided
        if not prompt:
            prompt = style or "instrumental music"
        
        # Handle lyrics file
        lyrics_path = None
        if lyrics:
            lyrics_path = Path(lyrics)
            if not lyrics_path.exists():
                click.echo(f"Error: Lyrics file not found: {lyrics}", err=True)
                return
        
        # Set output path
        output_path = None
        if output:
            output_path = Path(output)
        
        # Generate music
        result_path = provider_instance.generate_music(
            prompt=prompt,
            duration=duration,
            bpm=bpm,
            style=style,
            lyrics_file=lyrics_path,
            output_path=output_path,
        )
        
        click.echo(f"\n✓ Music generated successfully: {result_path}")
        
    except ValueError as e:
        click.echo(f"Error: {str(e)}", err=True)
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise


@main.command()
@click.option("--style", "-s", help="Preset style name")
@click.option("--provider", "-p", required=True, help="Provider name (veo)")
@click.option("--prompt", help="Custom prompt for generation")
@click.option("--duration", "-d", type=int, default=5, help="Duration in seconds")
@click.option("--aspect", "-a", default="16:9", help="Aspect ratio (e.g., 16:9, 9:16)")
@click.option("--image", type=click.Path(exists=True), help="Path to input image for image-to-video")
@click.option("--output", "-o", type=click.Path(), help="Output file path")
def video(style, provider, prompt, duration, aspect, image, output):
    """Generate video using specified provider."""
    try:
        # Get provider
        provider_instance = get_provider(provider)
        
        # Validate provider supports video
        if not provider_instance.get_capabilities().get("video", False):
            click.echo(f"Error: {provider} does not support video generation", err=True)
            return
        
        # Get preset if style provided
        if style:
            preset = get_video_preset(style)
            if not preset:
                click.echo(f"Warning: Unknown preset '{style}', ignoring", err=True)
            else:
                # Use preset aspect ratio if not specified
                if aspect == "16:9" and preset.get("aspect_ratio"):
                    aspect = preset.get("aspect_ratio")
                # Enhance prompt with preset description
                if prompt and preset.get("description"):
                    prompt = f"{preset['description']}, {prompt}"
                elif not prompt:
                    prompt = preset.get("description", "")
        
        # Use style as prompt if no prompt provided
        if not prompt:
            prompt = style or "video content"
        
        # Handle image path
        image_path = None
        if image:
            image_path = Path(image)
            if not image_path.exists():
                click.echo(f"Error: Image file not found: {image}", err=True)
                return
        
        # Set output path
        output_path = None
        if output:
            output_path = Path(output)
        
        # Generate video
        result_path = provider_instance.generate_video(
            prompt=prompt,
            duration=duration,
            aspect_ratio=aspect,
            style=style,
            image_path=image_path,
            output_path=output_path,
        )
        
        click.echo(f"\n✓ Video generated successfully: {result_path}")
        
    except ValueError as e:
        click.echo(f"Error: {str(e)}", err=True)
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise


if __name__ == "__main__":
    main()
