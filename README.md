# Guess Game

A simple number-guessing game built with Django. Try to find the randomly selected number from **1 to 20** in **five attempts**. The game tells you whether each guess is too high or too low, and starts a new round after a win or game over.

## Live demo

[Play Guess Game](https://guessgame-p5iy.onrender.com/game/)

## How to play

1. Open the game in your browser.
2. Enter a number between 1 and 20 and submit your guess.
3. Use the “Too High” or “Too Low” hint to guide your next guess.
4. Guess correctly within five tries to win!

## Run locally

You’ll need Python installed.

1. Clone the repository and move into the project directory:

   ```bash
   git clone https://github.com/psalm789/guessgame.git
   cd guessgame
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
   ```

3. Install dependencies and apply database migrations:

   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   ```

4. Start the development server:

   ```bash
   python manage.py runserver
   ```

5. Visit [http://127.0.0.1:8000/game/](http://127.0.0.1:8000/game/) in your browser.

## Built with

- Python
- Django
- SQLite

## License

See [LICENSE](LICENSE).
