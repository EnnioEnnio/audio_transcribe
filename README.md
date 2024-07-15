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
4. Create an `.env` file in the root directory and add the following:
- `OPENAI_API_KEY="YOUR_OPENAI_API_KEY"`
    - Alternatively run `export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"` in the terminal before running the script.


## Usage

Run the script using the following command:

```bash
poetry run python main.py -f <FILENAME_IN_INPUT_FOLDER> -l <LANGUAGE_CODE>
```

### Arguments
- --file or -f: name of the file to be transcribed with file ending (should be placed in the input folder).
- --language or -l: Language code of the audio file (e.g., en for English).
