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
