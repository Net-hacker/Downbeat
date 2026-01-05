from pytubefix import YouTube
from ytmusicapi import YTMusic
import FreeSimpleGUI as sg
import subprocess
import sys
import os

sg.theme("DarkGrey3")
ytmusic = YTMusic()
DOWNLOAD_DIR = "downloaded_songs"

def Author(Song):
    search = ytmusic.search(Song, "songs", None, 1, False)
    return str(search[0]['artists'][0]['name'])

def Title(Song):
    search = ytmusic.search(Song, "songs", None, 1, False)
    return str(search[0]['title'])

def Link(Song):
    search = ytmusic.search(Song, "songs", None, 1, False)
    Link = "https://youtube.com/watch?v=" + str(search[0]['videoId'])
    return Link

def GUI():
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "MP3":
            file = Title(values[0]) + ".mp3"
            yt = YouTube(Link(values[0])).streams.filter(only_audio=True).get_audio_only().download(output_path=values["-IN-"], filename=file)
            sg.Popup("Done!")
            window.close()
        elif event == "WAV":
            file = Title(values[0]) + ".wav"
            yt = YouTube(Link(values[0])).streams.filter(only_audio=True).get_audio_only().download(output_path=values["-IN-"], filename=file)
            sg.Popup("Done!")
            window.close()
        elif event == "FLAC":
            file = Title(values[0]) + ".flac"
            yt = YouTube(Link(values[0])).streams.filter(only_audio=True).get_audio_only().download(output_path=values["-IN-"], filename=file)
            sg.Popup("Done!")
            window.close()
        elif event == "OGG":
            file = Title(values[0]) + ".ogg"
            yt = YouTube(Link(values[0])).streams.filter(only_audio=True).get_audio_only().download(output_path=values["-IN-"], filename=file)
            sg.Popup("Done!")
            window.close()


layout = [
    [sg.Text("Music Downloader")],
    [sg.Text("Enter the Musicname: "), sg.Input()],
    [sg.Text("Where should the File be saved: "), sg.FolderBrowse(key="-IN-")],
    [sg.Button("MP3"), sg.Button("WAV"), sg.Button("FLAC"), sg.Button("OGG")]
]

if len(sys.argv) > 2:
    if sys.argv[2] == "--cli":
        args = sys.argv[2:]

        if "--list" in args:
            liste = sys.argv[1]
            isList = True
        else:
            name = sys.argv[1]
            isList = False

        if "--format=MP3" in args:
            format = ".mp3"
        elif "--format=WAV" in args:
            format = ".wav"
        elif "--format=FLAC" in args:
            format = ".flac"
        elif "--format=OGG" in args:
            format = ".ogg"
        else:
            format = ".mp3"

        if (isList):
            try:
                with open(liste, "r", encoding='utf-8') as r:
                    for line in r:
                        song = line.strip()
                        if song:
                            if not os.path.exists(DOWNLOAD_DIR):
                                os.makedirs(DOWNLOAD_DIR)
                            fileName = Title(song)
                            artist = Author(song)
                            yt = YouTube(Link(song)).streams.filter(only_audio=True).first()
                            out_file = yt.download(output_path=DOWNLOAD_DIR)

                            base, ext = os.path.splitext(out_file)
                            new_file = base + ' - ' + artist + '.mp3'
                            os.rename(out_file, new_file)

                            fixed_file = base + "_fixed.mp3"

                            ffmpeg_cmd = [
                                "ffmpeg",
                                "-i", new_file,
                                "-qscale:a", "2",
                                fixed_file
                            ]

                            subprocess.run(ffmpeg_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

                            os.remove(new_file)
                            os.rename(fixed_file, new_file)

                            print(f"{fileName} sucessfully downloaded!\n")
            except:
                    print("No such File")
        else:
            fileName = Title(name)
            artist = Author(name)
            file = fileName + " - " + artist + format
            yt = YouTube(Link(name)).streams.filter(only_audio=True).get_audio_only().download(filename=file)
            print(f"{fileName} - {artist} wurde heruntergeladen!")
        sys.exit(0)
if len(sys.argv) > 1 and not len(sys.argv) > 3:
    print("python3 main.py <Name/List> [Options] [CLI-Options]...")
    print("Options:")
    print("     --cli:                      Uses the CLI Application")
    print("CLI-Options:")
    print("     --list:                     Downloads each Song from a List .txt")
    print("     --format=<File Format>:     Choose your File Format. Default: MP3")
    print("              MP3")
    print("              WAV")
    print("              FLAC")
    print("              OGG")
    print("Help:")
    print("     --help:                     Displays help")
    sys.exit(0)

window = sg.Window("Music Downloader", icon="Icon.ico", element_justification='c').Layout(layout)
GUI()
window.close()
