from nltk.cluster.util import cosine_distance
import numpy as np
import nltk.corpus
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk import ne_chunk
from nltk import RegexpParser

# ------------------------------------------
#          TEXT BEAN HELPER METHODS
# ------------------------------------------
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
        sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
    sentences.pop()

    return sentences


def post_text_process(text):
    """
      Performs a post process with the text, preparing it for text deep analysis
      or other purposes.
    """
    # Splits words to tokens
    tokenized_word = word_tokenize(text.lower())

    # Normalize words to normal form
    # aka: playing -> play
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = []
    for word in tokenized_word:
        lemmatized_words.append(lemmatizer.lemmatize(word))

    # Remove stopwords from the set
    stopwords_set = set(stopwords.words('english'))
    stopwords_set.add('.')
    stopwords_text = [word for word in lemmatized_words if word not in stopwords_set]

    # Named entity recognition
    tags = nltk.pos_tag(stopwords_text)
    chunk = ne_chunk(tags)

    chunking_rule = "NP: {<DT>?<JJ>*<NN>}"
    chunking_text_parsed = RegexpParser(chunking_rule)
    chunking_result = chunking_text_parsed.parse(tags)

    # Returns important information created by the post processing
    return chunking_result, chunk


def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count


def levenshtein_distance(sent1, sent2):
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]

    all_words = list(set(sent1 + sent2))
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    for w in sent1:
        vector1[all_words.index(w)] += 1

    for w in sent2:
        vector2[all_words.index(w)] += 1

    return 1 - cosine_distance(vector1, vector2)
