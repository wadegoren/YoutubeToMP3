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
    youtube_url = "https://www.youtube.com/watch?v=abKcWjFMgsE&t=28s&ab_channel=ToshiAizawa"
    output_path = "C:\\Users\\wadeg\\ChiliPeppers\\RHCP_tracks"
    os.makedirs(output_path, exist_ok=True)

    # Define the segments with titles, start times, and end times
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

    main(youtube_url, tracks, output_path)
