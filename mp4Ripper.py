import yt_dlp
import moviepy.editor as mp

def download_youtube_video(youtube_url, output_path):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{output_path}/rhcptoronto.%(ext)s',
        'merge_output_format': 'mp4'
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

def convert_to_compatible_format(input_path, output_path):
    video = mp.VideoFileClip(input_path)
    video.write_videofile(output_path, codec='libx264', audio_codec='aac')

def main():
    youtube_url = "https://www.youtube.com/watch?v=abKcWjFMgsE&t=92s&ab_channel=ToshiAizawa"
    output_path = "C:\\Users\\wadeg\\ChiliPeppers\\LIVE_VIDEOS"
    
    print("Downloading video...")
    download_youtube_video(youtube_url, output_path)
    
    input_filename = f"{output_path}/rhcptoronto.mp4"
    output_filename = f"{output_path}/converted_rhcptoronto.mp4"
    
    print("Converting video to compatible format...")
    convert_to_compatible_format(input_filename, output_filename)
    
    print(f"Video downloaded and saved as {output_filename}")

if __name__ == "__main__":
    main()
