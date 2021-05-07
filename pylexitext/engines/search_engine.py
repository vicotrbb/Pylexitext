import math
from datetime import datetime
import json
from typing import Iterable

from numpy import iterable


class SearchEngine():

    def __init__(self, docs=[], match_threshold=0.0):
        self.__docs = []
        self.match_threshold = match_threshold
        for doc in docs:
            self.add_doc(doc)

    def __str__(self) -> str:
        return str(self.get_docs())

    def set_match_threshold(self, match_threshold) -> None:
        """
            Set a new match treshold of the search.
        """
        self.match_threshold = match_threshold

    def add_doc(self, doc) -> None:
        """
            Add a new document to the search engine portifolio.

            Returns the index of the new document.
        """
        if not isinstance(doc, str):
            raise ValueError('A document must be a string')

        if len(doc) == 0:
            raise ValueError('A document can not be empty')
        doc = doc.lower()
        self.__docs.append((doc, SearchEngine.extract_concordance_dict(doc)))

        return len(self.__docs) - 1

    def extend_docs(self, docs) -> None:
        """
            Extends the documents portifolio from an existing list.
        """
        if not isinstance(docs, list):
            raise ValueError('The input array must be a list of documents')

        for doc in docs:
            self.add_doc(doc)

    def remove_doc(self, doc_ix) -> set:
        """
            Remove a document from the portifolio by index.
        """
        if not isinstance(doc_ix, int) or len(self.__docs) <= doc_ix or (doc_ix != -1 and doc_ix < 0):
            raise ValueError(
                'A document index must be a valid integer representing a document from the Search Engine documents portifolio')

        return self.__docs.pop(doc_ix)[0]

    def get_docs(self) -> list:
        """
            Return a list of sets with all the documents and their indexes.
        """
        return [(k, v[0]) for k, v in enumerate(self.__docs)]

    def save_to_file(self, file_name='') -> None:
        """
            Dump the Search Engine documents portifolio data to a json file.

            Default file name pattern: '<todays datetime as %d-%m-%Y-%H-%M-%S>-search_engine-<number of documents>-docs.json'
        """
        if not file_name:
            file_name = f'{datetime.now().strftime("%d-%m-%Y-%H-%M-%S")}-search_engine-{len(self.__docs)}-docs.json'

        dto = {
            'match_threshold': self.match_threshold,
            'docs': self.__docs
        }
        with open(file_name, 'w') as json_file:
            json.dump(dto, json_file)

        return file_name

    def load_from_file(self, file_name) -> None:
        """
            Load a Search Engine object from file.
        """
        with open(file_name, 'r') as json_file:
            dto = json.load(json_file)
            try:
                self.__docs = dto['docs']
                self.match_threshold = dto['match_threshold']
            except:
                raise SyntaxError('Json file malformed')

        return self

    def search(self, query, top_n=1) -> list:
        """
            Searchs a string query on the documents portifolio.

            Result set: [(match score, doc id, doc text)]
        """
        if not isinstance(query, str):
            raise ValueError("Query must be a string")

        search_results = []
        query = SearchEngine.extract_concordance_dict(query.lower())
        for k, v in enumerate(self.__docs):
            search_results.append((SearchEngine.find_relation(query, v[1]), k))

        search_results.sort(reverse=True)
        # Result set: [(match score, doc id, doc text)]
        return [(i[0], i[1], self.__docs[i[1]][0]) for i in search_results[0:top_n] if i[0] > self.match_threshold]

    @staticmethod
    def magnitude(concordance) -> float:
        """
            Calculates the n-dimensions vector space.
        """
        if not isinstance(concordance, dict):
            raise ValueError('Concordance input must be a dict')

        total = 0
        for _, count in concordance.items():
            total += count ** 2
        return math.sqrt(total)

    @staticmethod
    def find_relation(query, search_object) -> float:
        """
            Scores a relation between a search query and a target document.

            Higher the score, higher the similarity between the query and the document.
        """
        if isinstance(query, str):
            query = SearchEngine.extract_concordance_dict(query)
        elif not isinstance(query, dict):
            raise ValueError("Query input must be a string or a concordance dict")

        if isinstance(search_object, str):
            search_object = SearchEngine.extract_concordance_dict(search_object)
        elif not isinstance(search_object, dict):
            raise ValueError("search_object input must be a string or a concordance dict")

        # relevance = 0
        topvalue = 0
        search_magnitude = SearchEngine.magnitude(query) * SearchEngine.magnitude(search_object)

        if search_magnitude == 0:
            return 0

        for word, count in query.items():
            if word in search_object:
                topvalue += count * search_object[word]

        return topvalue / search_magnitude

    @staticmethod
    def extract_concordance_dict(text) -> dict:
        """
            Create a concordance dict from the input text.

            A concordance dict counts the number of occurences of a word. 
        """
        if isinstance(text, str):
            text = text.split(' ')
        elif not isinstance(text, list):
            raise TypeError('A text meant to be a string or a list of strings')

        con = {}
        for i in text:
            if i not in con:
                con[i] = 1
            else:
                con[i] += 1
        return con
