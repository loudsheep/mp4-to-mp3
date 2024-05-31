# MP4 to MP3 Converter

This Python project converts a given .mp4 file into an audio .mp3 file. It uses the `moviepy` library to handle the video and audio extraction and outputs the .mp3 file into a timestamped directory.

## Features

- Converts .mp4 video files to .mp3 audio files.
- Outputs the .mp3 file into a uniquely timestamped directory.
- Automatically opens the directory containing the .mp3 file after conversion.

## Requirements

- Python 3.x
- `moviepy` library

## Installation

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/loudsheep/mp4-to-mp3
cd mp4-to-mp3
```

### Install Dependencies

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

`requirements.txt` should contain the following:

```text
moviepy
```

## Usage

To run the script, simply execute the `convert.py` file:

```bash
python convert.py
```

The script will prompt you to enter the path to the source .mp4 file. It will then extract the audio and save it as an .mp3 file in a newly created directory under `./OUT/` with the current timestamp.

### Example

```bash
Enter source file path (.mp4): /path/to/your/video.mp4
```

After the extraction is complete, the directory containing the .mp3 file will be opened automatically.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [MoviePy](https://zulko.github.io/moviepy/) for providing an easy-to-use interface for video and audio processing in Python.
