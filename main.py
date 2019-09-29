import requests, json
from flask import Flask


def get_valutes_list():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = json.loads(response.text)
    valutes = list(data['Valute'].values())
    return valutes


app = Flask(__name__)


def create_html(valutes):
    header = '<h1>Курс валют</h1>\n'
    rows = '\n'.join(
        [f'''<tr>{
                "".join( [f"<td>{value}</td>" for value in valute.values()] )
            }</tr>''' for valute in valutes]
    )
    table = f'<table>\n{rows}\n</table>'

    return header + table


@app.route("/")
def index():
    valutes = get_valutes_list()
    html = create_html(valutes)
    return html


if __name__ == "__main__":
    app.run()