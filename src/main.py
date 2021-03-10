from flask import Flask, request
from flask_cors import CORS, cross_origin
from waitress import serve

# Custom endpoints/classes
from gabs import get_all_gabs, get_one_gab

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/allgabs')
@cross_origin()
def get_all_gabs_endpoint():
  return get_all_gabs()

@app.route('/onegab')
@cross_origin()
def get_one_gab_endpoint():
  '''
  requires the body to be set in the get request
  {
    "gab_index": 0
  }
  '''
  return get_one_gab()


if __name__ == '__main__':
  serve(app, host='0.0.0.0', port=5000)