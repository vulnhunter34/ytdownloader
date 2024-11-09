import os
import yt_dlp

# Function to download a single video
def download_video(video_url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Best video + best audio
        'outtmpl': 'videos/%(title)s.%(ext)s',  # Output path for videos
        'merge_output_format': 'mp4',  # Merge audio and video into mp4
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Starting download for: {video_url}")
        ydl.download([video_url])
        print(f"Download complete for: {video_url}")

# Function to download all videos from a playlist
def download_playlist(playlist_url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Best video + best audio
        'outtmpl': 'videos/%(title)s.%(ext)s',  # Output path for videos
        'merge_output_format': 'mp4',  # Merge audio and video into mp4
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(f"Downloading playlist: {playlist_url}")
        ydl.download([playlist_url])

# Main function to handle user input
def main():
    url = input("Enter the YouTube video or playlist URL: ")

    # Check if the URL is a playlist or a single video
    if 'playlist' in url:
        download_playlist(url)
    else:
        download_video(url)

# Ensure the videos directory exists
if not os.path.exists('videos'):
    os.makedirs('videos')

if __name__ == "__main__":
    main()
