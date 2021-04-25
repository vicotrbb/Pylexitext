from setuptools import find_packages, setup

setup(
    name='pylexitext',
    packages=find_packages(include=['pylexitext']),
    version='0.2.3',
    description='Pylexitext is a python library that aggregates a series of NLP methods, text analysis, content converters and other usefull stuff.',
    author='Victor Bona',
    license='MIT',
    author_email='victor.bona@hotmail.com',
    download_url='https://pypi.org/project/pylexitext/',
    url='https://github.com/vicotrbb/Pylexitext',
    project_urls={
        "Bug Tracker": "https://github.com/vicotrbb/Pylexitext/issues",
        "Source Code": "https://github.com/vicotrbb/Pylexitext"
    },
    keywords=['NLP', 'readability', 'nltk', 'text', 'Python3', 'data-science'],
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    install_requires=['numpy', 'nltk', 'networkx', 'matplotlib'],
    setup_requires=['wheel', 'pytest-runner', 'flake8'],
    tests_require=['pytest'],
    python_requires=">=3.5",
    classifiers=(
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing",
        "Operating System :: OS Independent",
    ),
)
