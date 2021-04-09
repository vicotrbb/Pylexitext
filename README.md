# Pylexitext

<img src="https://img.shields.io/github/issues/vicotrbb/pylexitext"> <img src="https://img.shields.io/github/workflow/status/vicotrbb/Pylexitext/Python%20application"> <img src="https://img.shields.io/github/commit-activity/w/vicotrbb/Pylexitext">

Pylexitext is a python library that aggregates a series of NLP methods, text analysis, content converters and other usefull stuff.

## Supported languages

- English

## How to use

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

## Static methods

...

## About Creator

Find me on:

💡 https://github.com/vicotrbb  
📊 https://www.linkedin.com/in/victorbona/

## Collaborations
