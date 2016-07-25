# HumanDx Sample Problem

The first working implementation is available here: https://humandx-sample.herokuapp.com/heada, where **/heada** is an example of the query keyword.  

### Architecture

#### Conceptual blocks

- **Corpus** - the list of diagnoses taken from a given source
- **Relevance** - the algorithm allowing to check how relevant a given diagnosis is against the query keyword
- **UI** - the user interface to interact with the system

#### Implementation of conceptual blocks

- **Corpus** - a class in Python, where the source file (short-diagnoses.txt) is parsed into a list of diagnoses (method *populate()*). This list can be queried (method *query()*) against keywords based on Relevance block.
- **Relevance** - a couple of functions in Python allowing to calculate how relevant a given diagnosis (method *getRelevance()*) from the corpus is to the query keyword and to sort the query results according to the relevance score and alphabetical order (method *sortResults()*).  
- **UI** - a minimal *Flask* web-service allowing to get the query results in *JSON* using *GET* requests (e.g. https://humandx-sample.herokuapp.com/{keyword}), deployed on Heroku.

### Approach, tradeoffs, and expected outcomes
The overall strategy was to design as minimal application (still working) as possible, still easily extensible, that other features could be added without changing the general architecture.
While now corpus is just a Python list, it could be an SQL or no-SQL database, as such DBMS provide a genuine support for consistent storage of data and complex queries on it (including strings comparison).
Althouth Python is The data science language (together with R) with a rich collection of NLP and string processing libraries (to be discussed below), so such implementation is also appropriate.
The current relevance calculation is done in the following simple way: if the query keyword is a substring of a given diagnose, calculate the length of the query divide by the length of the diagnoses. This approach is very simplistic and naive still already provides a way to have relevance to sort based on.

### Tools and other technologies to investigate
As an extension I believe it is important to consider approaches, such as Levinshtein distance,  to match also strings allowing some mistakes (to deal with typing errors).
The diagnoses won't be just a list of titles, but will have a more complex data structure with a desctiption and symptoms, so that approaches such as TF-IDF could be used to recommend similar diagnoses.


### Evaluation criteria

### Time to accomplish
