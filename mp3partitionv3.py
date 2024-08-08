import os
import streamlit as st
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

def main():
    st.title('YouTube to MP3 Splitter')

    youtube_url = st.text_input('YouTube URL', value="https://www.youtube.com/watch?v=ay81SRjcq7w&t=2474s&ab_channel=ToshiAizawa")
    output_path = st.text_input('Output Path', value="C:\\Users\\wadeg\\ChiliPeppers\\RHCP_tracks")

    # Segment Input
    num_segments = st.number_input('Number of Tracks', min_value=1, max_value=50, value=23)

    segments = []
    for i in range(num_segments):
        title = st.text_input(f'Title {i+1}', value=f'Track {i+1}')
        start_time = st.text_input(f'Start Time {i+1} (HH:MM:SS)', value='0:00:00')
        end_time = st.text_input(f'End Time {i+1} (HH:MM:SS)', value='0:00:30')
        segments.append({"title": title, "start_time": start_time, "end_time": end_time})

    # Download and Split Button
    if st.button('Download and Split'):
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        mp3_file = download_youtube_video(youtube_url, output_path)
        split_mp3(mp3_file, segments, output_path)
        os.remove(mp3_file)
        st.success('Download and split complete!')

if __name__ == "__main__":
    main()
