# ♟️ Chess.com Performance Analysis

## 1️⃣ Project Objective

This project analyzes over **3,000 rated games** played on Chess.com using data retrieved via the Chess.com API.

The objective is to examine rating progression, performance trends, and opening effectiveness to uncover measurable patterns in gameplay behavior.

Rather than reviewing individual games, this analysis focuses on identifying systematic strengths, weaknesses, and performance drivers across formats.

---

## 2️⃣ Dataset & Data Source

- Source: Chess.com public API  
- Scope: Personal rated game history  
- Formats analyzed: Rapid, Blitz, and other available time controls  
- Total games analyzed: 3,000+

Each game record includes:
- Time control
- Opening classification
- Game result
- Rating at time of game
- Color played (White / Black)

---

## 3️⃣ Analytical Focus Areas

The analysis explores the following performance dimensions:

### Rating Progression
- Rating trends over time
- Format-specific rating behavior
- Volatility and improvement phases

### Win/Loss Trends
- Overall win rate
- Performance consistency across formats
- Outcome distribution

### Opening Effectiveness
- Most frequently played openings
- Win rate by opening (segmented by color)
- Underperforming vs overperforming lines

### Game Duration & Format Analysis
- Performance differences across time controls
- Strategic implications of rapid vs blitz play

---

## 4️⃣ Visualizations

The project includes multiple visual analyses:

- Line charts for rating progression  
- Bar charts for win rate by opening  
- Pie charts for opening frequency distribution  
- Heatmaps for outcome distribution across formats  

Example visualization:

![Rapid_win_rate_vs_opening_as_white](https://github.com/user-attachments/assets/f0a3729a-d884-47bf-8760-f525d2ff91f5)

---

## 5️⃣ Sample Insights

**High-Performing Opening (Rapid, White):**  
Englund Gambit 2.dxe5 Nc6 3.Nf3 Qe7 — approximately 75% win rate.

**Underperforming Line:**  
Zukertort Chigorin Variation shows significantly lower success rates relative to other openings.

These findings suggest measurable opening-specific performance differences that can inform strategic preparation.

---

## 6️⃣ Tools & Technologies

- Python  
- pandas  
- numpy  
- matplotlib  
- seaborn  
- Chess.com API  

---

## 7️⃣ Project Structure

```

Chess-data-analysis/
│
├── experiments.ipynb      # Data extraction and full analysis workflow
├── requirements.txt       # Dependencies
├── README.md              # Project documentation

````

---

## 8️⃣ How to Run Locally

```bash
git clone https://github.com/Fareed04/Chess-data-analysis.git
cd Chess-data-analysis
pip install -r requirements.txt
jupyter notebook experiments.ipynb
````

---

## 9️⃣ Key Takeaways

* Performance varies significantly by opening choice.
* Time control impacts win rate consistency.
* Long-term rating progression reveals identifiable growth phases.
* Data-driven self-analysis can replace anecdotal performance assumptions.

---

## 👤 Author

Fareed Ologundudu
Data Analyst | Python Developer

LinkedIn: [https://www.linkedin.com/in/fareed-ologundudu-129506249/](https://www.linkedin.com/in/fareed-ologundudu-129506249/)
GitHub: [https://github.com/Fareed04](https://github.com/Fareed04)

---

This project is intended for portfolio and analytical demonstration purposes.
