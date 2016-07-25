def sortQueryResults(results):
	# first sort alphabetically
	sort_alf = sorted(results, key=lambda x: x[0])
	# second sort based to matching scores
	sort_score = sorted(sort_alf, key=lambda x: x[1], reverse=True)
	return sort_score

def scoreQueryResult(query, diagnose):
	# if score is 0 the diagnose is completely irrelevant
	# if score is 1 the diagnose is equal to the query
	score = 0
	# NB: if full query match does not happen in diagnose the score is 0
	if query in diagnose:
		# score shows the size of diagnose string which query string occupies
		score = round(float(len(query))/len(diagnose),3)
	return score