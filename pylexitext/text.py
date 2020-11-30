from nltk.corpus import stopwords
import networkx as nx
import text_bean as bean 
import plots as plt
from nltk.probability import FreqDist

class Text:

  def __init__(self, text, language='english'):
    self.text = text
    self.language = language

    # Kickstart methods
    self.__generate_stop_words()
    self.extract_features()

  def describe(self):
    """
      Describes all the text features:
        * Text size
        * Number of words
        * List of stopwords
        * List of words wout/ stopwords
        * Number of words wout/ stopwords
        * Number of present stopwords
        * Number of unique words
        * Number of sentences
        * Lexical diversity (%)
    """
    return {
      "text_size": self.text_size,
      "text_words_number": self.text_words_number,
      "non_stop_words": self.stopwords_text,
      "stop_words": self.is_stopwords_text,
      "stop_words_number": self.number_stopwords,
      "unique_words": self.text_uniques_number,
      "sentences": self.text_sentences,
      "number_senteces": self.text_sentences_number,
      "lexical_diversity": self.lexical_diversity,
      "frequency_distribution": self.fdist
    }
  
  def __generate_stop_words(self):
    self.stopwords_set = set(stopwords.words('english'))
    self.stopwords_set.add('.')

  def extract_features(self):
    self.text_size = len(self.text)
    self.text_words_number = len(self.text.split(' '))
    self.stopwords_text = [word for word in self.text.split(' ') if word not in self.stopwords_set]
    self.is_stopwords_text = [word for word in self.text.split(' ') if word in self.stopwords_set]
    self.text_uniques_number = len(set(self.stopwords_text))
    self.text_sentences = self.text.split('.')
    self.text_sentences_number = len(self.sentences)
    self.number_stopwords = len(set(self.is_stopwords_text))
    self.lexical_diversity = len(set(self.stopwords_text)) / len(self.stopwords_text) * 100
    self.fdist = FreqDist(self.stopwords_text)
  
  def split_by(self, bias):
    text_chunks = []

    # TO-DO

    return text_chunks
  
  def misspeled(self):
    pass
  
  def word_cloud(self):
    """
    Plots a word frequency cloud.
    """
    plt.word_cloud(self.stop_words, self.text)
    pass
  
  def word_frequency_plot(self):
    """
    Plots a word frequency line plot.
    """
    plt.word_frequency_plot(self.fdist)
    pass
  
  def lexical_tree(self):
    pass

  def summarize(self, top_n=3):
    stop_words = stopwords.words(self.language)
    summarize_text = []
    sentences =  bean.read_text(self.text)

    sentence_similarity_martix = bean.build_similarity_matrix(sentences, stop_words)
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)

    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
    print("Indexes of top ranked_sentence order are ", ranked_sentence)    

    for i in range(top_n):
      summarize_text.append(" ".join(ranked_sentence[i][1]))

    print("Summarize Text: \n", ". ".join(summarize_text))