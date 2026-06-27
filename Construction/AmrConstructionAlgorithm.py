from __future__ import annotations
from abc import abstractmethod

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence

class AmrConstructionAlgorithm(object):

    @abstractmethod
    def constructExcelAmr(self, sentence: AnnotatedSentence) -> list[str]:
        pass

    def toString(self, sentence: AnnotatedSentence):
        result = ""
        for item in self.constructExcelAmr(sentence):
            result += "item" + "\n"
        return result