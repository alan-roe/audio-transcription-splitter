import os
import sys
import math
from pydub import AudioSegment

def split_audio(file_path, chunk_length_ms=30 * 60 * 1000):
    """
    Splits an audio file into chunks of a specified length.

    Args:
        file_path (str): Path to the input audio file.
        chunk_length_ms (int): Length of each chunk in milliseconds. Default is 30 minutes.
    """
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    filename = os.path.basename(file_path)
    name, ext = os.path.splitext(filename)
    
    # Create output directory
    output_dir = f"{name}_chunks"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")
    else:
        print(f"Using existing directory: {output_dir}")

    print(f"Loading audio file: {file_path}...")
    try:
        audio = AudioSegment.from_file(file_path)
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    total_length_ms = len(audio)
    num_chunks = math.ceil(total_length_ms / chunk_length_ms)
    
    print(f"Total duration: {total_length_ms / 1000 / 60:.2f} minutes")
    print(f"Splitting into {num_chunks} chunks of {chunk_length_ms / 1000 / 60:.2f} minutes each...")

    for i in range(num_chunks):
        start_time = i * chunk_length_ms
        end_time = min((i + 1) * chunk_length_ms, total_length_ms)
        
        chunk = audio[start_time:end_time]
        
        # Format chunk filename: part_001.mp3, part_002.mp3, etc.
        chunk_filename = f"part_{i+1:03d}{ext}"
        chunk_path = os.path.join(output_dir, chunk_filename)
        
        print(f"Exporting {chunk_filename}...")
        # Handle AAC format specifically
        fmt = ext.replace('.', '')
        if fmt == 'aac':
            fmt = 'adts'
            
        chunk.export(chunk_path, format=fmt)

    print("Done!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python splitter.py <audio_file_path> [chunk_length_minutes]")
    else:
        file_path = sys.argv[1]
        chunk_minutes = 30
        if len(sys.argv) > 2:
            try:
                chunk_minutes = int(sys.argv[2])
            except ValueError:
                print("Invalid chunk length provided. Using default 30 minutes.")
        
        split_audio(file_path, chunk_length_ms=chunk_minutes * 60 * 1000)
