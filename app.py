import dash
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)
server = app.server

num_click = 0

app.layout = html.Div([
    html.Button('Click', id = 'click'),
    html.Div('0', id = 'content'),
    html.Div('3rd Version')
        ])

@app.callback(
    Output('content', 'children'),
    Input('click', 'n_clicks'))
def display_hover_data(c):
    if c:
        global num_click
        num_click += 1
        return num_click
    else:
        return 0

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
