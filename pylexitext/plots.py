from matplotlib import pyplot as plt
import networkx as nx
# from wordcloud import WordCloud


# def word_cloud(stopwords, text):
#     wordcloud = WordCloud(stopwords=stopwords).generate(text)
#     plt.imshow(wordcloud, interpolation='bilinear')
#     plt.axis("off")
#     plt.show()


def word_frequency_plot(fdist):
    fdist.plot(25, cumulative=False)
    plt.show()


def lexical_graph(graph, size=(30, 24), dpi=80, **kwargs):
    if type(lexical_graph) != 'dict':
        raise TypeError('This method demands a adjacency list graph format')

    plt.figure(figsize=size, dpi=dpi)
    edges = []
    for i in graph.keys():
        for v in graph[i]:
            edges.append([i, v])

    G = nx.Graph()
    G.add_edges_from(edges)
    nx.draw_networkx(G, kwads=kwargs)
    plt.show()


def dependency_trees(graph):
    pass
