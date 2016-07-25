from matching import sortQueryResults, scoreQueryResult
import os 

class Corpus:
	def __init__(self, datasource_file = "short-diagnoses.txt"):
		self.__diagnoses = []	
		self.populate(datasource_file)
	
	def populate(self,datasource_file):
		if os.path.exists(datasource_file):
			with open(datasource_file) as f:
			    lines_of_file = f.readlines()
			    self.__diagnoses = [x.strip('\n') for x in lines_of_file]
		else:
			print("data source file '%s' does not exist" % datasource_file)

	def query(self,query):
		results = []
		if len(query)>1:
			for diagnose in self.__diagnoses:
				score = scoreQueryResult(query, diagnose)
				if (score>0):
					results.append({
						'diagnose':diagnose, 
						'score':score})
		else:
			print("Query string should be at least 2 characters long. '%s' is only %s long" %(query, (len(query))))
		results_sorted = sortQueryResults(results)
		return results_sorted
