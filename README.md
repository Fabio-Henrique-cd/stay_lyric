🎵 Terminal Music Lyrics Player

This project plays a song and displays its lyrics in the terminal with a typing effect, synchronized with the music.

📌 Features
Plays an .mp3 file using pygame
Displays lyrics with a typing animation
Custom speed per line
Custom delay between lines
Colored terminal output using colorama
Cursor hidden for a cleaner visual experience

📂 Requirements
Install the dependencies:
    pip install pygame colorama

▶️ How to use
1. Place your music file in the same folder as the script
2. Rename it to:
    music.mp3
3. Run the script
    python main.py

⚙️ How it work
🎧 Music playback
    Uses pygame.mixer to load and play th music
    Starts playback from a specific timestamp:
        pygamer.mixer.music.play(start=84.6)

🎨 Visual Effects
Text is printed letter by letter
Cyan color with brigthness using colorama
Cursor is hidden using ANSI escape:
    print("\033[?25l", end="")