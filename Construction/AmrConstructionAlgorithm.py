from __future__ import annotations
from abc import abstractmethod
from typing import List

from AnnotatedSentence.AnnotatedSentence import AnnotatedSentence

class AmrConstructionAlgorithm(object):

    @abstractmethod
    def constructExcelAmr(self, sentence: AnnotatedSentence) -> list[str]:
        pass

    def toString(self, sentence: AnnotatedSentence):
        result = ""
        for item in self.constructExcelAmr(sentence):
            result += item + "\n"
        return result

    def saveAmr(self, items: List[str], fileName: str):
        start_x = 750
        start_y = 100
        last_parent = [""] * 50
        last_x = [0] * 50
        child_count = [0] * 50
        words = set()
        out_file = open(fileName, "w", encoding="utf8")
        out_file.write("<Amr>\n")
        line = items[0]
        out_file.write("<Word name=\"" + line + "\" positionX=\"" + str(start_x) + "\" positionY=\"" + str(start_y) + "\"/>\n")
        words.add(line)
        last_parent[0] = line
        child_count[0] = 0
        last_x[0] = start_x
        for j in range (1, len(items)):
            line = items[j]
            tab_count = 0
            i = 0
            while line[i] == '\t':
                tab_count = tab_count + 1
                i = i + 1
            line = line[tab_count:]
            if ":" in line:
                last_parent[tab_count] = line[0: line.index(":")]
            else:
                last_parent[tab_count] = line
            child_count[tab_count] = 0
            last_x[tab_count] = last_x[tab_count - 1] + (child_count[tab_count - 1] - 1) * 100
            if ":" in line:
                candidate = line[0: line.rindex(":")]
                if not candidate in words:
                    out_file.write("<Word name=\"" + candidate + "\" positionX=\"" + str(last_x[tab_count]) + "\" positionY=\"" + str(start_y + 100 * tab_count) + "\"/>\n")
                    words.add(candidate)
                out_file.write("<Connection from=\"" + last_parent[tab_count - 1] + "\" to=\"" + candidate + "\" with=\"" + line[0: line.rindex(":") + 1] + "\"/>\n")
            else:
                if not line in words:
                    out_file.write("<Word name=\"" + line + "\" positionX=\"" + str(last_x[tab_count]) + "\" positionY=\"" + str(start_y + 100 * tab_count) + "\"/>")
                    words.add(line)
                out_file.write("<Connection from=\"" + last_parent[tab_count - 1] + "\" to=\"" + line + "\"/>\n")
            child_count[tab_count - 1] = child_count[tab_count - 1] + 1
        out_file.write("</Amr>\n")
        out_file.close()
