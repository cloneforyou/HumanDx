from humandx.corpus import Corpus

# initialize the corpus of diagnoses
corpus = Corpus()
# set the searching query
DIAGNOSE_QUERY = "he"

# check the corpus of diagnoses for matches with the query
results = corpus.query(DIAGNOSE_QUERY)
# for every result print the diagnose title and the relevance score
print("===============\nWe found %s results for the query '%s'" %(len(results),DIAGNOSE_QUERY))
for result in results:
	print("%s (%s)" %(result['diagnose'],result['score']))