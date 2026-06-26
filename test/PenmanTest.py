import unittest

from AmrSentence import AmrSentence

class PenmanTest(unittest.TestCase):

    def test(self):
        sentence = AmrSentence("../amrsentences", "000.test")
        print(sentence.__str__())
        sentence = AmrSentence("../amrsentences", "0001.test")
        print(sentence.__str__())
        sentence = AmrSentence("../amrsentences", "0002.test")
        print(sentence.__str__())
        sentence = AmrSentence("../amrsentences", "0003.test")
        print(sentence.__str__())
        sentence = AmrSentence("../amrsentences", "0004.test")
        print(sentence.__str__())
        sentence = AmrSentence("../amrsentences", "0005.test")
        print(sentence.__str__())
        sentence = AmrSentence("../amrsentences", "0006.test")
        print(sentence.__str__())
        sentence = AmrSentence("../amrsentences", "0007.test")
        print(sentence.__str__())
        sentence = AmrSentence("../amrsentences", "0008.test")
        print(sentence.__str__())
        sentence = AmrSentence("../amrsentences", "0009.test")
        print(sentence.__str__())
        sentence = AmrSentence("../amrsentences", "0010.test")
        print(sentence.__str__())

if __name__ == '__main__':
    unittest.main()
