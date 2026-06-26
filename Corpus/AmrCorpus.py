import os
import re

from Corpus.Corpus import Corpus

from AmrSentence import AmrSentence


class AmrCorpus(Corpus):

    def __init__(self,
                 folder: str,
                 pattern: str = None):
        """
        A constructor of AmrCorpus class which reads all AmrSentence files with the file
        name satisfying the given pattern inside the given folder. For each file inside that folder, the constructor
        creates an AmrSentence and puts in inside the list sentences.

        PARAMETERS
        ----------
        folder : str
            Folder where all sentences reside.
        pattern : str
            File pattern such as "." ".train" ".test".
        """
        self.sentences = []
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_name = os.path.join(root, file)
                if (pattern is None or pattern in file_name) and re.match("\\d+\\.", file):
                    sentence = AmrSentence(root, file_name)
                    self.sentences.append(sentence)
