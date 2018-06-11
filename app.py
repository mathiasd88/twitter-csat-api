from flask import Flask, Response, json, request
from analyzer.analyzer import analyze

app = Flask(__name__)


@app.route('/', methods=('get',))
def analysis():
    country = request.args.get('country')

    if country is None:
        country = 'chile'

    analyzed_data = {
        'polarity': analyze(country)
    }

    return Response(
        response=json.dumps(analyzed_data),
        status=200,
        mimetype='application/json'
    )


if __name__ == '__main__':
    app.run(debug=True)
