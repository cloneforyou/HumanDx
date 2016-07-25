from humandx.indexing import getRelevance, sortResults 
import os 

# constant defining the path to the datasource file
DATASOURCE_FILE = "humandx/short-diagnoses.txt"

# constants defining the warning messages
WARNING_1_FILE_ABSENT = "Data source file '%s' does not exist."
WARNING_2_QUERY_SHORT = "Query string should be at least 2 characters long. '%s' is only %s long."
WARNING_3_CORPUS_IS_EMPTY = "The corpus of diagnoses is empty. Please see other warnings for details."

# the container to work with the corpus of diagnoses
class Corpus:
	
	# initiate the corpus of diagnoses
	def __init__(self, datasource_file = DATASOURCE_FILE):
		self.__diagnoses = []	
		self.populate(datasource_file)
		# if after the corpus population it is still empty we warn about it
		if len(self.__diagnoses) == 0:
			print(WARNING_3_CORPUS_IS_EMPTY)

	# populate the corpus of diagnoses from the data-source file
	def populate(self,datasource_file):
		# check that file exists
		if os.path.exists(datasource_file):
			with open(datasource_file) as f:
				# read the content of the file
			    lines_of_file = f.readlines()
			    # clean the lines read from the file from unnecessary characters
			    self.__diagnoses = [x.strip('\n') for x in lines_of_file]
		else:
			# warn that the file is absent
			print(WARNING_1_FILE_ABSENT % datasource_file)
	
	# find diagnoses that match with the query and return them sorted
	def query(self,query):
		results = []
		# only perform the search if the query keyword is 2+ characters long
		if len(query)>1:
			for diagnose in self.__diagnoses:
				# check how relevant the current diagnose is against the query keyword
				relevance = getRelevance(query, diagnose)
				# if the current diagnose is not irrelevant - add it to the list of results
				if (relevance>0):
					results.append({
						"diagnose":diagnose, 
						"relevance":relevance})
		else:
			print(WARNING_2_QUERY_SHORT %(query, (len(query))))
		# sort the results 
		results_sorted = sortResults(results)
		return results_sorted
