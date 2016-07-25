def sortQueryResults(results):
	# first sort alphabetically
	results = sorted(results, key=lambda x: x['diagnose'])
	# second sort based to matching scores
	results = sorted(results, key=lambda x: x['score'], reverse=True)
	return results

def scoreQueryResult(query, diagnose):
	# if score is 0 the diagnose is completely irrelevant
	# if score is 1 the diagnose is equal to the query
	score = 0
	# NB: if full query match does not happen in diagnose the score is 0
	if query in diagnose:
		# score shows the size of diagnose string which query string occupies
		score = round(float(len(query))/len(diagnose),3)
	return score