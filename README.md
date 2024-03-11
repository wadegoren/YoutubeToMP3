# Red Hot Chili Peppers Live Concert Tracks

This Python script downloads a live concert video from YouTube using `pytube`, extracts the audio, and splits it into individual tracks based on predefined timestamps.

## Usage

1. Clone or download the repository.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Run the script.

## Dependencies

- [pytube](https://github.com/nficano/pytube): A lightweight, dependency-free Python library for downloading YouTube videos.
- [FFmpeg](https://www.ffmpeg.org/): A leading multimedia framework capable of decoding, encoding, transcoding, muxing, demuxing, streaming, and filtering audio and video files.

## Instructions

- Update the `video_url` variable with the YouTube URL of the concert video you want to process.
- Modify the `tracks` list with the timestamps and titles for each track of the concert.
- Ensure that `FFmpeg` is installed and available in your system's PATH.
- Run the script.

## Notes

- The script will download the video, extract the audio, convert it to MP3 format, and split it into individual tracks.
- Ensure that you have sufficient disk space for downloading and processing the video.
- This script assumes a stable internet connection for downloading the video from YouTube.

Feel free to contribute or suggest improvements!
