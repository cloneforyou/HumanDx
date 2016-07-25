from flask import Flask, Response
import json
from corpus import Corpus

corpus = Corpus()
app = Flask(__name__)

@app.route('/<search_keyword>')
def getResults(search_keyword):
	results = corpus.query(search_keyword)
	return Response(json.dumps(results),  mimetype='application/json')