A command-line Morse Code Encoder that converts English text into Morse code and plays the corresponding sounds using audio files (dot.mp3 and dash.mp3).

🚀 Features
Encodes English text (A–Z, 0–9) into Morse code

Plays .mp3 sounds for dots (.) and dashes (-) in real time

Lightweight and terminal-friendly (no GUI)

Simple and effective for learning or simulating Morse code

📁 Project Structure
morse-code-encoder/
├── project.py           # Main Python script
├── dot.mp3              # Audio file representing a Morse dot (.)
├── dash.mp3             # Audio file representing a Morse dash (-)
└── README.md            # Project documentation
🧠 How It Works
User enters an English message via terminal input

The script translates each character to Morse code

Morse code is printed on the screen

The program plays dot.mp3 for every dot (.) and dash.mp3 for every dash (-) with slight pauses to simulate timing

🛠️ How to Use
🔧 Requirements
Python 3.x

playsound module

📦 Installation
bash
Copy
Edit
pip install playsound
▶️ Running the Program
bash
Copy
Edit
python project.py
🧾 Example
Input:

yaml
Copy
Edit
Enter your message: HELLO WORLD
Output:

less
Copy
Edit
Morse Code: .... . .-.. .-.. --- / .-- --- .-. .-.. -..
Playing Morse code...
You will hear the sequence of dot.mp3 and dash.mp3 as the Morse code is played.

📝 Supported Characters
Alphabets: A–Z (case-insensitive)

Digits: 0–9

Space: Converted to / in Morse code (word separator)

🎵 Sound Playback Notes
Ensure dot.mp3 and dash.mp3 are in the same directory as project.py

Uses playsound to play sounds with brief pauses between signals
