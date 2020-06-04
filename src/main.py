from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
import collections

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

winery_foundation_year = 1920
current_year = datetime.datetime.now().year
winery_age = current_year - winery_foundation_year

excel_data = pandas.read_excel('data/wine.xlsx', na_values=None, keep_default_na=False)
wines = excel_data.to_dict('records')
grouped_wines = collections.defaultdict(list)

for wine in wines:
    grouped_wines[wine['Категория']].append(wine)

rendered_page = template.render(
    winery_age=winery_age,
    wines=grouped_wines
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
