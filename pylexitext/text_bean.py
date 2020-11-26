from nltk.cluster.util import cosine_distance
import numpy as np

def __sentence_similarity(sent1, sent2, stopwords=None):
  if stopwords is None:
      stopwords = []

  sent1 = [w.lower() for w in sent1]
  sent2 = [w.lower() for w in sent2]

  all_words = list(set(sent1 + sent2))

  vector1 = [0] * len(all_words)
  vector2 = [0] * len(all_words)

  for w in sent1:
      if w in stopwords:
          continue
      vector1[all_words.index(w)] += 1

  for w in sent2:
      if w in stopwords:
          continue
      vector2[all_words.index(w)] += 1

  return 1 - cosine_distance(vector1, vector2)

def build_similarity_matrix(sentences, stop_words):
  similarity_matrix = np.zeros((len(sentences), len(sentences)))

  for idx1 in range(len(sentences)):
      for idx2 in range(len(sentences)):
          if idx1 == idx2:
              continue 
          similarity_matrix[idx1][idx2] = __sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

  return similarity_matrix

def read_text(text):
  article = text.split(". ")
  sentences = []

  for sentence in article:
      print(sentence)
      sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
  sentences.pop()

  return sentences