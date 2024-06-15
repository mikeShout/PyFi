import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Define the tickers and period of time
tickers = ['KO', 'PEP']
end_date = pd.Timestamp.today()
start_date = end_date - pd.DateOffset(years=1)

# Download stock data
print("Getting data...")
data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']

# Calculate the percentage change from the start date
data = (data / data.iloc[0] - 1) * 100

# Create the percentage change line chart
fig = go.Figure()

# Add KO line with enhancements
fig.add_trace(go.Scatter(
    x=data.index, y=data['KO'], mode='lines', name='Coca-Cola (KO)',
    line=dict(color='red', width=2),
    hovertemplate='%{y:.2f}%'))

# Add PEP line with enhancements
fig.add_trace(go.Scatter(
    x=data.index, y=data['PEP'], mode='lines', name='PepsiCo (PEP)',
    line=dict(color='blue', width=2),
    hovertemplate='%{y:.2f}%'))

# Highlight significant period
fig.add_trace(go.Scatter(
    x=[data.index[0], data.index[0], data.index[-1], data.index[-1]],
    y=[-10, 20, 20, -10],
#    fill='toself', fillcolor='lightgrey',
    line=dict(color='lightgrey', width=0),
    showlegend=False, hoverinfo='none'))

# Find the peak value and corresponding date for KO
ko_max_y = data['KO'].max()
ko_max_x = data['KO'].idxmax()

# Find the peak value and corresponding date for PEP
pep_max_y = data['PEP'].max()
pep_max_x = data['PEP'].idxmax()

# Add annotations
fig.add_annotation(
    x=ko_max_x, y=ko_max_y,
    text="KO peak",
    showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor='red')

fig.add_annotation(
    x=pep_max_x, y=pep_max_y,
    text="PEP peak",
    showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2, arrowcolor='blue')

# Add titles and labels with enhancements
fig.update_layout(
    title='Percentage Change in Stock Prices of Coca-Cola (KO) and PepsiCo (PEP) Over the Last Year',
    xaxis_title='Date',
    yaxis_title='Percentage Change',
    xaxis_rangeslider_visible=True,
    legend_title='Stock',
    template='plotly_white',
    hovermode='x unified'
)

# Add a range selector for easier navigation
fig.update_xaxes(
    rangeselector=dict(
        buttons=list([
            dict(count=1, label='1m', step='month', stepmode='backward'),
            dict(count=3, label='3m', step='month', stepmode='backward'),
            dict(count=6, label='6m', step='month', stepmode='backward'),
            dict(step='all')
        ])
    )
)

# Display the chart
print("Displaying chart")
fig.show()
