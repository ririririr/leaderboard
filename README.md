# Finance Club Leaderboard

A beautiful leaderboard web app for your economics and finance club competition, built with Flask and Bootstrap. Add new players and their percentage earnings, and see the leaderboard update instantly. Rankings are stored persistently in a SQLite database.

## Features
- Add player name and % earnings
- Players ranked by highest % earnings
- Beautiful, modern UI (Bootstrap + custom styles)
- Persistent storage (SQLite)

## How to Run
1. Make sure you have Python 3.7+ installed.
2. Install dependencies (in your virtual environment):
   ```bash
   pip install flask flask_sqlalchemy
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Customization
- To reset the leaderboard, delete the `leaderboard.db` file and restart the app.
- You can further style the page by editing `templates/index.html`.

---
Made for the Finance Club Competition.
