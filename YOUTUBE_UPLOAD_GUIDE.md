# YouTube Upload Guide

This guide helps you upload your generated content to YouTube for Part 4 submission.

## Upload Requirements

### Title Format
```
[TRP1] Your Name - Content Description
```

**Examples**:
- `[TRP1] John Doe - Ethiopian Jazz Music`
- `[TRP1] Jane Smith - Nature Video with Jazz Soundtrack`
- `[TRP1] Alex Johnson - AI-Generated Music Video`

### Description Template

Your video description should include:

```markdown
Generated using the AI Content Generation Framework for TRP 1 Challenge.

🎵 Generation Details:
- Prompt: [Your prompt here]
- Provider: [lyria/minimax/veo]
- Preset: [preset name, if used]
- Duration: [duration in seconds]

🎨 Creative Decisions:
- [Decision 1: e.g., "Chose jazz preset for smooth, melodic background music"]
- [Decision 2: e.g., "Selected nature video to complement the jazz aesthetic"]
- [Decision 3: e.g., "Combined 30-second audio with matching video duration"]

🔧 Technical Details:
- Audio Format: WAV/MP3
- Video Format: MP4
- Resolution: [if known]
- Frame Rate: [if known]

#TRP1 #AIContentGeneration #AIArt #MusicGeneration #VideoGeneration
```

## Step-by-Step Upload Process

### 1. Prepare Your Content

- **Audio Files**: Ensure your audio is in a compatible format (WAV, MP3)
- **Video Files**: Ensure your video is in MP4 format
- **Combined Videos**: If combining audio and video, use the `combine_audio_video.py` script

### 2. Access YouTube Studio

1. Go to [YouTube Studio](https://studio.youtube.com/)
2. Click "Create" → "Upload video"
3. Select your video file

### 3. Fill in Video Details

#### Basic Information
- **Title**: Use format `[TRP1] Your Name - Content Description`
- **Description**: Use the template above
- **Thumbnail**: Upload a custom thumbnail (optional but recommended)
- **Visibility**: Set to **Unlisted** (as per requirements)

#### Additional Settings
- **Category**: Music / Entertainment / Education (as appropriate)
- **Tags**: Add relevant tags like `TRP1`, `AI`, `Music Generation`, etc.
- **Language**: Set appropriate language

### 4. Upload Settings

- **Visibility**: **Unlisted** (required - allows sharing via link)
- **Age Restriction**: Not required (unless content is inappropriate)
- **Comments**: Enable if you want feedback

### 5. Publish

Click "Publish" and wait for processing to complete.

## Upload Checklist

Before submitting, ensure:

- [ ] Video title follows format: `[TRP1] Your Name - Content Description`
- [ ] Description includes:
  - [ ] Prompt used
  - [ ] Provider name
  - [ ] Preset used (if applicable)
  - [ ] Creative decisions
- [ ] Video is set to **Unlisted**
- [ ] Video has been processed and is viewable
- [ ] YouTube link is copied and added to `SUBMISSION.md`

## Multiple Videos

If uploading multiple videos:

1. **Best Music Track**: Upload your best generated audio (as video with static image or waveform)
2. **Best Video**: Upload your best generated video
3. **Combined Music Video**: Upload your combined audio+video (bonus)

Each video should follow the same title format and include detailed descriptions.

## Tips for Better Uploads

### For Audio-Only Content

If you only have audio files:
1. Convert to video format using FFmpeg:
   ```bash
   # Create video with static image
   ffmpeg -loop 1 -i image.jpg -i audio.wav -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p -shortest output.mp4
   
   # Or create video with waveform visualization
   # (requires additional tools like ffmpeg with filters)
   ```

2. Use online tools to create simple video from audio:
   - [Kapwing](https://www.kapwing.com/)
   - [Clideo](https://clideo.com/)
   - [Online-Convert](https://www.online-convert.com/)

### For Video Content

- Ensure good quality (at least 720p if possible)
- Check that audio is synced properly
- Preview before uploading

### For Combined Videos

- Ensure audio and video are properly synchronized
- Check that durations match
- Verify audio quality is maintained

## Troubleshooting

### Upload Fails

- **File Too Large**: Compress video or use YouTube's compression
- **Format Not Supported**: Convert to MP4 using FFmpeg
- **Processing Stuck**: Wait longer (can take 10-30 minutes for longer videos)

### Video Quality Issues

- **Low Resolution**: Regenerate with higher quality settings if provider supports it
- **Audio Out of Sync**: Re-combine using `combine_audio_video.py` script
- **Poor Quality**: Check original generation parameters

### Privacy Settings

- **Unlisted**: Only people with the link can view (required)
- **Private**: Only you can view (not suitable for submission)
- **Public**: Anyone can view (optional, but not required)

## Example Uploads

### Example 1: Music Track
```
Title: [TRP1] John Doe - AI-Generated Jazz Music

Description:
Generated using Lyria provider with jazz preset.
Duration: 30 seconds
BPM: 120
Mood: Smooth

Creative Decision: Chose jazz preset for its melodic and relaxing qualities.
```

### Example 2: Combined Music Video
```
Title: [TRP1] Jane Smith - Nature Video with Ethiopian Jazz

Description:
Combined AI-generated nature video (Veo) with Ethiopian jazz music (Lyria).

Video:
- Provider: Veo
- Preset: nature
- Duration: 30 seconds
- Aspect Ratio: 16:9

Audio:
- Provider: Lyria
- Preset: ethio-jazz
- Duration: 30 seconds
- BPM: 110

Creative Decisions:
- Selected nature preset for visually appealing landscapes
- Paired with Ethiopian jazz for unique cultural fusion
- Matched durations for seamless synchronization
```

## Final Steps

1. ✅ Upload all videos to YouTube (unlisted)
2. ✅ Copy YouTube links
3. ✅ Add links to `SUBMISSION.md` under "Part 6: Links"
4. ✅ Verify all links work
5. ✅ Complete submission report

---

**Note**: Remember to keep your YouTube links accessible and ensure videos remain unlisted (not private) so evaluators can view them.
