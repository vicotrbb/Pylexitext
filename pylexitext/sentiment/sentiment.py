from nltk.sentiment.vader import SentimentIntensityAnalyzer


def vader_sentiment_analysis(text, verbose=False):
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)

    if verbose:
        for key in sorted(scores):
            print('{0}: {1}, '.format(key, scores[key]), end='')

    return scores
