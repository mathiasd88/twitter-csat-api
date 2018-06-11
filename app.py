from flask import Flask, Response, json, request
from analyzer.analyzer import analyze

app = Flask(__name__)


@app.route('/', methods=('get',))
def analysis():
    country = request.args.get('country')
    text = request.args.get('text')

    if country is None:
        country = 'chile'

    return Response(
        response=json.dumps(analyze(country, text)),
        status=200,
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run(debug=True)
