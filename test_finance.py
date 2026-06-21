import yfinance as yf

# 獲取騰訊 (1810.HK) 的數據
ticker = yf.Ticker("1810.HK")
hist = ticker.history(period="1y")

# 打印數據的前 5 行
print(hist.head())

# 1. 查看數據的基本資訊（確認數據類型和缺失值）
print(hist.info())

# 2. 計算每日的收盤價變動百分比 (Daily Return)
hist['Daily_Return'] = hist['Close'].pct_change()

# 3. 打印出最新的 5 行數據，看看有沒有多出 'Daily_Return' 這一列
print(hist.tail())

# 直接查看第一行數據 (iloc[0] 代表第 0 個位置)
print(hist.iloc[0])

# 找出所有 Daily_Return 為 NaN 的行
print(hist[hist['Daily_Return'].isna()])

# 1. 刪除 NaN 行，確保計算準確
hist.dropna(inplace=True)

# 2. 計算平均日收益率與波動率（標準差）
mean_return = hist['Daily_Return'].mean()
volatility = hist['Daily_Return'].std()

print(f"平均日收益率: {mean_return:.6f}")
print(f"波動率 (標準差): {volatility:.6f}")

import matplotlib.pyplot as plt

# 1. 計算 50 天移動平均線 (Rolling Mean)
hist['MA50'] = hist['Close'].rolling(window=50).mean()

# 2. 繪圖
plt.figure(figsize=(10, 6))
plt.plot(hist.index, hist['Close'], label='Close Price', alpha=0.5)
plt.plot(hist.index, hist['MA50'], label='50-Day MA', color='red')
plt.title('Tencent (0700.HK) Stock Price & 50-Day MA')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# 1. 確保 MA50 已經算好 (你原本的代碼中已經有)
# 2. 獲取最新的收盤價和最新的 MA50 值
# .iloc[-1] 的意思是獲取數據框中的最後一行（即最新的一天）
last_price = hist['Close'].iloc[-1]
last_ma50 = hist['MA50'].iloc[-1]

# 3. 自動判斷邏輯
print(f"最新價格: {last_price:.2f}")
print(f"50日移動平均線: {last_ma50:.2f}")

if last_price > last_ma50:
    print("狀態：強勢 (價格高於 MA50)")
else:
    print("狀態：弱勢 (價格低於 MA50)")







# 1. Build a list including more than one stocks in HK
stocks = ['3800.HK', '1810.HK', '9988.HK', '0700.HK', '1347.HK', '0285.HK', '0981.HK'] 
results_list = []

# 2. Using for loop to scan all stocks in the list.
for ticker_symbol in stocks:
    print(f"\n--- start handling: {ticker_symbol} ---")
    
    try:
        # 3 & 4. 單次下載過去 1 年的數據
        data = yf.download(ticker_symbol, period="1y")

        if data.empty:
            print(f"[{ticker_symbol}] no data being taken，because of trading suspension。")
            continue
        close_series = data['Close'].squeeze()
        print(f"[{ticker_symbol}] 數據抓取成功，長度為: {len(data)}")
        
        # 5. 計算 MA50 (注意這裡用 data)
        ma50 = close_series.rolling(window=50).mean().iloc[-1]
        current_price = close_series.iloc[-1]
        # === 這裡開始是新增的 RSI14 計算模組 ===
        
        # A. 算出每天的「漲跌價差」 (今天收盤價 - 昨天收盤價)
        delta = close_series.diff()
        
        # B. 把上漲和下跌分開
        # 如果大於 0 就保留，小於 0 就變 0
        gain = delta.where(delta > 0, 0)
        # 如果小於 0 就保留並取絕對值 (轉正數)，大於 0 就變 0
        loss = -delta.where(delta < 0, 0)
        
        # C. 計算 14 天的平均上漲與平均下跌 (業界常用指數移動平均 EMA)
        avg_gain = gain.ewm(span=14, adjust=False).mean()
        avg_loss = loss.ewm(span=14, adjust=False).mean()
        
        # D. 計算 RS (相對強度)
        # 為了避免除以 0 的錯誤，我們在分母加一個極小的值 1e-10
        rs = avg_gain / (avg_loss + 1e-10)
        
        # E. 計算最終的 RSI 數值，並只取最新一天的結果 (.iloc[-1])
        rsi_14 = 100 - (100 / (1 + rs)).iloc[-1]
        
        # === RSI 計算結束 ===
    
        
        # 7. 比較邏輯
        status = "Strong" if current_price > ma50 else "Weak"
        
        # 8. 輸出雙指標結果
        print(f"{ticker_symbol} 目前狀態: {status} | RSI: {rsi_14:.2f}")
        
        stock_result = {
            "Ticker": ticker_symbol,
            "MA50_Status": status,
            "RSI_14": round(rsi_14, 2),  # round 是用來四捨五入到小數點後兩位
            "Current_Price": round(current_price, 2)
        }
        except Exception as e:
        print(f"處理 {ticker_symbol} 時發生嚴重錯誤，原因: {e}")
        continue
print("\nAll stock have been done！")
final_report = pd.DataFrame(results_list)
final_report.to_csv("daily_stock_report.csv", index=True)
print("Report have been done：daily_stock_report.csv")
