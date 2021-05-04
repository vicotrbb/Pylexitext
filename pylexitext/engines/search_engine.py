import math
import pkg_resources


class SearchEngine():

    def __init__(self, docs, match_threshold=0.0):
        self.__docs = []
        self.match_threshold = match_threshold
        for doc in docs:
            self.add_doc(doc)

    def add_doc(self, doc) -> None:
        """
            Add a new document to the search engine portifolio.
        """
        if not isinstance(doc, str):
            raise ValueError('A document must be a string')

        self.__docs.append((doc, SearchEngine.extract_concordance_dict(doc)))

    def remove_doc(self, doc_ix) -> set:
        """
            Remove a document from the portifolio by index.
        """
        if not isinstance(doc_ix, int):
            raise ValueError(
                'A document index must be a valid integer representing a document from the Search Engine documents portifolio')

        return self.__docs.pop(doc_ix)

    def get_docs(self) -> list:
        """
            Return a list of sets with all the documents and their indexes.
        """
        return [(k, v[0]) for k, v in enumerate(self.__docs)]

    def save_to_file(self) -> None:
        """
            Dump the Search Engine documents portifolio data to a file.
        """
        pass

    def load_from_file(self, file) -> None:
        """
            Load all the documents from a file.
        """
        pass

    def convert_to_tensors(self):
        print('Not yet implemented')

        required = ('tensorflow')
        installed = (pkg.key for pkg in pkg_resources.working_set)
        missing = required - installed
        if missing:
            raise ImportError(f'The following dependencies are not installed: {required}')

        return None

    def __magnitude(self, concordance) -> float:
        """
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
        search_magnitude = SearchEngine.__magnitude(query) * SearchEngine.__magnitude(search_object)

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

    def search(self, query, top_n=1) -> list:
        """
        """
        search_results = []
        query = SearchEngine.extract_concordance_dict(query)
        for k, v in enumerate(self.__docs):
            search_results.append(SearchEngine.find_relation(query, v[1]), k)

        search_results.sort(reverse=True)
        # Result set: (match score, doc id, doc text)
        return [(i[0], i[1], self.__docs[i[1]][1]) for i in search_results[0:top_n]]
