class Point:

    __x: int
    __y: int

    def __init__(self, x: int,y: int):
        self.__x = x
        self.__y = y

    def getX(self) -> int:
        return self.__x

    def getY(self) -> int:
        return self.__y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y
