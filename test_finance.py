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






