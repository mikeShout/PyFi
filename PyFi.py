import yfinance as yf
import pandas as pd
import plotly.graph_objects as go



# Determine the ticker and period of time
ticker = 'BCOV'
end_date = pd.Timestamp.today()
start_date = end_date - pd.DateOffset(months=6)

# Get stock data from yahoo finance
print("Getting data...")
data = yf.download(ticker, start=start_date, end=end_date)

# Calculate the 10-day moving average
data['10_day_MA'] = data['Close'].rolling(window=10).mean()

# Calculate the daily percentage change
data['Daily % Change'] = data['Close'].pct_change() * 100
# Remove the first row with NaN values resulting from pct_change()
data = data.dropna()

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
print("Displaying candlestick chart")
fig.show()


fig_bar = go.Figure(data=[go.Bar(x=data.index, y=data['Daily % Change'], name='Daily % Change')])

# Add titles and labels to the bar chart
fig_bar.update_layout(
    title='Daily Percentage Change BCOV',
    xaxis_title='Date',
    yaxis_title='Daily % Change'
)

print("Displaying candlestick chart")
# Display the bar chart
fig_bar.show()

