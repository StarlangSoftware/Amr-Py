from __future__ import annotations
from Dictionary.Word import Word
from Point import Point

class AmrWord(Word):

    position: Point

    def __init__(self, name: str, position:Point):
        super().__init__(name)
        self.position = position

    def getPosition(self) -> Point:
        return self.position

    def move(self, deltaX: int, deltaY: int) -> None:
        self.position.setX(self.getPosition().getX() + deltaX)
        self.position.setY(self.getPosition().getY() + deltaY)

    def clone(self) -> AmrWord:
        return AmrWord(self.getName(), Point(self.getPosition().getX(), self.getPosition().getY()))