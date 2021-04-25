from nltk.corpus import stopwords
import networkx as nx
from . import text_bean as bean
from . import plots as plt
from nltk.probability import FreqDist
import numpy as np
# from spellchecker import SpellChecker
from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer
import nltk
import re
import string
from functools import lru_cache


class Text:

    """

    """

    def __init__(self, text, language='english', pre_process=True):
        self.__accepted_languages = ['english']

        if language not in self.__accepted_languages:
            raise TypeError("language not supported")

        if type(text) is not str:
            raise TypeError("Entry must be an String")

        self.raw_text = text
        self.text = text
        self.language = language

        # Startup methods
        if pre_process:
            self.__generate_stop_words()
            self.__extract_features()

    def __repr__(self):
        return self.describe()

    def set_lang(self, language='english'):
        self.language = language

        if self.language != language:
            self.__generate_stop_words()
            self.__extract_features()

    @lru_cache(maxsize=128)
    def describe(self, verbose=False):
        """
            Describes all the text features:
            * Text size
            * Number of words
            * List of stopwords
            * Characteres count
            * List of words wout/ stopwords
            * Number of words wout/ stopwords
            * Number of present stopwords
            * Unique words
            * Number of unique words
            * Number of sentences
            * Lexical diversity (%)
            * Total syllables
            * Total polysyllables
            * Flesch reading ease score
            * Flesch kincaid grade level score
            * Smog score
            * Gunning fog index score
        """
        description = {
            "text_size": self.text_size,
            "total_words": self.total_words,
            "char_count": self.char_count,
            "non_stop_words": self.stopwords_text,
            "stop_words": self.is_stopwords_text,
            "stop_words_number": self.number_stopwords,
            "unique_terms": self.unique_terms,
            "unique_words": self.text_uniques_number,
            "sentences": self.text_sentences,
            "number_senteces": self.text_sentences_number,
            "lexical_diversity": self.lexical_diversity,
            "frequency_distribution": self.fdist,
            "total_syllables": self.total_syllables,
            "total_polysyllables": self.total_polysyllables,
            "flesch_reading_ease_score": self.flesch_reading_ease_score,
            "flesch_kincaid_grade_level_score": self.flesch_kincaid_grade_level_score,
            "smog_score": self.smog_score,
            "gunning_fog_index_score": self.gunning_fog_index_score,
        }

        if verbose:
            print(description)

        return description

    @lru_cache(maxsize=128)
    def __generate_stop_words(self):
        self.stopwords_set = set(stopwords.words(self.language))
        self.stopwords_set.add('.')

    @lru_cache(maxsize=256)
    def __extract_features(self):
        self.text = self.text.lower()
        self.sentences = re.split(r' *[\.\?!][\'"\)\]]*[ |\n](?=[A-z])', self.text)
        self.total_sentences = self.senteces_count()
        self.text_size = len(self.text)
        self.words = Text.noise_removal(self.text).split(' ')
        self.total_words = len(self.words)
        self.char_count = len(self.text.replace(" ", ""))
        self.stopwords_text = [word for word in self.text.split(
            ' ') if word not in self.stopwords_set]
        self.is_stopwords_text = [word for word in self.text.split(
            ' ') if word in self.stopwords_set]
        self.unique_terms = set(self.stopwords_text)
        self.text_uniques_number = len(self.unique_terms)
        self.text_sentences = self.text.split('.')
        self.text_sentences_number = len(self.text_sentences)
        self.number_stopwords = len(set(self.is_stopwords_text))
        self.lexical_diversity = len(
            set(self.stopwords_text)) / len(self.stopwords_text) * 100
        self.fdist = FreqDist(self.stopwords_text)
        self.total_syllables = 0
        self.total_polysyllables = 0
        self.total_complex_words = 0
        for y in self.words:
            syllable_count_temp = bean.syllable_count(y)
            self.total_syllables += syllable_count_temp

            if syllable_count_temp >= 3:
                self.total_polysyllables += 1
                self.total_complex_words += 1

        self.flesch_reading_ease_score = self.flesch_reading_ease()
        self.flesch_kincaid_grade_level_score = self.flesch_kincaid_grade_level()
        self.smog_score = self.smog()
        self.gunning_fog_index_score = self.gunning_fog_index()

    @lru_cache(maxsize=128)
    def topics_extraction(self):
        """
            TO-BE-DONE
        """
        pass

    # def misspeled(self):
    #     """
    #         Return an array with all the misspelled words of the text.
    #     """
    #     print('')
    #     spell = SpellChecker()
    #     misspelled = spell.unknown(self.stopwords_text)
    #     return misspelled

    # @lru_cache(maxsize=128)
    # def word_cloud(self):
    #     """
    #       Plots a word frequency cloud.
    #     """
    #     plt.word_cloud(self.stop_words, self.text)
    #     pass

    @lru_cache(maxsize=128)
    def word_frequency_plot(self):
        """
          Plots a word frequency line plot.
        """
        plt.word_frequency_plot(self.fdist)
        pass

    @lru_cache(maxsize=128)
    def lexical_tree(self, size=(30, 24), **kwargs):
        """
            TO-BE-DONE
        """
        pass

    @lru_cache(maxsize=128)
    def lexical_graph(self):
        """
          Generates a lexical graph from the original clened text, this lexical graph is represented by all the unique terms from the cleaned text(including stopwords)
          as the Vertex and the edges are the possible connections between words from the text.
        """
        lexical_graph = {}

        for sentence in self.sentences:
            text_nodes = Text.noise_removal(sentence).split(' ')

            for index, word in enumerate(text_nodes):
                if word not in lexical_graph:
                    lexical_graph[word] = []

                if index + 1 < len(text_nodes):
                    if text_nodes[index + 1] not in lexical_graph[word]:
                        lexical_graph[word].append(text_nodes[index + 1])

        return lexical_graph

    def lexical_graph_plot(self, size=(30, 24), dpi=80, **kwargs):
        """
            Plots a graph from the lexical graph method.

            This method can be used for any other graph as well, find it on pylexitext.plots.
        """
        graph = self.lexical_graph()
        plt.lexical_graph(graph, size, dpi, kwargs)

    @lru_cache(maxsize=256)
    def summarize(self, top_n=3, verbose=False):
        """
          Extracts a n chunk summary from the main text.
          Default n chunks = 3
        """
        stop_words = stopwords.words(self.language)
        summarize_text = []
        sentences = bean.read_text(self.raw_text)

        sentence_similarity_martix = bean.build_similarity_matrix(
            sentences, stop_words)
        sentence_similarity_graph = nx.from_numpy_array(
            sentence_similarity_martix)
        scores = nx.pagerank(sentence_similarity_graph)

        ranked_sentence = sorted(
            ((scores[i], s) for i, s in enumerate(sentences)), reverse=True)

        for i in range(top_n):
            summarize_text.append(" ".join(ranked_sentence[i][1]))

        self.summary = ". ".join(summarize_text)

        if verbose:
            print(self.summary)

        return self.summary

    @lru_cache(maxsize=128)
    def sentiment_analysis(self, verbose=False, method='vader'):
        if method == 'vader':
            from .sentiment import sentiment

            return sentiment.vader_sentiment_analysis(self.text, verbose)

        else:
            pass

    def named_entity_recognition(self):
        pass

    @lru_cache(maxsize=128)
    def senteces_count(self):
        self.total_sentences = 0
        for sentece in self.sentences:
            if len(Text.remove_punctuation(text=sentece).split(' ')) > 2:
                self.total_sentences += 1
        return max(1, self.total_sentences)

    @lru_cache(maxsize=256)
    def speech_tagging(self, embedded=False):
        """
            Performs a POS tagging on the text
        """
        tokens = word_tokenize(self.text)
        self.pos = pos_tag(tokens)

        embedded_pos = []
        if embedded:
            for word, tag in self.pos:
                embedded_word = word + "_" + tag
                embedded_pos.append(embedded_word)

            return embedded_pos

        return self.pos

    @lru_cache(maxsize=128)
    def stemming(self):
        """
            Normalization method to return inflacted words to it's morphological original form.
            Ex: fishing, fished, and fisher -> fish
        """
        stemmer = nltk.porter.PorterStemmer()
        self.stemmed_text = ' '.join([stemmer.stem(word) for word in self.text.split()])
        return self.stemmed_text

    @lru_cache(maxsize=256)
    def normalization(self):
        """
            Normalizes a text using series of techniques
            Noise removal, stop words remoaval, stemming, word tokenization, lemmatization
        """
        cleaned_text = ""
        lemmatizer = WordNetLemmatizer()
        for word in self.stopwords_text:
            cleaned_text = cleaned_text + " " + lemmatizer.lemmatize(word)

        normalizad_text = cleaned_text[1:]

        stemmer = nltk.porter.PorterStemmer()
        self.normalizad_text = ' '.join([stemmer.stem(word) for word in normalizad_text.split()])

        return self.normalizad_text

    @lru_cache(maxsize=128)
    def topics_modeling(self):
        """
            TO-BE-DONE
        """
        pass

    @lru_cache(maxsize=256)
    def ngrams_extraction(self, n=3):
        """
            Perform a ngrams extraction on the text.
            ngrams = chunks of 'n' words from the text splited in lists
        """
        out = []
        for i in range(len(self.words)-n+1):
            out.append(self.words[i:i+n])

        return out

    @lru_cache(maxsize=256)
    def bigrams_extraction(self):
        """
            Perform a bigrams extraction on the text.
            bigrams = chunks of 2 words from the text splited in lists
        """
        self.bigrams = self.ngrams_extraction(n=2)
        return self.bigrams

    def avg_sentence_length(self):
        """
            Calculates the avarage sentence length from the text.
        """
        return round(float(self.total_words / self.total_sentences))

    @lru_cache(maxsize=128)
    def term_frequency(self):
        """
            Performs an unique words frequency(%) count on the text. 
        """
        terms = []
        for term in self.unique_terms:
            result = {
                term: (self.words.count(term) / self.text_size) * 100
            }
            terms.append(result)

        self.terms_frequency = terms
        return self.terms_frequency

    @lru_cache(maxsize=128)
    def text_similarity(self, text):
        """
            Compares the raw text at the pylexitext Text object and the inputed text to compare, 
            returns the similarity as 0-1.

            The text similarity is calculated using the levenshtein distance method.
        """
        return bean.levenshtein_distance(self.raw_text, text)

    # -----------------------------------------
    # Readibility of the text: English
    # -----------------------------------------

    @lru_cache(maxsize=128)
    def flesch_reading_ease(self):
        return 206.835 - (1.015*(self.total_words/self.text_sentences_number)) - (84.7*(self.total_syllables/self.total_words))

    @lru_cache(maxsize=128)
    def flesch_kincaid_grade_level(self):
        return (0.39*(self.total_words/self.text_sentences_number)) + (11.8*(self.total_syllables/self.total_words)) - 15.59

    @lru_cache(maxsize=128)
    def smog(self):
        return (1.0430*(np.sqrt(self.total_polysyllables*(30/self.text_sentences_number)))) + 3.1291

    @lru_cache(maxsize=128)
    def gunning_fog_index(self):
        """
            Under work
        """
        return (0.4*(self.total_words/self.total_sentences) + 100*(self.total_complex_words/self.total_words))

    # -----------------------------------------
    # Statistics methods
    # -----------------------------------------

    @staticmethod
    def split_by(text=''):
        text_chunks = []

        # TO-DO

        return text_chunks

    @staticmethod
    def remove_numbers(text=''):
        """
           Remove numbers from the text
        """
        pattern = r'[^a-zA-z.,!?/:;\"\'\s]'
        return re.sub(pattern, '', text)

    @staticmethod
    def remove_punctuation(text=''):
        """
           Remove ponctuation from the text
        """
        output = ''.join([c for c in text if c not in string.punctuation])
        return output

    @staticmethod
    def remove_extra_whitespace_tabs(text):
        """
           Remove extra white spaces and tabs from the text
        """
        pattern = r'^\s*|\s\s*'
        return re.sub(pattern, ' ', text).strip()

    @staticmethod
    def remove_non_unicode(text):
        return ''.join([i if ord(i) < 128 else '' for i in text])

    @staticmethod
    def noise_removal(text):
        """
            Remove all the noise from the text, including:
                * Numbers
                * stopwords
                * special characters
                * extra whitespaces and tabs
                * non unicode

            Outputs the resultant text
        """
        text = Text.remove_numbers(text)
        text = Text.remove_punctuation(text)
        text = Text.remove_extra_whitespace_tabs(text)
        text = Text.remove_non_unicode(text)
        text = text.lower()
        return text

    @staticmethod
    def sentence_similarity(sentence1, sentence2, percentage_base=False):
        """
           Compares two sentences and outputs the sentence similarity of them.
           The sentences similarity is calculated using the levenshtein distance method.
        """
        output = bean.levenshtein_distance(sentence1, sentence2)
        if percentage_base:
            return round(output * 100, 2)
        return output
