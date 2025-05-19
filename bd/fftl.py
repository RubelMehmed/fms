import plotly.graph_objects as go

labels = ['Agriculture', 'Infrastructure', 'Housing', 'Health',
          'Educational Infrastructure', 'Industries']
sizes = [35.85, 32.37, 16.69, 14.30, 0.62, 0.26]

fig = go.Figure(data=[go.Pie(
    labels=labels,
    values=sizes,
    hole=0.3,
    textinfo='percent+label',
    pull=[0.05 if v > 1 else 0.1 for v in sizes],
    marker=dict(
        colors=['#2ca02c', '#ff7f0e', '#9467bd', '#d62728', '#17becf', '#8c564b'],
        line=dict(color='black', width=1)
    )
)])

fig.update_layout(
    title_text='Sector-Wise Flood Losses (2024)<br><sub>Total Losses: TK14,421CR</sub>',
    title_font=dict(size=20, color='black'),
    showlegend=False
)

fig.show()
