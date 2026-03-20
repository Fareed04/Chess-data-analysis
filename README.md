# ♟️ Chess.com Performance Analysis

## Phase 1: Ask

### Business Task Statement

**Client:** Fareed (Chess.com player) — acting as both analyst and client.

**Business Task:**
Analyze personal Chess.com game data from March 2024 to present across 
Bullet, Blitz, and Rapid time controls to identify performance patterns, 
strengths, and weaknesses — with a focus on opening repertoire 
effectiveness — in order to generate actionable recommendations for 
targeted improvement toward rating goals of 2000 (Rapid), 1500 (Blitz), 
and 1500 (Bullet).

---

### Key Factors Being Investigated
- Win/loss/draw rates by time control, color (White/Black), and opening
- Accuracy trends over time and across openings
- Rating progression toward target ratings
- Openings where performance is strongest and weakest (both as White and Black)

---

### Metrics
- Win rate %, Loss rate %, Draw rate %
- Average accuracy per opening / time control
- Rating delta over time (progression curve)
- Performance split by color (White vs Black)

---

### Guiding Questions
1. What type of company does your client represent, and what are they asking you to accomplish?
2. What are the key factors involved in the business task you are investigating?
3. What type of data will be appropriate for your analysis?
4. Where will you obtain that data?
5. Who is your audience, and what materials will help you present to them effectively?

---

### Stakeholders
- **Primary:** Fareed (player and analyst)
- **Secondary:** Portfolio reviewers

---

### Deliverable
A clear statement of the business task has been defined above. The analysis 
will be fully reproducible — any Chess.com user can substitute their own 
username to replicate the full analysis pipeline.

## Phase 2: Prepare

### Data Source
- **Platform:** Chess.com
- **Access Method:** Chess.com Public API via Python `requests` library
- **Data Format:** CSV (saved locally after API import)
- **Dataset:** `chess_games_raw.csv`
- **Time Period:** March 2023 – March 2026
- **Total Records:** 3,257 games

---

### Dataset Structure
| Column | Description |
|---|---|
| `url` | Link to the game on Chess.com |
| `pgn` | Full game notation including opening, moves, and metadata |
| `time_control` | Time control in seconds |
| `time_class` | Time control category (bullet, blitz, rapid, daily) |
| `end_time` | Unix timestamp of when the game ended |
| `rated` | Whether the game was rated |
| `eco` | URL containing the ECO opening code and name |
| `accuracies.white` | Accuracy score for White (where available) |
| `accuracies.black` | Accuracy score for Black (where available) |
| `white.username` | Username of the player with the White pieces |
| `white.rating` | Rating of the White player at the time of the game |
| `white.result` | Result for the White player |
| `black.username` | Username of the player with the Black pieces |
| `black.rating` | Rating of the Black player at the time of the game |
| `black.result` | Result for the Black player |
| `uuid` | Unique game identifier |
| `fen` | Final board position in FEN notation |
| `tournament` | Tournament ID (mostly null — not applicable) |
| `start_time` | Unix timestamp of game start (mostly null) |

---

### Game Breakdown by Time Control
| Time Class | Games |
|---|---|
| Blitz | 1,722 |
| Rapid | 1,430 |
| Bullet | 102 |
| Daily | 3 |
| **Total** | **3,257** |

---

### ROCCC Assessment
| Criteria | Assessment |
|---|---|
| **Reliable** | Data pulled directly from Chess.com's official public API — no third-party intermediaries |
| **Original** | First-party data sourced directly from the platform |
| **Comprehensive** | Covers all game types across the full account history |
| **Current** | Data reflects games up to March 2026 |
| **Cited** | Source: [Chess.com Public API](https://www.chess.com/news/view/published-data-api) |

---

### Known Limitations
- **Accuracy data is sparse:** `accuracies.white` and `accuracies.black` are null
  for approximately 80% of games (2,604 out of 3,257). Chess.com only provides
  accuracy for games that have been reviewed. Accuracy-based analysis will be
  limited to the available subset.
- **Daily games excluded:** 3 daily (correspondence) games are present in the
  dataset but will be filtered out as they fall outside the scope of this analysis.
- **Opening names not directly stored:** ECO opening names are embedded within
  URL strings and will need to be extracted during the Process phase.
- **Player color not directly stored:** Whether the analyst played as White or
  Black must be derived by matching the username against `white.username`
  and `black.username`.

---

### Licensing & Privacy
- Data was accessed via Chess.com's publicly available API in accordance with
  their [Terms of Service](https://www.chess.com/legal/user-agreement).
- The dataset contains only publicly visible game data. No private or sensitive
  user information is included.
- This project is intended for personal portfolio use and educational purposes only.

---

### Deliverable
A description of all data sources used has been documented above. The raw dataset
(`chess_games_raw.csv`) has been saved locally and will be preserved alongside the
cleaned version to maintain a full audit trail of the data pipeline.