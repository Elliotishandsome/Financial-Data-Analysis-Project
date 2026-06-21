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


# 📈 HK-Stock-Quant-Bot (港股雙因子量化分析機器人)

這是一個基於 Python 開發的自動化港股分析工具。透過抓取 Yahoo Finance 的歷史數據，結合 **移動平均線 (MA50)** 與 **相對強弱指數 (RSI14)**，自動產出具備商業價值的結構化量化報表，協助排除市場情緒雜訊，尋找潛在的交易機會。

## ✨ 核心功能 (Features)

* **自動化數據獲取**：一鍵批量下載指定港股過去一年的歷史股價。
* **穩健防禦機制**：內建防呆與例外處理 (`try-except`)，遇停牌或數據缺失會自動跳過，確保程式穩定運行不崩潰。
* **雙因子策略運算**：
  * **MA50 (大趨勢)**：判斷目前股價處於多頭 (Strong) 還是空頭 (Weak) 狀態。
  * **RSI14 (短線情緒)**：運用 EMA 指數移動平均權重，精準捕捉超買 (>70) 與超賣 (<30) 的潛在轉折點。
* **一鍵生成商業報表**：自動將運算結果匯出為乾淨的 `.csv` 檔案，方便後續在 Excel 進行排序與策略分析。

## 📊 輸出範例 (Output Example)

程式執行後會自動生成 `daily_stock_report.csv`，內容範例如下：

| Ticker  | MA50_Status | RSI_14 | Current_Price |
|---------|-------------|--------|---------------|
| 3800.HK | Strong      | 25.43  | 15.50         |
| 0700.HK | Weak        | 82.10  | 350.20        |
| 1810.HK | Strong      | 55.30  | 18.20         |

*(註：Strong + RSI < 30 通常視為多頭回檔潛在買點；Weak + RSI > 70 通常視為空頭死貓反彈潛在賣點。)*

## 🚀 未來升級計畫 (Roadmap)

* [ ] **Day 2**: 擴充進階功能 (自動化推播 / 歷史回測 / 視覺化儀表板 開發中...)
