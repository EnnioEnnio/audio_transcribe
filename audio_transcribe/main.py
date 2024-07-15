import argparse
import logging
import threading
import time
from pathlib import Path

from openai import OpenAI

logger = logging.Logger(__name__)

loading = True


def loading_animation():
    frames = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    while loading:
        for frame in frames:
            if not loading:
                break
            print(f"\r{frame} Transcribing...", end="", flush=True)
            time.sleep(0.1)
    print("\rTranscription complete!       ")


def transcribe_audio(file_path: str, output_path: str, language: str) -> None:
    global loading
    client = OpenAI()
    logger.log(logging.INFO, "Transcribing audio file...")

    loading = True
    animation_thread = threading.Thread(target=loading_animation)
    animation_thread.start()

    with open(file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            language=language,
            model="whisper-1",
            file=audio_file,
            response_format="text",
        )

    loading = False
    animation_thread.join()

    with open(output_path, "w") as output_file:
        output_file.write(transcription)

    logger.log(logging.INFO, f"Transcription saved to {output_path}")


def get_file_paths(input_file: str) -> tuple[str, str]:
    base_dir = Path(__file__).parent.parent

    input_dir = base_dir / "input"
    output_dir = base_dir / "output"

    input_file_path = input_dir / input_file
    output_file_name = f"{input_file_path.stem}_transcription.txt"
    output_file_path = output_dir / output_file_name

    if not input_file_path.exists():
        logger.log(logging.ERROR, f"Error: The file {input_file_path} does not exist.")
        raise FileNotFoundError(f"The file {input_file_path} does not exist.")

    return str(input_file_path), str(output_file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe audio files.")
    parser.add_argument(
        "--file",
        "-f",
        required=True,
        help="Name of the input audio file including extension, e.g. audio.mp3",
    )
    parser.add_argument(
        "--language",
        "-l",
        default="en",
        help="Language of the audio file, e.g. en, de, ...",
    )
    args = parser.parse_args()

    input_file_path, output_file_path = get_file_paths(args.file)

    transcribe_audio(input_file_path, output_file_path, args.language)
