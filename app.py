from flask import Flask
from corpus import Corpus
corpus = Corpus()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'try to add /heada in your browser'

@app.route('/<search_keyword>')
def getResults(search_keyword):
	results = corpus.query(search_keyword)
    return Response(json.dumps(results),  mimetype='application/json')