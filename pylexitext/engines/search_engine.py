import math


class SearchEngine():

    def __init__(self, text):
        self.text_chunks = []
        chunk_count = 1
        n_chunks = round(len(text) / 100) + 1
        while chunk_count <= n_chunks:
            self.text_chunks.append(text[(100 * chunk_count) - 100:100 * chunk_count].lower())
            chunk_count += 1

    def __magnitude(self, concordance):
        """
        """
        if not isinstance(concordance, dict):
            raise ValueError('Concordance input must be a dict')

        total = 0
        for _, count in concordance.items():
            total += count ** 2
        return math.sqrt(total)

    def search(self, query, top_n=1):
        """
        """
        if not isinstance(query, str):
            raise ValueError("Query input must be a string")

        print(self.text_chunks)
        query = SearchEngine.extract_concordance_dict(query.lower())

        results = []
        for index, text in enumerate(self.text_chunks):
            text_concordance = SearchEngine.extract_concordance_dict(text)

            # relevance = 0
            topvalue = 0
            for word, count in text_concordance.items():
                if word in query:
                    topvalue += count * query[word]
            results.append((topvalue / (self.__magnitude(text_concordance) * self.__magnitude(query)), index))

        results.sort(reverse=True)
        return [(i[0], self.text_chunks[i[1]]) for i in results[0:top_n]]

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
