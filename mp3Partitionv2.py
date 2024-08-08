import os
import subprocess
from yt_dlp import YoutubeDL
from pydub import AudioSegment

def download_youtube_video(youtube_url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

    for file in os.listdir(output_path):
        if file.endswith(".mp3"):
            return os.path.join(output_path, file)

def time_str_to_ms(time_str):
    """Convert time string 'HH:MM:SS' to milliseconds."""
    h, m, s = map(int, time_str.split(':'))
    return (h * 3600 + m * 60 + s) * 1000

def split_mp3(mp3_file, segments, output_path):
    audio = AudioSegment.from_mp3(mp3_file)
    for segment in segments:
        start_time = time_str_to_ms(segment['start_time'])
        end_time = time_str_to_ms(segment['end_time'])
        title = segment['title']
        segment_audio = audio[start_time:end_time]
        segment_audio.export(os.path.join(output_path, f"{title}.mp3"), format='mp3')

def main(youtube_url, segments, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    mp3_file = download_youtube_video(youtube_url, output_path)
    split_mp3(mp3_file, segments, output_path)
    os.remove(mp3_file)

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=ay81SRjcq7w&t=2474s&ab_channel=ToshiAizawa"
    output_path = "C:\\Users\\wadeg\\ChiliPeppers\\RHCP_tracks"

    # Define the segments with titles, start times, and end times
    tracks = [
    {"title": "Intro Jam", "start_time": "0:00:17", "end_time": "0:05:36"},
    {"title": "Around The World", "start_time": "0:05:36", "end_time": "0:10:17"},
    {"title": "Dani California", "start_time": "0:10:17", "end_time": "0:15:44"},
    {"title": "The Zephyr Song", "start_time": "0:15:44", "end_time": "0:20:35"},
    {"title": "Aquatic Mouth Dance", "start_time": "0:20:35", "end_time": "0:25:48"},
    {"title": "Danny's Song", "start_time": "0:25:48", "end_time": "0:27:17"},
    {"title": "Otherside", "start_time": "0:27:17", "end_time": "0:32:40"},
    {"title": "Eddie", "start_time": "0:32:40", "end_time": "0:39:36"},
    {"title": "Right On Time", "start_time": "0:39:36", "end_time": "0:42:26"},
    {"title": "Strip My Mind", "start_time": "0:42:26", "end_time": "0:47:14"},
    {"title": "Tippa My Tongue", "start_time": "0:47:14", "end_time": "0:51:56"},
    {"title": "Throw Away Your Television", "start_time": "0:51:56", "end_time": "0:56:46"},
    {"title": "Hard To Concentrate", "start_time": "0:56:46", "end_time": "1:01:26"},
    {"title": "Suck My Kiss", "start_time": "1:01:26", "end_time": "1:05:23"},
    {"title": "Californication Jam", "start_time": "1:05:23", "end_time": "1:08:52"},
    {"title": "Californication", "start_time": "1:08:52", "end_time": "1:14:37"},
    {"title": "Black Summer Jam", "start_time": "1:14:37", "end_time": "1:15:27"},
    {"title": "Black Summer", "start_time": "1:15:27", "end_time": "1:20:14"},
    {"title": "By The Way", "start_time": "1:20:14", "end_time": "1:23:58"},
    {"title": "Encore Break", "start_time": "1:23:58", "end_time": "1:26:30"},
    {"title": "Encore", "start_time": "1:26:30", "end_time": "1:26:51"},
    {"title": "Under The Bridge", "start_time": "1:26:51", "end_time": "1:31:33"},
    {"title": "Give It Away", "start_time": "1:31:33", "end_time": "1:36:25"},
]

    main(youtube_url, tracks, output_path)
