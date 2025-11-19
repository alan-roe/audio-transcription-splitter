# Audio Splitter for Transcription

A simple Python utility to split large audio files into smaller chunks (default 30 minutes) to avoid API limits (e.g., Gemini API 600s limit).

## Features
- Splits audio files into specified time chunks.
- Supports various audio formats (MP3, AAC, etc.).
- Automatically handles AAC files by exporting to ADTS format.
- Creates organized output directories for chunks.

## Requirements
- Python 3.x
- [ffmpeg](https://ffmpeg.org/) installed and available in your system PATH.
- Python packages listed in `requirements.txt`.

## Installation

1.  **Install ffmpeg:**
    - **macOS:** `brew install ffmpeg`
    - **Windows/Linux:** Follow official instructions.

2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script with the audio file path:

```bash
python splitter.py <path_to_audio_file> [chunk_length_minutes]
```

**Examples:**

Split into default 30-minute chunks:
```bash
python splitter.py my_podcast.mp3
```

Split into 15-minute chunks:
```bash
python splitter.py interview.aac 15
```

## Output
The script creates a directory named `{filename}_chunks` containing the split files (e.g., `part_001.mp3`, `part_002.mp3`).
