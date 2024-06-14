import yfinance as yf
import pandas as pd
import plotly.graph_objects as go



# Determine the ticker and period of time
ticker = 'BCOV'
end_date = pd.Timestamp.today()
start_date = end_date - pd.DateOffset(months=2)

# Get stock data from yahoo finance
print("Getting data...")
data = yf.download(ticker, start=start_date, end=end_date)

# Calculate the 10-day moving average
data['10_day_MA'] = data['Close'].rolling(window=10).mean()

# Create a Plotly candlestick chart
fig = go.Figure(data=[go.Candlestick(x=data.index,
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['Close'])])

# Add the 10-day moving average line
fig.add_trace(go.Scatter(x=data.index, y=data['10_day_MA'], 
                         mode='lines', 
                         name='10 Day MA',
                         line=dict(color='blue')))

# Add titles and labels
fig.update_layout(
    title='BCOV Candlestick Chart (Last 2 Months)',
    xaxis_title='Date',
    yaxis_title='Price',
    xaxis_rangeslider_visible=False
)

# Display chart
print("Displaying chart")
fig.show()

