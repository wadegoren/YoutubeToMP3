from pytube import YouTube
import subprocess
import os
import re

# Define the YouTube URL
video_url = "https://www.youtube.com/watch?v=abKcWjFMgsE&t=28s&ab_channel=ToshiAizawa"

# Tracks information
tracks = [
    {"title": "SE: Amerique", "start_time": "0:00:00", "end_time": "0:00:22"},
    {"title": "Intro Jam", "start_time": "0:00:22", "end_time": "0:04:57"},
    {"title": "Can't Stop", "start_time": "0:04:57", "end_time": "0:10:24"},
    {"title": "Scar Tissue", "start_time": "0:10:24", "end_time": "0:15:15"},
    {"title": "Here Ever After", "start_time": "0:15:15", "end_time": "0:19:55"},
    {"title": "Snow (Hey Oh)", "start_time": "0:19:55", "end_time": "0:27:41"},
    {"title": "Parallel Universe", "start_time": "0:27:41", "end_time": "0:34:28"},
    {"title": "Eddie", "start_time": "0:34:28", "end_time": "0:41:05"},
    {"title": "I Like Dirt", "start_time": "0:41:05", "end_time": "0:43:42"},
    {"title": "Soul To Squeeze Jam", "start_time": "0:43:42", "end_time": "0:44:44"},
    {"title": "Soul To Squeeze", "start_time": "0:44:44", "end_time": "0:50:42"},
    {"title": "Me & My Friends", "start_time": "0:50:42", "end_time": "0:53:34"},
    {"title": "Jam", "start_time": "0:53:34", "end_time": "0:55:10"},
    {"title": "Havana Affair", "start_time": "0:55:10", "end_time": "0:57:45"},
    {"title": "Soul Love", "start_time": "0:57:45", "end_time": "0:59:07"},
    {"title": "Tell Me Baby", "start_time": "0:59:07", "end_time": "1:03:51"},
    {"title": "The Heavy Wing", "start_time": "1:03:51", "end_time": "1:09:33"},
    {"title": "Californication Jam", "start_time": "1:09:33", "end_time": "1:13:58"},
    {"title": "Californication", "start_time": "1:13:58", "end_time": "1:19:33"},
    {"title": "Black Summer Jam", "start_time": "1:19:33", "end_time": "1:20:28"},
    {"title": "Black Summer", "start_time": "1:20:28", "end_time": "1:25:04"},
    {"title": "By The Way", "start_time": "1:25:04", "end_time": "1:31:45"},
    {"title": "I Could Have Lied", "start_time": "1:31:45", "end_time": "1:36:25"},
    {"title": "Give It Away", "start_time": "1:36:25", "end_time": "1:40:00"}
]

# Define the path to the temporary audio file
temp_audio_path = "C:\\Users\\wadeg\\ChiliPeppers\\RHCP_tracks\\temp_audio.mp4"

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
    exit(1)

# Convert AAC to MP3
output_mp3_path = os.path.join(output_dir, "temp_audio.mp3")
subprocess.run(["ffmpeg", "-i", temp_audio_path, "-c:a", "libmp3lame", output_mp3_path])

# Check if the conversion is successful
if os.path.exists(output_mp3_path):
    print("Audio conversion to MP3 completed successfully.")
else:
    print("Error: Audio conversion to MP3 failed.")
    exit(1)

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

    subprocess.run([
        "ffmpeg", "-i", output_mp3_path, "-ss", start_time, "-to", end_time, 
        "-c", "copy", output_file
    ])

# Remove the temporary files
os.remove(temp_audio_path)
os.remove(output_mp3_path)

print("Download, conversion, and splitting completed successfully.")
