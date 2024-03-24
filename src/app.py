import dash
from dash import Dash, html, dcc, callback, Input, Output

app = Dash(__name__,pages_folder="pages",use_pages=True)


app.layout = html.Div(children=[
    # html.Div(children=[
	#     dcc.Link(page['name'], href=page["relative_path"], className="btn btn-dark m-2 fs-5")\
	# 		  for page in dash.page_registry.values()]
	# ),
	dash.page_container
])

if __name__ == '__main__':
    app.run_server(debug=True)
