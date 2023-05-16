# EasyTranscriber

The Easy Transcriber is a tool developed using PySide6 and using OpenAI whisper for transcribing audio and video files. It provides a user-friendly interface for selecting files, performing transcription, and saving transcribed text.

## Features

-   Transcribe audio files (MP3 format) using the Whisper library.
-   Transcribe video files (MP4 format) by extracting audio and performing transcription.
-   Display transcribed text in the application window.
-   Save transcribed text as an SRT (SubRip) file.

## Technologies Used

-   Python: Programming language used for the development of the software.
-   PySide6: Python bindings for the Qt framework, used for creating the graphical user interface.
-   Whisper: A library for speech recognition and transcription.
-   FFmpeg: A multimedia framework used for extracting audio from video files.

## Getting Started

To run the Transcriber Software, follow these steps:

1. Install the required dependencies:

    - Python (version X.X.X)
    - PySide6 (installation instructions: [link])
    - Whisper library (installation instructions: [link])
    - FFmpeg (installation instructions: [link])

2. Clone the project repository:
    ```bash
    git clone https://github.com/your-username/transcriber-software.git
    ```
    Navigate to the Project Directory:
    ```bash
    cd EasyTranscriber
    ```
    Run the Application:
    ```bash
    python ./main.py
    ```
