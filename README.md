# Financial Sentiment Stock Analyzer

A Python script that analyzes sentiment from financial news headlines in historical datasets and correlates it with stock price movements for Nifty 50 stocks. It enables hypothesis testing and model training to check for alpha generation via sentiment-based predictions.

## Features
- Sentiment analysis on historical Indian financial news using NLTK's VADER.
- Correlation between sentiment scores and next-day stock returns.
- Data processing and merging of Kaggle datasets for news and Nifty 50 prices.
- Model training (e.g., XGBoost) for return predictions and backtesting.
- Visualizations and reports.

## Installation
1. Clone the repo:
   ```
   git clone https://github.com/sarbajitsaha/financial-sentiment-stock-analyzer.git
   cd financial-sentiment-stock-analyzer
   ```
2. Set up virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Data Setup
Uses Kaggle datasets for historical data. To download:
1. Set up Kaggle API: Download `kaggle.json` from [kaggle.com/account](https://www.kaggle.com/account) > API, place in `~/.kaggle/`, and `chmod 600 ~/.kaggle/kaggle.json`.
2. Run: `python scripts/download_datasets.py`
   - Fetches news (2003-2020) to `data/raw/news/` and stocks (2000-2021) to `data/raw/stocks/`.

## Project Structure
```
financial-sentiment-stock-analyzer/
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── config/
│   └── config.py
├── src/
│   ├── __init__.py
│   ├── news_scraper.py  # Adapted for dataset processing
│   ├── sentiment_analyzer.py
│   ├── stock_data.py
│   ├── correlation_engine.py
│   └── visualization.py
├── data/
│   ├── raw/  # Downloaded data
│   ├── processed/
│   └── .gitkeep
├── tests/
│   └── __init__.py
├── results/
│   └── .gitkeep
├── scripts/
│   └── download_datasets.py
└── main.py
```

## Dependencies
- Python 3.8+
- Full list in `requirements.txt`.

## License
MIT License
