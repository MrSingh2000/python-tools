import os
import argparse
from pytube import Playlist, YouTube
from pytube.cli import on_progress

def main(args):
    if(args.output == None):
        output = os.getcwd()
    else:
        output = args.output
        
    links_array = []
    if(args.video):
        links_array.append(args.video)
        print("Please wait... downloading Video...")
    else:
        playlist = Playlist(args.playlist)
        links_array = playlist
        print("Please wait... downloading Playlist...")
        output = os.path.join(output, playlist.title)

    for link in links_array:
        video = YouTube(link, on_progress_callback=on_progress)
        print('\n', video.title)
        try:
            video.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').desc().first().download(output)
        except Exception as e:
            print("Error during download: ", e)
    
    print("\n\n Download Completed")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Python Script for downloading youtube videos and playlists.", epilog="Ensure good internet connectivity while downloading, otherwise download will be failed.")

    # Define command-line arguments
    parser.add_argument("--playlist", help="the url of the playlist to download")
    parser.add_argument("--output", help="the output directory where the downloaded files are stored, if not provided it will be working dir. \n NOTE: Playlists are downloaded into a new generated folder by the title of the playlist")
    parser.add_argument("--video", help="the url of the video to download")

    args = parser.parse_args()
    main(args)
