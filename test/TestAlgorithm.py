import unittest

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from WordNet import WordNet

from RuleBasedConstructionAlgorithm import RuleBasedConstructionAlgorithm
from WordNet.WordNet import WordNet

class TestAlgorithm(unittest.TestCase):

    def testAlgorithm(self):
        algorithm = RuleBasedConstructionAlgorithm(WordNet())
        sentence = AnnotatedSentence(open("../sentences/0000.test", "r", encoding='utf8'), "../sentences/0000.test")
        print(algorithm.toString(sentence))
        sentence = AnnotatedSentence(open("../sentences/0001.test", "r", encoding='utf8'), "../sentences/0001.test")
        print(algorithm.toString(sentence))
        sentence = AnnotatedSentence(open("../sentences/0002.test", "r", encoding='utf8'), "../sentences/0002.test")
        print(algorithm.toString(sentence))
        sentence = AnnotatedSentence(open("../sentences/0003.test", "r", encoding='utf8'), "../sentences/0003.test")
        print(algorithm.toString(sentence))
        sentence = AnnotatedSentence(open("../sentences/0004.test", "r", encoding='utf8'), "../sentences/0004.test")
        print(algorithm.toString(sentence))
        sentence = AnnotatedSentence(open("../sentences/0005.test", "r", encoding='utf8'), "../sentences/0005.test")
        print(algorithm.toString(sentence))
        sentence = AnnotatedSentence(open("../sentences/0006.test", "r", encoding='utf8'), "../sentences/0006.test")
        print(algorithm.toString(sentence))
        sentence = AnnotatedSentence(open("../sentences/0008.test", "r", encoding='utf8'), "../sentences/0008.test")
        print(algorithm.toString(sentence))
        sentence = AnnotatedSentence(open("../sentences/0009.test", "r", encoding='utf8'), "../sentences/0009.test")
        print(algorithm.toString(sentence))
        sentence = AnnotatedSentence(open("../sentences/0010.test", "r", encoding='utf8'), "../sentences/0010.test")
        print(algorithm.toString(sentence))
        sentence = AnnotatedSentence(open("../sentences/0027.test", "r", encoding='utf8'), "../sentences/0027.test")
        print(algorithm.toString(sentence))
        sentence = AnnotatedSentence(open("../sentences/0392.test", "r", encoding='utf8'), "../sentences/0392.test")
        print(algorithm.toString(sentence))
        sentence = AnnotatedSentence(open("../sentences/0534.test", "r", encoding='utf8'), "../sentences/0534.test")
        print(algorithm.toString(sentence))

if __name__ == '__main__':
    unittest.main()
