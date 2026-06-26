import xml.etree.ElementTree

from Corpus.FileDescription import FileDescription
from Corpus.Sentence import Sentence

from AmrConnection import AmrConnection
from AmrWord import AmrWord
from Point import Point


class AmrSentence(Sentence):

    __connections: list[AmrConnection]
    __file_description: FileDescription

    def constructor1(self, file_description: FileDescription):
        self.__file_description = file_description
        self.reload()

    def constructor2(self, path: str, file_name: str):
        self.__file_description = FileDescription(path, file_name)
        self.reload()

    def __init__(self, param1: str | FileDescription, param2: str | None = None):
        self.words = []
        self.__connections = []
        if param2 is not None and isinstance(param1, str):
            self.constructor2(param1, param2)
        elif isinstance(param1, FileDescription):
            self.constructor1(param1)

    def reload(self):
        file_name = self.__file_description.getFileName()
        root = xml.etree.ElementTree.parse(file_name).getroot()
        self.__load_from_xml(root)

    def getRawFileName(self) -> str:
        return self.__file_description.getRawFileName()

    def getFileName(self) -> str:
        return self.__file_description.getFileName()

    def getFileDescription(self) -> FileDescription:
        return self.__file_description

    def __getWord(self, name: str) -> AmrWord | None:
        for word in self.words:
            if word.getName() == name:
                return word
        return None

    def getConnection(self, index: int) -> AmrConnection:
        return self.__connections[index]

    def connection_count(self) -> int:
        return len(self.__connections)

    def add_connection(self, _from: AmrWord, _to: AmrWord, _with: str):
        self.__connections.append(AmrConnection(_from, _to, _with))

    def __load_from_xml(self, root):
        for child_node in root:
            if child_node.tag == "Word":
                new_word = AmrWord(child_node.attrib["name"], Point(child_node.attrib["positionX"], child_node.attrib["positionY"]))
                self.addWord(new_word)
            elif child_node.tag == "Connection":
                _from = self.__getWord(child_node.attrib["from"])
                _to = self.__getWord(child_node.attrib["to"])
                if child_node.attrib["with"] is not None:
                    _with = child_node.attrib["with"]
                else:
                    _with = ""
                if _from is not None and _to is not None:
                    self.add_connection(_from, _to, _with)

    def __get_root(self) -> AmrWord | None:
        done = set()
        for word in self.words:
            done.add(word.getName())
        for connection in self.__connections:
            if connection.getTo().getName() in done:
                done.remove(connection.getTo().getName())
        return self.__getWord(done.pop())

    def __word_to_string(self, word: AmrWord | None, tab_count: int) -> str:
        result = "(" + word.getName()
        for connection in self.__connections:
            if connection.getFrom().getName() == word.getName():
                child = "\n"
                for i in range(tab_count + 1):
                    child += "\t"
                child += ":" + connection.getWith()
                child += " " + self.__word_to_string(connection.getTo(), tab_count + 1)
                result += child
        return result + ")"

    def __repr__(self):
        return self.getFileName() + "\n" + self.__word_to_string(self.__get_root(), 0)

    def __str__(self):
        return self.__repr__()
