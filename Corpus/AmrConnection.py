from AmrWord import AmrWord

class AmrConnection:

    __from : AmrWord
    __to: AmrWord
    __with: str

    def __init__(self, _from: AmrWord, _to: AmrWord, _with: str):
        self.__from = _from
        self.__to = _to
        self.__with = _with

    def getFrom(self) -> AmrWord:
        return self.__from

    def getTo(self) -> AmrWord:
        return self.__to

    def getWith(self) -> str:
        return self.__with
