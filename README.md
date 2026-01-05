# Downbeat
It's a Program that let's you download Songs (which are on YT-Music)

## Prerequisites
- python3
- FFmpeg

## Usage
```
pip install -r requirements.txt
```

```
> python3 main.py <Name/List> [Options] [CLI-Options]...
> Options:
>      --cli:                      Uses the CLI Application
> CLI-Options:
>      --list:                     Downloads each Song from a List .txt
>      --format=<File Format>:     Choose your File Format. Default: MP3
>               MP3
>               WAV
>               FLAC
>               OGG
> Help:
>      --help:                     Displays help
```

## Example for CLI
```
> python3 main.py "Never Gonna Give You Up!" --cli --format=MP3
```

## Example for GUI
```
> python3 main.py
```
