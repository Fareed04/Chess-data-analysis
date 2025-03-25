from http.client import responses
from turtledemo.clock import current_day

import requests
import json
from datetime import datetime, timedelta
import pandas as pd

# Replace this with your Chess.com username
USERNAME = "Fareed04"

def get_games():
    url = f"https://api.chess.com/pub/player/Fareed04/games/2023/03"
    headers = {
        "User-Agent": "MyPythonScript/1.0 (contact: ologundudufareed@gmail.com)"
    }
    response = requests.get(url, headers=headers)
    print(response.status_code)
    data = response.json()
    print(data)

def get_monthly_games(year, month):
    url = f"https://api.chess.com/pub/player/Fareed04/games/{year}/{month:02d}"
    headers = {
        "User-Agent": "MyPythonScript/1.0 (contact: ologundudufareed@gmail.com)"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json().get("games", [])
        return data
    else:
        print(f"Failed to fetch games for {year}/{month:02d} (Status Code: {response.status_code})")
        return []

print(get_monthly_games(2024, 3))

def get_all_games():
    all_games = []
    start_date = datetime(2023,3,1)
    current_date = start_date
    today = datetime.today()

    while current_date <= today:
        year = current_date.year
        month = current_date.month
        print(f"Fetching games for {year}-{month:02d}...")

        monthly_game_data = get_monthly_games(year, month)

        for game in monthly_game_data:
            game_date = datetime.fromtimestamp(game["end_time"])  # Convert UNIX timestamp
            if game_date >= start_date:  # Ignore games before March 3, 2023
                all_games.append(game)

        # Move to next month
        current_date += timedelta(days=32)
        current_date = current_date.replace(day=1)

    return all_games

games_data = get_all_games()

# Convert games list to DataFrame
df = pd.json_normalize(games_data)  # Flatten nested JSON fields

# Save to CSV
df.to_csv("data/chess_games_raw.csv", index=False)