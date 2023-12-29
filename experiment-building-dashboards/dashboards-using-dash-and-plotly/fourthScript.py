import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
ecom_sales = pd.read_csv('/usr/local/share/datasets/ecom_sales.csv')
ecom_line = ecom_sales.groupby('Year-Month')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
line_fig = px.line(data_frame=ecom_line, x='Year-Month', y='Total Sales ($)', title='Total Sales by Month')
ecom_bar = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
max_country = ecom_bar.sort_values(by='Total Sales ($)', ascending=False).loc[0]['Country']
bar_fig = px.bar(data_frame=ecom_bar, x='Total Sales ($)', y='Country', orientation='h', title='Total Sales by Country')

app = dash.Dash(__name__)

# Create the dash layout and overall div
app.layout = html.Div(children=[
    html.H1('Sales Figures'), 
    # Add a div containing the line figure
    html.Div(dcc.Graph(id='my-line-fig', figure=line_fig)), 
    # Add a div containing the bar figure
    html.Div(dcc.Graph(id='my-bar-fig', figure=bar_fig)), 
    # Add the H3
    html.H3(f'The largest country by sales was {max_country}')
    ])

if __name__ == '__main__':
    app.run_server(debug=True)