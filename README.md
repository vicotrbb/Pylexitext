# Pylexitext

<img src="https://img.shields.io/github/issues/vicotrbb/pylexitext"> <img src="https://img.shields.io/github/workflow/status/vicotrbb/Pylexitext/Python%20application"> <img src="https://img.shields.io/github/commit-activity/w/vicotrbb/Pylexitext">

Pylexitext is a python library that aggregates a series of NLP methods, text analysis, content converters and other usefull stuff.

## Supported languages

- English

## How to use

First you need to install the library using pip.

```
pip install pylexitext
```

Pylexitext uses a main object called `text` that wrapps all the text functions and some helpers to perform aditional functions.
A basic functionality would looks like this:

```
from pylexitext import text

sample = text.Text('<YOUR TEXT>')
sample.describe()
```

This script will load the pylexitext object with your text, perform all the pre-processing and then, with the `describe()` method, return to you a dict with some proprierties of your text.

With the text:

```
Best hello world ever made by a Developer.
```

The output would be:

```
{'text_size': 42, 'total_words': 8, 'char_count': 35, 'non_stop_words': ['best', 'hello', 'world', 'ever', 'made', 'developer.'], 'stop_words': ['by', 'a'], 'stop_words_number': 2, 'unique_terms': {'made', 'hello', 'ever', 'best', 'developer.', 'world'}, 'unique_words': 6, 'sentences': ['best hello world ever made by a developer', ''], 'number_senteces': 2, 'lexical_diversity': 100.0, 'frequency_distribution': FreqDist({'best': 1, 'hello': 1, 'world': 1, 'ever': 1, 'made': 1, 'developer.': 1}), 'total_syllables': 13, 'total_polysyllables': 1, 'flesch_reading_ease_score': 65.13749999999999, 'flesch_kincaid_grade_level_score': 5.145, 'smog_score': 7.168621630094336, 'gunning_fog_index_score': 15.7}
```

Those are all the proprierties described by pylexitext:

- Text size
- Number of words
- List of stopwords
- Characteres count
- List of words wout/ stopwords
- Number of words wout/ stopwords
- Number of present stopwords
- Unique words
- Number of unique words
- Number of sentences
- Lexical diversity (%)
- Total syllables
- Total polysyllables
- Flesch reading ease score
- Flesch kincaid grade level score
- Smog score
- Gunning fog index score(Not ready!)

## Create a summary from your text

Pylexitext can create summaries of your texts using sentences ranking, generating and joining chunks. By default the number of chunks generated are 3.

Usually, this function don't work well for small texts and if your text is big, you should generate more chunks(improving the final result).

```
from pylexitext import text

sample = text.Text('<YOUR BIG TEXT>')
sample.summarize(top_n=5)
```

## Part-of-speech(POS) tagging

Using NLTK, Pylexitext can perform a grammatical tagging which is the process of marking up a word in a text (corpus) as corresponding to a particular part of speech.

The embedded parameter is used to join the tag and the word, if False, the result will be a tuple.

```
from pylexitext import text

sample = text.Text('Best hello world ever made by a Developer.')
sample.speech_tagging(embedded=True)
```

Output:

```
['best_JJS', 'hello_NN', 'world_NN', 'ever_RB', 'made_VBN', 'by_IN', 'a_DT', 'developer_NN', '._.']
```

## Generation of ngrams

Pylexitext can extracts ngrams from the text, which is a list of n(default=3) words from the text.

There is also a method `bigrams_extraction`, that extracts a bigram(2 words) by default.

```
from pylexitext import text

sample = text.Text('Best hello world ever made by a Developer.')
sample.ngrams_extraction(n=3)
```

output:

```
[['best', 'hello', 'world'], ['hello', 'world', 'ever'], ['world', 'ever', 'made'], ['ever', 'made', 'by'], ['made', 'by', 'a'], ['by', 'a', 'developer']]
```

## Text stemming

Text stemming is a normalization method to return inflacted words to it's morphological original form.

Ex: fishing, fished, and fisher -> fish

```
from pylexitext import text

sample = text.Text("I'm coding it to be the best application.")
sample.stemming()
```

output:

```
i'm code it to be the best application.
```

## Text Lexical Graph generation & plotting

Pylexitext can generate a lexical graph from the cleaned raw text at the Text object, this graph represents all the possible connections between words, being unique words as vertex and the connections as edges.

```
from pylexitext import text

sample = text.Text("I'm coding it to be the best application.")
sample.lexical_graph()

# {'im': ['coding'], 'coding': ['it'], 'it': ['to'], 'to': ['be'], 'be': ['the'] , 'the': ['best'], 'best': ['application'], 'application': []}
```

As a visualization resource, you can easily plot the generated graph using the **lexical_graph_plot** method, that creates a pyploy graph for you.

```
from pylexitext import text

sample = text.Text("I'm coding it to be the best application.")
sample.lexical_graph_plot()
```

This method can be used as static from the **pylexitext.plots** as well.

## Text Normalization

Text normalization is a series of techniques used to "clean" the text to it's most base level, trying to reduce the randomness os the text. Usually, this type of method is used to pre-process text before use on NLP/ML models.

```
from pylexitext import text

sample = text.Text("I'm coding it to be the best application.")
sample.normalization()
```

output:

```
im code best applic
```

## Static methods

Pylexitext has some usefull static methods for text processment and normalization, that can be used without define a main Text object.

Those methods are:

```
from pylexitext.text import remove_numbers, remove_punctuation, remove_extra_whitespace_tabs, remove_non_unicode, noise_remoaval

remove_numbers('Hi1 I'm    Victor Ceñía')
# Hi I'm    Victor Ceñía

remove_punctuation('Hi I'm    Victor Ceñía')
# Hi Im    Victor Ceñía

remove_numbers('Hi Im    Victor Ceñía')
# Hi Im Victor Ceñía

remove_non_unicode('Ceñía')
# Hi Im Victor Cea

noise_removal('Hi1 I'm    Victor Ceñía')
# hi Im victor cea
```

### Sentence similarity

Sentence similarity static method uses levenshtein distance method to compoare and calculate the similarity of two sentences.

```
from pylexitext.text import sentence_similarity

sentence_similarity('hello beautiful world', 'hello world')
# 0.8598892366800223

# You can get the output in 0-100% as well:
sentence_similarity('hello beautiful world', 'hello world', percentage_base=True)
# 85.99
```

## Engines

Pylexitext provides a series of usefull Text Engines.

### Search Engine

The search engine provide an easy way to search for a query string match on list of documents, this documents should be "summaries" from bigger documents, that, one time
found on the documents portifolio, could lead to the complete original document.

The engine object itself hold the documents, and handle all the search protocol to find the desired document. A document search will have a relevance score, that quantifies how much the document matches with the search query. The match score have a treshold of 0 by default, that can be changed if needed, adding more confidence to the search, but reducing the number of results.

Bellow an example of how to create the Engine object:

```
from pylexitext.engines import SearchEngine

documents = [
  '''At Scale You Will Hit Every Performance Issue I used to think I knew a bit about performance scalability and how to keep things trucking when you hit large amounts of data Truth is I know diddly squat on the subject since the most I have ever done is read about how its done To understand how I came about realising this you need some background''',
  '''Richard Stallman to visit Australia Im not usually one to promote events and the like unless I feel there is a genuine benefit to be had by attending but this is one stands out Richard M Stallman the guru of Free Software is coming Down Under to hold a talk You can read about him here Open Source Celebrity to visit Australia''',
  '''MySQL Backups Done Easily One thing that comes up a lot on sites like Stackoverflow and the like is how to backup MySQL databases The first answer is usually use mysqldump This is all fine and good till you start to want to dump multiple databases You can do this all in one like using the all databases option however this makes restoring a single database an issue since you have to parse out the parts you want which can be a pain'''
]

document =  '''The Great Benefit of Test Driven Development Nobody Talks About The feeling of productivity because you are writing lots of code Think about that for a moment Ask any developer who wants to develop why they became a developer One of the first things that comes up is I enjoy writing code This is one of the things that I personally enjoy doing Writing code any code especially when its solving my current problem makes me feel productive It makes me feel like Im getting somewhere Its empowering'''

# By default, match_threshold is 0.0
engine = SearchEngine(match_threshold=0.2)

# Adds a single document to the Engine portifolio and returns the index of the document.
engine.add_doc(document)

# Adds a list of documents to the Engine portifolio.
engine.extend_docs(documents)

# We could remove a document using it's index:
# engine.remove_doc(doc_ix=?)

# To list the documents, we could use, that will return a list of sets with (doc index, document string):
# engine.get_docs()

# Search a string query on the Engine documents portifolio, by default, it returns the top 1 result.
# To change the number of results, change the parameter 'top_n'
engines.search('How to backup a MySQL database', top_n=2)
```

The search method will return the two best matchs for the query:

```
 [(0.39346959912353996,
 5,
 'setting up git to use a subversion svn style workflow moving from subversion svn to git can be a little confusing at first i think the biggest thing i noticed was that git doesnt have a specific workflow you have to pick your own personally i wanted to stick to my subversion like work-flow with a central server which all my machines would pull and push too since it took a while to set up i thought i would throw up a blog post on how to do it'),
 (0.38138503569823695,
  2,
  'mysql backups done easily one thing that comes up a lot on sites like stackoverflow and the like is how to backup mysql databases the first answer is usually use mysqldump this is all fine and good till you start to want to dump multiple databases you can do this all in one like using the all databases option however this makes restoring a single database an issue since you have to parse out the parts you want which can be a pain')]
```

Other available methods are:

```
engine.save_to_file()
# Dump the Search Engine object to a json file and returns the name of the generated document.
# Default file_name pattern: '<todays datetime as %d-%m-%Y-%H-%M-%S>-search_engine-<number of documents>-docs.json'

engine.load_from_file(file_name='<FILE NAME>.json')
# Load a Search Engine object from json file.
```

### Static methods

All the static methods available are related to the search process of the engine, and can be used as the example below:

```
SearchEngine.extract_concordance_dict('<DOCUMENT STRING>')
# Create a concordance dict from the input text.
# A concordance dict counts the number of occurences of a word.

SearchEngine.magnitude(<CONCORDANCE DICT>)
# Calculates the n-dimensions vector space from a concordance dict.

SearchEngine.find_relation(query, <CONCORDANCE DICT>)
# Scores the relation between a query and a concordance dict, it is used to search for top matchind documents
# with the query.
```

## About Creator

Find me on:

💡 https://github.com/vicotrbb  
📊 https://www.linkedin.com/in/victorbona/

## Collaborations
