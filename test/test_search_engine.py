import pytest
from pylexitext.engines import SearchEngine

text_sample = "I got a lot of questions about programming but i don't think they're the right questions to ask questions like. How many languages do i need to learn what language do i need to learn to get to company x what's the difference between a and b and which makes more money what are the exact steps i need to take. To become the. What kind of program should i write to build up my resume so why don't i like these questions because it feels like the people who are asking these questions they are learning how to program just for the sake of learning how to program. The program is just a tool. Being a programmer for me means you write code to automate things. Or to make things perform certain actions for example programming a refrigerator to turn on the light when you open the door. When you think about it. Programming is actually kind of boring. You're just giving a series of instructions to a machine over and over again until you get it right i don't want to speak for all of you. But i think it's a pay wasn't great i don't think a lot of you would spend hours and hours every night in front of the computer trying to learn how to code or to just debug your program sometimes we get caught up learning languages or doing coding challenges or fantasizing about you not working for these big tech companies that weforget why we wanted to learn programming in the first place. You wanted to program because you saw the amazing things that can be built using programming. So don't just learn how to program build something that matters build something that means something to you build something that solves a problem you're a problem solver a creator an innovator you're not a programmer programming is just a tool in your arsenal to build something amazing. You can be analytical trade of empathetic and programming allows you to express those qualities of yourself but programming in of itself is nothing special it's like a pencil it can mark stuff down if you press on the pencil hard enough. That's it but with a pencil you can write novels draw beautiful portraits build plans for a skyscraper or anything limited only by your imagination. You don't learn how to program to get into google. You learn how to program to build something meaningful something that helps real people with real problems i'm partnered of ibm today to talk about a global initiative called call for code which calls for developers to build something impactful and have a positive change across the world through their code as you know there are hundreds and hundreds of natural disasters every year like hurricanes and earthquakes floods volcanoes and wildfires those affect numerous lies and causes tremendous damage to many families around the world if you strive for real impact we desperately need you this is why 2018 call for code global challenge is a competition that ass people like you to build solutions to improve what we can do to reduce the destructive impact of his natural disasters we need all kinds of technologies."


@pytest.fixture
def text():
    return SearchEngine(text_sample)


def test_health_check(text):
    assert text is not None


def test_search(text):
    pass


def test_magnitude(text):
    pass


def test_extract_concordance_dict(text):
    pass
