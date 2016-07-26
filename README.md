# HumanDx Sample Problem

The first working implementation is available here: https://humandx-sample.herokuapp.com/heada, where **/heada** is an example of the query keyword.  

### Architecture

#### Conceptual blocks

- **Data Storage** - the place to store the corpus of diagnoses
- **Search** - the algorithm to check how relevant given diagnoses are to a query keyword
- **UI** - the user interface to perform queries

#### Implementation of conceptual blocks

- **Data Storage** - a class in Python (*humandx/corpus.py*), where the source file (short-diagnoses.txt) is parsed into a list of diagnoses (method *populate()*). This list can be queried (method *query()*) against keywords according the algorithm from Search block.
- **Search** - a couple of functions in Python (*humandx/relevance.py*) allowing to calculate how relevant a given diagnosis (method *getRelevance()*) from the corpus is to the query keyword and to sort the query results according to the relevance score and alphabetical order (method *sortResults()*).  
- **UI** - a minimal *Flask* web-service (*app.py*) allowing to get the query results in *JSON* using *GET* requests (e.g. [https://humandx-sample.herokuapp.com/{keyword}](https://humandx-sample.herokuapp.com/heada)), deployed on Heroku.

### Approach, tradeoffs, and expected outcomes
#### Assumptions
- the system is open and it does not require any access control
- the system should be later integratable into web-applications
- while now the system should support only a list of 102 examples (short-diagnoses.txt), in future it should support complex queries based on tens of thousands of diagnoses.
- for the first implementation doctors enter keywords without mistakes (no need to typo-tolerant search)

#### Strategy
The overall strategy was to design as **minimal application** (still working) as possible, still easily extensible, that **other features could be added without changing the general architecture**.
Althouth Python is the data science language (together with R) with a rich collection of NLP and string processing libraries, so the implementation was done in Python.
The current relevance calculation is done in the following simple way: if the query keyword is a substring of a given diagnose, calculate the length of the query divide by the length of the diagnoses. This approach is very simplistic and naive still already provides a way to have relevance to sort based on.


### Tools and other technologies to investigate
- **Data Storage** - not a simple list of diagnoses but a more complete database with corresponding symptoms, diagnoses descrption etc. It could be an SQL or no-SQL database, as such DBMS provide a genuine support for consistent storage of data and complex queries on it (including strings comparison). RDS Amazon Database could also be an appropriate option.
- **Search** - many things could be done in various dimensions, such as content, context, collaborative filtering and Google-search like suggestions (the list is not complete).
  - *Content* - a more advanced search allowing mistakes in spellings, using algorithms, such as [Levinshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) or [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance). Apart from the pure search, algorithms such as [bag of words](https://en.wikipedia.org/wiki/Bag-of-words_model), [TF-IDF](https://en.wikipedia.org/wiki/Tf–idf), [clustering](https://en.wikipedia.org/wiki/Cluster_analysis) could be utilized to recommend diagnoses relevant to a given one.
  - *Context* - to utilize in the scoring function current trends (the diagnoses more relevant to the region where the doctor is quering have higher relevance score as for doctors from regions where they are not much applicable)
  - *Collaborative filtering* - when other doctors from the similar context (e.g. location) indicate that a given diagnose is relevant to the source one, it appears with the higher relevance score also in searches for other doctors 
  - *Google/style suggestions* - the query keyword is suggested based on searches of other doctors
- **UI** - a RESTFull API, so that the system could be easily integrated into web-applications, mobile applications etc. 

### Evaluation criteria

### Time to accomplish
- **Current implementation** - was done in 2.5 hours, the documentation took another 1.5.
- **If a week is given (40 hours)** - I would dedicate: 
  - 15 hours interviewing doctors and stakeholders to understand the priorities the system should work, 
  - 5 hours to design an architecture based on the requirements I collected from the interviews 
  - 6 hours to make a solid Data Storage
  - 14 hours to implement a more advanced Search system, prioritizing some technologies mentioned above according to the requirements from the interviews. 
  - In 1 week time it is unlikely I would do any improvements on the UI side, as even the current implementation allows queries over web. 
