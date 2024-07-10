# Audio Transcription Script

This script transcribes audio files using the OpenAI API. 

## Prerequisites

Ensure you have the following installed:
- Python 3.12
- Poetry

## Setup

1. Clone the repository or download the script.
2. Install the necessary Python packages:
    ```bash
    poetry install
    ```
3. Place your input audio files in the `input` folder.

## Usage

Run the script using the following command:

```bash
poetry run python main.py -f <FILENAME_IN_INPUT_FOLDER> -l <LANGUAGE_CODE>
```

### Arguments
- --input or -i: Path to the input audio file (should be placed in the input folder).
- --output or -o: Path to save the output transcription file (will be saved in the output folder).
- --language or -l: Language code of the audio file (e.g., en for English).
