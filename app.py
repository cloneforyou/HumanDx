from flask import Flask, Response
import json
from humandx.corpus import Corpus

app = Flask(__name__)
corpus = Corpus()

@app.route('/<search_keyword>')
def getResults(search_keyword):
	results = corpus.query(search_keyword)
	return Response(json.dumps(results),  mimetype='application/json')