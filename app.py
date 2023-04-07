import json

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/request-xray')
def index():
    body = json.dumps(request.data.decode())
    http_method = request.method
    request_headers = []
    for header in request.headers.items():
        print(header)
        request_headers.append(header[0] + ': ' + header[1])

    return jsonify({'body': body, 'http_method': http_method, 'request_headers': request_headers})


app.run(host='0.0.0.0', port=8099)
