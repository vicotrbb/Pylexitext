from matplotlib import pyplot as plt
from wordcloud import WordCloud

def cloud_word(stopwords, text):
    wordcloud = WordCloud(stopwords=stopwords).generate(text)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()