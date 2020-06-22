from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_url_path='')
CORS(app)  # preventing cors errors


@app.route("/")
def hello():
    return jsonify('Cannot GET /')


# for json data
@app.route("/json")
def json_data():
    # some test data
    data = [
        {
            'fullname': 'Olivier Nshimiye',
            'username': 'onshimiye',
            'email': 'onshimiye17@gmail.com',
            'points': '5',
        },
        {
            'fullname': 'Mark Essien',
            'username': 'mark',
            'email': 'markessien@hotels.ng',
            'points': '10',
        }
    ]
    return jsonify(data)


# for csv data
@app.route("/csv")
def csv_file():
    return send_from_directory('.', 'data.csv')


if __name__ == '__main__':
    app.run()
