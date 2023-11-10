# Pixie: Python Voice Assistant 🎙️

Pixie Voice Assistant is a Python-based voice assistant that allows you to interact with your computer using voice commands. You can ask for the time, search the web, get information from Wikipedia, open websites, and more.

## Table of Contents
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Features](#features)
- [Usage](#usage)
- [Commands](#commands)
- [License](#license)

## Getting Started 🚀

To get started with Pixel Voice Assistant, follow the installation steps below:

### Prerequisites

- Python 3.x
- An active internet connection
- A microphone (for voice input)

### Installation

1. Clone or download this repository.

2. Install the required Python libraries using pip:

   ```bash
   pip install pyttsx3 speech_recognition wikipedia-api
   ```

3. Specify the path to your Microsoft Edge executable (msedge.exe) in the `msedge_path` variable inside the code.

4. Run the `Pixie.py` script:

   ```bash
   python Pixie.py
   ```

## Dependencies 📦

- [pyttsx3](https://pypi.org/project/pyttsx3/): A text-to-speech conversion library.
- [speech_recognition](https://pypi.org/project/SpeechRecognition/): Recognizes speech and converts it to text.
- [wikipedia-api](https://pypi.org/project/Wikipedia-API/): Allows access to Wikipedia articles.

## Features 🌟

- Time and date information ⏰📅
- Web search using Google 🔍
- Wikipedia search and summary retrieval 📚
- Opening websites (e.g., YouTube, Google, Gmail, WhatsApp) 🌐
- Customized voice greetings 👋
- Text-to-speech response for user interactions 🗣️

## Usage 💡

1. When you run the `Pixie.py` script, Pixel Voice Assistant will greet you and wait for your voice commands.

2. You can issue commands or questions, and Pixel Voice Assistant will respond accordingly.

3. To exit the assistant, simply say "exit" or "bye," and it will bid you farewell.

## Commands 🗣️

Pixel Voice Assistant supports a variety of voice commands, including but not limited to:

- Asking for the time and date ⏰📅
- Searching Google 🔍
- Looking up information on Wikipedia 📚
- Opening specific websites (e.g., YouTube, Google, Gmail) 🌐
- Playing music 🎵

Feel free to extend the list of supported commands to suit your needs.

## Contributing 🤝

Thank you for considering contributing to Pixie Voice Assistant! Your contributions are valuable and help improve the project. Please take a moment to review the [contribution guidelines](CONTRIBUTING.md) before getting started.

## License 📜

This project is licensed under the `MIT License` - see the [LICENSE](LICENSE) file for details.

