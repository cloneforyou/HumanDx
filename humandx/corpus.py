from humandx.indexing import sortQueryResults, scoreQueryResult
import os 

DATASOURCE_FILE = "humandx/short-diagnoses.txt"
WARNING_1_FILE_ABSENT = "Data source file '%s' does not exist"
WARNING_2_QUERY_SHORT = "Query string should be at least 2 characters long. '%s' is only %s long"

class Corpus:
	def __init__(self, datasource_file = DATASOURCE_FILE):
		self.__diagnoses = []	
		self.populate(datasource_file)
	
	def populate(self,datasource_file):
		if os.path.exists(datasource_file):
			with open(datasource_file) as f:
			    lines_of_file = f.readlines()
			    self.__diagnoses = [x.strip('\n') for x in lines_of_file]
		else:
			print(WARNING_1_FILE_ABSENT % datasource_file)

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
			print(WARNING_2_QUERY_SHORT %(query, (len(query))))
		results_sorted = sortQueryResults(results)
		return results_sorted
