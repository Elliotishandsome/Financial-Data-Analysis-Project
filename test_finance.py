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







# 1. 建立一個包含多個股票代碼的「列表 (List)」
stocks = ['1810.HK', '0700.HK', '9988.HK', '3690.HK'] 

# 2. 開始「迴圈 (For Loop)」，這就像是用一個掃描器，依次讀取列表裡的每一隻股票
for ticker_symbol in stocks:
    
    # 3. 根據當前的代碼 (ticker_symbol) 建立對應的數據對象
    ticker = yf.Ticker(ticker_symbol)
    
    # 4. 拉取數據，這裡我們改為近 6 個月的數據
    df = ticker.history(period="6mo") 
    
    # 5. 計算 50 天移動平均線 (MA50)
    # df['Close'] 是收盤價，.rolling(50).mean() 是取過去50天的平均值
    # .iloc[-1] 是選取最後一行的數據，代表「最新的一天」的 MA50
    ma50 = df['Close'].rolling(window=50).mean().iloc[-1]
    
    # 6. 獲取最新一天的收盤價
    current_price = df['Close'].iloc[-1]
    
    # 7. 比較邏輯：如果最新價格大於 MA50，狀態就是強勢，否則為弱勢
    status = "強勢" if current_price > ma50 else "弱勢"
    
    # 8. 輸出結果，f-string (f"...") 可以讓你把變數直接塞進文字裡
    print(f"{ticker_symbol} 目前狀態: {status}")
