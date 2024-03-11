from pytube import YouTube
import subprocess
import os
import re

# Define the YouTube URL
video_url = "https://www.youtube.com/watch?v=d_HiP0i7dyk&ab_channel=RedHotChiliPeppersArgentina"

# Define the timestamps and titles for each track
tracks = [
    {"title": "Stage Entrance", "start_time": "0:56", "end_time": "1:20"},
    {"title": "Intro Jam", "start_time": "1:20", "end_time": "6:26"},
    {"title": "Can't Stop", "start_time": "6:26", "end_time": "12:40"},
    {"title": "The Zephyr Song", "start_time": "12:40", "end_time": "17:24"},
    {"title": "Chad Solo", "start_time": "17:24", "end_time": "18:28"},
    {"title": "Dani California", "start_time": "18:28", "end_time": "24:33"},
    {"title": "Aquatic Mouth Dance", "start_time": "24:33", "end_time": "29:51"},
    {"title": "Jam into Throw Away Your Television", "start_time": "29:51", "end_time": "36:05"},
    {"title": "Eddie (John Frusciante)", "start_time": "36:05", "end_time": "42:48"},
    {"title": "Jam into Soul to Squeeze", "start_time": "42:48", "end_time": "49:56"},
    {"title": "Parallel Universe", "start_time": "49:56", "end_time": "55:03"},
    {"title": "Terrapin (Syd Barret Cover by John)", "start_time": "55:03", "end_time": "57:10"},
    {"title": "Strip My Mind", "start_time": "57:10", "end_time": "1:02:28"},
    {"title": "London Calling Tease into Right On Time", "start_time": "1:02:28", "end_time": "1:05:10"},
    {"title": "The Heavy Wing", "start_time": "1:05:10", "end_time": "1:11:56"},
    {"title": "Suck My Kiss", "start_time": "1:11:56", "end_time": "1:15:43"},
    {"title": "Californication Intro Jam", "start_time": "1:15:43", "end_time": "1:19:35"},
    {"title": "Californication", "start_time": "1:19:35", "end_time": "1:25:06"},
    {"title": "What is Soul Outro Jam (Funkadelic Cover)", "start_time": "1:25:06", "end_time": "1:26:58"},
    {"title": "Black Summer", "start_time": "1:26:58", "end_time": "1:31:51"},
    {"title": "By the Way", "start_time": "1:31:51", "end_time": "1:35:33"},
    {"title": "End of Main Set", "start_time": "1:35:33", "end_time": "1:37:56"},
    {"title": "Encore", "start_time": "1:37:56", "end_time": "1:38:16"},
    {"title": "I Could Have Lied", "start_time": "1:38:16", "end_time": None}
]



# Define the path to the temporary audio file
temp_audio_path = "C:\\Users\\wadeg\\ChiliPeppers\\RHCP_tracks\\temp_audio"

# Create a directory to store the individual tracks
output_dir = "C:\\Users\\wadeg\\ChiliPeppers\\RHCP_tracks"
os.makedirs(output_dir, exist_ok=True)

# Download the video using pytube
yt = YouTube(video_url)
stream = yt.streams.filter(only_audio=True).first()
stream.download(output_path=output_dir, filename="temp_audio")

# Check if the file is downloaded properly
if os.path.exists(temp_audio_path):
    print("Temporary audio file downloaded successfully.")
else:
    print("Error: Temporary audio file not downloaded.")

# Convert AAC to MP3
output_mp3_path = "C:\\Users\\wadeg\\ChiliPeppers\\RHCP_tracks\\temp_audio.mp3"
subprocess.run(["ffmpeg", "-i", temp_audio_path, "-c:a", "libmp3lame", output_mp3_path])

# Check if the conversion is successful
if os.path.exists(output_mp3_path):
    print("Audio conversion to MP3 completed successfully.")
else:
    print("Error: Audio conversion to MP3 failed.")

# Function to sanitize filenames by removing or replacing special characters
def sanitize_filename(filename):
    # Replace special characters with underscores
    sanitized_filename = re.sub(r'[^\w\-_. ]', '_', filename)
    return sanitized_filename

# Split the audio into individual tracks
for i, track in enumerate(tracks):
    output_file = os.path.join(output_dir, f"{i+1:02d}_{sanitize_filename(track['title'])}.mp3")
    start_time = track["start_time"]
    end_time = track["end_time"]

    if end_time:
        subprocess.run(["ffmpeg", "-i", output_mp3_path, "-ss", start_time, "-to", end_time, "-c", "copy", output_file])
    else:
        subprocess.run(["ffmpeg", "-i", output_mp3_path, "-ss", start_time, "-c", "copy", output_file])

# Remove the temporary files
os.remove(temp_audio_path)
os.remove(output_mp3_path)

print("Download, conversion, and splitting completed successfully.")
