# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)


@app.route('/query-example')
def query_example():
    return 'Query String Example!'


@app.route('/form-example')
def form_example():
    return 'Form Data Example!'


@app.route('/json-example')
def json_example():
    return 'JSON Object Example!'


if __name__ == '__main__':
    # run app in debug mode!
    app.run(debug=True)
