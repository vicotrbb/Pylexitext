import pytest
from pylexitext.engines import SearchEngine

documents = [
    '''At Scale You Will Hit Every Performance Issue I used to think I knew a bit about performance scalability and how to keep things trucking when you hit large amounts of data Truth is I know diddly squat on the subject since the most I have ever done is read about how its done To understand how I came about realising this you need some background''',
    '''Richard Stallman to visit Australia Im not usually one to promote events and the like unless I feel there is a genuine benefit to be had by attending but this is one stands out Richard M Stallman the guru of Free Software is coming Down Under to hold a talk You can read about him here Open Source Celebrity to visit Australia''',
    '''MySQL Backups Done Easily One thing that comes up a lot on sites like Stackoverflow and the like is how to backup MySQL databases The first answer is usually use mysqldump This is all fine and good till you start to want to dump multiple databases You can do this all in one like using the all databases option however this makes restoring a single database an issue since you have to parse out the parts you want which can be a pain''',
    '''Why You Shouldnt roll your own CAPTCHA At a TechEd I attended a few years ago I was watching a presentation about Security presented by Rocky Heckman read his blog its quite good In it he was talking about security algorithms The part that really stuck with me went like this''',
    '''The Great Benefit of Test Driven Development Nobody Talks About The feeling of productivity because you are writing lots of code Think about that for a moment Ask any developer who wants to develop why they became a developer One of the first things that comes up is I enjoy writing code This is one of the things that I personally enjoy doing Writing code any code especially when its solving my current problem makes me feel productive It makes me feel like Im getting somewhere Its empowering''',
    '''Setting up GIT to use a Subversion SVN style workflow Moving from Subversion SVN to GIT can be a little confusing at first I think the biggest thing I noticed was that GIT doesnt have a specific workflow you have to pick your own Personally I wanted to stick to my Subversion like work-flow with a central server which all my machines would pull and push too Since it took a while to set up I thought I would throw up a blog post on how to do it''',
]


@pytest.fixture
def search_engine():
    return SearchEngine(docs=documents)


@pytest.fixture
def concordance():
    return SearchEngine.extract_concordance_dict(documents[0])


def test_health_check():
    try:
        x = SearchEngine(docs=documents[0])
        assert False
    except:
        assert True


def test_search(search_engine):
    result = search_engine.search('feeling of productivity because you are writing lots of code')
    assert result
    assert len(result[0]) == 3
    assert result[0][0] >= search_engine.match_threshold


def test_treshold(search_engine):
    search_engine.set_match_threshold(0.99)
    result = search_engine.search('feeling of productivity because you are writing lots of code')
    assert not result


def test_add_document(search_engine):
    old_len = len(search_engine.get_docs()) - 1
    doc_to_add = '''Why CAPTCHA Never Use Numbers 0 1 5 7 Interestingly this sort of question pops up a lot in my referring search term stats Why CAPTCHAs never use the numbers 0 1 5 7 Its a relativity simple question with a reasonably simple answer Its because each of the above numbers are easy to confuse with a letter See the below'''
    assert search_engine.add_doc(doc_to_add) > old_len


def test_get_docs(search_engine):
    sample = search_engine.get_docs()
    assert len(sample) > 0
    assert len(sample[0]) == 2


def test_remove_doc(search_engine):
    try:
        assert search_engine.remove_doc(0) is not None
    except:
        assert False

    try:
        search_engine.remove_doc(9999999)
        assert False
    except:
        assert True


def test_extend_docs(search_engine):
    old_len = len(search_engine.get_docs())
    to_add = ['''The Great Benefit of Test Driven Development Nobody Talks About The feeling of productivity because you are writing lots of code Think about that for a moment Ask any developer who wants to develop why they became a developer One of the first things that comes up is I enjoy writing code This is one of the things that I personally enjoy doing Writing code any code especially when its solving my current problem makes me feel productive It makes me feel like Im getting somewhere Its empowering''',
              '''Setting up GIT to use a Subversion SVN style workflow Moving from Subversion SVN to GIT can be a little confusing at first I think the biggest thing I noticed was that GIT doesnt have a specific workflow you have to pick your own Personally I wanted to stick to my Subversion like work-flow with a central server which all my machines would pull and push too Since it took a while to set up I thought I would throw up a blog post on how to do it''',
              ]
    search_engine.extend_docs(to_add)
    assert len(search_engine.get_docs()) - old_len == 2


def test_magnitude(concordance):
    assert SearchEngine.magnitude(concordance) > 0


def test_extract_concordance_dict(concordance):
    assert concordance
    assert isinstance(concordance, dict)
