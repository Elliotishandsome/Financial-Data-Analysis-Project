# Financial Data Analysis Project

This project aims to build an automated financial data analysis and monitoring system using Python, helping analysts quickly identify trends and perform initial screenings on Hong Kong technology stocks.

## Key Features
- **Automated Data Acquisition**: Real-time fetching of historical market data via the yfinance API.
- **Technical Indicator Calculation**: Built-in logic for calculating the 50-Day Moving Average (MA50).
- **Automated Decision System**: Automatically classifies stock trends into "Bullish" (Strong) or "Bearish" (Weak).
- **Batch Processing**: Supports concurrent analysis of multiple stocks to improve workflow efficiency.

## Tech Stack
- **Language**: Python 3.x
- **Data Manipulation**: Pandas, NumPy
- **Visualization**: Matplotlib
- **Data Source**: yfinance

## Usage
1. Install necessary dependencies:
   ```bash
   pip install yfinance pandas matplotlib
Support batch processing for sector-wide performance tracking


# 📈 HK-Stock-Quant-Bot (Dual-Factor Quantitative Analysis Bot)

This is an automated Hong Kong stock analysis tool developed in Python. By fetching historical data from Yahoo Finance and combining the **Moving Average (MA50)** with the **Relative Strength Index (RSI14)**, it automatically generates structured, commercially valuable quantitative reports. This helps filter out market sentiment noise and identify potential trading opportunities.

## ✨ Core Features

* **Automated Data Fetching**: Batch downloads one year of historical stock prices for specified HK stocks with a single click.
* **Robust Defensive Mechanism**: Built-in error and exception handling (`try-except`) automatically skips suspended stocks or missing data, ensuring the pipeline runs smoothly without crashing.
* **Dual-Factor Strategy Calculation**:
  * **MA50 (Macro Trend)**: Determines whether the current stock price is in a bullish (`Strong`) or bearish (`Weak`) state.
  * **RSI14 (Short-Term Momentum)**: Utilizes Exponential Moving Average (EMA) weighting to accurately capture potential reversal points such as overbought (>70) and oversold (<30) conditions.
* **One-Click Business Report Generation**: Automatically exports the calculation results into a clean `.csv` file, facilitating subsequent sorting, filtering, and strategy analysis in Excel.

## 📊 Output Example

After execution, the program will automatically generate `daily_stock_report.csv`. Here is an example of the output:

| Ticker  | MA50_Status | RSI_14 | Current_Price |
|---------|-------------|--------|---------------|
| 3800.HK | Strong      | 25.43  | 15.50         |
| 0700.HK | Weak        | 82.10  | 350.20        |
| 1810.HK | Strong      | 55.30  | 18.20         |

*(Note: `Strong` + RSI < 30 is generally considered a potential "buy-the-dip" signal in a bullish trend; `Weak` + RSI > 70 is typically seen as a potential "dead-cat bounce" sell signal in a bearish trend.)*

## 🚀 Roadmap

* [ ] **Day 2**: Expand advanced features (Automated Telegram/Line Notifications / Historical Backtesting / Interactive Web Dashboard in development...)
