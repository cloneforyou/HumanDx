# calculate how relevant the diagnose is to the query
def getRelevance(query, diagnose):
	# if relevance is 0 the diagnose is completely irrelevant
	# if relevance is 1 the diagnose is equal to the query
	relevance = 0
	# NB: if full query match does not happen in diagnose the relevance is 0
	if query in diagnose:
		# relevance shows the size of diagnose string which query string occupies
		relevance = round(float(len(query))/len(diagnose),3)
	return relevance

# sort the query results based on the relevance and alphabetically (for diagnoses with the same relevance)
def sortResults(results):
	# first sort alphabetically
	results = sorted(results, key=lambda x: x['diagnose'])
	# second sort based on relevance scores
	results = sorted(results, key=lambda x: x['relevance'], reverse=True)
	return results

