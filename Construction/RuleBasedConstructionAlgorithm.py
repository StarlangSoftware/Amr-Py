from typing import List

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence
from AnnotatedSentence.AnnotatedWord import AnnotatedWord
from MorphologicalAnalysis import MorphologicalTag
from WordNet import SemanticRelation
from WordNet.SynSet import SynSet
from WordNet.WordNet import WordNet
from WordNet.SemanticRelation import SemanticRelation

from AmrConstructionAlgorithm import AmrConstructionAlgorithm
from MorphologicalAnalysis.MorphologicalTag import MorphologicalTag

class RuleBasedConstructionAlgorithm(AmrConstructionAlgorithm):

    __word_net: WordNet
    __sentence: AnnotatedSentence

    def __init__(self, word_net: WordNet) -> None:
        self.__word_net = word_net

    def __with_tabs(self, tabCount: int, string: str) -> str:
        result = ""
        for i in range(tabCount):
            result += "\t"
        return result + string

    def __only_word(self, word: AnnotatedWord, i: int) -> str:
        return str(i + 1) + "/" + word.getParse().getWord().getName()

    def __contains_arg0(self, semantic: str) -> bool:
        for i in range(self.__sentence.wordCount()):
            word = self.__sentence.getWord(i)
            if isinstance(word, AnnotatedWord) and word.getArgumentList() and word.getArgumentList().containsArgument("ARG0", semantic):
                return True
        return False

    def __extra_args(self, output: List[str], word: AnnotatedWord, tabCount: int):
        if word.getParse().getRootPos() == "VERB" and word.getParse().containsTag(MorphologicalTag.A1SG) and "ben " not in self.__sentence.toStems():
            output.append(self.__with_tabs(tabCount + 1, "ben:ARG0"))
        if word.getParse().getRootPos() == "VERB" and word.getParse().getPos() == "NOUN" and word.getParse().containsTag(MorphologicalTag.P1SG):
            output.append(self.__with_tabs(tabCount + 1, "ben:ARG0"))
        if word.getParse().getRootPos() == "VERB" and word.getParse().containsTag(MorphologicalTag.A1PL) and "biz " not in self.__sentence.toStems():
            output.append(self.__with_tabs(tabCount + 1, "biz:ARG0"))
        if word.getParse().getRootPos() == "VERB" and word.getParse().getPos() == "NOUN" and word.getParse().containsTag(MorphologicalTag.P1PL):
            output.append(self.__with_tabs(tabCount + 1, "biz:ARG0"))
        if word.getParse().getRootPos() == "VERB" and word.getParse().containsTag(MorphologicalTag.A2SG) and "sen " not in self.__sentence.toStems():
            output.append(self.__with_tabs(tabCount + 1, "sen:ARG0"))
        if word.getParse().getRootPos() == "VERB" and word.getParse().getPos() == "NOUN" and word.getParse().containsTag(MorphologicalTag.P2SG):
            output.append(self.__with_tabs(tabCount + 1, "sen:ARG0"))
        if word.getParse().getRootPos() == "VERB" and word.getParse().containsTag(MorphologicalTag.A2PL) and "siz " not in self.__sentence.toStems():
            output.append(self.__with_tabs(tabCount + 1, "siz:ARG0"))
        if word.getParse().getRootPos() == "VERB" and word.getParse().getPos() == "NOUN" and word.getParse().containsTag(MorphologicalTag.P2PL):
            output.append(self.__with_tabs(tabCount + 1, "siz:ARG0"))
        if word.getParse().getRootPos() == "VERB" and word.getParse().containsTag(MorphologicalTag.A3SG) and "o " not in self.__sentence.toStems():
            if not self.__contains_arg0(word.getSemantic()):
                if not (word.getParse().getPos() == "NOUN" and (word.getParse().containsTag(MorphologicalTag.P1SG) or word.getParse().containsTag(MorphologicalTag.P1PL) or word.getParse().containsTag(MorphologicalTag.P2SG) or word.getParse().containsTag(MorphologicalTag.P2PL))):
                    output.append(self.__with_tabs(tabCount + 1, "o:ARG0"))
        if word.getParse().getRootPos() == "VERB" and word.getParse().containsTag(MorphologicalTag.A3PL) and "onlar " not in self.__sentence.toStems():
            if not self.__contains_arg0(word.getSemantic()):
                if not (word.getParse().getPos() == "NOUN" and (word.getParse().containsTag(MorphologicalTag.P1SG) or word.getParse().containsTag(MorphologicalTag.P1PL) or word.getParse().containsTag(MorphologicalTag.P2SG) or word.getParse().containsTag(MorphologicalTag.P2PL))):
                    output.append(self.__with_tabs(tabCount + 1, "onlar:ARG0"))

    def __contains_mode(self, index: int) -> bool:
        for i in range(self.__sentence.wordCount()):
            word = self.__sentence.getWord(i)
            if isinstance(word, AnnotatedWord) and word.getUniversalDependency() is not None and word.getUniversalDependency().to() == index + 1:
                if word.getUniversalDependency().__str__() == "AMOD" or word.getUniversalDependency().__str__() == "NMOD":
                    return True
        return False

    def __extra_possessive(self, output: List[str], word: AnnotatedWord, wordIndex: int, tabCount: int):
        if word.getParse().containsTag(MorphologicalTag.P1SG):
            if word.getParse().getRootPos() != "VERB" or word.getParse().getRootPos() != "NOUN":
                output.append(self.__with_tabs(tabCount + 1, "ben:poss"))
        if word.getParse().containsTag(MorphologicalTag.P1PL):
            if word.getParse().getRootPos() != "VERB" or word.getParse().getRootPos() != "NOUN":
                output.append(self.__with_tabs(tabCount + 1, "biz:poss"))
        if word.getParse().containsTag(MorphologicalTag.P2SG):
            if word.getParse().getRootPos() != "VERB" or word.getParse().getRootPos() != "NOUN":
                output.append(self.__with_tabs(tabCount + 1, "sen:poss"))
        if word.getParse().containsTag(MorphologicalTag.P2PL):
            if word.getParse().getRootPos() != "VERB" or word.getParse().getRootPos() != "NOUN":
                output.append(self.__with_tabs(tabCount + 1, "siz:poss"))
        if word.getParse().containsTag(MorphologicalTag.P3SG):
            if not self.__contains_mode(wordIndex):
                output.append(self.__with_tabs(tabCount + 1, "o:poss"))
        if word.getParse().containsTag(MorphologicalTag.P3PL):
            if not self.__contains_mode(wordIndex):
                output.append(self.__with_tabs(tabCount + 1, "onlar:poss"))

    def __is_month(self, next: str) -> bool:
        return next in ["ocak", "şubat", "mart", "nisan", "mayıs", "haziran", "temmuz", "ağustos",
                "eylül", "ekim", "kasım", "aralık"]

    def __is_weekday(self, next: str) -> bool:
        return next in ["pazartesi", "salı", "çarşamba", "perşembe", "cuma", "cumartesi", "pazar"]

    def __is_ordinal(self, next: str) -> int:
        if next == "birinci":
            return 1
        elif next == "ikinci":
            return 2
        elif next == "üçüncü":
            return 3
        elif next == "dördüncü":
            return 4
        elif next == "beşinci":
            return 5
        elif next == "altıncı":
            return 6
        elif next == "yedinci":
            return 7
        elif next == "sekizinci":
            return 8
        elif next == "dokuzuncu":
            return 9
        return 0

    def __add_argument_list(self, output: List[str], current: AnnotatedWord, semantic: str, currentText: str) -> bool:
        if current.getArgumentList() is not None:
            argument_list = current.getArgumentList()
            if argument_list.containsArgument("ARG0", semantic):
                output.append(currentText + ":ARG0")
                return True
            elif argument_list.containsArgument("ARG1", semantic):
                output.append(currentText + ":ARG1")
                return True
            elif argument_list.containsArgument("ARG2", semantic):
                output.append(currentText + ":ARG2")
                return True
        return False

    def __add_details(self, tabCount: int, output: List[str], current: AnnotatedWord, wordIndex: int) -> bool:
        if current.getParse().containsTag(MorphologicalTag.NEGATIVE):
            output.append(self.__with_tabs(tabCount + 1, ":polarity"))
        self.__extra_args(output, current, tabCount)
        self.__extra_possessive(output, current, wordIndex, tabCount)
        if current.getParse().containsTag(MorphologicalTag.IMPERATIVE):
            output.append(self.__with_tabs(tabCount + 1, ":imperative:mode"))

    def __get_preliminary_extra(self, current: AnnotatedWord, index: int, added: List[str]) -> int:
        added.append("")
        if current.getParse().containsTag(MorphologicalTag.CONDITIONAL):
            added[0] = ":cond"
        for i in range(self.__sentence.wordCount()):
            word = self.__sentence.getWord(i)
            if isinstance(word, AnnotatedWord) and word.getUniversalDependency() is not None and word.getUniversalDependency().to() == index + 1:
                if word.getParse().getWord().getName() == "kadar":
                    added[0] = ":extent"
                    return i
                elif word.getParse().getWord().getName() in ["rağmen", "karşın", "karşılık"]:
                    added[0] = ":concession"
                    return i
                elif word.getParse().getWord().getName() in ["için", "sayesinde", "dolayı"]:
                    added[0] = ":cause"
                    return i
        return -1

    def __add_default_case(self, done: List[bool], tabCount: int, output: List[str], defaultString: str, extraAdded: str, added: str, addedIndex: int):
        if extraAdded != "":
            output.append(self.__with_tabs(tabCount, defaultString + extraAdded))
        else:
            output.append(self.__with_tabs(tabCount, defaultString + added))
            if addedIndex != -1:
                done[addedIndex] = True

    def __print_amr_recursively(self, done: List[bool], index: int, tabCount: int, output: List[str], relation: str, semantic: str, wordNet: WordNet, extraAdded: str):
        current_word_index = index
        if done[index]:
            return
        done[index] = True
        current = self.__sentence.getWord(index)
        if isinstance(current, AnnotatedWord):
            if relation == "DET" and current.getParse().getWord().getName() == "bir":
                return
            if current.getParse().getWord().getName() in ["ve", "veya", "hem", "ama"]:
                return
            if current.getParse().getWord().getName() == "değil":
                output.append(self.__with_tabs(tabCount, "-:polarity"))
                return
            if current.isPunctuation():
                return
            added = [""]
            added_index = self.__get_preliminary_extra(current, index, added)
            if current.getParse().isCardinal() and index + 1 < self.__sentence.wordCount():
                next_word = self.__sentence.getWord(index + 1)
                if isinstance(next_word, AnnotatedWord):
                    next = next_word.getParse().getWord().getName()
                    if self.__is_month(next):
                        output.append(self.__with_tabs(tabCount, "date-entity:date"))
                        output.append(self.__with_tabs(tabCount + 1, self.__only_word(current, index) + ":day"))
                        output.append(self.__with_tabs(tabCount + 1, self.__only_word(next_word, index + 1) + ":month"))
                    else:
                        self.__add_default_case(done, tabCount, output, self.__only_word(current, index), extraAdded, added[0], added_index)
            elif current.getParse().isProperNoun():
                wiki_type = "person"
                synsets = wordNet.getSynSetsWithLiteral(current.getParse().getWord().getName())
                for synset in synsets:
                    if isinstance(synset, SynSet) and synset.containsRelation(SemanticRelation("TUR10-0820020", "INSTANCE_HYPERNYM")):
                        wiki_type = "city"
                argument_added = self.__add_argument_list(output, current, semantic, self.__with_tabs(tabCount, wiki_type))
                if not argument_added:
                    if not current.getParse().getRootPos() == "VERB" and current.getParse().containsTag(MorphologicalTag.INSTRUMENTAL):
                        output.append(self.__with_tabs(tabCount, wiki_type) + ":instrument")
                    elif not current.getParse().getRootPos() == "VERB" and current.getParse().containsTag(MorphologicalTag.LOCATIVE):
                        output.append(self.__with_tabs(tabCount, wiki_type) + ":location")
                    else:
                        self.__add_default_case(done, tabCount, output, self.__with_tabs(tabCount, wiki_type), extraAdded, added[0], added_index)
                output.append(self.__with_tabs(tabCount + 1, "name:name"))
                output.append(self.__with_tabs(tabCount + 2, self.__only_word(current, index) + ":op1"))
                for i in range(1, 3):
                    if index + i < self.__sentence.wordCount():
                        check_word = self.__sentence.getWord(index + i)
                        if isinstance(check_word, AnnotatedWord):
                            if check_word.getSemantic() is not None and check_word.getSemantic() == current.getSemantic():
                                output.append(self.__with_tabs(tabCount + 2, self.__only_word(check_word, index + 1) + ":op1" + str(1 + i)))
                                done[index + i] = True
                            else:
                                break
                    else:
                        break
                if wiki_type == "person":
                    output.append(self.__with_tabs(tabCount + 1, "-:wiki"))
                else:
                    output.append(self.__with_tabs(tabCount + 1, current.getParse().getWord().getName() + "-:wiki"))
            elif self.__is_month(current.getParse().getWord().getName()):
                output.append(self.__with_tabs(tabCount, "date-entity:date"))
                output.append(self.__with_tabs(tabCount + 1, self.__only_word(current, index) + ":month"))
            elif self.__is_weekday(current.getParse().getWord().getName()):
                output.append(self.__with_tabs(tabCount, "date-entity:date"))
                output.append(self.__with_tabs(tabCount + 1, self.__only_word(current, index) + ":weekday"))
            else:
                current_word = self.__only_word(current, index)
                for i in range(1, 3):
                    if index > i - 1 and index - i < self.__sentence.wordCount() and not done[index - i]:
                        check_word = self.__sentence.getWord(index - i)
                        if isinstance(check_word, AnnotatedWord):
                            if check_word.getSemantic() is not None and check_word.getSemantic() == current.getSemantic():
                                current_word = self.__only_word(check_word, index - i) + " " + current_word
                                done[index - i] = True
                            else:
                                break
                    else:
                        break
                for i in range(1, 3):
                    if index + i < self.__sentence.wordCount():
                        check_word = self.__sentence.getWord(index + i)
                        if isinstance(check_word, AnnotatedWord):
                            if check_word.getSemantic() is not None and check_word.getSemantic() == current.getSemantic():
                                current_word += " " + self.__only_word(check_word, index + i)
                                done[index + i] = True
                                current = check_word
                                current_word_index = index + i
                            else:
                                break
                    else:
                        break
                if current.getParse().getWord().getName() in ["çok", "gayet", "tam", "bayağı", "fazla", "hiç"]:
                    output.append(self.__with_tabs(tabCount, current_word) + ":degree")
                elif current.getParse().getWord().getName() in ["hep", "sürekli"]:
                    output.append(self.__with_tabs(tabCount, current_word) + ":frequency")
                else:
                    argument_added = self.__add_argument_list(output, current, semantic, self.__with_tabs(tabCount, current_word))
                    if argument_added:
                        self.__add_details(tabCount, output, current, current_word_index)
                    elif current.getParse().containsTag(MorphologicalTag.ORDINAL) or self.__is_ordinal(current.getParse().getWord().getName()) > 0:
                        output.append(self.__with_tabs(tabCount, "ordinal-entity:ord"))
                        value = self.__is_ordinal(current.getParse().getWord().getName())
                        if value > 0:
                            output.append(self.__with_tabs(tabCount + 1, str(value) + ":value"))
                        else:
                            output.append(self.__with_tabs(tabCount + 1, current.getParse().getWord().getName() + ":value"))
                    else:
                        if relation == "AMOD" or relation == "NMOD":
                            output.append(self.__with_tabs(tabCount, current_word) + ":mod")
                        elif relation == "NUMMOD":
                            output.append(self.__with_tabs(tabCount, current_word) + ":quant")
                        elif relation == "ADVMOD":
                            output.append(self.__with_tabs(tabCount, current_word) + ":manner")
                        else:
                            if current.getParse().getRootPos() != "VERB" and current.getParse().containsTag(
                                    MorphologicalTag.INSTRUMENTAL):
                                output.append(self.__with_tabs(tabCount, current_word) + ":instrument")
                            elif current.getParse().getRootPos() != "VERB" and current.getParse().containsTag(
                                    MorphologicalTag.LOCATIVE):
                                output.append(self.__with_tabs(tabCount, current_word) + ":location")
                            else:
                                self.__add_default_case(done, tabCount, output, self.__with_tabs(tabCount, current_word), extraAdded, added[0], added_index)
                                self.__add_details(tabCount, output, current, current_word_index)
        i = 0
        while i < self.__sentence.wordCount():
            word = self.__sentence.getWord(i)
            if isinstance(word, AnnotatedWord):
                if word.getParse().isCardinal() and i + 1 < self.__sentence.wordCount():
                    next_word = self.__sentence.getWord(i + 1)
                    if isinstance(next_word, AnnotatedWord):
                        next = next_word.getParse().getWord().getName()
                        if self.__is_month(next):
                            if next_word.getUniversalDependency().to() == index + 1:
                                self.__meta_verb_tags(word, done, i, tabCount + 1, output, word.getUniversalDependency().__str__(), current.getSemantic(), wordNet)
                            i = i + 2
                            continue
                j = i
                while i < self.__sentence.wordCount() - 1 and self.__sentence.getWord(i + 1).getSemantic() is not None and self.__sentence.getWord(i + 1).getSemantic() == word.getSemantic():
                    i = i + 1
                if word.getUniversalDependency() is not None and word.getUniversalDependency().to() == index + 1:
                    self.__meta_verb_tags(word, done, j, tabCount + 1, output, word.getUniversalDependency().__str__(), current.getSemantic(), wordNet)
                elif j != i and self.__sentence.getWord(i).getUniversalDependency() is not None and self.__sentence.getWord(i).getUniversalDependency().to() == index + 1:
                    self.__meta_verb_tags(word, done, j, tabCount + 1, output, word.getUniversalDependency().__str__(), current.getSemantic(), wordNet)
            i = i + 1

    def __meta_verb_tags(self, word: AnnotatedWord, done: List[bool], index: int, tabCount: int, output: List[str], relation: str, semantic: str, wordNet: WordNet):
        parataxis_or_conj = False
        for i in range(self.__sentence.wordCount()):
            connected_word = self.__sentence.getWord(i)
            if isinstance(connected_word, AnnotatedWord):
                if connected_word.getUniversalDependency() is not None and connected_word.getUniversalDependency().to() == index + 1 and connected_word.getUniversalDependency().__str__() in ["PARATAXIS", "CONJ"]:
                    parataxis_or_conj = True
                    break
        if parataxis_or_conj:
            output.append(self.__with_tabs(tabCount, "and"))
            count = 1
            for i in range(self.__sentence.wordCount()):
                connected_word = self.__sentence.getWord(i)
                if isinstance(connected_word, AnnotatedWord):
                    if connected_word.getUniversalDependency() is not None and connected_word.getUniversalDependency().to() == index + 1 and connected_word.getUniversalDependency().__str__() in ["PARATAXIS", "CONJ"]:
                        self.__print_amr_recursively(done, i, tabCount + 1, output, relation, semantic, wordNet, ":op" + str(count))
                        count = count + 1
            self.__print_amr_recursively(done, index, tabCount + 1, output, relation, semantic, wordNet, ":op" + str(count))
        else:
            if word.getParse().containsTag(MorphologicalTag.NECESSITY):
                output.append(self.__with_tabs(tabCount, "öner"))
                tabCount = tabCount + 1
            if word.getParse().containsTag(MorphologicalTag.ABLE):
                output.append(self.__with_tabs(tabCount, "mümkün"))
                tabCount = tabCount + 1
            if word.getParse().containsTag(MorphologicalTag.CAUSATIVE):
                output.append(self.__with_tabs(tabCount, "yap"))
                tabCount = tabCount + 1
            self.__print_amr_recursively(done, index, tabCount, output, relation, semantic, wordNet,"")

    def constructExcelAmr(self, sentence: AnnotatedSentence) -> list[str]:
        output = []
        self.__sentence = sentence
        done = []
        for i in range(self.__sentence.wordCount()):
            done.append(False)
        output.append(sentence.getFileName() + "\t" + sentence.toString())
        for i in range(sentence.wordCount()):
            word = sentence.getWord(i)
            if isinstance(word, AnnotatedWord):
                if word.getUniversalDependency() is not None and word.getUniversalDependency().__str__() == "ROOT":
                    self.__meta_verb_tags(word, done, i, 0, output, "ROOT", word.getSemantic(), self.__word_net)
        return output
