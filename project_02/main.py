import sys
import os
from api_communication import upload, save_transcript

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_audio_file> [output_filename]")
        sys.exit(1)

    input_filename = sys.argv[1]

    if not os.path.exists(input_filename):
        print(f"Error: File '{input_filename}' not found.")
        sys.exit(1)

    # If user provides a second argument, use it as the output filename
    if len(sys.argv) >= 3:
        output_filename = sys.argv[2]
    else:
        # Default to input filename if not specified
        output_filename = os.path.splitext(input_filename)[0]

    print(f"Uploading '{input_filename}'...")
    audio_url = upload(input_filename)

    if audio_url:
        print("Upload successful. Starting transcription...")
        save_transcript(audio_url, output_filename)
    else:
        print("Upload failed.")

if __name__ == "__main__":
    main()
