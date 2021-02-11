from setuptools import find_packages, setup

setup(
    name='pylexitext',
    packages=find_packages(include=['pylexitext']),
    version='0.1.0',
    description='Pylexitext is a python library that aggregates a series of NLP methods, text analysis, content converters and other usefull stuff.',
    author='Victor Bona',
    license='MIT',
    author_email='victor.bona@hotmail.com',
    keywords=['NLP', 'readability', 'nltk', 'text'],

    install_requires=['numpy', 'networkx', 'matplotlib', 'wordcloud'],
    setup_requires=[''],
    tests_require=['pytest'],
    test_suite='tests',
)
